# Onm.py
# O(nm) - 두 개의 다른 크기에 비례하는 시간복잡도
# n과 m이 서로 다른 크기일 때

def matrix_multiply_simple(a, b):
  """간단한 행렬 곱셈 - O(nm)"""
  if len(a[0]) != len(b):
    return None

  result = []
  for i in range(len(a)):
    row = []
    for j in range(len(b[0])):
      sum_val = 0
      for k in range(len(b)):
        sum_val += a[i][k] * b[k][j]
      row.append(sum_val)
    result.append(row)
  return result


def find_common_elements(arr1, arr2):
  """두 배열의 공통 요소 찾기 - O(nm)"""
  common = []
  for num1 in arr1:
    for num2 in arr2:
      if num1 == num2 and num1 not in common:
        common.append(num1)
  return common


def cartesian_product(arr1, arr2):
  """카테시안 곱 - O(nm)"""
  result = []
  for item1 in arr1:
    for item2 in arr2:
      result.append((item1, item2))
  return result


# 사용 예시
if __name__ == "__main__":
  # 행렬 곱셈 예시
  matrix_a = [[1, 2], [3, 4]]
  matrix_b = [[5, 6], [7, 8]]

  print("O(nm) 예시들:")
  print(f"행렬 A: {matrix_a}")
  print(f"행렬 B: {matrix_b}")
  print(f"곱셈 결과: {matrix_multiply_simple(matrix_a, matrix_b)}")

  # 공통 요소 찾기
  arr1 = [1, 2, 3, 4, 5]
  arr2 = [3, 4, 5, 6, 7]
  print(f"공통 요소: {find_common_elements(arr1, arr2)}")

  # 카테시안 곱
  set1 = ['a', 'b']
  set2 = [1, 2, 3]
  print(f"카테시안 곱: {cartesian_product(set1, set2)}")
