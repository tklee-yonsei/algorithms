// bubbleSort.c
#include <stdbool.h>
#include <stdio.h>

// 버블 정렬 함수 (기본 버전)
void bubbleSort(int arr[], int size) {
  // 모든 패스를 수행 (size-1번)
  for (int i = 0; i < size - 1; i++) {
    // 마지막 i개 요소는 이미 정렬됨
    for (int j = 0; j < size - i - 1; j++) {
      // 인접한 요소들을 비교
      if (arr[j] > arr[j + 1]) {
        // 큰 요소를 뒤로 보내기 (swap)
        int temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
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
