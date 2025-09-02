// Onm.c
#include <stdbool.h>
#include <stdio.h>

// O(nm) - 두 개의 다른 크기에 비례하는 시간복잡도
// n과 m이 서로 다른 크기일 때

void matrix_multiply_simple(int a[][2], int b[][2], int result[][2], int rows,
                            int cols) {
  // 간단한 행렬 곱셈 - O(nm)
  for (int i = 0; i < rows; i++) {
    for (int j = 0; j < cols; j++) {
      result[i][j] = 0;
      for (int k = 0; k < cols; k++) {
        result[i][j] += a[i][k] * b[k][j];
      }
    }
  }
}

void find_common_elements(int arr1[], int size1, int arr2[], int size2,
                          int common[], int* common_count) {
  // 두 배열의 공통 요소 찾기 - O(nm)
  *common_count = 0;
  for (int i = 0; i < size1; i++) {
    for (int j = 0; j < size2; j++) {
      if (arr1[i] == arr2[j]) {
        // 이미 추가되었는지 확인
        bool already_added = false;
        for (int k = 0; k < *common_count; k++) {
          if (common[k] == arr1[i]) {
            already_added = true;
            break;
          }
        }
        if (!already_added) {
          common[*common_count] = arr1[i];
          (*common_count)++;
        }
      }
    }
  }
}

void cartesian_product(char set1[], int size1, int set2[], int size2) {
  // 카테시안 곱 - O(nm)
  printf("카테시안 곱: ");
  for (int i = 0; i < size1; i++) {
    for (int j = 0; j < size2; j++) {
      printf("(%c, %d) ", set1[i], set2[j]);
    }
  }
  printf("\n");
}

void print_matrix(int matrix[][2], int rows, int cols) {
  for (int i = 0; i < rows; i++) {
    printf("[");
    for (int j = 0; j < cols; j++) {
      printf("%d", matrix[i][j]);
      if (j < cols - 1)
        printf(" ");
    }
    printf("]\n");
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
  printf("O(nm) 예시들:\n");

  // 행렬 곱셈 예시
  int matrix_a[2][2] = {{1, 2}, {3, 4}};
  int matrix_b[2][2] = {{5, 6}, {7, 8}};
  int result[2][2];

  printf("행렬 A:\n");
  print_matrix(matrix_a, 2, 2);
  printf("행렬 B:\n");
  print_matrix(matrix_b, 2, 2);

  matrix_multiply_simple(matrix_a, matrix_b, result, 2, 2);
  printf("곱셈 결과:\n");
  print_matrix(result, 2, 2);

  // 공통 요소 찾기
  int arr1[] = {1, 2, 3, 4, 5};
  int arr2[] = {3, 4, 5, 6, 7};
  int size1 = sizeof(arr1) / sizeof(arr1[0]);
  int size2 = sizeof(arr2) / sizeof(arr2[0]);
  int common[10];
  int common_count;

  find_common_elements(arr1, size1, arr2, size2, common, &common_count);
  printf("공통 요소: ");
  print_array(common, common_count);
  printf("\n");

  // 카테시안 곱
  char set1[] = {'a', 'b'};
  int set2[] = {1, 2, 3};
  int set1_size = sizeof(set1) / sizeof(set1[0]);
  int set2_size = sizeof(set2) / sizeof(set2[0]);
  cartesian_product(set1, set1_size, set2, set2_size);

  return 0;
}
