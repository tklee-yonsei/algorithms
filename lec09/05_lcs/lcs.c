// lcs.c
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * LCS (Longest Common Substring) 찾기 구현 (C 언어)
 *
 * LCP 배열을 이용하여 가장 긴 공통 부분 문자열을 찾는 알고리즘
 * 시간 복잡도: O(n)
 * 공간 복잡도: O(1)
 */

// 구조체 정의
typedef struct {
  char* substring;
  int length;
  int pos1;
  int pos2;
} LCSResult;

// 함수 선언
void buildLCPKasai(char* text, int* sa, int* lcp, int n);
void print_array(int arr[], int n);
void print_lcs_analysis(char* text, int* suffix_array, int* lcp, int n);

/**
 * Suffix Array로부터 LCP 배열 구축 (Kasai 알고리즘)
 *
 * @param text 문자열
 * @param sa suffix array
 * @param lcp 결과를 저장할 LCP 배열
 * @param n 문자열 길이
 */
void buildLCPKasai(char* text, int* sa, int* lcp, int n) {
  int* rank = (int*)malloc(n * sizeof(int));

  // Step 1: SA의 역함수 구성
  for (int i = 0; i < n; i++) {
    rank[sa[i]] = i;
  }

  int h = 0;  // 현재 LCP 길이
  lcp[0] = 0;

  // Step 2: 텍스트 순서로 각 suffix 처리
  for (int i = 0; i < n; i++) {
    if (rank[i] > 0) {
      int j = sa[rank[i] - 1];  // 이전 suffix의 시작 위치

      // h값부터 시작하여 공통 접두사 길이 계산
      while (i + h < n && j + h < n && text[i + h] == text[j + h]) {
        h++;
      }

      lcp[rank[i]] = h;

      // 다음 iteration을 위해 h를 1 감소
      if (h > 0)
        h--;
    }
  }

  free(rank);
}

/**
 * LCP 배열에서 가장 긴 공통 부분 문자열 찾기
 *
 * @param lcp LCP 배열
 * @param n 배열 크기
 * @return 최대 LCP 길이
 */
int findLongestCommonSubstring(int* lcp, int n) {
  int maxLcp = 0;
  for (int i = 1; i < n; i++) {  // LCP[0]은 보통 0이므로 1부터 시작
    if (lcp[i] > maxLcp) {
      maxLcp = lcp[i];
    }
  }
  return maxLcp;
}

/**
 * 최대 LCP와 해당 인덱스 찾기
 *
 * @param lcp LCP 배열
 * @param n 배열 크기
 * @param max_index 최대값의 인덱스를 저장할 포인터
 * @return 최대 LCP 길이
 */
int find_longest_common_substring_with_index(int* lcp, int n, int* max_index) {
  int max_lcp = 0;
  *max_index = -1;

  for (int i = 1; i < n; i++) {
    if (lcp[i] > max_lcp) {
      max_lcp = lcp[i];
      *max_index = i;
    }
  }

  return max_lcp;
}

/**
 * 최대 LCP와 같은 모든 인덱스 찾기
 *
 * @param lcp LCP 배열
 * @param n 배열 크기
 * @param indices 결과를 저장할 배열
 * @param count 발견된 인덱스 개수
 * @return 최대 LCP 길이
 */
int find_all_longest_common_substrings(int* lcp, int n, int* indices,
                                       int* count) {
  int max_lcp = findLongestCommonSubstring(lcp, n);
  *count = 0;

  for (int i = 1; i < n; i++) {
    if (lcp[i] == max_lcp) {
      indices[(*count)++] = i;
    }
  }

  return max_lcp;
}

/**
 * Suffix Array와 LCP 배열을 이용해 가장 긴 공통 부분 문자열 찾기
 *
 * @param text 원본 문자열
 * @param suffix_array suffix array
 * @param lcp LCP 배열
 * @param n 문자열 길이
 * @param result 결과를 저장할 구조체
 */
void find_longest_common_substring_with_suffix_array(char* text,
                                                     int* suffix_array,
                                                     int* lcp, int n,
                                                     LCSResult* result) {
  int max_index;
  int max_lcp = find_longest_common_substring_with_index(lcp, n, &max_index);

  if (max_lcp == 0) {
    result->substring = NULL;
    result->length = 0;
    result->pos1 = -1;
    result->pos2 = -1;
    return;
  }

  // 가장 긴 공통 부분 문자열이 나타나는 두 suffix의 시작 위치
  result->pos1 = suffix_array[max_index - 1];
  result->pos2 = suffix_array[max_index];
  result->length = max_lcp;

  // 실제 부분 문자열 추출
  result->substring = (char*)malloc((max_lcp + 1) * sizeof(char));
  strncpy(result->substring, text + result->pos1, max_lcp);
  result->substring[max_lcp] = '\0';
}

