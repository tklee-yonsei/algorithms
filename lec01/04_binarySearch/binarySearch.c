// binarySearch.c
#include <stdio.h>

// 이진 탐색 함수
int binarySearch(int arr[], int size, int target) {
  int left = 0;
  int right = size - 1;

  while (left <= right) {
    int mid = left + (right - left) / 2;  // 오버플로우 방지

    if (arr[mid] == target) {
      return mid;  // 찾은 인덱스 반환
    } else if (arr[mid] < target) {
      left = mid + 1;  // 오른쪽 절반 탐색
    } else {
      right = mid - 1;  // 왼쪽 절반 탐색
    }
  }

  return -1;  // 찾지 못한 경우
}

// 사용 예시
int main() {
  int arr[] = {11, 12, 22, 25, 34, 64, 90};  // 정렬된 배열
  int size = sizeof(arr) / sizeof(arr[0]);
  int target = 22;

  int result = binarySearch(arr, size, target);

  if (result != -1) {
    printf("값 %d를 인덱스 %d에서 찾았습니다.\n", target, result);
  } else {
    printf("값 %d를 찾을 수 없습니다.\n", target);
  }

  return 0;
}