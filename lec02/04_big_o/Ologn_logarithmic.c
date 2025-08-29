// Ologn_logarithmic.c
#include <stdio.h>

// O(log n) - 로그 시간복잡도
// 입력 크기의 로그에 비례하여 시간이 증가

int binary_search(int arr[], int size, int target) {
  // 이진 탐색 - O(log n)
  int left = 0;
  int right = size - 1;

  while (left <= right) {
    int mid = (left + right) / 2;
    if (arr[mid] == target) {
      return mid;
    } else if (arr[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  return -1;  // 찾지 못함
}

int power_recursive(int base, int exponent) {
  // 거듭제곱 (재귀) - O(log n)
  if (exponent == 0) {
    return 1;
  } else if (exponent % 2 == 0) {
    int half = power_recursive(base, exponent / 2);
    return half * half;
  } else {
    int half = power_recursive(base, exponent / 2);
    return base * half * half;
  }
}

int find_peak(int arr[], int size) {
  // 피크 찾기 (이진 탐색) - O(log n)
  int left = 0;
  int right = size - 1;

  while (left < right) {
    int mid = (left + right) / 2;
    if (arr[mid] < arr[mid + 1]) {
      left = mid + 1;
    } else {
      right = mid;
    }
  }

  return left;
}

void print_array(int arr[], int size) {
  printf("[");
  for (int i = 0; i < size; i++) {
    printf("%d", arr[i]);
    if (i < size - 1)
      printf(", ");
  }
  printf("]");
}

int main() {
  printf("O(log n) 예시들:\n");

  // 이진 탐색
  int sorted_arr[] = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19};
  int size = sizeof(sorted_arr) / sizeof(sorted_arr[0]);
  int target = 7;
  int result = binary_search(sorted_arr, size, target);

  printf("배열 ");
  print_array(sorted_arr, size);
  printf("에서 %d 찾기: 인덱스 %d\n", target, result);

  // 거듭제곱
  int base = 2, exp = 10;
  printf("%d^%d = %d\n", base, exp, power_recursive(base, exp));

  // 피크 찾기
  int peak_arr[] = {1, 3, 5, 4, 2, 0};
  int peak_size = sizeof(peak_arr) / sizeof(peak_arr[0]);
  int peak_index = find_peak(peak_arr, peak_size);

  printf("배열 ");
  print_array(peak_arr, peak_size);
  printf("의 피크: 인덱스 %d, 값 %d\n", peak_index, peak_arr[peak_index]);

  return 0;
}
