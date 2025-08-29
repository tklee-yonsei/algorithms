// On_linear.c
#include <stdio.h>

// O(n) - 선형 시간복잡도
// 입력 크기에 비례하여 시간이 증가

int find_max(int arr[], int size) {
  // 배열에서 최댓값 찾기 - O(n)
  if (size <= 0) {
    return -1;
  }

  int max_val = arr[0];
  for (int i = 1; i < size; i++) {
    if (arr[i] > max_val) {
      max_val = arr[i];
    }
  }
  return max_val;
}

int count_occurrences(int arr[], int size, int target) {
  // 배열에서 특정 값의 개수 세기 - O(n)
  int count = 0;
  for (int i = 0; i < size; i++) {
    if (arr[i] == target) {
      count++;
    }
  }
  return count;
}

void reverse_array(int arr[], int size) {
  // 배열 뒤집기 - O(n)
  for (int i = 0; i < size / 2; i++) {
    int temp = arr[i];
    arr[i] = arr[size - 1 - i];
    arr[size - 1 - i] = temp;
  }
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
  int numbers[] = {3, 7, 2, 9, 1, 5, 8, 4, 6};
  int size = sizeof(numbers) / sizeof(numbers[0]);

  printf("O(n) 예시들:\n");
  printf("배열: ");
  print_array(numbers, size);
  printf("\n");

  printf("최댓값: %d\n", find_max(numbers, size));
  printf("5의 개수: %d\n", count_occurrences(numbers, size, 5));

  reverse_array(numbers, size);
  printf("뒤집은 배열: ");
  print_array(numbers, size);
  printf("\n");

  return 0;
}
