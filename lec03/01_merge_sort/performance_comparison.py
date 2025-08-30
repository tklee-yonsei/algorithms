# performance_comparison.py
import random
import time
import copy


def merge(arr, left, mid, right):
  """두 개의 정렬된 부분 배열을 합치는 함수"""
  # 임시 배열 생성
  left_arr = arr[left:mid+1]
  right_arr = arr[mid+1:right+1]

  # 인덱스 초기화
  i = j = 0  # 임시 배열들의 인덱스
  k = left   # 원본 배열의 인덱스

  # 두 배열을 비교하며 작은 값부터 원본 배열에 복사
  while i < len(left_arr) and j < len(right_arr):
    if left_arr[i] <= right_arr[j]:
      arr[k] = left_arr[i]
      i += 1
    else:
      arr[k] = right_arr[j]
      j += 1
    k += 1

  # 남은 요소들 복사
  while i < len(left_arr):
    arr[k] = left_arr[i]
    i += 1
    k += 1

  while j < len(right_arr):
    arr[k] = right_arr[j]
    j += 1
    k += 1


def merge_sort(arr, left=None, right=None):
  """병합 정렬 함수"""
  if left is None:
    left = 0
  if right is None:
    right = len(arr) - 1

  if left < right:
    # 중간점 계산
    mid = (left + right) // 2

    # 왼쪽 부분 정렬
    merge_sort(arr, left, mid)

    # 오른쪽 부분 정렬
    merge_sort(arr, mid + 1, right)

    # 정렬된 두 부분을 합치기
    merge(arr, left, mid, right)


def generate_random_array(size):
  """랜덤 배열 생성"""
  return [random.randint(1, 1000) for _ in range(size)]


def generate_nearly_sorted_array(size):
  """거의 정렬된 배열 생성 (10% 정도만 무작위)"""
  arr = list(range(1, size + 1))
  # 10%의 요소를 무작위로 섞기
  num_swaps = size // 10
  for _ in range(num_swaps):
    i = random.randint(0, size - 1)
    j = random.randint(0, size - 1)
    arr[i], arr[j] = arr[j], arr[i]
  return arr


def generate_reversed_array(size):
  """역순 배열 생성"""
  return list(range(size, 0, -1))


def generate_few_unique_array(size):
  """중복이 많은 배열 생성 (1-10 사이의 값만 사용)"""
  return [random.randint(1, 10) for _ in range(size)]


def measure_sorting_time(sort_func, arr):
  """정렬 시간 측정"""
  arr_copy = copy.deepcopy(arr)
  start_time = time.time()
  sort_func(arr_copy)
  end_time = time.time()
  return end_time - start_time


def test_performance():
  """다양한 데이터 패턴에 대한 성능 테스트"""
  sizes = [100, 500, 1000, 2000, 5000]

  print("병합 정렬 성능 비교")
  print("=" * 60)

  for size in sizes:
    print(f"\n배열 크기: {size}")
    print("-" * 40)

    # 랜덤 배열
    random_arr = generate_random_array(size)
    random_time = measure_sorting_time(merge_sort, random_arr)
    print(f"랜덤 배열:     {random_time:.6f}초")

    # 거의 정렬된 배열
    nearly_sorted_arr = generate_nearly_sorted_array(size)
    nearly_sorted_time = measure_sorting_time(merge_sort, nearly_sorted_arr)
    print(f"거의 정렬된:   {nearly_sorted_time:.6f}초")

    # 역순 배열
    reversed_arr = generate_reversed_array(size)
    reversed_time = measure_sorting_time(merge_sort, reversed_arr)
    print(f"역순 배열:     {reversed_time:.6f}초")

    # 중복이 많은 배열
    few_unique_arr = generate_few_unique_array(size)
    few_unique_time = measure_sorting_time(merge_sort, few_unique_arr)
    print(f"중복이 많은:   {few_unique_time:.6f}초")


def verify_sorting():
  """정렬이 올바르게 작동하는지 확인"""
  print("\n정렬 검증")
  print("=" * 30)

  # 테스트 케이스들
  test_cases = [
      ([64, 34, 25, 12, 22, 11, 90], "기본 테스트"),
      ([1], "단일 요소"),
      ([], "빈 배열"),
      ([3, 3, 3, 3], "모든 요소가 동일"),
      ([5, 4, 3, 2, 1], "역순"),
      ([1, 2, 3, 4, 5], "이미 정렬됨"),
      ([1, 3, 2, 5, 4, 7, 6, 8], "부분적으로 정렬됨")
  ]

  for arr, description in test_cases:
    original = arr.copy()
    merge_sort(arr)
    is_sorted = arr == sorted(original)
    print(f"{description}: {'✓' if is_sorted else '✗'} {arr}")


def compare_with_builtin():
  """내장 정렬 함수와 성능 비교"""
  print("\n내장 정렬 함수와의 성능 비교")
  print("=" * 50)

  sizes = [1000, 5000, 10000]

  for size in sizes:
    print(f"\n배열 크기: {size}")
    print("-" * 30)

    # 랜덤 배열 생성
    random_arr = generate_random_array(size)

    # 병합 정렬 시간 측정
    merge_time = measure_sorting_time(merge_sort, random_arr.copy())

    # 내장 정렬 시간 측정
    builtin_time = measure_sorting_time(lambda arr: arr.sort(), random_arr.copy())

    print(f"병합 정렬:   {merge_time:.6f}초")
    print(f"내장 정렬:   {builtin_time:.6f}초")
    print(f"비율:       {merge_time / builtin_time:.2f}배")


def analyze_time_complexity():
  """시간 복잡도 분석"""
  print("\n시간 복잡도 분석")
  print("=" * 40)

  sizes = [100, 200, 400, 800, 1600, 3200]
  times = []

  print("크기\t시간(초)\t이론적 비율\t실제 비율")
  print("-" * 50)

  prev_time = None
  prev_size = None

  for size in sizes:
    random_arr = generate_random_array(size)
    time_taken = measure_sorting_time(merge_sort, random_arr)
    times.append(time_taken)

    # 이론적 비율: O(n log n)이므로 크기가 2배가 되면 약 2.2배 정도 증가
    theoretical_ratio = (size * np.log2(size)) / (prev_size *
                                                  np.log2(prev_size)) if prev_size else 1
    actual_ratio = time_taken / prev_time if prev_time else 1

    print(f"{size}\t{time_taken:.6f}\t{theoretical_ratio:.2f}\t\t{actual_ratio:.2f}")

    prev_time = time_taken
    prev_size = size


if __name__ == "__main__":
  import numpy as np

  # 정렬 검증
  verify_sorting()

  # 성능 테스트
  test_performance()

  # 내장 정렬과 비교
  compare_with_builtin()

  # 시간 복잡도 분석
  analyze_time_complexity()
