# performance_comparison.py
import random
import time
import copy


def selection_sort(arr):
  """선택 정렬 함수"""
  n = len(arr)

  for i in range(n - 1):
    min_index = i

    # i번째 위치부터 끝까지 최솟값 찾기
    for j in range(i + 1, n):
      if arr[j] < arr[min_index]:
        min_index = j

    # 최솟값을 i번째 위치로 교환
    if min_index != i:
      arr[i], arr[min_index] = arr[min_index], arr[i]


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
  sizes = [100, 500, 1000, 2000]

  print("선택 정렬 성능 비교")
  print("=" * 60)

  for size in sizes:
    print(f"\n배열 크기: {size}")
    print("-" * 40)

    # 랜덤 배열
    random_arr = generate_random_array(size)
    random_time = measure_sorting_time(selection_sort, random_arr)
    print(f"랜덤 배열:     {random_time:.6f}초")

    # 거의 정렬된 배열
    nearly_sorted_arr = generate_nearly_sorted_array(size)
    nearly_sorted_time = measure_sorting_time(selection_sort, nearly_sorted_arr)
    print(f"거의 정렬된:   {nearly_sorted_time:.6f}초")

    # 역순 배열
    reversed_arr = generate_reversed_array(size)
    reversed_time = measure_sorting_time(selection_sort, reversed_arr)
    print(f"역순 배열:      {reversed_time:.6f}초")

    # 중복이 많은 배열
    few_unique_arr = generate_few_unique_array(size)
    few_unique_time = measure_sorting_time(selection_sort, few_unique_arr)
    print(f"중복이 많은:    {few_unique_time:.6f}초")


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
      ([1, 2, 3, 4, 5], "이미 정렬됨")
  ]

  for arr, description in test_cases:
    original = arr.copy()
    selection_sort(arr)
    is_sorted = arr == sorted(original)
    print(f"{description}: {'✓' if is_sorted else '✗'} {arr}")


if __name__ == "__main__":
  # 정렬 검증
  verify_sorting()

  # 성능 테스트
  test_performance()
