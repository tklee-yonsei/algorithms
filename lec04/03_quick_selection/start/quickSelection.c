// quickSelection.c
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

// TODO: k번째로 작은 원소를 찾는 함수를 구현하세요 (0-based index)
int quickSelect(int arr[], int low, int high, int k) {
  // 여기에 코드를 작성하세요
  // 힌트:
  // 1. 베이스 케이스: low == high이면 arr[low] 반환
  // 2. partition 함수로 배열 분할
  // 3. k의 위치에 따라 왼쪽 또는 오른쪽 부분에서 재귀 호출
  //    - k <= pivotIndex이면 왼쪽 부분에서 탐색
  //    - 그렇지 않으면 오른쪽 부분에서 탐색
  return -1;
}

// TODO: k번째로 작은 원소를 찾는 함수를 구현하세요 (1-based index, 사용자
// 친화적)
int findKthSmallest(int arr[], int size, int k) {
  // 여기에 코드를 작성하세요
  // 힌트:
  // 1. k가 유효한 범위인지 확인 (1 <= k <= size)
  // 2. 배열을 복사하여 원본 배열 보존
  // 3. quickSelect 함수 호출 (k-1로 0-based 변환)
  // 4. 메모리 해제 후 결과 반환
  return -1;
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
