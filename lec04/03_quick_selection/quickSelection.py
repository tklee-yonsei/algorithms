# quickSelection.py
def partition(arr, low, high):
  """배열을 분할하는 함수 (Hoare partition scheme)"""
  # 첫 번째 요소를 피벗으로 선택
  pivot = arr[low]

  i = low - 1
  j = high + 1

  while True:
    # 왼쪽에서 피벗보다 큰 요소 찾기
    i += 1
    while i <= high and arr[i] < pivot:
      i += 1

    # 오른쪽에서 피벗보다 작은 요소 찾기
    j -= 1
    while j >= low and arr[j] > pivot:
      j -= 1

    # 교환할 요소가 없으면 종료
    if i >= j:
      return j

    # 요소 교환
    arr[i], arr[j] = arr[j], arr[i]


def quick_select(arr, low, high, k):
  """k번째로 작은 원소를 찾는 함수 (0-based index)"""
  if low == high:
    return arr[low]

  # 분할
  pivot_index = partition(arr, low, high)

  # k번째 원소의 위치 확인
  if k <= pivot_index:
    # k번째 원소가 왼쪽 부분에 있음
    return quick_select(arr, low, pivot_index, k)
  else:
    # k번째 원소가 오른쪽 부분에 있음
    return quick_select(arr, pivot_index + 1, high, k)


def find_kth_smallest(arr, k):
  """k번째로 작은 원소를 찾는 함수 (1-based index, 사용자 친화적)"""
  if k < 1 or k > len(arr):
    print(f"오류: k는 1부터 {len(arr)} 사이의 값이어야 합니다.")
    return None

  # 배열을 복사하여 원본 배열을 보존
  temp_arr = arr.copy()

  return quick_select(temp_arr, 0, len(temp_arr) - 1, k - 1)  # 0-based로 변환


def find_kth_largest(arr, k):
  """k번째로 큰 원소를 찾는 함수"""
  return find_kth_smallest(arr, len(arr) - k + 1)


# 사용 예시
if __name__ == "__main__":
  arr = [64, 34, 25, 12, 22, 11, 90, 3, 77, 45]

  print("원본 배열:", arr)

  # 다양한 k값에 대해 테스트
  for k in range(1, len(arr) + 1):
    kth_smallest = find_kth_smallest(arr, k)
    if kth_smallest is not None:
      print(f"{k}번째로 작은 원소: {kth_smallest}")

  # 특별한 케이스들 테스트
  print("\n특별한 케이스들:")
  print(f"가장 작은 원소 (1번째): {find_kth_smallest(arr, 1)}")
  print(
      f"중앙값 (median, {(len(arr) + 1) // 2}번째): {find_kth_smallest(arr, (len(arr) + 1) // 2)}")
  print(f"가장 큰 원소 ({len(arr)}번째): {find_kth_smallest(arr, len(arr))}")

  # k번째로 큰 원소 테스트
  print("\nk번째로 큰 원소들:")
  for k in range(1, 4):
    kth_largest = find_kth_largest(arr, k)
    print(f"{k}번째로 큰 원소: {kth_largest}")

  # 원본 배열이 변경되지 않았는지 확인
  print("\n원본 배열 (변경 확인):", arr)
