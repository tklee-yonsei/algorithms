// bubbleSort.c
#include <stdbool.h>
#include <stdio.h>

// TODO: 버블 정렬 알고리즘을 구현하세요.
// 버블 정렬 함수 (기본 버전)
void bubbleSort(int arr[], int size) {
  // 여기에 코드를 작성하세요
  // 힌트:
  // 1. 외부 루프: 패스 횟수 (size-1번)
  // 2. 내부 루프: 인접한 요소들 비교
  // 3. 큰 요소를 뒤로 보내기 (swap)
  // 4. 각 패스마다 마지막 요소는 이미 정렬됨
}

// 배열 출력 함수
void printArray(int arr[], int size) {
  for (int i = 0; i < size; i++) {
    printf("%d ", arr[i]);
  }
  printf("\n");
}

// 사용 예시
int main() {
  int arr[] = {64, 34, 25, 12, 22, 11, 90};
  int size = sizeof(arr) / sizeof(arr[0]);

  printf("정렬 전 배열: ");
  printArray(arr, size);

  bubbleSort(arr, size);

  printf("정렬 후 배열: ");
  printArray(arr, size);

  return 0;
}
