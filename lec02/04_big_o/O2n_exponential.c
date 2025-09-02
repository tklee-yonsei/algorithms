// O2n_exponential.c
#include <stdio.h>
#include <stdlib.h>

// O(2^n) - 지수 시간복잡도
// 입력 크기에 대해 지수적으로 시간이 증가

int fibonacci_recursive(int n) {
  // 피보나치 수열 (재귀) - O(2^n)
  if (n <= 1) {
    return n;
  }
  return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2);
}

void generate_subsets_recursive(int arr[], int size, int current[],
                                int current_size, int start, int subsets[][10],
                                int* subset_count) {
  // 모든 부분집합 생성 - O(2^n)
  // 현재 부분집합을 결과에 추가
  for (int i = 0; i < current_size; i++) {
    subsets[*subset_count][i] = current[i];
  }
  subsets[*subset_count][current_size] = -1;  // 끝 표시
  (*subset_count)++;

  // 다음 요소들을 추가하여 부분집합 생성
  for (int i = start; i < size; i++) {
    current[current_size] = arr[i];
    generate_subsets_recursive(arr, size, current, current_size + 1, i + 1,
                               subsets, subset_count);
  }
}

void generate_subsets(int arr[], int size, int subsets[][10],
                      int* subset_count) {
  int current[10];
  *subset_count = 0;
  generate_subsets_recursive(arr, size, current, 0, 0, subsets, subset_count);
}

void hanoi_towers(int n, char source, char auxiliary, char target) {
  // 하노이 탑 - O(2^n)
  if (n == 1) {
    printf("원반 1을 %c에서 %c로 이동\n", source, target);
    return;
  }

  hanoi_towers(n - 1, source, target, auxiliary);
  printf("원반 %d을 %c에서 %c로 이동\n", n, source, target);
  hanoi_towers(n - 1, auxiliary, source, target);
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

void print_subsets(int subsets[][10], int subset_count) {
  printf("[");
  for (int i = 0; i < subset_count; i++) {
    printf("[");
    int j = 0;
    while (subsets[i][j] != -1) {
      printf("%d", subsets[i][j]);
      if (subsets[i][j + 1] != -1)
        printf(", ");
      j++;
    }
    printf("]");
    if (i < subset_count - 1)
      printf(", ");
  }
  printf("]");
}

int main() {
  printf("O(2^n) 예시들:\n");

  // 피보나치 (작은 수로 테스트)
  int n = 8;
  printf("피보나치(%d) = %d\n", n, fibonacci_recursive(n));

  // 부분집합 생성
  int arr[] = {1, 2, 3};
  int size = sizeof(arr) / sizeof(arr[0]);
  int subsets[100][10];
  int subset_count;

  generate_subsets(arr, size, subsets, &subset_count);
  printf("배열 ");
  print_array(arr, size);
  printf("의 모든 부분집합: ");
  print_subsets(subsets, subset_count);
  printf("\n");

  // 하노이 탑 (3개 원반)
  printf("하노이 탑 (3개 원반):\n");
  hanoi_towers(3, 'A', 'B', 'C');

  return 0;
}
