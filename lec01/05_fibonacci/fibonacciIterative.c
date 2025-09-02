// fibonacciIterative.c
#include <stdio.h>
#include <time.h>

// 반복 방식 피보나치
long long fibonacciIterative(int n) {
  if (n <= 1) {
    return n;
  }

  long long a = 0, b = 1, temp;

  for (int i = 2; i <= n; i++) {
    temp = a + b;
    a = b;
    b = temp;
  }

  return b;
}

// 사용 예시
int main() {
  int n = 50;

  clock_t start = clock();
  long long result = fibonacciIterative(n);
  clock_t end = clock();

  double cpu_time = ((double)(end - start)) / CLOCKS_PER_SEC;

  printf("반복 방식: fibonacci(%d) = %lld\n", n, result);
  printf("실행시간: %f초\n", cpu_time);

  return 0;
}
