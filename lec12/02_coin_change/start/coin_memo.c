#include <limits.h>
#include <stdio.h>
#include <string.h>

#define MAX_AMOUNT 1000

int memo[MAX_AMOUNT + 1];

int coinChangeMemo(int amount, int coins[], int coinSize) {
  // TODO: 메모이제이션을 이용한 구현
  // 힌트: memo 배열을 -1로 초기화하여 미계산 상태 표시
  // 재귀 호출로 구현
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
  memset(memo, -1, sizeof(memo));
  int amount = 6;
  int coins[] = {2, 3, 5};
  int result = coinChangeMemo(amount, coins, 3);
  printf("결과: %d\n", result);
  print_array(memo, amount + 1);
  return 0;
}