// coinChangeGreedy.c
#include <stdio.h>
#include <stdlib.h>

// 내림차순 정렬을 위한 비교 함수
int compare_desc(const void *a, const void *b) {
  return (*(int *)b - *(int *)a);
}

// TODO: 탐욕 알고리즘을 사용하여 동전 교환 문제를 해결하는 함수를 작성하세요.
int coin_change_greedy(int coins[], int coin_count, int amount, int result[]) {
  // TODO: 여기에 탐욕 알고리즘을 구현하세요
  // 1. 동전을 내림차순으로 정렬 (qsort 사용)
  qsort(coins, coin_count, sizeof(int), compare_desc);
  // 2. 가장 큰 동전부터 가능한 많이 사용
  // 3. 남은 금액에 대해 다음 큰 동전으로 반복
  // 4. 사용된 총 동전 개수를 반환
  return 0;
}

// 배열 출력 함수
void print_array(int arr[], int size) {
  printf("[");
  for (int i = 0; i < size; i++) {
    printf("%d", arr[i]);
    if (i < size - 1)
      printf(", ");
  }
  printf("]");
}

// 사용 예시
int main() {
  int coins[] = {500, 100, 50, 10};
  int coin_count = 4;
  int amount = 1260;
  int result[100];  // 충분한 크기의 결과 배열

  int count = coin_change_greedy(coins, coin_count, amount, result);

  printf("사용된 동전: ");
  print_array(result, count);
  printf("\n총 동전 개수: %d\n", count);

  return 0;
}
