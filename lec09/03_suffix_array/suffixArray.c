// suffixArray.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * Suffix Array 구현 (C 언어)
 *
 * Naive 방법: O(n^2 log n)
 * Doubling 알고리즘: O(n log^2 n)
 */

// Naive 방법용 구조체
typedef struct {
  int index;
  char* suffix;
} SuffixEntry;

// Doubling 알고리즘용 구조체
typedef struct {
  int rank[2];  // 현재와 다음 위치의 rank
  int index;    // 원래 인덱스
} SuffixRank;

// 함수 선언
void print_suffix_array(char* text, int* suffix_array, int n);
int search_pattern(char* text, int* suffix_array, int n, char* pattern);
void build_lcp_array(char* text, int* suffix_array, int* lcp_array, int n);
int compute_lcp(char* text, int i, int j, int n);
int search_pattern_advanced(char* text, int* suffix_array, char* pattern, int n,
                            int m);
void find_all_patterns(char* text, int* suffix_array, char* pattern, int n,
                       int m, int* results, int* count);
int find_longest_repeated_substring(char* text, int* suffix_array,
                                    int* lcp_array, int n);
void print_lcp_array(int* lcp_array, int n);

/**
 * Naive 방법용 비교 함수
 */
int compare_suffix(const void* a, const void* b) {
  SuffixEntry* sa = (SuffixEntry*)a;
  SuffixEntry* sb = (SuffixEntry*)b;
  return strcmp(sa->suffix, sb->suffix);
}

/**
 * Doubling 알고리즘용 비교 함수
 */
int compare_ranks(const void* a, const void* b) {
  SuffixRank* sa = (SuffixRank*)a;
  SuffixRank* sb = (SuffixRank*)b;

  if (sa->rank[0] != sb->rank[0]) {
    return sa->rank[0] - sb->rank[0];
  }
  return sa->rank[1] - sb->rank[1];
}

/**
 * Naive 방법으로 Suffix Array 구축
 * 시간 복잡도: O(n^2 log n)
 * 공간 복잡도: O(n)
 *
 * @param text 입력 문자열
 * @param suffix_array 결과를 저장할 배열
 * @param n 문자열 길이
 */
void build_suffix_array_naive(char* text, int* suffix_array, int n) {
  SuffixEntry* suffixes = (SuffixEntry*)malloc(n * sizeof(SuffixEntry));

  // 모든 suffix 생성
  for (int i = 0; i < n; i++) {
    suffixes[i].index = i;
    suffixes[i].suffix = text + i;
  }

  // 사전순 정렬
  qsort(suffixes, n, sizeof(SuffixEntry), compare_suffix);

  // 결과를 suffix array로 복사
  for (int i = 0; i < n; i++) {
    suffix_array[i] = suffixes[i].index;
  }

  free(suffixes);
}

/**
 * Doubling 알고리즘으로 Suffix Array 구축
 * 시간 복잡도: O(n log^2 n)
 * 공간 복잡도: O(n)
 *
 * @param text 입력 문자열
 * @param suffix_array 결과를 저장할 배열
 * @param n 문자열 길이
 */
void build_suffix_array_doubling(char* text, int* suffix_array, int n) {
  SuffixRank* suffixes = (SuffixRank*)malloc(n * sizeof(SuffixRank));

  // 초기 rank 설정 (각 문자)
  for (int i = 0; i < n; i++) {
    suffixes[i].rank[0] = text[i];
    suffixes[i].rank[1] = (i + 1 < n) ? text[i + 1] : -1;
    suffixes[i].index = i;
  }

  // 정렬
  qsort(suffixes, n, sizeof(SuffixRank), compare_ranks);

  // 각 단계마다 길이를 2배씩 증가
  for (int k = 4; k < 2 * n; k *= 2) {
    // 새로운 rank 할당
    int rank = 0;
    int prev_rank0 = suffixes[0].rank[0];
    int prev_rank1 = suffixes[0].rank[1];
    suffixes[0].rank[0] = rank;

    int* index = (int*)malloc(n * sizeof(int));
    index[suffixes[0].index] = 0;

    for (int i = 1; i < n; i++) {
      if (suffixes[i].rank[0] != prev_rank0 ||
          suffixes[i].rank[1] != prev_rank1) {
        rank++;
      }

      prev_rank0 = suffixes[i].rank[0];
      prev_rank1 = suffixes[i].rank[1];
      suffixes[i].rank[0] = rank;
      index[suffixes[i].index] = i;
    }

    // 다음 위치의 rank 업데이트
    for (int i = 0; i < n; i++) {
      int next_index = suffixes[i].index + k / 2;
      suffixes[i].rank[1] =
          (next_index < n) ? suffixes[index[next_index]].rank[0] : -1;
    }

    free(index);

    // 다시 정렬
    qsort(suffixes, n, sizeof(SuffixRank), compare_ranks);
  }

  // 최종 suffix array 생성
  for (int i = 0; i < n; i++) {
    suffix_array[i] = suffixes[i].index;
  }

  free(suffixes);
}

