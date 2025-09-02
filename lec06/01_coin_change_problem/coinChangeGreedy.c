// coinChangeGreedy.c
#include <stdio.h>
#include <stdlib.h>

// 내림차순 정렬을 위한 비교 함수
int compare_desc(const void *a, const void *b) {
  return (*(int *)b - *(int *)a);
}

// 탐욕 알고리즘을 사용하여 동전 교환 문제를 해결하는 함수
int coin_change_greedy(int coins[], int coin_count, int amount, int result[]) {
  // 동전을 내림차순으로 정렬
  qsort(coins, coin_count, sizeof(int), compare_desc);

  int result_count = 0;

  for (int i = 0; i < coin_count; i++) {
    int count = amount / coins[i];
    if (count > 0) {
      // 결과 배열에 동전 추가
      for (int j = 0; j < count; j++) {
        result[result_count++] = coins[i];
      }
      amount %= coins[i];
    }
  }

  return result_count;
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

  // 추가 테스트 케이스
  printf("\n--- 추가 테스트 케이스 ---\n");

  // 테스트 케이스 1
  int coins1[] = {500, 100, 50, 10};
  int amount1 = 380;
  int result1[100];
  int count1 = coin_change_greedy(coins1, 4, amount1, result1);
  printf("동전: [500, 100, 50, 10], 금액: %d -> 사용된 동전: ", amount1);
  print_array(result1, count1);
  printf(", 개수: %d\n", count1);

  // 테스트 케이스 2
  int coins2[] = {500, 100, 50, 10};
  int amount2 = 1000;
  int result2[100];
  int count2 = coin_change_greedy(coins2, 4, amount2, result2);
  printf("동전: [500, 100, 50, 10], 금액: %d -> 사용된 동전: ", amount2);
  print_array(result2, count2);
  printf(", 개수: %d\n", count2);

  return 0;
}
