#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fibonacci Recursive vs Iterative 성능 비교 (Python)
"""

import time
import psutil
import os
import statistics
from typing import Dict, List
import sys


def get_memory_usage() -> int:
  """현재 프로세스의 메모리 사용량을 KB 단위로 반환"""
  process = psutil.Process(os.getpid())
  return process.memory_info().rss // 1024  # KB 단위


def fibonacci_recursive(n: int) -> int:
  """재귀 방식 피보나치 - O(2^n)"""
  if n <= 1:
    return n
  else:
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n: int) -> int:
  """반복 방식 피보나치 - O(n)"""
  if n <= 1:
    return n

  a, b = 0, 1
  for i in range(2, n + 1):
    a, b = b, a + b

  return b


def performance_test(n: int) -> None:
  """특정 n값으로 성능 테스트 수행"""
  print(f"\n=== 피보나치({n}) 성능 테스트 ===")

  # 메모리 사용량 측정 시작
  initial_memory = get_memory_usage()

  # 각 알고리즘별 성능 측정
  algorithms = {
      "반복 방식": fibonacci_iterative
  }

  results = {}

  # 반복 방식, 동적 프로그래밍, 메모이제이션 테스트
  for name, func in algorithms.items():
    try:
      start_time = time.perf_counter()
      result = func(n)
      end_time = time.perf_counter()

      time_taken = (end_time - start_time) * 1_000_000  # 마이크로초
      results[name] = {"result": result, "time": time_taken}

      print(f"{name}: {result} ({time_taken:.2f} μs)")

    except Exception as e:
      print(f"{name}: 오류 발생 - {e}")
      results[name] = {"result": None, "time": float('inf')}

  # 재귀 방식 테스트 (작은 값에서만)
  if n <= 40:  # 재귀는 큰 값에서 너무 느림
    try:
      start_time = time.perf_counter()
      result = fibonacci_recursive(n)
      end_time = time.perf_counter()

      time_taken = (end_time - start_time) * 1_000_000  # 마이크로초
      results["재귀 방식"] = {"result": result, "time": time_taken}

      print(f"재귀 방식: {result} ({time_taken:.2f} μs)")

    except RecursionError:
      print(f"재귀 방식: 재귀 깊이 초과 (n={n}이 너무 큼)")
      results["재귀 방식"] = {"result": None, "time": float('inf')}
    except Exception as e:
      print(f"재귀 방식: 오류 발생 - {e}")
      results["재귀 방식"] = {"result": None, "time": float('inf')}
  else:
    print("재귀 방식: n이 너무 커서 건너뜀 (n > 40)")

  # 메모리 사용량 측정
  final_memory = get_memory_usage()
  memory_used = final_memory - initial_memory
  print(f"메모리 사용량: {memory_used:,} KB")

  # 성능 비교
  print("\n--- 성능 비교 ---")
  valid_results = {k: v for k, v in results.items() if v["time"] != float('inf')}

  if valid_results:
    fastest = min(valid_results.items(), key=lambda x: x[1]["time"])
    slowest = max(valid_results.items(), key=lambda x: x[1]["time"])

    print(f"가장 빠른 알고리즘: {fastest[0]} ({fastest[1]['time']:.2f} μs)")
    print(f"가장 느린 알고리즘: {slowest[0]} ({slowest[1]['time']:.2f} μs)")

    if fastest[1]["time"] > 0:
      speedup = slowest[1]["time"] / fastest[1]["time"]
      print(f"성능 차이: {speedup:.2f}배")

  # 결과 검증
  print("\n--- 결과 검증 ---")
  valid_results_list = [v["result"]
                        for v in valid_results.values() if v["result"] is not None]
  if len(set(valid_results_list)) == 1:
    print("✓ 모든 알고리즘이 동일한 결과를 반환")
  else:
    print("✗ 알고리즘 간 결과가 다름")


def main():
  """메인 함수"""
  print("Fibonacci Recursive vs Iterative 성능 비교 (Python)")
  print("=" * 50)

  # 다양한 n값으로 테스트
  test_values = [10, 20, 30, 35, 40, 50, 100]

  for n in test_values:
    try:
      performance_test(n)
    except Exception as e:
      print(f"n={n} 테스트 중 오류 발생: {e}")
      break

  print("\n=== 결론 ===")
  print("1. 시간 복잡도:")
  print("   - 재귀 방식: O(2^n) - 지수적 증가")
  print("   - 반복 방식: O(n) - 선형 증가")
  print("2. 공간 복잡도:")
  print("   - 재귀 방식: O(n) - 스택 공간")
  print("   - 반복 방식: O(1) - 상수 공간")
  print("3. 권장사항:")
  print("   - 작은 n (n < 40): 모든 방식 사용 가능")
  print("   - 큰 n (n >= 40): 반복 방식 권장")
  print("   - 메모리 제약: 반복 방식 권장")


if __name__ == "__main__":
  main()
