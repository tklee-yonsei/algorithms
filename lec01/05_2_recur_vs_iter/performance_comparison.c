// performance_comparison.c
// Fibonacci Recursive vs Iterative 성능 비교
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/resource.h>
#include <time.h>

// 메모리 사용량 측정 함수
long get_memory_usage() {
  struct rusage r_usage;
  getrusage(RUSAGE_SELF, &r_usage);
  return r_usage.ru_maxrss;  //ㄱ KB 단위
}

// 재귀 방식 피보나치 - O(2^n)
long long fibonacci_recursive(int n) {
  if (n <= 1) {
    return n;
  }
  return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2);
}

// 반복 방식 피보나치 - O(n)
long long fibonacci_iterative(int n) {
  if (n <= 1) {
    return n;
  }

  long long a = 0, b = 1;
  for (int i = 2; i <= n; i++) {
    long long temp = a + b;
    a = b;
    b = temp;
  }
  return b;
}

// 성능 테스트 함수
void performance_test(int n) {
  printf("\n=== 피보나치(%d) 성능 테스트 ===\n", n);

  // 메모리 사용량 측정 시작
  long initial_memory = get_memory_usage();

  // 각 알고리즘별 성능 측정
  struct {
    char* name;
    long long (*func)(int);
    long long result;
    double time_taken;
    int success;
  } algorithms[] = {{"반복 방식", fibonacci_iterative, 0, 0.0, 0}};

  int num_algorithms = sizeof(algorithms) / sizeof(algorithms[0]);

  // 반복, 동적 프로그래밍, 메모이제이션 테스트
  for (int i = 0; i < num_algorithms; i++) {
    clock_t start = clock();
    algorithms[i].result = algorithms[i].func(n);
    clock_t end = clock();

    algorithms[i].time_taken =
        ((double)(end - start)) / CLOCKS_PER_SEC * 1000000;  // 마이크로초
    algorithms[i].success = (algorithms[i].result != -1);

    if (algorithms[i].success) {
      printf("%s: %lld (%.2f μs)\n", algorithms[i].name, algorithms[i].result,
             algorithms[i].time_taken);
    } else {
      printf("%s: 오류 발생\n", algorithms[i].name);
    }
  }

  // 재귀 방식 테스트 (작은 값에서만)
  if (n <= 40) {  // 재귀는 큰 값에서 너무 느림
    clock_t start = clock();
    long long result = fibonacci_recursive(n);
    clock_t end = clock();

    double time_taken =
        ((double)(end - start)) / CLOCKS_PER_SEC * 1000000;  // 마이크로초
    printf("재귀 방식: %lld (%.2f μs)\n", result, time_taken);

    // 재귀 결과를 배열에 추가
    algorithms[num_algorithms - 1].result = result;
    algorithms[num_algorithms - 1].time_taken = time_taken;
    algorithms[num_algorithms - 1].success = 1;
  } else {
    printf("재귀 방식: n이 너무 커서 건너뜀 (n > 40)\n");
  }

  // 메모리 사용량 측정
  long final_memory = get_memory_usage();
  long memory_used = final_memory - initial_memory;
  printf("메모리 사용량: %ld KB\n", memory_used);

  // 성능 비교
  printf("\n--- 성능 비교 ---\n");
  double fastest_time = __DBL_MAX__;
  double slowest_time = 0.0;
  char* fastest_name = NULL;
  char* slowest_name = NULL;

  for (int i = 0; i < num_algorithms; i++) {
    if (algorithms[i].success) {
      if (algorithms[i].time_taken < fastest_time) {
        fastest_time = algorithms[i].time_taken;
        fastest_name = algorithms[i].name;
      }
      if (algorithms[i].time_taken > slowest_time) {
        slowest_time = algorithms[i].time_taken;
        slowest_name = algorithms[i].name;
      }
    }
  }

  if (fastest_name && slowest_name) {
    printf("가장 빠른 알고리즘: %s (%.2f μs)\n", fastest_name, fastest_time);
    printf("가장 느린 알고리즘: %s (%.2f μs)\n", slowest_name, slowest_time);

    if (fastest_time > 0) {
      double speedup = slowest_time / fastest_time;
      printf("성능 차이: %.2f배\n", speedup);
    }
  }

  // 결과 검증
  printf("\n--- 결과 검증 ---\n");
  long long first_result = -1;
  int all_same = 1;

  for (int i = 0; i < num_algorithms; i++) {
    if (algorithms[i].success) {
      if (first_result == -1) {
        first_result = algorithms[i].result;
      } else if (algorithms[i].result != first_result) {
        all_same = 0;
        break;
      }
    }
  }

  if (all_same) {
    printf("✓ 모든 알고리즘이 동일한 결과를 반환\n");
  } else {
    printf("✗ 알고리즘 간 결과가 다름\n");
  }
}

int main() {
  printf("Fibonacci Recursive vs Iterative 성능 비교 (C)\n");
  printf("============================================\n");

  // 다양한 n값으로 테스트
  int test_values[] = {10, 20, 30, 35, 40, 50, 100};
  int num_tests = sizeof(test_values) / sizeof(test_values[0]);

  for (int i = 0; i < num_tests; i++) {
    performance_test(test_values[i]);
  }

  printf("\n=== 결론 ===\n");
  printf("1. 시간 복잡도:\n");
  printf("   - 재귀 방식: O(2^n) - 지수적 증가\n");
  printf("   - 반복 방식: O(n) - 선형 증가\n");
  printf("2. 공간 복잡도:\n");
  printf("   - 재귀 방식: O(n) - 스택 공간\n");
  printf("   - 반복 방식: O(1) - 상수 공간\n");
  printf("3. 권장사항:\n");
  printf("   - 작은 n (n < 40): 모든 방식 사용 가능\n");
  printf("   - 큰 n (n >= 40): 반복 방식 권장\n");
  printf("   - 메모리 제약: 반복 방식 권장\n");

  return 0;
}