/**
 * Suffix Array 출력 함수
 *
 * @param text 원본 문자열
 * @param suffix_array suffix array
 * @param n 문자열 길이
 */
void print_suffix_array(char* text, int* suffix_array, int n) {
  printf("Index\tSuffix\n");
  printf("-----\t------\n");
  for (int i = 0; i < n; i++) {
    int idx = suffix_array[i];
    printf("%d\t%s\n", idx, text + idx);
  }
}

/**
 * LCP (Longest Common Prefix) 계산 함수
 *
 * @param text 원본 문자열
 * @param i 첫 번째 위치
 * @param j 두 번째 위치
 * @param n 문자열 길이
 * @return 두 위치의 LCP 길이
 */
int compute_lcp(char* text, int i, int j, int n) {
  int lcp = 0;
  while (i + lcp < n && j + lcp < n && text[i + lcp] == text[j + lcp]) {
    lcp++;
  }
  return lcp;
}

/**
 * LCP 배열 구축 (Kasai 알고리즘)
 *
 * @param text 원본 문자열
 * @param suffix_array suffix array
 * @param lcp_array LCP 배열 (결과 저장)
 * @param n 문자열 길이
 */
void build_lcp_array(char* text, int* suffix_array, int* lcp_array, int n) {
  int* rank = (int*)malloc(n * sizeof(int));

  // LCP 배열 초기화
  for (int i = 0; i < n; i++) {
    lcp_array[i] = 0;
  }

  // suffix array의 역순 배열 생성
  for (int i = 0; i < n; i++) {
    rank[suffix_array[i]] = i;
  }

  int h = 0;
  for (int i = 0; i < n; i++) {
    if (rank[i] > 0) {
      int j = suffix_array[rank[i] - 1];
      while (i + h < n && j + h < n && text[i + h] == text[j + h]) {
        h++;
      }
      lcp_array[rank[i]] = h;
      if (h > 0)
        h--;
    }
  }

  free(rank);
}

/**
 * 패턴 검색 함수 (이진 탐색 사용)
 *
 * @param text 원본 문자열
 * @param suffix_array suffix array
 * @param n 문자열 길이
 * @param pattern 검색할 패턴
 * @return 패턴이 발견된 위치, 없으면 -1
 */
int search_pattern(char* text, int* suffix_array, int n, char* pattern) {
  int left = 0;
  int right = n - 1;
  int pattern_len = strlen(pattern);

  while (left <= right) {
    int mid = (left + right) / 2;
    char* suffix = text + suffix_array[mid];

    int cmp = strncmp(pattern, suffix, pattern_len);
    if (cmp == 0) {
      return suffix_array[mid];  // 패턴 발견
    } else if (cmp < 0) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }

  return -1;  // 패턴을 찾지 못함
}

/**
 * 고급 패턴 검색 함수 (더 효율적인 버전)
 *
 * @param text 원본 문자열
 * @param suffix_array suffix array
 * @param pattern 검색할 패턴
 * @param n 문자열 길이
 * @param m 패턴 길이
 * @return 패턴이 발견된 위치, 없으면 -1
 */
