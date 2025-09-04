// lcp.c - LCP (Longest Common Prefix) (START CODE)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * LCP (Longest Common Prefix) 계산 구현 (C 언어)
 *
 * 시간 복잡도: O(n) per comparison
 * 공간 복잡도: O(1)
 */

// 함수 선언
void print_lcp_comparison(char* s, int i, int j, int lcp, int n);
void print_array(int arr[], int n);

/**
 * 두 위치의 LCP (Longest Common Prefix) 계산 (완성됨)
 *
 * @param s 문자열
 * @param i 첫 번째 위치
 * @param j 두 번째 위치
 * @param n 문자열 길이
 * @return LCP 길이
 */
int computeLCP(char* s, int i, int j, int n) {
  int lcp = 0;
  while (i + lcp < n && j + lcp < n && s[i + lcp] == s[j + lcp]) {
    lcp++;
  }
  return lcp;
}

/**
 * 주어진 모든 위치 쌍에 대해 LCP 계산 (완성됨)
 *
 * @param s 문자열
 * @param positions 위치 배열
 * @param n 문자열 길이
 * @param pos_count 위치 개수
 * @param results 결과를 저장할 2차원 배열
 */
void compute_all_lcp(char* s, int* positions, int n, int pos_count,
                     int results[][pos_count]) {
  for (int i = 0; i < pos_count; i++) {
    for (int j = 0; j < pos_count; j++) {
      if (i != j) {
        results[i][j] = computeLCP(s, positions[i], positions[j], n);
      } else {
        results[i][j] =
            n - positions[i];  // 자기 자신과의 LCP는 남은 문자열 길이
      }
    }
  }
}

/**
 * 모든 위치 쌍 중 최대 LCP 찾기 (완성됨)
 *
 * @param s 문자열
 * @param positions 위치 배열
 * @param n 문자열 길이
 * @param pos_count 위치 개수
 * @param best_i 최대 LCP를 가진 첫 번째 위치 (출력)
 * @param best_j 최대 LCP를 가진 두 번째 위치 (출력)
 * @return 최대 LCP 길이
 */
int find_max_lcp(char* s, int* positions, int n, int pos_count, int* best_i,
                 int* best_j) {
  int max_lcp = 0;
  *best_i = -1;
  *best_j = -1;

  for (int i = 0; i < pos_count; i++) {
    for (int j = i + 1; j < pos_count; j++) {
      int current_lcp = computeLCP(s, positions[i], positions[j], n);
      if (current_lcp > max_lcp) {
        max_lcp = current_lcp;
        *best_i = positions[i];
        *best_j = positions[j];
      }
    }
  }

  return max_lcp;
}

/**
 * TODO: Suffix Array로부터 LCP 배열 구축 (Kasai 알고리즘)
 *
 * @param text 문자열
 * @param sa suffix array
 * @param lcp 결과를 저장할 LCP 배열
 * @param n 문자열 길이
 */
void buildLCPKasai(char* text, int* sa, int* lcp, int n) {
  // TODO: Kasai 알고리즘을 구현하세요
  // 힌트:
  // 1. rank 배열 할당: int* rank = malloc(n * sizeof(int))
  // 2. Step 1: SA의 역함수 구성: rank[sa[i]] = i
  // 3. h = 0, lcp[0] = 0으로 초기화
  // 4. Step 2: 텍스트 순서로 각 suffix 처리 (i = 0 to n-1):
  //    - rank[i] > 0인 경우만 처리
  //    - j = sa[rank[i] - 1] (이전 suffix의 시작 위치)
  //    - h값부터 시작하여 공통 접두사 길이 계산
  //    - lcp[rank[i]] = h
  //    - 다음 iteration을 위해 h를 1 감소 (h > 0인 경우만)
  // 5. 메모리 해제: free(rank)

  printf("buildLCPKasai 구현 필요\n");
}

/**
 * LCP 비교 결과 출력 (완성됨)
 *
 * @param s 문자열
 * @param i 첫 번째 위치
 * @param j 두 번째 위치
 * @param lcp LCP 길이
 * @param n 문자열 길이
 */
void print_lcp_comparison(char* s, int i, int j, int lcp, int n) {
  printf("위치 %d: %s\n", i, s + i);
  printf("위치 %d: %s\n", j, s + j);
  printf("LCP 길이: %d\n", lcp);
  if (lcp > 0) {
    printf("공통 접두사: ");
    for (int k = 0; k < lcp; k++) {
      printf("%c", s[i + k]);
    }
    printf("\n");
  } else {
    printf("공통 접두사: 없음\n");
  }
}

/**
 * 배열 출력 (완성됨)
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
 * 테스트 함수 (완성됨)
 */
