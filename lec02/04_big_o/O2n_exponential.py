# O2n_exponential.py
# O(2^n) - 지수 시간복잡도
# 입력 크기에 대해 지수적으로 시간이 증가

def fibonacci_recursive(n):
  """피보나치 수열 (재귀) - O(2^n)"""
  if n <= 1:
    return n
  return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def generate_subsets(arr):
  """모든 부분집합 생성 - O(2^n)"""
  def backtrack(start, current):
    result.append(current[:])
    for i in range(start, len(arr)):
      current.append(arr[i])
      backtrack(i + 1, current)
      current.pop()

  result = []
  backtrack(0, [])
  return result


def hanoi_towers(n, source, auxiliary, target):
  """하노이 탑 - O(2^n)"""
  if n == 1:
    print(f"원반 1을 {source}에서 {target}로 이동")
    return

  hanoi_towers(n - 1, source, target, auxiliary)
  print(f"원반 {n}을 {source}에서 {target}로 이동")
  hanoi_towers(n - 1, auxiliary, source, target)


# 사용 예시
if __name__ == "__main__":
  print("O(2^n) 예시들:")

  # 피보나치 (작은 수로 테스트)
  n = 8
  print(f"피보나치({n}) = {fibonacci_recursive(n)}")

  # 부분집합 생성
  arr = [1, 2, 3]
  subsets = generate_subsets(arr)
  print(f"배열 {arr}의 모든 부분집합: {subsets}")

  # 하노이 탑 (3개 원반)
  print("하노이 탑 (3개 원반):")
  hanoi_towers(3, 'A', 'B', 'C')
