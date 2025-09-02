# fibonacciRecursive.py
import time


def fibonacci_recursive(n):
  """재귀 방식 피보나치"""
  if n <= 1:
    return n
  else:
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# 사용 예시
if __name__ == "__main__":
  n = 35

  start_time = time.time()
  result = fibonacci_recursive(n)
  end_time = time.time()

  print(f"재귀 방식: fibonacci({n}) = {result}")
  print(f"실행시간: {end_time - start_time:.6f}초")
