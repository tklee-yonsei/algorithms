// fibonacciRecursive.c
#include <stdio.h>
#include <time.h>

// 재귀 방식 피보나치
long long fibonacciRecursive(int n) {
  if (n <= 1) {
    return n;
  } else {
    return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
  }
}

// 사용 예시
int main() {
  int n = 43;

  clock_t start = clock();
  long long result = fibonacciRecursive(n);
  clock_t end = clock();

  double cpu_time = ((double)(end - start)) / CLOCKS_PER_SEC;

  printf("재귀 방식: fibonacci(%d) = %lld\n", n, result);
  printf("실행시간: %f초\n", cpu_time);

  return 0;
}