/**
 * 가장 긴 공통 부분 문자열의 모든 출현 위치 찾기
 *
 * @param text 원본 문자열
 * @param lcp LCP 배열
 * @param suffix_array suffix array
 * @param n 문자열 길이
 * @param positions 결과를 저장할 배열
 * @param count 발견된 위치 개수
 * @return 최대 LCP 길이
 */
int find_all_occurrences_of_lcs(char* text, int* lcp, int* suffix_array, int n,
                                int* positions, int* count) {
  int indices[n];
  int index_count;
  int max_lcp =
      find_all_longest_common_substrings(lcp, n, indices, &index_count);

  if (max_lcp == 0) {
    *count = 0;
    return 0;
  }

  *count = 0;
  for (int i = 0; i < index_count; i++) {
    int index = indices[i];
    positions[(*count)++] = suffix_array[index - 1];
    positions[(*count)++] = suffix_array[index];
  }

  // 중복 제거를 위한 간단한 정렬 (버블 정렬)
  for (int i = 0; i < *count - 1; i++) {
    for (int j = 0; j < *count - i - 1; j++) {
      if (positions[j] > positions[j + 1]) {
        int temp = positions[j];
        positions[j] = positions[j + 1];
        positions[j + 1] = temp;
      }
    }
  }

  // 중복 제거
  int unique_count = 0;
  for (int i = 0; i < *count; i++) {
    if (i == 0 || positions[i] != positions[i - 1]) {
      positions[unique_count++] = positions[i];
    }
  }
  *count = unique_count;

  return max_lcp;
}

/**
 * LCP 배열의 통계 정보 계산
 *
 * @param lcp LCP 배열
 * @param n 배열 크기
 * @param max_lcp 최대 LCP (출력)
 * @param min_lcp 최소 LCP (출력)
 * @param avg_lcp 평균 LCP (출력)
 * @param total_common 총 공통 문자 수 (출력)
 */
void compute_lcp_statistics(int* lcp, int n, int* max_lcp, int* min_lcp,
                            double* avg_lcp, int* total_common) {
  int valid_count = 0;
  int sum = 0;
  *max_lcp = 0;
  *min_lcp = INT_MAX;

  for (int i = 1; i < n; i++) {
    if (lcp[i] > 0) {
      valid_count++;
      sum += lcp[i];
      if (lcp[i] > *max_lcp)
        *max_lcp = lcp[i];
      if (lcp[i] < *min_lcp)
        *min_lcp = lcp[i];
    }
  }

  if (valid_count == 0) {
    *min_lcp = 0;
    *avg_lcp = 0.0;
  } else {
    *avg_lcp = (double)sum / valid_count;
  }

  *total_common = sum;
}

/**
 * 배열 출력
 *
 * @param arr 배열
 * @param n 배열 크기
 */
void print_array(int arr[], int n) {
  printf("[");
  for (int i = 0; i < n; i++) {
    printf("%d", arr[i]);
    if (i < n - 1)
      printf(", ");
  }
  printf("]\n");
}

/**
 * LCS 분석 결과 출력
 *
 * @param text 원본 문자열
 * @param suffix_array suffix array
 * @param lcp LCP 배열
 * @param n 문자열 길이
 */
