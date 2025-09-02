# fibonacciRecursive.py
import time

# TODO: 재귀 방식으로 피보나치 수를 계산하는 함수를 작성하세요.


def fibonacci_recursive(n):
  """재귀 방식 피보나치"""
  # 여기에 코드를 작성하세요
  return -1


# 사용 예시
if __name__ == "__main__":
  n = 35

  start_time = time.time()
  result = fibonacci_recursive(n)
  end_time = time.time()

  print(f"재귀 방식: fibonacci({n}) = {result}")
  print(f"실행시간: {end_time - start_time:.6f}초")
