#include <limits.h>
#include <stdio.h>
#include <string.h>

#define MAX_AMOUNT 1000

int memo[MAX_AMOUNT + 1];

int coinChangeMemo(int amount, int coins[], int coinSize) {
  // 1. 초기 조건
  if (amount == 0)
    return 0;
  if (amount < 0)
    return INT_MAX;

  // 2. 메모이제이션 체크
  if (memo[amount] != -1)
    return memo[amount];

  printf("💭 계산: 금액 %d\n", amount);

  // 3. 재귀 호출
  int minCoins = INT_MAX;
  for (int i = 0; i < coinSize; i++) {
    int result = coinChangeMemo(amount - coins[i], coins, coinSize);
    if (result != INT_MAX) {
      if (result + 1 < minCoins) {
        minCoins = result + 1;
      }
    }
  }

  // 4. 메모이제이션 저장
  memo[amount] = minCoins;
  return minCoins;
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
  memset(memo, -1, sizeof(memo));
  int amount = 6;
  int coins[] = {2, 3, 5};
  int result = coinChangeMemo(amount, coins, 3);
  printf("결과: %d\n", result);
  print_array(memo, amount + 1);
  return 0;
}