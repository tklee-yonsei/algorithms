// shellSort.c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void insertion_sort_for_gap(int arr[], int n, int start, int gap) {
  /*
   * 특정 gap 그룹에 대해 삽입 정렬을 수행하는 함수
   * arr: 정렬할 배열
   * n: 배열 크기
   * start: 그룹의 시작 인덱스
   * gap: 간격
   */
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

void shellSort(int arr[], int n) {
  int gap, start;

  // gap을 n/2부터 시작하여 점진적으로 줄여나감
  for (gap = n / 2; gap > 0; gap /= 2) {
    // 각 gap 그룹에 대해 삽입 정렬 수행
    for (start = 0; start < gap; start++) {
      insertion_sort_for_gap(arr, n, start, gap);
    }
  }
}

void printArray(int arr[], int n) {
  for (int i = 0; i < n; i++) {
    printf("%d ", arr[i]);
  }
  printf("\n");
}

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
