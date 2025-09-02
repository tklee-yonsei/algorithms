# search_comparison.py - 탐색 알고리즘 비교 예시

def sequential_search(arr, target):
  """순차 탐색 - 특정 값 찾기"""
  for i, value in enumerate(arr):
    if value == target:
      return i  # 인덱스 반환
  return -1  # 찾지 못함


def binary_search(arr, target):
  """이진 탐색 - 정렬된 배열에서 특정 값 찾기"""
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


def quick_select_for_value(arr, target):
  """Quick Selection으로 특정 값 찾기 (비효율적 예시)"""
  temp_arr = arr.copy()

  # 정렬하면서 타겟의 위치 찾기 (비효율적!)
  for k in range(1, len(arr) + 1):
    kth_value = find_kth_smallest(temp_arr, k)
    if kth_value == target:
      return k - 1  # 0-based 인덱스로 변환
  return -1


def find_kth_smallest(arr, k):
  """Quick Selection - k번째 작은 값 찾기 (효율적 사용)"""
  # 이전에 구현한 함수 사용
  from quickSelection import find_kth_smallest as quick_select
  return quick_select(arr, k)


# 비교 테스트
if __name__ == "__main__":
  import time

  # 테스트 데이터
  arr = [64, 34, 25, 12, 42, 11, 90, 77, 33, 55]
  target_value = 42
  target_rank = 5  # 5번째로 작은 값

  print("=== 탐색 알고리즘 비교 ===")
  print(f"배열: {arr}")
  print(f"찾을 값: {target_value}")
  print(f"찾을 순위: {target_rank}번째로 작은 값")
  print()

  # 1. 특정 값 찾기 비교
  print("1. 특정 값 찾기 (값 42 찾기):")

  # Sequential Search
  start = time.time()
  seq_result = sequential_search(arr, target_value)
  seq_time = time.time() - start
  print(f"   Sequential Search: 인덱스 {seq_result} ({seq_time:.6f}초)")

  # Binary Search (정렬된 배열)
  sorted_arr = sorted(arr)
  start = time.time()
  bin_result = binary_search(sorted_arr, target_value)
  bin_time = time.time() - start
  print(f"   Binary Search: 인덱스 {bin_result} ({bin_time:.6f}초)")

  # Quick Selection (비효율적 사용)
  start = time.time()
  qs_result = quick_select_for_value(arr, target_value)
  qs_time = time.time() - start
  print(f"   Quick Selection: 인덱스 {qs_result} ({qs_time:.6f}초) ❌ 비효율적!")

  print()

  # 2. 순위 기반 탐색
  print("2. 순위 기반 탐색 (5번째로 작은 값 찾기):")

  # Quick Selection (효율적 사용)
  start = time.time()
  kth_value = find_kth_smallest(arr, target_rank)
  qs_rank_time = time.time() - start
  print(f"   Quick Selection: {kth_value} ({qs_rank_time:.6f}초) ✅ 효율적!")

  # 전체 정렬 후 인덱싱 (비효율적)
  start = time.time()
  sorted_arr = sorted(arr)
  sort_result = sorted_arr[target_rank - 1]
  sort_time = time.time() - start
  print(f"   전체 정렬 후: {sort_result} ({sort_time:.6f}초) ❌ 비효율적!")

  print()
  print("=== 결론 ===")
  print("✅ 특정 값 찾기 → Sequential/Binary Search 사용")
  print("✅ k번째 값 찾기 → Quick Selection 사용")
  print("❌ Quick Selection으로 특정 값 찾기는 비효율적")
