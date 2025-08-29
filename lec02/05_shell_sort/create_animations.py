# create_animations.py
import random
import numpy as np
import os
from shell_sort_animation import create_animation_for_data


def create_animations_with_same_data():
  """같은 데이터를 다른 순서로 배치하여 셸 정렬 애니메이션 생성"""
  print("=" * 60)
  print("셸 정렬 애니메이션 생성")
  print("=" * 60)

  # img 디렉토리 생성
  if not os.path.exists('img'):
    os.makedirs('img')

  # 기본 데이터 생성 (1-15까지의 숫자)
  base_data = list(range(1, 16))
  print(f"기본 데이터: {base_data}")

  # 1. 랜덤 배열 (기본 데이터를 무작위로 섞기)
  print(f"\n1. 랜덤 배열 애니메이션 생성 중...")
  random.seed(42)  # 일관된 결과를 위해 시드 고정
  random_arr = base_data.copy()
  random.shuffle(random_arr)
  print(f"랜덤 배열: {random_arr}")
  create_animation_for_data(random_arr, 'img/random_array.gif')

  # 2. 거의 정렬된 배열 (기본 데이터에서 몇 개만 교환)
  print(f"\n2. 거의 정렬된 배열 애니메이션 생성 중...")
  nearly_sorted_arr = base_data.copy()
  # 3-4개만 교환
  for _ in range(3):
    i = random.randint(0, 14)
    j = random.randint(0, 14)
    nearly_sorted_arr[i], nearly_sorted_arr[j] = nearly_sorted_arr[j], nearly_sorted_arr[i]
  print(f"거의 정렬된 배열: {nearly_sorted_arr}")
  create_animation_for_data(nearly_sorted_arr, 'img/nearly_sorted.gif')

  # 3. 역순 배열 (기본 데이터를 역순으로)
  print(f"\n3. 역순 배열 애니메이션 생성 중...")
  reversed_arr = base_data.copy()
  reversed_arr.reverse()
  print(f"역순 배열: {reversed_arr}")
  create_animation_for_data(reversed_arr, 'img/reversed_array.gif')

  # 4. 중복이 많은 배열 (기본 데이터에서 일부를 중복으로)
  print(f"\n4. 중복이 많은 배열 애니메이션 생성 중...")
  few_unique_arr = base_data.copy()
  # 일부 위치를 같은 값으로 변경
  for i in range(3, 8):  # 4, 5, 6, 7, 8번째 위치를 1로 변경
    few_unique_arr[i] = 1
  for i in range(9, 14):  # 10, 11, 12, 13, 14번째 위치를 2로 변경
    few_unique_arr[i] = 2
  print(f"중복이 많은 배열: {few_unique_arr}")
  create_animation_for_data(few_unique_arr, 'img/few_unique.gif')

  # 5. 셸 정렬에 유리한 배열 (큰 값들이 앞쪽에, 작은 값들이 뒤쪽에)
  print(f"\n5. 셸 정렬 유리 배열 애니메이션 생성 중...")
  shell_favorable_arr = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
                         1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
  print(f"셸 정렬 유리 배열: {shell_favorable_arr}")
  create_animation_for_data(shell_favorable_arr, 'img/shell_favorable.gif')

  # 6. 삽입 정렬에 유리한 배열 (부분적으로 정렬된 배열)
  print(f"\n6. 삽입 정렬 유리 배열 애니메이션 생성 중...")
  insertion_favorable_arr = [1, 2, 3, 4, 5, 15, 16,
                             17, 18, 19, 20, 6, 7, 8, 9, 10, 11, 12, 13, 14]
  print(f"삽입 정렬 유리 배열: {insertion_favorable_arr}")
  create_animation_for_data(insertion_favorable_arr, 'img/insertion_favorable.gif')

  print(f"\n" + "=" * 60)
  print("개별 애니메이션 생성 완료!")
  print("=" * 60)
  print("생성된 파일들:")
  print("- img/random_array.gif")
  print("- img/nearly_sorted.gif")
  print("- img/reversed_array.gif")
  print("- img/few_unique.gif")
  print("- img/shell_favorable.gif")
  print("- img/insertion_favorable.gif")
  print("=" * 60)

  # 각 배열의 정렬 결과 비교
  print("\n정렬 결과 비교:")
  print(f"랜덤 배열 정렬 후: {sorted(random_arr)}")
  print(f"거의 정렬된 배열 정렬 후: {sorted(nearly_sorted_arr)}")
  print(f"역순 배열 정렬 후: {sorted(reversed_arr)}")
  print(f"중복이 많은 배열 정렬 후: {sorted(few_unique_arr)}")
  print(f"셸 정렬 유리 배열 정렬 후: {sorted(shell_favorable_arr)}")
  print(f"삽입 정렬 유리 배열 정렬 후: {sorted(insertion_favorable_arr)}")

  # 성능 분석
  print(f"\n" + "=" * 60)
  print("성능 분석")
  print("=" * 60)

  try:
    from comparison_animation import performance_comparison

    print("\n1. 랜덤 배열 성능:")
    performance_comparison(random_arr)

    print("\n2. 거의 정렬된 배열 성능:")
    performance_comparison(nearly_sorted_arr)

    print("\n3. 역순 배열 성능:")
    performance_comparison(reversed_arr)

    print("\n4. 중복이 많은 배열 성능:")
    performance_comparison(few_unique_arr)

    print("\n5. 셸 정렬 유리 배열 성능:")
    performance_comparison(shell_favorable_arr)

    print("\n6. 삽입 정렬 유리 배열 성능:")
    performance_comparison(insertion_favorable_arr)

  except ImportError:
    print("❌ comparison_animation.py 파일을 찾을 수 없습니다.")
  except Exception as e:
    print(f"❌ 성능 분석 중 오류: {e}")

  # 비교 애니메이션 생성
  print(f"\n" + "=" * 60)
  print("비교 애니메이션 생성 중...")
  print("=" * 60)

  try:
    from comparison_animation import create_comparison_animation, shell_sort_with_steps, insertion_sort_with_steps

    # 셸 정렬 vs 삽입 정렬 비교 애니메이션들
    print("1. 랜덤 배열 비교 애니메이션 생성...")
    shell_steps, insertion_steps = shell_sort_with_steps(
        random_arr.copy()), insertion_sort_with_steps(random_arr.copy())
    create_comparison_animation(shell_steps, insertion_steps,
                                "img/random_comparison.gif", "Random Array - Shell vs Insertion")

    print("2. 셸 정렬 유리 배열 비교 애니메이션 생성...")
    shell_steps, insertion_steps = shell_sort_with_steps(
        shell_favorable_arr.copy()), insertion_sort_with_steps(shell_favorable_arr.copy())
    create_comparison_animation(shell_steps, insertion_steps,
                                "img/shell_vs_insertion.gif", "Shell Favorable - Shell vs Insertion")

    print("3. 삽입 정렬 유리 배열 비교 애니메이션 생성...")
    shell_steps, insertion_steps = shell_sort_with_steps(
        insertion_favorable_arr.copy()), insertion_sort_with_steps(insertion_favorable_arr.copy())
    create_comparison_animation(shell_steps, insertion_steps,
                                "img/insertion_vs_shell.gif", "Insertion Favorable - Shell vs Insertion")

    print("✅ 비교 애니메이션 생성 완료!")
    print("파일들:")
    print("- img/random_comparison.gif")
    print("- img/shell_vs_insertion.gif")
    print("- img/insertion_vs_shell.gif")

  except ImportError:
    print("❌ comparison_animation.py 파일을 찾을 수 없습니다.")
  except Exception as e:
    print(f"❌ 비교 애니메이션 생성 중 오류: {e}")


