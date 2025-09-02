// shellSort.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// TODO: 특정 gap 그룹에 대해 삽입 정렬을 수행하는 함수를 구현하세요
void insertion_sort_for_gap(int arr[], int n, int start, int gap) {
  // 여기에 코드를 작성하세요
  // 힌트: gap만큼 떨어진 요소들 사이에서 삽입 정렬 수행
}

// TODO: Shell Sort 메인 함수를 구현하세요
void shellSort(int arr[], int n) {
  // 여기에 코드를 작성하세요
  // 힌트:
  // 1. 초기 gap을 n/2로 설정
  // 2. gap을 점진적으로 줄여가며 (gap = gap/2) 각 그룹에 대해 삽입 정렬 수행
  // 3. gap이 0이 될 때까지 반복
  // Shell's original sequence: n/2, n/4, n/8, ..., 1
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
