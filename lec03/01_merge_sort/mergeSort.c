// mergeSort.c
#include <stdio.h>
#include <stdlib.h>

// 두 개의 정렬된 부분 배열을 합치는 함수
void merge(int arr[], int left, int mid, int right) {
  int i, j, k;
  int n1 = mid - left + 1;  // 왼쪽 부분 배열의 크기
  int n2 = right - mid;     // 오른쪽 부분 배열의 크기

  // 임시 배열 생성
  int *leftArr = (int *)malloc(n1 * sizeof(int));
  int *rightArr = (int *)malloc(n2 * sizeof(int));

  // 임시 배열에 데이터 복사
  for (i = 0; i < n1; i++)
    leftArr[i] = arr[left + i];
  for (j = 0; j < n2; j++)
    rightArr[j] = arr[mid + 1 + j];

  // 두 배열을 비교하며 작은 값부터 원본 배열에 복사
  i = 0;     // 왼쪽 배열의 인덱스
  j = 0;     // 오른쪽 배열의 인덱스
  k = left;  // 원본 배열의 인덱스

  while (i < n1 && j < n2) {
    if (leftArr[i] <= rightArr[j]) {
      arr[k] = leftArr[i];
      i++;
    } else {
      arr[k] = rightArr[j];
      j++;
    }
    k++;
  }

  // 남은 요소들 복사
  while (i < n1) {
    arr[k] = leftArr[i];
    i++;
    k++;
  }

  while (j < n2) {
    arr[k] = rightArr[j];
    j++;
    k++;
  }

  // 메모리 해제
  free(leftArr);
  free(rightArr);
}

// 병합 정렬 함수
void mergeSort(int arr[], int left, int right) {
  if (left < right) {
    // 중간점 계산 (오버플로우 방지)
    int mid = left + (right - left) / 2;

    // 왼쪽 부분 정렬
    mergeSort(arr, left, mid);

    // 오른쪽 부분 정렬
    mergeSort(arr, mid + 1, right);

    // 정렬된 두 부분을 합치기
    merge(arr, left, mid, right);
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

  mergeSort(arr, 0, size - 1);

  printf("정렬 후 배열: ");
  printArray(arr, size);

  return 0;
}
