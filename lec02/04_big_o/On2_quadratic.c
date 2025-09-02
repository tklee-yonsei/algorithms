// On2_quadratic.c
#include <stdbool.h>
#include <stdio.h>

// O(n^2) - 이차 시간복잡도
// 입력 크기의 제곱에 비례하여 시간이 증가

void bubble_sort(int arr[], int size) {
  // 버블 정렬 - O(n^2)
  for (int i = 0; i < size - 1; i++) {
    for (int j = 0; j < size - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        // 교환
        int temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
}

void find_duplicates(int arr[], int size, int duplicates[], int* dup_count) {
  // 중복 요소 찾기 - O(n^2)
  *dup_count = 0;
  for (int i = 0; i < size; i++) {
    for (int j = i + 1; j < size; j++) {
      if (arr[i] == arr[j]) {
        // 이미 추가되었는지 확인
        bool already_added = false;
        for (int k = 0; k < *dup_count; k++) {
          if (duplicates[k] == arr[i]) {
            already_added = true;
            break;
          }
        }
        if (!already_added) {
          duplicates[*dup_count] = arr[i];
          (*dup_count)++;
        }
      }
    }
  }
}

void print_pairs(int arr[], int size) {
  // 모든 쌍 출력 - O(n^2)
  for (int i = 0; i < size; i++) {
    for (int j = 0; j < size; j++) {
      printf("(%d, %d) ", arr[i], arr[j]);
    }
    printf("\n");
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
  int numbers[] = {4, 2, 7, 1, 9, 3};
  int size = sizeof(numbers) / sizeof(numbers[0]);

  printf("O(n^2) 예시들:\n");
  printf("원본 배열: ");
  print_array(numbers, size);
  printf("\n");

  // 버블 정렬
  int sorted_numbers[6];
  for (int i = 0; i < size; i++) {
    sorted_numbers[i] = numbers[i];
  }
  bubble_sort(sorted_numbers, size);
  printf("버블 정렬: ");
  print_array(sorted_numbers, size);
  printf("\n");

  // 중복 요소 찾기
  int numbers_with_duplicates[] = {1, 2, 3, 2, 4, 1, 5};
  int dup_size =
      sizeof(numbers_with_duplicates) / sizeof(numbers_with_duplicates[0]);
  int duplicates[10];
  int dup_count;
  find_duplicates(numbers_with_duplicates, dup_size, duplicates, &dup_count);

  printf("중복 요소: ");
  print_array(duplicates, dup_count);
  printf("\n");

  // 모든 쌍 출력 (작은 배열로)
  int small_array[] = {1, 2, 3};
  int small_size = sizeof(small_array) / sizeof(small_array[0]);
  printf("모든 쌍:\n");
  print_pairs(small_array, small_size);

  return 0;
}
