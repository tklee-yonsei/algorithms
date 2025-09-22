#include <stdio.h>

int max(int a, int b) {
  return a > b ? a : b;
}

int lisTab(int arr[], int n) {
  int dp[n];

  // 초기화: 각 원소 하나만으로는 길이 1
  for (int i = 0; i < n; i++) {
    dp[i] = 1;
  }

  for (int i = 1; i < n; i++) {
    printf("📊 계산: index %d (값: %d)\n", i, arr[i]);
    for (int j = 0; j < i; j++) {
      if (arr[j] < arr[i]) {
        dp[i] = max(dp[i], dp[j] + 1);
      }
    }
  }

  // 최대값 찾기
  int result = dp[0];
  for (int i = 1; i < n; i++) {
    result = max(result, dp[i]);
  }

  return result;
}

int main() {
  int arr[] = {10, 9, 2, 5, 3, 7, 101, 18};
  int n = sizeof(arr) / sizeof(arr[0]);
  int result = lisTab(arr, n);
  printf("결과: %d\n", result);
  return 0;
}