// performance_comparison.c
// Sequential Search vs Binary Search 성능 비교
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/resource.h>
#include <time.h>

// 메모리 사용량 측정 함수
long get_memory_usage() {
  struct rusage r_usage;
  getrusage(RUSAGE_SELF, &r_usage);
  return r_usage.ru_maxrss;  // KB 단위
}

// Sequential Search (선형 탐색)
int sequential_search(int arr[], int n, int target) {
  for (int i = 0; i < n; i++) {
    if (arr[i] == target) {
      return i;
    }
  }
  return -1;  // 찾지 못함
}

// Binary Search (이진 탐색) - 배열이 정렬되어 있어야 함
int binary_search(int arr[], int n, int target) {
  int left = 0;
  int right = n - 1;

  while (left <= right) {
    int mid = left + (right - left) / 2;

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

// 배열 정렬 함수 (Quick Sort)
void quick_sort(int arr[], int low, int high) {
  if (low < high) {
    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; j++) {
      if (arr[j] <= pivot) {
        i++;
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
      }
    }

    int temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;

    int pi = i + 1;
    quick_sort(arr, low, pi - 1);
    quick_sort(arr, pi + 1, high);
  }
}

// 성능 테스트 함수
void performance_test(int size) {
  printf("\n=== 배열 크기: %d ===\n", size);

  // 메모리 사용량 측정 시작
  long initial_memory = get_memory_usage();

  // 배열 생성 및 초기화
  int* arr = (int*)malloc(size * sizeof(int));
  if (arr == NULL) {
    printf("메모리 할당 실패!\n");
    return;
  }

  // 랜덤 데이터로 배열 초기화
  srand(time(NULL));
  for (int i = 0; i < size; i++) {
    arr[i] = rand() % (size * 10);  // 0 ~ size*10 범위의 랜덤 값
  }

  // Binary search를 위한 정렬
  int* sorted_arr = (int*)malloc(size * sizeof(int));
  memcpy(sorted_arr, arr, size * sizeof(int));
  quick_sort(sorted_arr, 0, size - 1);

  // 메모리 사용량 측정
  long after_allocation = get_memory_usage();
  long memory_used = after_allocation - initial_memory;

  printf("메모리 사용량: %ld KB\n", memory_used);

  // 테스트할 타겟 값들 (존재하는 값과 존재하지 않는 값)
  int test_targets[] = {arr[0], arr[size / 2], arr[size - 1], -1, size * 20};
  int num_tests = 5;

  printf("\n--- Sequential Search 성능 ---\n");
  clock_t seq_total_time = 0;

  for (int t = 0; t < num_tests; t++) {
    int target = test_targets[t];

    clock_t start = clock();
    int result = sequential_search(arr, size, target);
    clock_t end = clock();

    double time_taken =
        ((double)(end - start)) / CLOCKS_PER_SEC * 1000000;  // 마이크로초
    seq_total_time += (end - start);

    printf("타겟 %d: %d (%.2f μs)\n", target, result, time_taken);
  }

  printf("Sequential Search 평균 시간: %.2f μs\n",
         ((double)seq_total_time / CLOCKS_PER_SEC * 1000000) / num_tests);

  printf("\n--- Binary Search 성능 ---\n");
  clock_t bin_total_time = 0;

  for (int t = 0; t < num_tests; t++) {
    int target = test_targets[t];

    clock_t start = clock();
    int result = binary_search(sorted_arr, size, target);
    clock_t end = clock();

    double time_taken =
        ((double)(end - start)) / CLOCKS_PER_SEC * 1000000;  // 마이크로초
    bin_total_time += (end - start);

    printf("타겟 %d: %d (%.2f μs)\n", target, result, time_taken);
  }

  printf("Binary Search 평균 시간: %.2f μs\n",
         ((double)bin_total_time / CLOCKS_PER_SEC * 1000000) / num_tests);

  // 성능 비교
  double seq_avg =
      ((double)seq_total_time / CLOCKS_PER_SEC * 1000000) / num_tests;
  double bin_avg =
      ((double)bin_total_time / CLOCKS_PER_SEC * 1000000) / num_tests;

  printf("\n--- 성능 비교 ---\n");
  printf("Sequential Search: %.2f μs\n", seq_avg);
  printf("Binary Search: %.2f μs\n", bin_avg);

  if (seq_avg > bin_avg) {
    printf("Binary Search가 %.2f배 빠름\n", seq_avg / bin_avg);
  } else {
    printf("Sequential Search가 %.2f배 빠름\n", bin_avg / seq_avg);
  }

  // 메모리 해제
  free(arr);
  free(sorted_arr);
}

int main() {
  printf("Sequential Search vs Binary Search 성능 비교 (C)\n");
  printf("==============================================\n");

  // 다양한 크기로 테스트
  int sizes[] = {1000, 10000, 100000, 1000000};
  int num_sizes = 4;

  for (int i = 0; i < num_sizes; i++) {
    performance_test(sizes[i]);
  }

  printf("\n=== 결론 ===\n");
  printf("1. 메모리: 두 알고리즘 모두 O(n) 메모리 사용\n");
  printf("2. 시간 복잡도:\n");
  printf("   - Sequential Search: O(n)\n");
  printf("   - Binary Search: O(log n)\n");
  printf("3. Binary Search는 정렬이 필요하지만, 큰 데이터셋에서 훨씬 빠름\n");

  return 0;
}
