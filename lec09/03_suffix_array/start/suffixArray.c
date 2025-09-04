// suffixArray.c - Suffix Array (START CODE)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * Suffix Array 구현 (C 언어)
 *
 * Naive 방법: O(n^2 log n)
 * Doubling 알고리즘: O(n log^2 n)
 */

// Naive 방법용 구조체 (완성됨)
typedef struct {
  int index;
  char* suffix;
} SuffixEntry;

// Doubling 알고리즘용 구조체 (완성됨)
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
 * Naive 방법용 비교 함수 (완성됨)
 */
int compare_suffix(const void* a, const void* b) {
  SuffixEntry* sa = (SuffixEntry*)a;
  SuffixEntry* sb = (SuffixEntry*)b;
  return strcmp(sa->suffix, sb->suffix);
}

/**
 * Doubling 알고리즘용 비교 함수 (완성됨)
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
 * TODO: Naive 방법으로 Suffix Array 구축
 * 시간 복잡도: O(n^2 log n)
 * 공간 복잡도: O(n)
 *
 * @param text 입력 문자열
 * @param suffix_array 결과를 저장할 배열
 * @param n 문자열 길이
 */
void build_suffix_array_naive(char* text, int* suffix_array, int n) {
  // TODO: Naive 방법으로 Suffix Array를 구축하세요
  // 힌트:
  // 1. SuffixEntry 배열 할당: suffixes = malloc(n * sizeof(SuffixEntry))
  // 2. 모든 suffix 생성: suffixes[i].index = i, suffixes[i].suffix = text + i
  // 3. qsort로 사전순 정렬: qsort(suffixes, n, sizeof(SuffixEntry),
  // compare_suffix)
  // 4. 결과를 suffix_array로 복사: suffix_array[i] = suffixes[i].index
  // 5. 메모리 해제: free(suffixes)

  printf("build_suffix_array_naive 구현 필요\n");
}

/**
 * TODO: Doubling 알고리즘으로 Suffix Array 구축
 * 시간 복잡도: O(n log^2 n)
 * 공간 복잡도: O(n)
 *
 * @param text 입력 문자열
 * @param suffix_array 결과를 저장할 배열
 * @param n 문자열 길이
 */
void build_suffix_array_doubling(char* text, int* suffix_array, int n) {
  // TODO: Doubling 알고리즘으로 Suffix Array를 구축하세요
  // 힌트:
  // 1. SuffixRank 배열 할당
  // 2. 초기 rank 설정 (각 문자와 다음 문자)
  // 3. 정렬 (compare_ranks 함수 사용)
  // 4. k=4부터 시작해서 2배씩 증가하며 반복:
  //    - 새로운 rank 할당
  //    - index 배열로 위치 추적
  //    - 다음 위치의 rank 업데이트
  //    - 다시 정렬
  // 5. 최종 suffix array 생성
  // 6. 메모리 해제

  printf("build_suffix_array_doubling 구현 필요\n");
}

/**
 * LCP (Longest Common Prefix) 계산 (완성됨)
 *
 * @param text 문자열
 * @param i 첫 번째 위치
 * @param j 두 번째 위치
 * @param n 문자열 길이
 * @return LCP 길이
 */
int compute_lcp(char* text, int i, int j, int n) {
  int lcp = 0;
  while (i + lcp < n && j + lcp < n && text[i + lcp] == text[j + lcp]) {
    lcp++;
  }
  return lcp;
}

/**
 * LCP 배열 구축 (Kasai 알고리즘) (완성됨)
 *
 * @param text 문자열
 * @param suffix_array suffix array
 * @param lcp_array 결과를 저장할 LCP 배열
 * @param n 문자열 길이
 */
