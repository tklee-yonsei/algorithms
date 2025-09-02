// binarySearch.c
#include <stdio.h>

// TODO: 정렬된 배열에서 특정 값을 이진 탐색으로 찾는 함수를 작성하세요.
// 이진 탐색 함수
int binarySearch(int arr[], int size, int target) {
  // 여기에 코드를 작성하세요
  // 힌트: left, right, mid 변수를 사용하세요
  return -1;
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
