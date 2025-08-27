// On3_cubic.c
#include <stdio.h>

// O(n^3) - 삼차 시간복잡도
// 입력 크기의 세제곱에 비례하여 시간이 증가

void find_triplets(int arr[], int size, int triplets[][3], int* triplet_count) {
  // 세 개의 요소로 이루어진 모든 조합 찾기 - O(n^3)
  *triplet_count = 0;
  for (int i = 0; i < size; i++) {
    for (int j = i + 1; j < size; j++) {
      for (int k = j + 1; k < size; k++) {
        triplets[*triplet_count][0] = arr[i];
        triplets[*triplet_count][1] = arr[j];
        triplets[*triplet_count][2] = arr[k];
        (*triplet_count)++;
      }
    }
  }
}

void matrix_multiply_3d(int a[][2][2], int b[][2][2], int c[][2][2],
                        int result[][2][2], int n) {
  // 3차원 행렬 곱셈 - O(n^3)
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      for (int k = 0; k < n; k++) {
        result[i][j][k] = 0;
        for (int l = 0; l < n; l++) {
          result[i][j][k] += a[i][j][l] * b[l][j][k] * c[i][l][k];
        }
      }
    }
  }
}

void find_all_triangles(int points[][2], int size, int triangles[][3][2],
                        int* triangle_count) {
  // 모든 삼각형 조합 찾기 - O(n^3)
  *triangle_count = 0;
  for (int i = 0; i < size; i++) {
    for (int j = i + 1; j < size; j++) {
      for (int k = j + 1; k < size; k++) {
        // 삼각형의 세 점 저장
        triangles[*triangle_count][0][0] = points[i][0];
        triangles[*triangle_count][0][1] = points[i][1];
        triangles[*triangle_count][1][0] = points[j][0];
        triangles[*triangle_count][1][1] = points[j][1];
        triangles[*triangle_count][2][0] = points[k][0];
        triangles[*triangle_count][2][1] = points[k][1];
        (*triangle_count)++;
      }
    }
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

void print_triplets(int triplets[][3], int count) {
  printf("[");
  for (int i = 0; i < count; i++) {
    printf("(%d, %d, %d)", triplets[i][0], triplets[i][1], triplets[i][2]);
    if (i < count - 1)
      printf(", ");
  }
  printf("]");
}

void print_triangles(int triangles[][3][2], int count) {
  printf("[");
  for (int i = 0; i < count; i++) {
    printf("((%d,%d), (%d,%d), (%d,%d))", triangles[i][0][0],
           triangles[i][0][1], triangles[i][1][0], triangles[i][1][1],
           triangles[i][2][0], triangles[i][2][1]);
    if (i < count - 1)
      printf(", ");
  }
  printf("]");
}

int main() {
  printf("O(n^3) 예시들:\n");

  // 모든 삼중 조합 찾기
  int numbers[] = {1, 2, 3, 4};
  int size = sizeof(numbers) / sizeof(numbers[0]);
  int triplets[100][3];
  int triplet_count;

  printf("배열: ");
  print_array(numbers, size);
  printf("\n");

  find_triplets(numbers, size, triplets, &triplet_count);
  printf("모든 삼중 조합: ");
  print_triplets(triplets, triplet_count);
  printf("\n");

  // 간단한 3차원 행렬 예시 (2x2x2)
  int matrix_3d[2][2][2] = {{{1, 2}, {3, 4}}, {{5, 6}, {7, 8}}};
  printf("3차원 행렬: [2x2x2]\n");

  // 점들의 삼각형 조합
  int points[][2] = {{0, 0}, {1, 0}, {0, 1}, {1, 1}};
  int points_size = sizeof(points) / sizeof(points[0]);
  int triangles[100][3][2];
  int triangle_count;

  find_all_triangles(points, points_size, triangles, &triangle_count);
  printf("삼각형 조합: ");
  print_triangles(triangles, triangle_count);
  printf("\n");

  return 0;
}
