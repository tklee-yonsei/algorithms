# random_program.py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
간단한 랜덤 프로그램
1. 고정 시드로 숫자 출력
2. 다른 시드로 숫자 출력  
3. 시간 시드로 숫자 출력
"""

import random
import time


def fixed_no_seed():
  """고정 시드 없이 랜덤 숫자 생성
  - 매번 다른 숫자 출력
  """
  print("1. 고정 시드 없이:")
  for i in range(5):
    print(random.randint(1, 100))


def fixed_seed_123():
  """고정 시드 123으로 랜덤 숫자 생성"""
  print("2. 다른 시드 (123):")
  random.seed(123)
  for i in range(5):
    print(random.randint(1, 100))


def time_seed():
  """시간 기반 시드로 랜덤 숫자 생성"""
  print("3. 시간 시드 (매번 다름):")
  random.seed(int(time.time()))
  for i in range(5):
    print(random.randint(1, 100))


def main():
  print("=== Python 랜덤 프로그램 ===")

  fixed_no_seed()
  print()

  fixed_seed_123()
  print()

  time_seed()


if __name__ == "__main__":
  main()