void build_lcp_array(char* text, int* suffix_array, int* lcp_array, int n) {
  int* rank = (int*)malloc(n * sizeof(int));

  // Initialize LCP array
  for (int i = 0; i < n; i++) {
    lcp_array[i] = 0;
  }

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
 * 이진 탐색을 이용한 패턴 검색 (완성됨)
 *
 * @param text 원본 문자열
 * @param suffix_array suffix array
 * @param n 문자열 길이
 * @param pattern 찾을 패턴
 * @return 패턴이 발견된 위치 (없으면 -1)
 */
int search_pattern(char* text, int* suffix_array, int n, char* pattern) {
  int left = 0, right = n - 1;
  int m = strlen(pattern);

  while (left <= right) {
    int mid = (left + right) / 2;
    int cmp = strncmp(text + suffix_array[mid], pattern, m);

    if (cmp == 0) {
      return suffix_array[mid];
    } else if (cmp < 0) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  return -1;
}

/**
 * 고급 패턴 검색 (더 정확한 구현) (완성됨)
 *
 * @param text 원본 문자열
 * @param suffix_array suffix array
 * @param pattern 찾을 패턴
 * @param n 문자열 길이
 * @param m 패턴 길이
 * @return 패턴이 발견된 위치 (없으면 -1)
 */
int search_pattern_advanced(char* text, int* suffix_array, char* pattern, int n,
                            int m) {
  int left = 0, right = n - 1;

  while (left <= right) {
    int mid = (left + right) / 2;
    int cmp = strncmp(text + suffix_array[mid], pattern, m);

    if (cmp == 0) {
      return suffix_array[mid];
    } else if (cmp < 0) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  return -1;
}

/**
 * 모든 패턴 출현 위치 찾기 (완성됨)
 *
 * @param text 원본 문자열
 * @param suffix_array suffix array
 * @param pattern 찾을 패턴
 * @param n 문자열 길이
 * @param m 패턴 길이
 * @param results 결과를 저장할 배열
 * @param count 발견된 패턴의 개수
 */
void find_all_patterns(char* text, int* suffix_array, char* pattern, int n,
                       int m, int* results, int* count) {
  *count = 0;
  int left = 0, right = n - 1, first = -1;

  // 첫 번째 출현 위치 찾기
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

  // 연속된 모든 매칭 찾기
  for (int i = first; i < n; i++) {
    if (strncmp(text + suffix_array[i], pattern, m) == 0) {
      results[(*count)++] = suffix_array[i];
    } else {
      break;
    }
  }
}

/**
 * 가장 긴 반복 부분 문자열 찾기 (완성됨)
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
 * Suffix Array 출력 (완성됨)
 *
 * @param text 원본 문자열
 * @param suffix_array suffix array
 * @param n 문자열 길이
 */
void print_suffix_array(char* text, int* suffix_array, int n) {
  printf("Suffix Array:\n");
  printf("Index | Suffix\n");
  printf("------|-------\n");
  for (int i = 0; i < n; i++) {
    printf("%5d | %s\n", suffix_array[i], text + suffix_array[i]);
  }
}

/**
 * LCP 배열 출력 (완성됨)
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
 * 테스트 함수 (완성됨)
 */
void test_suffix_array() {
  printf("=== Suffix Array 테스트 ===\n\n");

  // 테스트 케이스 1: Naive 방법
  printf("=== Naive 방법 테스트 ===\n");
  char text1[] = "banana";
  int n1 = strlen(text1);
  int* suffix_array1 = (int*)malloc(n1 * sizeof(int));

  printf("문자열: %s\n", text1);
  build_suffix_array_naive(text1, suffix_array1, n1);
  print_suffix_array(text1, suffix_array1, n1);

  // 패턴 검색 테스트
  char pattern1[] = "ana";
  int pos1 = search_pattern(text1, suffix_array1, n1, pattern1);
  printf("패턴 '%s' 검색 결과: %d\n", pattern1, pos1);

  free(suffix_array1);
  printf("\n");

  // 테스트 케이스 2: Doubling 방법
  printf("=== Doubling 알고리즘 테스트 ===\n");
  char text2[] = "mississippi";
  int n2 = strlen(text2);
  int* suffix_array2 = (int*)malloc(n2 * sizeof(int));

  printf("문자열: %s\n", text2);
  build_suffix_array_doubling(text2, suffix_array2, n2);
  print_suffix_array(text2, suffix_array2, n2);

  // LCP 배열 구축
  int* lcp_array2 = (int*)malloc(n2 * sizeof(int));
  build_lcp_array(text2, suffix_array2, lcp_array2, n2);
  print_lcp_array(lcp_array2, n2);

  // 패턴 검색 테스트
  char pattern2[] = "issi";
  int pos2 = search_pattern_advanced(text2, suffix_array2, pattern2, n2,
                                     strlen(pattern2));
  printf("패턴 '%s' 검색 결과: %d\n", pattern2, pos2);

  // 모든 패턴 찾기
  char pattern3[] = "si";
  int results[10];
  int count;
  find_all_patterns(text2, suffix_array2, pattern3, n2, strlen(pattern3),
                    results, &count);
  printf("패턴 '%s'의 모든 출현 위치 (%d개): ", pattern3, count);
  for (int i = 0; i < count; i++) {
    printf("%d ", results[i]);
  }
  printf("\n");

  // 가장 긴 반복 부분 문자열
  int longest_pos =
      find_longest_repeated_substring(text2, suffix_array2, lcp_array2, n2);
  printf("가장 긴 반복 부분 문자열 시작 위치: %d\n", longest_pos);

  free(suffix_array2);
  free(lcp_array2);
  printf("\n");

  // 테스트 케이스 3: 비교 테스트
  printf("=== 방법 비교 테스트 ===\n");
  char text3[] = "abcabc";
  int n3 = strlen(text3);
  int* sa_naive = (int*)malloc(n3 * sizeof(int));
  int* sa_doubling = (int*)malloc(n3 * sizeof(int));

  printf("문자열: %s\n", text3);

  build_suffix_array_naive(text3, sa_naive, n3);
  build_suffix_array_doubling(text3, sa_doubling, n3);

  printf("Naive 결과:    ");
  for (int i = 0; i < n3; i++) {
    printf("%d ", sa_naive[i]);
  }
  printf("\n");

  printf("Doubling 결과: ");
  for (int i = 0; i < n3; i++) {
    printf("%d ", sa_doubling[i]);
  }
  printf("\n");

  // 결과 일치 확인
  int match = 1;
  for (int i = 0; i < n3; i++) {
    if (sa_naive[i] != sa_doubling[i]) {
      match = 0;
      break;
    }
  }
  printf("결과 일치: %s\n", match ? "예" : "아니오");

  free(sa_naive);
  free(sa_doubling);
}

// 메인 함수 (완성됨)
int main() {
  test_suffix_array();
  return 0;
}