int search_pattern_advanced(char* text, int* suffix_array, char* pattern, int n,
                            int m) {
  int left = 0, right = n - 1;

  while (left <= right) {
    int mid = (left + right) / 2;
    int cmp = strncmp(text + suffix_array[mid], pattern, m);

    if (cmp == 0) {
      return suffix_array[mid];  // 패턴 찾음
    } else if (cmp < 0) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return -1;  // 패턴 없음
}

/**
 * 패턴의 모든 출현 위치 찾기
 *
 * @param text 원본 문자열
 * @param suffix_array suffix array
 * @param pattern 검색할 패턴
 * @param n 문자열 길이
 * @param m 패턴 길이
 * @param results 결과를 저장할 배열
 * @param count 발견된 패턴 개수
 */
void find_all_patterns(char* text, int* suffix_array, char* pattern, int n,
                       int m, int* results, int* count) {
  *count = 0;

  // 첫 번째 출현 위치 찾기
  int left = 0, right = n - 1, first = -1;

  // 이진 탐색으로 첫 번째 출현 위치 찾기
  while (left <= right) {
    int mid = (left + right) / 2;
    int cmp = strncmp(text + suffix_array[mid], pattern, m);

    if (cmp >= 0) {
      if (cmp == 0)
        first = mid;
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }

  if (first == -1)
    return;

  // 첫 번째 위치부터 연속된 모든 출현 위치 찾기
  for (int i = first; i < n; i++) {
    if (strncmp(text + suffix_array[i], pattern, m) == 0) {
      results[(*count)++] = suffix_array[i];
    } else {
      break;
    }
  }
}

/**
 * 가장 긴 반복 부분 문자열 찾기
 *
 * @param text 원본 문자열
 * @param suffix_array suffix array
 * @param lcp_array LCP 배열
 * @param n 문자열 길이
 * @return 가장 긴 반복 부분 문자열의 시작 위치
 */
int find_longest_repeated_substring(char* text, int* suffix_array,
                                    int* lcp_array, int n) {
  int max_lcp = 0;
  int result_index = -1;

  for (int i = 1; i < n; i++) {
    if (lcp_array[i] > max_lcp) {
      max_lcp = lcp_array[i];
      result_index = suffix_array[i];
    }
  }

  return result_index;
}

/**
 * LCP 배열 출력 함수
 *
 * @param lcp_array LCP 배열
 * @param n 배열 크기
 */
void print_lcp_array(int* lcp_array, int n) {
  printf("LCP Array: [");
  for (int i = 0; i < n; i++) {
    printf("%d", lcp_array[i]);
    if (i < n - 1)
      printf(", ");
  }
  printf("]\n");
}

/**
 * 테스트 함수
 */
void test_suffix_array() {
  printf("=== Suffix Array 테스트 ===\n\n");

  // 테스트 케이스 1: Naive 방법
  printf("=== Naive 방법 테스트 ===\n");
  char text1[] = "banana$";
  int n1 = strlen(text1);
  int suffix_array1[n1];

  printf("문자열: %s\n", text1);
  build_suffix_array_naive(text1, suffix_array1, n1);
  print_suffix_array(text1, suffix_array1, n1);

  // 테스트 케이스 2: Doubling 알고리즘
  printf("\n=== Doubling 알고리즘 테스트 ===\n");
  char text2[] = "abcdef";
  int n2 = strlen(text2);
  int suffix_array2[n2];

  printf("문자열: %s\n", text2);
  build_suffix_array_doubling(text2, suffix_array2, n2);
  print_suffix_array(text2, suffix_array2, n2);

  // 테스트 케이스 3: 복잡한 문자열
  printf("\n=== 복잡한 문자열 테스트 ===\n");
  char text3[] = "mississippi";
  int n3 = strlen(text3);
  int suffix_array3[n3];

  printf("문자열: %s\n", text3);
  build_suffix_array_doubling(text3, suffix_array3, n3);
  print_suffix_array(text3, suffix_array3, n3);

  // 테스트 케이스 4: 패턴 검색
  printf("\n=== 패턴 검색 테스트 ===\n");
  char pattern1[] = "iss";
  char pattern2[] = "ana";
  char pattern3[] = "xyz";

  int result1 = search_pattern(text3, suffix_array3, n3, pattern1);
  printf("패턴 '%s': ", pattern1);
  if (result1 != -1) {
    printf("위치 %d에서 발견\n", result1);
  } else {
    printf("찾을 수 없음\n");
  }

  int result2 = search_pattern(text1, suffix_array1, n1, pattern2);
  printf("패턴 '%s': ", pattern2);
  if (result2 != -1) {
    printf("위치 %d에서 발견\n", result2);
  } else {
    printf("찾을 수 없음\n");
  }

  int result3 = search_pattern(text3, suffix_array3, n3, pattern3);
  printf("패턴 '%s': ", pattern3);
  if (result3 != -1) {
    printf("위치 %d에서 발견\n", result3);
  } else {
    printf("찾을 수 없음\n");
  }

  // 테스트 케이스 5: 반복 문자
  printf("\n=== 반복 문자 테스트 ===\n");
  char text4[] = "aaaa";
  int n4 = strlen(text4);
  int suffix_array4[n4];

  printf("문자열: %s\n", text4);
  build_suffix_array_doubling(text4, suffix_array4, n4);
  print_suffix_array(text4, suffix_array4, n4);

  // 테스트 케이스 6: 알파벳 순서
  printf("\n=== 알파벳 순서 테스트 ===\n");
  char text5[] = "dcba";
  int n5 = strlen(text5);
  int suffix_array5[n5];

  printf("문자열: %s\n", text5);
  build_suffix_array_naive(text5, suffix_array5, n5);
  print_suffix_array(text5, suffix_array5, n5);

  // 테스트 케이스 7: LCP 배열 테스트
  printf("\n=== LCP 배열 테스트 ===\n");
  char text6[] = "abcabxabcd";
  int n6 = strlen(text6);
  int suffix_array6[n6];
  int lcp_array6[n6];

  printf("문자열: %s\n", text6);
  build_suffix_array_doubling(text6, suffix_array6, n6);
  build_lcp_array(text6, suffix_array6, lcp_array6, n6);

  print_suffix_array(text6, suffix_array6, n6);
  print_lcp_array(lcp_array6, n6);

  // 테스트 케이스 8: 고급 패턴 검색
  printf("\n=== 고급 패턴 검색 테스트 ===\n");
  char pattern_adv[] = "abc";
  int m = strlen(pattern_adv);

  int result_adv =
      search_pattern_advanced(text6, suffix_array6, pattern_adv, n6, m);
  printf("고급 검색 - 패턴 '%s': ", pattern_adv);
  if (result_adv != -1) {
    printf("위치 %d에서 발견\n", result_adv);
  } else {
    printf("찾을 수 없음\n");
  }

  // 테스트 케이스 9: 모든 패턴 출현 위치 찾기
  printf("\n=== 모든 패턴 출현 위치 테스트 ===\n");
  int results[n6];
  int count;

  find_all_patterns(text6, suffix_array6, pattern_adv, n6, m, results, &count);
  printf("패턴 '%s'의 모든 출현 위치 (%d개): ", pattern_adv, count);
  for (int i = 0; i < count; i++) {
    printf("%d", results[i]);
    if (i < count - 1)
      printf(", ");
  }
  printf("\n");

  // 테스트 케이스 10: 가장 긴 반복 부분 문자열
  printf("\n=== 가장 긴 반복 부분 문자열 테스트 ===\n");
  int longest_pos =
      find_longest_repeated_substring(text6, suffix_array6, lcp_array6, n6);
  if (longest_pos != -1) {
    // 가장 긴 LCP 찾기
    int max_lcp = 0;
    for (int i = 1; i < n6; i++) {
      if (lcp_array6[i] > max_lcp) {
        max_lcp = lcp_array6[i];
      }
    }
    printf("가장 긴 반복 부분 문자열: '");
    for (int i = 0; i < max_lcp; i++) {
      printf("%c", text6[longest_pos + i]);
    }
    printf("' (위치 %d, 길이 %d)\n", longest_pos, max_lcp);
  } else {
    printf("반복 부분 문자열이 없습니다.\n");
  }

  // 테스트 케이스 11: LCP를 이용한 두 suffix 비교
  printf("\n=== LCP 계산 테스트 ===\n");
  int pos1 = 0, pos2 = 3;  // "abcabxabcd"에서 0번째와 3번째 위치
  int lcp_direct = compute_lcp(text6, pos1, pos2, n6);
  printf("위치 %d('%s')와 위치 %d('%s')의 LCP: %d\n", pos1, text6 + pos1, pos2,
         text6 + pos2, lcp_direct);
}

// 메인 함수
int main() {
  test_suffix_array();
  return 0;
}
