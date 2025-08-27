#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sequential Search vs Binary Search 성능 비교 (Python)
"""

import time
import random
import psutil
import os
from typing import List, Optional
import statistics


def get_memory_usage() -> int:
  """현재 프로세스의 메모리 사용량을 KB 단위로 반환"""
  process = psutil.Process(os.getpid())
  return process.memory_info().rss // 1024  # KB 단위


def sequential_search(arr: List[int], target: int) -> Optional[int]:
  """Sequential Search (선형 탐색) - O(n)"""
  for i, value in enumerate(arr):
    if value == target:
      return i
  return None


def binary_search(arr: List[int], target: int) -> Optional[int]:
  """Binary Search (이진 탐색) - O(log n) - 배열이 정렬되어 있어야 함"""
  left, right = 0, len(arr) - 1

  while left <= right:
    mid = left + (right - left) // 2

    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      left = mid + 1
    else:
      right = mid - 1

  return None


def quick_sort(arr: List[int]) -> List[int]:
  """Quick Sort 구현 - O(n log n)"""
  if len(arr) <= 1:
    return arr

  pivot = arr[len(arr) // 2]
  left = [x for x in arr if x < pivot]
  middle = [x for x in arr if x == pivot]
  right = [x for x in arr if x > pivot]

  return quick_sort(left) + middle + quick_sort(right)


def performance_test(size: int) -> None:
  """특정 크기의 배열로 성능 테스트 수행"""
  print(f"\n=== 배열 크기: {size:,} ===")

  # 메모리 사용량 측정 시작
  initial_memory = get_memory_usage()

  # 랜덤 데이터로 배열 생성
  random.seed(42)  # 재현 가능한 결과를 위해 시드 설정
  arr = [random.randint(0, size * 10) for _ in range(size)]

  # Binary search를 위한 정렬된 배열 생성
  sorted_arr = quick_sort(arr.copy())

  # 메모리 사용량 측정
  after_allocation = get_memory_usage()
  memory_used = after_allocation - initial_memory

  print(f"메모리 사용량: {memory_used:,} KB")

  # 테스트할 타겟 값들 (존재하는 값과 존재하지 않는 값)
  test_targets = [
      arr[0],           # 첫 번째 요소
      arr[size // 2],   # 중간 요소
      arr[-1],          # 마지막 요소
      -1,               # 존재하지 않는 값
      size * 20         # 존재하지 않는 큰 값
  ]

  print("\n--- Sequential Search 성능 ---")
  seq_times = []

  for target in test_targets:
    start_time = time.perf_counter()
    result = sequential_search(arr, target)
    end_time = time.perf_counter()

    time_taken = (end_time - start_time) * 1_000_000  # 마이크로초
    seq_times.append(time_taken)

    print(f"타겟 {target}: {result} ({time_taken:.2f} μs)")

  seq_avg = statistics.mean(seq_times)
  print(f"Sequential Search 평균 시간: {seq_avg:.2f} μs")

  print("\n--- Binary Search 성능 ---")
  bin_times = []

  for target in test_targets:
    start_time = time.perf_counter()
    result = binary_search(sorted_arr, target)
    end_time = time.perf_counter()

    time_taken = (end_time - start_time) * 1_000_000  # 마이크로초
    bin_times.append(time_taken)

    print(f"타겟 {target}: {result} ({time_taken:.2f} μs)")

  bin_avg = statistics.mean(bin_times)
  print(f"Binary Search 평균 시간: {bin_avg:.2f} μs")

  # 성능 비교
  print("\n--- 성능 비교 ---")
  print(f"Sequential Search: {seq_avg:.2f} μs")
  print(f"Binary Search: {bin_avg:.2f} μs")

  if seq_avg > bin_avg:
    speedup = seq_avg / bin_avg
    print(f"Binary Search가 {speedup:.2f}배 빠름")
  else:
    speedup = bin_avg / seq_avg
    print(f"Sequential Search가 {speedup:.2f}배 빠름")

  # 시간 복잡도 이론적 비교
  theoretical_ratio = size / (size.bit_length() if size > 0 else 1)
  print(f"이론적 성능 비율 (n/log n): {theoretical_ratio:.2f}")


def main():
  """메인 함수"""
  print("Sequential Search vs Binary Search 성능 비교 (Python)")
  print("=" * 50)

  # 다양한 크기로 테스트
  sizes = [1_000, 10_000, 100_000, 1_000_000]

  for size in sizes:
    try:
      performance_test(size)
    except MemoryError:
      print(f"메모리 부족으로 {size:,} 크기 테스트를 건너뜁니다.")
      break
    except Exception as e:
      print(f"오류 발생: {e}")
      break

  print("\n=== 결론 ===")
  print("1. 메모리: 두 알고리즘 모두 O(n) 메모리 사용")
  print("2. 시간 복잡도:")
  print("   - Sequential Search: O(n)")
  print("   - Binary Search: O(log n)")
  print("3. Binary Search는 정렬이 필요하지만, 큰 데이터셋에서 훨씬 빠름")
  print("4. Python의 내장 bisect 모듈을 사용하면 더 효율적일 수 있음")


if __name__ == "__main__":
  main()
