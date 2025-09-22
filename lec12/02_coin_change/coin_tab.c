#include <limits.h>
#include <stdio.h>

#define MAX_AMOUNT 1000

int dp[MAX_AMOUNT + 1];

int coinChangeTab(int amount, int coins[], int coinSize) {
  // 1. 초기화
  for (int i = 0; i <= amount; i++) {
    dp[i] = INT_MAX;
  }
  dp[0] = 0;

  // 2. 계산
  for (int i = 1; i <= amount; i++) {
    printf("📊 계산: 금액 %d\n", i);
    for (int j = 0; j < coinSize; j++) {
      if (i >= coins[j] && dp[i - coins[j]] != INT_MAX) {
        if (dp[i - coins[j]] + 1 < dp[i]) {
          dp[i] = dp[i - coins[j]] + 1;
        }
      }
    }
  }

  // 3. 반환
  return dp[amount] == INT_MAX ? -1 : dp[amount];
}

void print_array(int arr[], int size) {
  printf("[");
  for (int i = 0; i < size; i++) {
    printf("%d", arr[i]);
    if (i < size - 1)
      printf(", ");
  }
  printf("]");
}

int main() {
  int amount = 6;
  int coins[] = {2, 3, 5};
  int result = coinChangeTab(amount, coins, 3);
  printf("결과: %d\n", result);
  print_array(dp, amount + 1);
  return 0;
}