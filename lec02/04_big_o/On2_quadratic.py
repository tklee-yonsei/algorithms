# On2_quadratic.py
# O(n^2) - 이차 시간복잡도
# 입력 크기의 제곱에 비례하여 시간이 증가

def bubble_sort(arr):
  """버블 정렬 - O(n^2)"""
  n = len(arr)
  for i in range(n):
    for j in range(0, n - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
  return arr


def find_duplicates(arr):
  """중복 요소 찾기 - O(n^2)"""
  duplicates = []
  for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
      if arr[i] == arr[j] and arr[i] not in duplicates:
        duplicates.append(arr[i])
  return duplicates


def print_pairs(arr):
  """모든 쌍 출력 - O(n^2)"""
  for i in range(len(arr)):
    for j in range(len(arr)):
      print(f"({arr[i]}, {arr[j]})", end=" ")
    print()


# 사용 예시
if __name__ == "__main__":
  numbers = [4, 2, 7, 1, 9, 3]

  print("O(n^2) 예시들:")
  print(f"원본 배열: {numbers}")
  print(f"버블 정렬: {bubble_sort(numbers.copy())}")

  numbers_with_duplicates = [1, 2, 3, 2, 4, 1, 5]
  print(f"중복 요소: {find_duplicates(numbers_with_duplicates)}")

  small_array = [1, 2, 3]
  print("모든 쌍:")
  print_pairs(small_array)
