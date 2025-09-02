// insertionSort.c
#include <stdio.h>

// TODO: 삽입 정렬 알고리즘을 구현하세요.
// 삽입 정렬 함수
void insertionSort(int arr[], int size) {
  // 여기에 코드를 작성하세요
  // 힌트:
  // 1. 두 번째 요소부터 시작 (첫 번째는 이미 정렬됨)
  // 2. 현재 요소(key)를 저장
  // 3. key보다 큰 요소들을 오른쪽으로 이동
  // 4. key를 올바른 위치에 삽입
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

  insertionSort(arr, size);

  printf("정렬 후 배열: ");
  printArray(arr, size);

  return 0;
}
