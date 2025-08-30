# countingSort.py

def find_min_max(arr):
  """최대값과 최소값 찾기"""
  min_val = arr[0]
  max_val = arr[0]
  for num in arr:
    if num < min_val:
      min_val = num
    if num > max_val:
      max_val = num
  return min_val, max_val


def counting_sort(arr):
  """
  카운팅 정렬 알고리즘

  Args:
      arr: 정렬할 정수 배열

  Returns:
      정렬된 배열

  시간 복잡도: O(n + k) - n은 원소 개수, k는 값의 범위
  공간 복잡도: O(k) - 카운팅 배열을 위한 공간
  """
  if not arr:
    return []

  # 1. 최대값과 최소값 찾기
  min_val, max_val = find_min_max(arr)

  # 2. 카운팅 배열 초기화
  range_size = max_val - min_val + 1
  offset = -min_val
  count = [0] * range_size

  # 3. 각 원소의 개수 세기
  for num in arr:
    count[num + offset] += 1

  # 4. 카운팅 배열을 누적합으로 변환
  for i in range(1, len(count)):
    count[i] += count[i - 1]

  # 5. 결과 배열에 배치 (뒤에서부터)
  result = [0] * len(arr)
  for i in range(len(arr) - 1, -1, -1):
    value = arr[i]
    position = count[value + offset] - 1
    result[position] = value
    count[value + offset] -= 1

  return result


# 사용 예시
if __name__ == "__main__":
  # 기본 예시
  print("=== 기본 카운팅 정렬 예시 ===")
  arr1 = [4, 2, 2, 8, 3, 3, 1]
  print(f"정렬 전: {arr1}")
  sorted_arr1 = counting_sort(arr1)
  print(f"정렬 후: {sorted_arr1}")

  print("\n=== 중복값 포함 예시 ===")
  arr2 = [1, 4, 1, 2, 7, 5, 2]
  print(f"정렬 전: {arr2}")
  sorted_arr2 = counting_sort(arr2)
  print(f"정렬 후: {sorted_arr2}")

  print("\n=== 더 긴 배열 예시 ===")
  arr3 = [3, 1, 4, 1, 5, 9, 2, 6]
  print(f"정렬 전: {arr3}")
  sorted_arr3 = counting_sort(arr3)
  print(f"정렬 후: {sorted_arr3}")

  print("\n=== 음수 포함 예시 ===")
  arr4 = [-2, 1, -1, 3, 0, 2]
  print(f"정렬 전: {arr4}")
  sorted_arr4 = counting_sort(arr4)
  print(f"정렬 후: {sorted_arr4}")

  print("\n=== 중복값이 많은 경우 ===")
  arr5 = [3, 1, 1, 3, 2, 2, 3, 1]
  print(f"정렬 전: {arr5}")
  sorted_arr5 = counting_sort(arr5)
  print(f"정렬 후: {sorted_arr5}")
