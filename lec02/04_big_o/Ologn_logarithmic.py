# Ologn_logarithmic.py
# O(log n) - 로그 시간복잡도
# 입력 크기의 로그에 비례하여 시간이 증가

def binary_search(arr, target):
  """이진 탐색 - O(log n)"""
  left, right = 0, len(arr) - 1

  while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
  return -1


def power_recursive(base, exponent):
  """거듭제곱 (재귀) - O(log n)"""
  if exponent == 0:
    return 1
  elif exponent % 2 == 0:
    half = power_recursive(base, exponent // 2)
    return half * half
  else:
    half = power_recursive(base, exponent // 2)
    return base * half * half


def find_peak(arr):
  """피크 찾기 (이진 탐색) - O(log n)"""
  left, right = 0, len(arr) - 1

  while left < right:
    mid = (left + right) // 2
    if arr[mid] < arr[mid + 1]:
      left = mid + 1
    else:
      right = mid

  return left


# 사용 예시
if __name__ == "__main__":
  print("O(log n) 예시들:")

  # 이진 탐색
  sorted_arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
  target = 7
  result = binary_search(sorted_arr, target)
  print(f"배열 {sorted_arr}에서 {target} 찾기: 인덱스 {result}")

  # 거듭제곱
  base, exp = 2, 10
  print(f"{base}^{exp} = {power_recursive(base, exp)}")

  # 피크 찾기
  peak_arr = [1, 3, 5, 4, 2, 0]
  peak_index = find_peak(peak_arr)
  print(f"배열 {peak_arr}의 피크: 인덱스 {peak_index}, 값 {peak_arr[peak_index]}")
