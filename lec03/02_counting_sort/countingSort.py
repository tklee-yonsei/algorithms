# countingSort.py

def counting_sort(arr):
  """
  카운팅 정렬 알고리즘

  Args:
      arr: 정렬할 정수 배열 (0 이상의 값들)

  Returns:
      정렬된 배열

  시간 복잡도: O(n + k) - n은 원소 개수, k는 값의 범위
  공간 복잡도: O(k) - 카운팅 배열을 위한 공간
  """
  if not arr:
    return []

  # 1. 최대값과 최소값 찾기
  min_val = min(arr)
  max_val = max(arr)

  # 음수 처리를 위해 오프셋 사용
  offset = -min_val
  range_size = max_val - min_val + 1

  # 2. 카운팅 배열 초기화 (각 값의 출현 횟수를 저장)
  count = [0] * range_size

  # 3. 각 원소의 개수 세기
  for num in arr:
    count[num + offset] += 1

  # 4. 카운팅 배열을 누적합으로 변환 (각 값의 최종 위치 계산)
  for i in range(1, len(count)):
    count[i] += count[i - 1]

  # 5. 결과 배열 생성
  result = [0] * len(arr)

  # 6. 원본 배열을 뒤에서부터 순회하며 결과 배열에 배치 (안정 정렬 보장)
  for i in range(len(arr) - 1, -1, -1):
    value = arr[i]
    position = count[value + offset] - 1
    result[position] = value
    count[value + offset] -= 1

  return result


def counting_sort_with_steps(arr, show_steps=True):
  """
  단계별 출력을 포함한 카운팅 정렬

  Args:
      arr: 정렬할 배열
      show_steps: 단계별 출력 여부

  Returns:
      정렬된 배열
  """
  if not arr:
    return []

  if show_steps:
    print(f"입력 배열: {arr}")

  # 1. 최대값과 최소값 찾기
  min_val = min(arr)
  max_val = max(arr)
  offset = -min_val
  range_size = max_val - min_val + 1

  if show_steps:
    print(f"값의 범위: {min_val} ~ {max_val} (크기: {range_size})")

  # 2. 카운팅 배열 초기화
  count = [0] * range_size

  # 3. 각 원소의 개수 세기
  for num in arr:
    count[num + offset] += 1

  if show_steps:
    print(f"카운팅 배열 (개수): {count}")

  # 4. 누적합으로 변환
  for i in range(1, len(count)):
    count[i] += count[i - 1]

  if show_steps:
    print(f"카운팅 배열 (누적): {count}")

  # 5. 결과 배열 생성
  result = [0] * len(arr)

  # 6. 배치 과정
  if show_steps:
    print("\n배치 과정:")

  for i in range(len(arr) - 1, -1, -1):
    value = arr[i]
    position = count[value + offset] - 1
    result[position] = value
    count[value + offset] -= 1

    if show_steps:
      print(f"  {value}을(를) 위치 {position}에 배치")

  if show_steps:
    print(f"\n최종 결과: {result}")

  return result


# 사용 예시
if __name__ == "__main__":
  # 기본 예시
  print("=== 기본 카운팅 정렬 예시 ===")
  arr1 = [4, 2, 2, 8, 3, 3, 1]
  print(f"정렬 전: {arr1}")
  sorted_arr1 = counting_sort(arr1)
  print(f"정렬 후: {sorted_arr1}")

  print("\n=== 단계별 카운팅 정렬 ===")
  arr2 = [1, 4, 1, 2, 7, 5, 2]
  counting_sort_with_steps(arr2)

  print("\n=== 기본 정렬 예시 2 ===")
  arr3 = [3, 1, 4, 1, 5, 9, 2, 6]
  print(f"정렬 전: {arr3}")
  sorted_arr3 = counting_sort(arr3)
  print(f"정렬 후: {sorted_arr3}")

  print("\n=== 음수 포함 예시 ===")
  arr4 = [-2, 1, -1, 3, 0, 2]
  print(f"정렬 전: {arr4}")
  sorted_arr4 = counting_sort(arr4)
  print(f"정렬 후: {sorted_arr4}")

  print("\n=== 중복값 많은 경우 ===")
  arr5 = [3, 1, 1, 3, 2, 2, 3, 1]
  print(f"정렬 전: {arr5}")
  sorted_arr5 = counting_sort(arr5)
  print(f"정렬 후: {sorted_arr5}")