void test_lcp() {
  printf("=== LCP 계산 테스트 ===\n\n");

  // 테스트 케이스 1: 기본 LCP 계산
  printf("=== LCP 계산 테스트 1 ===\n");
  char text1[] = "banana$";
  int n1 = strlen(text1);
  printf("문자열: %s\n\n", text1);

  // 몇 가지 위치 쌍에 대해 LCP 계산
  int pairs[][2] = {{0, 1}, {0, 3}, {1, 3}, {2, 4}};
  int pair_count = sizeof(pairs) / sizeof(pairs[0]);

  for (int p = 0; p < pair_count; p++) {
    int i = pairs[p][0];
    int j = pairs[p][1];
    int lcp = computeLCP(text1, i, j, n1);
    print_lcp_comparison(text1, i, j, lcp, n1);
    printf("\n");
  }

  // 테스트 케이스 2: 반복 패턴에서 최대 LCP 찾기
  printf("=== LCP 계산 테스트 2 ===\n");
  char text2[] = "abcabcab";
  int n2 = strlen(text2);
  printf("문자열: %s\n", text2);

  int positions[] = {0, 1, 2, 3, 4, 5};
  int pos_count = 6;
  int best_i, best_j;
  int max_lcp = find_max_lcp(text2, positions, n2, pos_count, &best_i, &best_j);

  printf("최대 LCP: %d (위치 %d와 %d)\n", max_lcp, best_i, best_j);
  if (max_lcp > 0) {
    printf("공통 접두사: ");
    for (int k = 0; k < max_lcp; k++) {
      printf("%c", text2[best_i + k]);
    }
    printf("\n");
  }
  printf("\n");

  // 테스트 케이스 3: Suffix Array와 LCP 배열
  printf("=== Suffix Array와 LCP 배열 테스트 ===\n");
  char text3[] = "banana$";
  int n3 = strlen(text3);
  printf("문자열: %s\n", text3);

  // 미리 계산된 suffix array (실제로는 다른 알고리즘으로 구축)
  int suffix_array3[] = {6, 5, 3, 1, 0, 4, 2};
  int lcp_array3[n3];

  // LCP 배열 초기화
  for (int i = 0; i < n3; i++) {
    lcp_array3[i] = 0;
  }

  buildLCPKasai(text3, suffix_array3, lcp_array3, n3);

  printf("Suffix Array: ");
  print_array(suffix_array3, n3);
  printf("LCP Array: ");
  print_array(lcp_array3, n3);
  printf("\n");

  // LCP 배열의 각 값이 의미하는 바 설명
  printf("LCP 배열 상세 분석:\n");
  for (int i = 1; i < n3; i++) {
    int pos1 = suffix_array3[i - 1];
    int pos2 = suffix_array3[i];
    printf("SA[%d] = %d, SA[%d] = %d\n", i - 1, pos1, i, pos2);
    printf("LCP[%d] = %d\n", i, lcp_array3[i]);
    if (lcp_array3[i] > 0) {
      printf("공통 접두사: ");
      for (int k = 0; k < lcp_array3[i]; k++) {
        printf("%c", text3[pos1 + k]);
      }
      printf("\n");
    }
    printf("suffix[%d]: %s\n", pos1, text3 + pos1);
    printf("suffix[%d]: %s\n", pos2, text3 + pos2);
    printf("\n");
  }

  // 테스트 케이스 4: 모든 LCP 매트릭스
  printf("=== 모든 위치 쌍 LCP 매트릭스 ===\n");
  char text4[] = "ababa";
  int n4 = strlen(text4);
  printf("문자열: %s\n", text4);

  int positions4[] = {0, 1, 2, 3, 4};
  int pos_count4 = 5;
  int results[pos_count4][pos_count4];

  compute_all_lcp(text4, positions4, n4, pos_count4, results);

  printf("LCP 매트릭스:\n");
  printf("    ");
  for (int j = 0; j < pos_count4; j++) {
    printf("%3d", j);
  }
  printf("\n");

  for (int i = 0; i < pos_count4; i++) {
    printf("%2d: ", i);
    for (int j = 0; j < pos_count4; j++) {
      printf("%3d", results[i][j]);
    }
    printf("\n");
  }

  // 테스트 케이스 5: 특수 케이스
  printf("\n=== 특수 케이스 테스트 ===\n");

  // 다른 문자열로 테스트
  char text5[] = "mississippi$";
  int n5 = strlen(text5);
  printf("문자열: %s\n", text5);

  // 미리 계산된 suffix array
  int suffix_array5[] = {11, 10, 7, 4, 1, 0, 9, 8, 6, 3, 5, 2};
  int lcp_array5[n5];

  // LCP 배열 초기화
  for (int i = 0; i < n5; i++) {
    lcp_array5[i] = 0;
  }

  buildLCPKasai(text5, suffix_array5, lcp_array5, n5);

  printf("Suffix Array: ");
  print_array(suffix_array5, n5);
  printf("LCP Array: ");
  print_array(lcp_array5, n5);
}

// 메인 함수 (완성됨)
int main() {
  test_lcp();
  return 0;
}
