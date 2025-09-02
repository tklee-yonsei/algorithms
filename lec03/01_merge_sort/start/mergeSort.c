// mergeSort.c
#include <stdio.h>
#include <stdlib.h>

// TODO: 두 개의 정렬된 부분 배열을 합치는 함수를 구현하세요
void merge(int arr[], int left, int mid, int right) {
  // 여기에 코드를 작성하세요
  // 힌트:
  // 1. 왼쪽과 오른쪽 부분 배열의 크기 계산
  // 2. 임시 배열들에 데이터 복사
  // 3. 두 배열을 비교하며 작은 값부터 원본 배열에 복사
  // 4. 남은 요소들 모두 복사
  // 5. 메모리 해제
}

// TODO: 병합 정렬 함수를 구현하세요
void mergeSort(int arr[], int left, int right) {
  // 여기에 코드를 작성하세요
  // 힌트:
  // 1. 베이스 케이스: left < right인지 확인
  // 2. 중간점 계산 (오버플로우 방지)
  // 3. 왼쪽 부분 재귀 정렬
  // 4. 오른쪽 부분 재귀 정렬
  // 5. 정렬된 두 부분을 합치기
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