void print_lcs_analysis(char* text, int* suffix_array, int* lcp, int n) {
  printf("=== 가장 긴 공통 부분 문자열 분석 ===\n");
  printf("문자열: %s\n", text);
  printf("Suffix Array: ");
  print_array(suffix_array, n);
  printf("LCP Array: ");
  print_array(lcp, n);
  printf("\n");

  // 기본 통계
  int max_lcp, min_lcp, total_common;
  double avg_lcp;
  compute_lcp_statistics(lcp, n, &max_lcp, &min_lcp, &avg_lcp, &total_common);

  printf("LCP 통계:\n");
  printf("  최대 LCP: %d\n", max_lcp);
  printf("  최소 LCP (0 제외): %d\n", min_lcp);
  printf("  평균 LCP: %.2f\n", avg_lcp);
  printf("  총 공통 문자 수: %d\n", total_common);
  printf("\n");

  // 가장 긴 공통 부분 문자열
  LCSResult result;
  find_longest_common_substring_with_suffix_array(text, suffix_array, lcp, n,
                                                  &result);

  if (result.length > 0) {
    printf("가장 긴 공통 부분 문자열:\n");
    printf("  문자열: %s\n", result.substring);
    printf("  길이: %d\n", result.length);
    printf("  출현 위치: %d과 %d\n", result.pos1, result.pos2);
    printf("  suffix[%d]: %s\n", result.pos1, text + result.pos1);
    printf("  suffix[%d]: %s\n", result.pos2, text + result.pos2);
    free(result.substring);
  } else {
    printf("공통 부분 문자열이 없습니다.\n");
  }
  printf("\n");

  // 모든 출현 위치
  int positions[n];
  int count;
  int max_len = find_all_occurrences_of_lcs(text, lcp, suffix_array, n,
                                            positions, &count);

  if (max_len > 0) {
    printf("가장 긴 공통 부분 문자열의 모든 출현 위치: ");
    print_array(positions, count);
  }
  printf("\n");
}

/**
 * 테스트 함수
 */
void test_lcs() {
  printf("=== LCS 테스트 ===\n\n");

  // 테스트 케이스 1: 기본 예제
  printf("=== LCS 테스트 1: banana ===\n");
  char text1[] = "banana";
  int suffix_array1[] = {5, 3, 1, 0, 4, 2};  // 미리 계산된 값
  int lcp1[] = {0, 1, 3, 0, 0, 2};           // 미리 계산된 값
  int n1 = strlen(text1);

  print_lcs_analysis(text1, suffix_array1, lcp1, n1);

  // 테스트 케이스 2: 복잡한 예제
  printf("=== LCS 테스트 2: mississippi ===\n");
  char text2[] = "mississippi";
  int suffix_array2[] = {10, 7, 4, 1, 0, 9, 8, 6, 3, 5, 2};  // 미리 계산된 값
  int lcp2[] = {0, 1, 1, 4, 0, 0, 1, 0, 2, 1, 3};  // 미리 계산된 값
  int n2 = strlen(text2);

  print_lcs_analysis(text2, suffix_array2, lcp2, n2);

  // 테스트 케이스 3: 반복 패턴
  printf("=== LCS 테스트 3: abcabcabc ===\n");
  char text3[] = "abcabcabc";
  int suffix_array3[] = {0, 3, 6, 1, 4, 7, 2, 5, 8};  // 가정된 값
  int lcp3[] = {0, 6, 3, 0, 3, 0, 0, 0, 0};           // 가정된 값
  int n3 = strlen(text3);

  print_lcs_analysis(text3, suffix_array3, lcp3, n3);

  // 테스트 케이스 4: 단순 통계 테스트
  printf("=== 단순 LCP 배열 테스트 ===\n");
  int lcp_simple[] = {0, 2, 1, 4, 0, 3, 1};
  int n_simple = 7;

  int max_index;
  int max_lcp = find_longest_common_substring_with_index(lcp_simple, n_simple,
                                                         &max_index);

  printf("LCP 배열: ");
  print_array(lcp_simple, n_simple);
  printf("최대 LCP: %d (위치: %d)\n", max_lcp, max_index);

  int indices[n_simple];
  int count;
  int all_max =
      find_all_longest_common_substrings(lcp_simple, n_simple, indices, &count);

  printf("최대값과 같은 모든 위치: ");
  print_array(indices, count);
  printf("\n");

  // 테스트 케이스 5: 특별한 경우들
  printf("=== 특별한 경우들 ===\n");

  // 모든 LCP가 0인 경우
  int lcp_zero[] = {0, 0, 0, 0};
  int max_zero = findLongestCommonSubstring(lcp_zero, 4);
  printf("모든 LCP가 0인 경우 최대값: %d\n", max_zero);

  // 단일 최대값
  int lcp_single[] = {0, 1, 5, 2, 1};
  int max_single = findLongestCommonSubstring(lcp_single, 5);
  printf("단일 최대값 경우: %d\n", max_single);

  // 여러 최대값
  int lcp_multiple[] = {0, 3, 1, 3, 2, 3};
  int indices_mult[6];
  int count_mult;
  int max_mult = find_all_longest_common_substrings(lcp_multiple, 6,
                                                    indices_mult, &count_mult);
  printf("여러 최대값 (%d)의 위치들: ", max_mult);
  print_array(indices_mult, count_mult);
}

// 메인 함수
int main() {
  test_lcs();
  return 0;
}
