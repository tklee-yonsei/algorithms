// fibonacciIterative.c
#include <stdio.h>
#include <time.h>

// TODO: 반복 방식으로 피보나치 수를 계산하는 함수를 작성하세요.
// 반복 방식 피보나치
long long fibonacciIterative(int n) {
  // 여기에 코드를 작성하세요
  return -1;
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