def create_gap_sequence_comparison():
  """다양한 gap 시퀀스 비교 애니메이션 생성"""
  print(f"\n" + "=" * 60)
  print("Gap 시퀀스 비교 애니메이션 생성")
  print("=" * 60)

  # 테스트 배열
  test_array = [64, 34, 25, 12, 22, 11, 90, 45, 67, 23, 78, 56, 89, 34, 12]
  print(f"테스트 배열: {test_array}")

  try:
    from shellSort import shell_sort

    # Shell's original sequence
    print("\n1. Shell's original sequence 애니메이션 생성...")
    arr_copy = test_array.copy()
    shell_sort(arr_copy, "shell")
    create_animation_for_data(test_array, 'img/shell_original.gif')

    # Knuth's sequence
    print("2. Knuth's sequence 애니메이션 생성...")
    arr_copy = test_array.copy()
    shell_sort(arr_copy, "knuth")
    create_animation_for_data(test_array, 'img/knuth_sequence.gif')

    print("✅ Gap 시퀀스 비교 애니메이션 생성 완료!")
    print("파일들:")
    print("- img/shell_original.gif")
    print("- img/knuth_sequence.gif")

  except ImportError:
    print("❌ shellSort.py 파일을 찾을 수 없습니다.")
  except Exception as e:
    print(f"❌ Gap 시퀀스 비교 애니메이션 생성 중 오류: {e}")


if __name__ == "__main__":
  create_animations_with_same_data()
  create_gap_sequence_comparison()

  print(f"\n" + "=" * 60)
  print("🎉 모든 셸 정렬 애니메이션 생성 완료!")
  print("=" * 60)
