// insertionSort.c
#include <stdio.h>

// 삽입 정렬 함수
void insertionSort(int arr[], int size) {
  for (int i = 1; i < size; i++) {
    int key = arr[i];
    int j = i - 1;

    // key보다 큰 원소들을 오른쪽으로 이동
    while (j >= 0 && arr[j] > key) {
      arr[j + 1] = arr[j];
      j = j - 1;
    }

    // key를 올바른 위치에 삽입
    arr[j + 1] = key;
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

  insertionSort(arr, size);

  printf("정렬 후 배열: ");
  printArray(arr, size);

  return 0;
}
