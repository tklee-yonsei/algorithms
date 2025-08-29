// Onlogn_linearithmic.c
#include <stdio.h>
#include <stdlib.h>

// O(n log n) - 선형로그 시간복잡도
// 입력 크기와 로그의 곱에 비례하여 시간이 증가

void merge(int left[], int left_size, int right[], int right_size,
           int result[]) {
  // 병합 함수
  int i = 0, j = 0, k = 0;

  while (i < left_size && j < right_size) {
    if (left[i] <= right[j]) {
      result[k++] = left[i++];
    } else {
      result[k++] = right[j++];
    }
  }

  // 남은 요소들 복사
  while (i < left_size) {
    result[k++] = left[i++];
  }
  while (j < right_size) {
    result[k++] = right[j++];
  }
}

void merge_sort(int arr[], int size) {
  // 병합 정렬 - O(n log n)
  if (size <= 1) {
    return;
  }

  int mid = size / 2;
  int* left = (int*)malloc(mid * sizeof(int));
  int* right = (int*)malloc((size - mid) * sizeof(int));

  // 배열 분할
  for (int i = 0; i < mid; i++) {
    left[i] = arr[i];
  }
  for (int i = mid; i < size; i++) {
    right[i - mid] = arr[i];
  }

  // 재귀적으로 정렬
  merge_sort(left, mid);
  merge_sort(right, size - mid);

  // 병합
  merge(left, mid, right, size - mid, arr);

  free(left);
  free(right);
}

void quick_sort(int arr[], int low, int high) {
  // 퀵 정렬 - O(n log n) 평균
  if (low < high) {
    // 피벗 선택 (간단하게 중간값 사용)
    int pivot = arr[(low + high) / 2];
    int i = low - 1;
    int j = high + 1;

    while (1) {
      do {
        i++;
      } while (arr[i] < pivot);

      do {
        j--;
      } while (arr[j] > pivot);

      if (i >= j)
        break;

      // 교환
      int temp = arr[i];
      arr[i] = arr[j];
      arr[j] = temp;
    }

    quick_sort(arr, low, j);
    quick_sort(arr, j + 1, high);
  }
}

void heapify(int arr[], int n, int i) {
  // 힙 구성 함수
  int largest = i;
  int left = 2 * i + 1;
  int right = 2 * i + 2;

  if (left < n && arr[left] > arr[largest]) {
    largest = left;
  }

  if (right < n && arr[right] > arr[largest]) {
    largest = right;
  }

  if (largest != i) {
    int temp = arr[i];
    arr[i] = arr[largest];
    arr[largest] = temp;
    heapify(arr, n, largest);
  }
}

void heap_sort(int arr[], int size) {
  // 힙 정렬 - O(n log n)

  // 힙 구성
  for (int i = size / 2 - 1; i >= 0; i--) {
    heapify(arr, size, i);
  }

  // 힙에서 요소 추출
  for (int i = size - 1; i > 0; i--) {
    int temp = arr[0];
    arr[0] = arr[i];
    arr[i] = temp;
    heapify(arr, i, 0);
  }
}

void print_array(int arr[], int size) {
  printf("[");
  for (int i = 0; i < size; i++) {
    printf("%d", arr[i]);
    if (i < size - 1)
      printf(", ");
  }
  printf("]");
}

void copy_array(int source[], int dest[], int size) {
  for (int i = 0; i < size; i++) {
    dest[i] = source[i];
  }
}

int main() {
  printf("O(n log n) 예시들:\n");

  // 병합 정렬
  int arr1[] = {64, 34, 25, 12, 22, 11, 90};
  int size1 = sizeof(arr1) / sizeof(arr1[0]);
  int sorted1[10];

  copy_array(arr1, sorted1, size1);
  printf("원본 배열: ");
  print_array(arr1, size1);
  printf("\n");

  merge_sort(sorted1, size1);
  printf("병합 정렬: ");
  print_array(sorted1, size1);
  printf("\n");

  // 퀵 정렬
  int arr2[] = {38, 27, 43, 3, 9, 82, 10};
  int size2 = sizeof(arr2) / sizeof(arr2[0]);
  int sorted2[10];

  copy_array(arr2, sorted2, size2);
  quick_sort(sorted2, 0, size2 - 1);
  printf("퀵 정렬: ");
  print_array(sorted2, size2);
  printf("\n");

  // 힙 정렬
  int arr3[] = {12, 11, 13, 5, 6, 7};
  int size3 = sizeof(arr3) / sizeof(arr3[0]);
  int sorted3[10];

  copy_array(arr3, sorted3, size3);
  heap_sort(sorted3, size3);
  printf("힙 정렬: ");
  print_array(sorted3, size3);
  printf("\n");

  return 0;
}
