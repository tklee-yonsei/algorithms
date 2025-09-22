#include <limits.h>
#include <stdio.h>

#define MAX_AMOUNT 1000

int dp[MAX_AMOUNT + 1];

int coinChangeTab(int amount, int coins[], int coinSize) {
  // TODO: 테이블을 이용한 구현
  // 힌트: dp 배열 생성, 이중 반복문 사용
  return -1;  // 임시 반환값
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