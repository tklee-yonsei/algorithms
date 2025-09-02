// quickSort.c
#include <stdio.h>
#include <stdlib.h>

void swap(int* a, int* b) {
  int temp = *a;
  *a = *b;
  *b = temp;
}

// TODO: 배열을 분할하는 함수를 구현하세요 (Hoare partition scheme)
int partition(int arr[], int low, int high) {
  // 여기에 코드를 작성하세요
  // 힌트:
  // 1. 첫 번째 요소를 피벗으로 선택
  // 2. i를 low-1, j를 high+1로 초기화
  // 3. 무한 루프에서:
  //    - 왼쪽에서 피벗보다 큰 요소 찾기
  //    - 오른쪽에서 피벗보다 작은 요소 찾기
  //    - i >= j이면 j 반환
  //    - 그렇지 않으면 arr[i]와 arr[j] 교환
  return -1;
}

// TODO: 퀵 정렬 함수를 구현하세요
void quickSort(int arr[], int low, int high) {
  // 여기에 코드를 작성하세요
  // 힌트:
  // 1. 베이스 케이스: low < high인지 확인
  // 2. partition 함수로 배열 분할
  // 3. 왼쪽 부분 재귀 정렬
  // 4. 오른쪽 부분 재귀 정렬
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

  quickSort(arr, 0, size - 1);

  printf("정렬 후 배열: ");
  printArray(arr, size);

  return 0;
}
