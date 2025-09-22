#include <stdio.h>

int max(int a, int b) {
  return a > b ? a : b;
}

int lisTab(int arr[], int n) {
  return 0;
}

int main() {
  int arr[] = {10, 9, 2, 5, 3, 7, 101, 18};
  int n = sizeof(arr) / sizeof(arr[0]);
  int result = lisTab(arr, n);
  printf("결과: %d\n", result);
  return 0;
}