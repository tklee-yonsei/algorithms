# quickSelection.py
# TODO: 배열을 분할하는 함수를 구현하세요 (Hoare partition scheme)
def partition(arr, low, high):
  """배열을 분할하는 함수 (Hoare partition scheme)"""
  # 여기에 코드를 작성하세요
  # 힌트:
  # 1. 첫 번째 요소를 피벗으로 선택
  # 2. i를 low-1, j를 high+1로 초기화
  # 3. 무한 루프에서:
  #    - 왼쪽에서 피벗보다 큰 요소 찾기
  #    - 오른쪽에서 피벗보다 작은 요소 찾기
  #    - i >= j이면 j 반환
  #    - 그렇지 않으면 arr[i]와 arr[j] 교환
  return -1


# TODO: k번째로 작은 원소를 찾는 함수를 구현하세요 (0-based index)
def quick_select(arr, low, high, k):
  """k번째로 작은 원소를 찾는 함수 (0-based index)"""
  # 여기에 코드를 작성하세요
  # 힌트:
  # 1. 베이스 케이스: low == high이면 arr[low] 반환
  # 2. partition 함수로 배열 분할
  # 3. k의 위치에 따라 왼쪽 또는 오른쪽 부분에서 재귀 호출
  #    - k <= pivot_index이면 왼쪽 부분에서 탐색
  #    - 그렇지 않으면 오른쪽 부분에서 탐색
  return -1


# TODO: k번째로 작은 원소를 찾는 함수를 구현하세요 (1-based index, 사용자 친화적)
def find_kth_smallest(arr, k):
  """k번째로 작은 원소를 찾는 함수 (1-based index, 사용자 친화적)"""
  # 여기에 코드를 작성하세요
  # 힌트:
  # 1. k가 유효한 범위인지 확인 (1 <= k <= len(arr))
  # 2. 배열을 복사하여 원본 배열 보존
  # 3. quick_select 함수 호출 (k-1로 0-based 변환)
  # 4. 결과 반환
  return None


# TODO: k번째로 큰 원소를 찾는 함수를 구현하세요
def find_kth_largest(arr, k):
  """k번째로 큰 원소를 찾는 함수"""
  # 여기에 코드를 작성하세요
  # 힌트: k번째로 큰 원소 = (len(arr) - k + 1)번째로 작은 원소
  return None


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
