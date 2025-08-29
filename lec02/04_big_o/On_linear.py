# On_linear.py
# O(n) - 선형 시간복잡도
# 입력 크기에 비례하여 시간이 증가

def find_max(arr):
  """배열에서 최댓값 찾기 - O(n)"""
  if not arr:
    return None

  max_val = arr[0]
  for num in arr:
    if num > max_val:
      max_val = num
  return max_val


def count_occurrences(arr, target):
  """배열에서 특정 값의 개수 세기 - O(n)"""
  count = 0
  for num in arr:
    if num == target:
      count += 1
  return count


def reverse_array(arr):
  """배열 뒤집기 - O(n)"""
  return arr[::-1]


# 사용 예시
if __name__ == "__main__":
  numbers = [3, 7, 2, 9, 1, 5, 8, 4, 6]

  print("O(n) 예시들:")
  print(f"배열: {numbers}")
  print(f"최댓값: {find_max(numbers)}")
  print(f"5의 개수: {count_occurrences(numbers, 5)}")
  print(f"뒤집은 배열: {reverse_array(numbers)}")
