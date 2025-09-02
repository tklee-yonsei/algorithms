import time
import random
import matplotlib.pyplot as plt
import numpy as np


def insertion_sort_for_gap(arr, start, gap):
  """특정 gap 그룹에 대해 삽입 정렬을 수행하는 함수"""
  n = len(arr)

  # 현재 gap 그룹의 요소들을 삽입 정렬
  for i in range(start + gap, n, gap):
    temp = arr[i]
    j = i

    while j >= start + gap and arr[j - gap] > temp:
      arr[j] = arr[j - gap]
      j -= gap

    arr[j] = temp


def shell_sort(arr):
  """Shell Sort 구현"""
  n = len(arr)
  gap = n // 2

  while gap > 0:
    # 각 gap 그룹에 대해 삽입 정렬 수행
    for start in range(gap):
      insertion_sort_for_gap(arr, start, gap)

    gap //= 2

  return arr


def insertion_sort(arr):
  """Insertion Sort 구현"""
  for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
      arr[j + 1] = arr[j]
      j -= 1

    arr[j + 1] = key

  return arr


def selection_sort(arr):
  """Selection Sort 구현"""
  n = len(arr)

  for i in range(n):
    min_idx = i
    for j in range(i + 1, n):
      if arr[j] < arr[min_idx]:
        min_idx = j

    arr[i], arr[min_idx] = arr[min_idx], arr[i]

  return arr


def bubble_sort(arr):
  """Bubble Sort 구현"""
  n = len(arr)

  for i in range(n):
    for j in range(0, n - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]

  return arr


def measure_time(sort_func, arr):
  """정렬 함수의 실행 시간 측정"""
  arr_copy = arr.copy()
  start_time = time.time()
  sort_func(arr_copy)
  end_time = time.time()
  return end_time - start_time


def generate_test_data(size):
  """테스트 데이터 생성"""
  return [random.randint(1, 1000) for _ in range(size)]


def performance_test():
  """성능 테스트 실행"""
  sizes = [100, 500, 1000, 2000, 3000]
  algorithms = {
      'Shell Sort': shell_sort,
      'Insertion Sort': insertion_sort,
      'Selection Sort': selection_sort,
      'Bubble Sort': bubble_sort
  }

  results = {name: [] for name in algorithms.keys()}

  print("성능 테스트 시작...")
  print("-" * 50)

  for size in sizes:
    print(f"배열 크기: {size}")

    # 각 크기에 대해 여러 번 테스트하여 평균 계산
    test_times = {name: [] for name in algorithms.keys()}

    for _ in range(5):  # 5번 테스트
      test_data = generate_test_data(size)

      for name, func in algorithms.items():
        time_taken = measure_time(func, test_data)
        test_times[name].append(time_taken)

    # 평균 시간 계산
    for name in algorithms.keys():
      avg_time = np.mean(test_times[name])
      results[name].append(avg_time)
      print(f"  {name}: {avg_time:.6f}초")

    print()

  return sizes, results


def plot_results(sizes, results):
  """결과를 그래프로 시각화"""
  plt.figure(figsize=(12, 8))

  # 색상 설정 (shell_sort_animation.py와 동일한 색상 체계)
  colors = {
      'Shell Sort': '#4CAF50',      # 초록색
      'Insertion Sort': '#FFD54F',   # 노란색
      'Selection Sort': '#FF8A80',   # 빨간색
      'Bubble Sort': '#FFB74D'       # 주황색
  }

  for name, times in results.items():
    plt.plot(sizes, times, marker='o', label=name,
             linewidth=2, markersize=8, color=colors[name])

  plt.xlabel('Array Size', fontsize=12, fontweight='bold', color='#2C3E50')
  plt.ylabel('Execution Time (seconds)', fontsize=12,
             fontweight='bold', color='#2C3E50')
  plt.title('Sorting Algorithms Performance Comparison',
            fontsize=14, fontweight='bold', color='#2C3E50')
  plt.legend(frameon=True, fancybox=True, shadow=True, fontsize=11)
  plt.grid(True, alpha=0.3, color='#95A5A6')
  plt.xscale('log')
  plt.yscale('log')

  # 축 스타일링
  plt.gca().spines['top'].set_visible(False)
  plt.gca().spines['right'].set_visible(False)
  plt.gca().spines['left'].set_color('#BDC3C7')
  plt.gca().spines['bottom'].set_color('#BDC3C7')

  plt.tight_layout()
  plt.show()


def main():
  print("Shell Sort vs 다른 정렬 알고리즘 성능 비교")
  print("=" * 50)

  # 성능 테스트 실행
  sizes, results = performance_test()

  # 결과 출력
  print("\n결과 요약:")
  print("-" * 50)
  for name, times in results.items():
    print(f"{name}:")
    for i, size in enumerate(sizes):
      print(f"  크기 {size}: {times[i]:.6f}초")
    print()

  # 그래프 생성
  plot_results(sizes, results)


if __name__ == "__main__":
  main()
