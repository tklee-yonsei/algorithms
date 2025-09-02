# fibonacciIterative.py
import time


def fibonacci_iterative(n):
  """반복 방식 피보나치"""
  if n <= 1:
    return n

  a, b = 0, 1

  for i in range(2, n + 1):
    a, b = b, a + b  # Python의 튜플 할당 활용

  return b


# 사용 예시
if __name__ == "__main__":
  n = 50

  start_time = time.time()
  result = fibonacci_iterative(n)
  end_time = time.time()

  print(f"반복 방식: fibonacci({n}) = {result}")
  print(f"실행시간: {end_time - start_time:.6f}초")
