# create_animations.py
import random
import numpy as np
from selection_sort_animation import create_animation_for_data


def create_animations_with_same_data():
  """같은 데이터를 다른 순서로 배치하여 애니메이션 생성"""
  print("=" * 60)
  print("선택 정렬 애니메이션 생성")
  print("=" * 60)

  # 기본 데이터 생성 (1-10까지의 숫자)
  base_data = list(range(1, 11))
  print(f"기본 데이터: {base_data}")

  # 1. 랜덤 배열 (기본 데이터를 무작위로 섞기)
  print(f"\n1. 랜덤 배열 애니메이션 생성 중...")
  random_arr = base_data.copy()
  random.shuffle(random_arr)
  print(f"랜덤 배열: {random_arr}")
  create_animation_for_data(random_arr, 'random_array.gif')

  # 2. 거의 정렬된 배열 (기본 데이터에서 몇 개만 교환)
  print(f"\n2. 거의 정렬된 배열 애니메이션 생성 중...")
  nearly_sorted_arr = base_data.copy()
  # 2-3개만 교환
  for _ in range(2):
    i = random.randint(0, 9)
    j = random.randint(0, 9)
    nearly_sorted_arr[i], nearly_sorted_arr[j] = nearly_sorted_arr[j], nearly_sorted_arr[i]
  print(f"거의 정렬된 배열: {nearly_sorted_arr}")
  create_animation_for_data(nearly_sorted_arr, 'nearly_sorted.gif')

  # 3. 역순 배열 (기본 데이터를 역순으로)
  print(f"\n3. 역순 배열 애니메이션 생성 중...")
  reversed_arr = base_data.copy()
  reversed_arr.reverse()
  print(f"역순 배열: {reversed_arr}")
  create_animation_for_data(reversed_arr, 'reversed_array.gif')

  # 4. 중복이 많은 배열 (기본 데이터에서 일부를 중복으로)
  print(f"\n4. 중복이 많은 배열 애니메이션 생성 중...")
  few_unique_arr = base_data.copy()
  # 일부 위치를 같은 값으로 변경
  for i in range(3, 6):  # 4, 5, 6번째 위치를 1로 변경
    few_unique_arr[i] = 1
  for i in range(7, 10):  # 8, 9, 10번째 위치를 2로 변경
    few_unique_arr[i] = 2
  print(f"중복이 많은 배열: {few_unique_arr}")
  create_animation_for_data(few_unique_arr, 'few_unique.gif')

  print(f"\n" + "=" * 60)
  print("모든 애니메이션이 생성되었습니다!")
  print("=" * 60)
  print("생성된 파일들:")
  print("- random_array.gif")
  print("- nearly_sorted.gif")
  print("- reversed_array.gif")
  print("- few_unique.gif")
  print("=" * 60)

  # 각 배열의 정렬 결과 비교
  print("\n정렬 결과 비교:")
  print(f"랜덤 배열 정렬 후: {sorted(random_arr)}")
  print(f"거의 정렬된 배열 정렬 후: {sorted(nearly_sorted_arr)}")
  print(f"역순 배열 정렬 후: {sorted(reversed_arr)}")
  print(f"중복이 많은 배열 정렬 후: {sorted(few_unique_arr)}")


if __name__ == "__main__":
  create_animations_with_same_data()
