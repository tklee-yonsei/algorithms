// sequentialSearch.c
#include <stdio.h>

// 순차 탐색 함수
int sequentialSearch(int arr[], int size, int target) {
  for (int i = 0; i < size; i++) {
    if (arr[i] == target) {
      return i;  // 찾은 인덱스 반환
    }
  }
  return -1;  // 찾지 못한 경우
}

// 사용 예시
int main() {
  int arr[] = {64, 34, 25, 12, 22, 11, 90};
  int size = sizeof(arr) / sizeof(arr[0]);
  int target = 22;

  int result = sequentialSearch(arr, size, target);

  if (result != -1) {
    printf("값 %d를 인덱스 %d에서 찾았습니다.\n", target, result);
  } else {
    printf("값 %d를 찾을 수 없습니다.\n", target);
  }

  return 0;
}