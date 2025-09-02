// quickSelection.c
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

// k번째로 작은 원소를 찾는 함수 (0-based index)
int quickSelect(int arr[], int low, int high, int k) {
  if (low == high) {
    return arr[low];
  }

  // 분할
  int pivotIndex = partition(arr, low, high);

  // k번째 원소의 위치 확인
  if (k <= pivotIndex) {
    // k번째 원소가 왼쪽 부분에 있음
    return quickSelect(arr, low, pivotIndex, k);
  } else {
    // k번째 원소가 오른쪽 부분에 있음
    return quickSelect(arr, pivotIndex + 1, high, k);
  }
}

// k번째로 작은 원소를 찾는 함수 (1-based index, 사용자 친화적)
int findKthSmallest(int arr[], int size, int k) {
  if (k < 1 || k > size) {
    printf("오류: k는 1부터 %d 사이의 값이어야 합니다.\n", size);
    return -1;
  }

  // 배열을 복사하여 원본 배열을 보존
  int* tempArr = (int*)malloc(size * sizeof(int));
  for (int i = 0; i < size; i++) {
    tempArr[i] = arr[i];
  }

  int result = quickSelect(tempArr, 0, size - 1, k - 1);  // 0-based로 변환

  free(tempArr);
  return result;
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
  int arr[] = {64, 34, 25, 12, 22, 11, 90, 3, 77, 45};
  int size = sizeof(arr) / sizeof(arr[0]);

  printf("원본 배열: ");
  printArray(arr, size);

  // 다양한 k값에 대해 테스트
  for (int k = 1; k <= size; k++) {
    int kthSmallest = findKthSmallest(arr, size, k);
    if (kthSmallest != -1) {
      printf("%d번째로 작은 원소: %d\n", k, kthSmallest);
    }
  }

  // 특별한 케이스들 테스트
  printf("\n특별한 케이스들:\n");
  printf("가장 작은 원소 (1번째): %d\n", findKthSmallest(arr, size, 1));
  printf("중앙값 (median, %d번째): %d\n", (size + 1) / 2,
         findKthSmallest(arr, size, (size + 1) / 2));
  printf("가장 큰 원소 (%d번째): %d\n", size, findKthSmallest(arr, size, size));

  return 0;
}
