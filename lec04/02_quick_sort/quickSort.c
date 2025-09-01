// quickSort.c
#include <stdio.h>
#include <stdlib.h>

// 두 요소를 교환하는 함수
void swap(int* a, int* b) {
  int temp = *a;
  *a = *b;
  *b = temp;
}

// 배열을 분할하는 함수 (Hoare partition scheme)
int partition(int arr[], int low, int high) {
  // 첫 번째 요소를 피벗으로 선택
  int pivot = arr[low];

  int i = low - 1;
  int j = high + 1;

  while (1) {
    // 왼쪽에서 피벗보다 큰 요소 찾기
    do {
      i++;
    } while (i <= high && arr[i] < pivot);

    // 오른쪽에서 피벗보다 작은 요소 찾기
    do {
      j--;
    } while (j >= low && arr[j] > pivot);

    // 교환할 요소가 없으면 종료
    if (i >= j) {
      return j;
    }

    // 요소 교환
    swap(&arr[i], &arr[j]);
  }
}

// 퀵 정렬 함수 (Hoare partition)
void quickSort(int arr[], int low, int high) {
  if (low < high) {
    // 분할
    int pivotIndex = partition(arr, low, high);

    // 정복
    quickSort(arr, low, pivotIndex);
    quickSort(arr, pivotIndex + 1, high);
  }
}

// 배열 출력 함수
void printArray(int arr[], int size) {
  for (int i = 0; i < size; i++) {
    printf("%d ", arr[i]);
  }
  printf("\n");
}

// 배열 복사 함수
void copyArray(int source[], int dest[], int size) {
  for (int i = 0; i < size; i++) {
    dest[i] = source[i];
  }
}

// 사용 예시
int main() {
  int arr[] = {64, 34, 25, 12, 22, 11, 90};
  int size = sizeof(arr) / sizeof(arr[0]);

  printf("정렬 전 배열: ");
  printArray(arr, size);

  // Hoare 방식 퀵 정렬
  quickSort(arr, 0, size - 1);
  printf("정렬 후 배열: ");
  printArray(arr, size);

  return 0;
}
