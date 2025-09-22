#include <stdio.h>
#include <string.h>

#define MAX_N 100

int memo[MAX_N][MAX_N + 1];  // memo[i][prev_idx+1]

/**
 * @brief 최대값 함수
 *
 * @param a 첫 번째 값
 * @param b 두 번째 값
 * @return int 최대값
 */
int max(int a, int b) {
  return a > b ? a : b;
}

/**
 * @brief 최장 증가 부분 수열 도우미 함수
 *
 * @param arr 배열
 * @param n 배열의 크기
 * @param i 현재 인덱스
 * @param prev_idx 이전 인덱스
 * @return int 최장 증가 부분 수열의 길이
 */
int lisHelper(int arr[], int n, int i, int prev_idx) {
  // TODO: 메모이제이션을 이용한 LIS 구하기
  // prev_idx는 -1부터 시작하므로 배열 인덱스로 사용시 +1 필요
  return 0;  // 임시 반환값
}

int lisMemo(int arr[], int n) {
  memset(memo, -1, sizeof(memo));
  return lisHelper(arr, n, 0, -1);
}

int main() {
  int arr[] = {10, 9, 2, 5, 3, 7, 101, 18};
  int n = sizeof(arr) / sizeof(arr[0]);
  int result = lisMemo(arr, n);
  printf("결과: %d\n", result);
  return 0;
}