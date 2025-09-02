// selectionSort.c
#include <stdio.h>

// TODO: 선택 정렬 알고리즘을 구현하세요.
// 선택 정렬 함수
void selectionSort(int arr[], int size) {
  // 여기에 코드를 작성하세요
  // 힌트:
  // 1. 첫 번째 루프에서 정렬되지 않은 부분의 시작 인덱스를 설정
  // 2. 두 번째 루프에서 최솟값을 찾기
  // 3. 최솟값을 현재 위치와 교환
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

  selectionSort(arr, size);

  printf("정렬 후 배열: ");
  printArray(arr, size);

  return 0;
}
