// shellSort.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 특정 gap 그룹에 대해 삽입 정렬을 수행하는 함수
void insertion_sort_for_gap(int arr[], int n, int start, int gap) {
  int i, j, temp;

  // 현재 gap 그룹의 요소들을 삽입 정렬
  for (i = start + gap; i < n; i += gap) {
    temp = arr[i];

    // gap만큼 떨어진 요소들과 비교하여 삽입
    for (j = i; j >= start + gap && arr[j - gap] > temp; j -= gap) {
      arr[j] = arr[j - gap];
    }
    arr[j] = temp;
  }
}

// Shell Sort 메인 함수 (Shell's original sequence 사용)
void shellSort(int arr[], int n) {
  int gap, start;

  // Shell's original sequence: n/2, n/4, n/8, ..., 1
  for (gap = n / 2; gap > 0; gap = gap / 2) {
    // 각 gap 그룹에 대해 삽입 정렬 수행
    for (start = 0; start < gap; start++) {
      insertion_sort_for_gap(arr, n, start, gap);
    }
  }
}

// 배열 출력 함수
void printArray(int arr[], int n) {
  for (int i = 0; i < n; i++) {
    printf("%d ", arr[i]);
  }
  printf("\n");
}

// 사용 예시
int main() {
  int arr[] = {64, 34, 25, 12, 22, 11, 90};
  int n = sizeof(arr) / sizeof(arr[0]);

  printf("정렬 전 배열: ");
  printArray(arr, n);

  shellSort(arr, n);

  printf("정렬 후 배열: ");
  printArray(arr, n);

  return 0;
}
