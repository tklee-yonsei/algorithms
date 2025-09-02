// countingSort.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 함수 선언
void print_array(int arr[], int n);

// TODO: 배열의 최대값과 최소값을 찾는 함수를 구현하세요
void find_min_max(int arr[], int n, int *min_val, int *max_val) {
  // 여기에 코드를 작성하세요
  // 힌트:
  // 1. 첫 번째 원소로 min_val, max_val 초기화
  // 2. 배열을 순회하며 최소값과 최대값 업데이트
}

// TODO: 카운팅 정렬 함수를 구현하세요
void counting_sort(int arr[], int n, int result[]) {
  // 여기에 코드를 작성하세요
  // 힌트:
  // 1. 최대값과 최소값 찾기
  // 2. 값의 범위 계산 및 카운팅 배열 동적 할당
  // 3. 각 원소의 개수 세기
  // 4. 카운팅 배열을 누적합으로 변환
  // 5. 원본 배열을 뒤에서부터 순회하며 결과 배열에 배치
  // 6. 메모리 해제
}

// 배열 출력 함수
void print_array(int arr[], int n) {
  printf("[");
  for (int i = 0; i < n; i++) {
    printf("%d", arr[i]);
    if (i < n - 1) {
      printf(", ");
    }
  }
  printf("]\n");
}

// 사용 예시
int main() {
  int arr[] = {4, 2, 2, 8, 3, 3, 1};
  int n = sizeof(arr) / sizeof(arr[0]);
  int result[n];

  printf("정렬 전: ");
  print_array(arr, n);

  counting_sort(arr, n, result);

  printf("정렬 후: ");
  print_array(result, n);

  return 0;
}
