# On3_cubic.py
# O(n^3) - 삼차 시간복잡도
# 입력 크기의 세제곱에 비례하여 시간이 증가

def find_triplets(arr):
  """세 개의 요소로 이루어진 모든 조합 찾기 - O(n^3)"""
  triplets = []
  for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
      for k in range(j + 1, len(arr)):
        triplets.append((arr[i], arr[j], arr[k]))
  return triplets


def matrix_multiply_3d(a, b, c):
  """3차원 행렬 곱셈 - O(n^3)"""
  n = len(a)
  result = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]

  for i in range(n):
    for j in range(n):
      for k in range(n):
        for l in range(n):
          result[i][j][k] += a[i][j][l] * b[l][j][k] * c[i][l][k]
  return result


def find_all_triangles(points):
  """모든 삼각형 조합 찾기 - O(n^3)"""
  triangles = []
  for i in range(len(points)):
    for j in range(i + 1, len(points)):
      for k in range(j + 1, len(points)):
        triangles.append((points[i], points[j], points[k]))
  return triangles


# 사용 예시
if __name__ == "__main__":
  numbers = [1, 2, 3, 4]

  print("O(n^3) 예시들:")
  print(f"배열: {numbers}")
  print(f"모든 삼중 조합: {find_triplets(numbers)}")

  # 간단한 3차원 행렬 예시 (2x2x2)
  matrix_3d = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
  print(f"3차원 행렬: {matrix_3d}")

  # 점들의 삼각형 조합
  points = [(0, 0), (1, 0), (0, 1), (1, 1)]
  print(f"삼각형 조합: {find_all_triangles(points)}")
