# create_animations.py
import random
import numpy as np
from merge_sort_animation import create_animation_for_data


def create_animations_with_same_data():
  """같은 데이터를 다른 순서로 배치하여 애니메이션 생성"""
  print("=" * 60)
  print("병합 정렬 애니메이션 생성")
  print("=" * 60)

  # 기본 데이터 생성 (1-8까지의 숫자, merge sort는 복잡하므로 작은 크기 사용)
  base_data = list(range(1, 9))
  print(f"기본 데이터: {base_data}")

  # 1. 랜덤 배열 (기본 데이터를 무작위로 섞기)
  print(f"\n1. 랜덤 배열 애니메이션 생성 중...")
  random_arr = base_data.copy()
  random.shuffle(random_arr)
  print(f"랜덤 배열: {random_arr}")
  create_animation_for_data(random_arr, 'img/random_array.gif')

  # 2. 거의 정렬된 배열 (기본 데이터에서 몇 개만 교환)
  print(f"\n2. 거의 정렬된 배열 애니메이션 생성 중...")
  nearly_sorted_arr = base_data.copy()
  # 2-3개만 교환
  for _ in range(2):
    i = random.randint(0, 7)
    j = random.randint(0, 7)
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
  for i in range(2, 4):  # 3, 4번째 위치를 1로 변경
    few_unique_arr[i] = 1
  for i in range(5, 7):  # 6, 7번째 위치를 2로 변경
    few_unique_arr[i] = 2
  print(f"중복이 많은 배열: {few_unique_arr}")
  create_animation_for_data(few_unique_arr, 'img/few_unique.gif')

  print(f"\n" + "=" * 60)
  print("개별 애니메이션 생성 완료!")
  print("=" * 60)
  print("생성된 파일들:")
  print("- img/random_array.gif")
  print("- img/nearly_sorted.gif")
  print("- img/reversed_array.gif")
  print("- img/few_unique.gif")
  print("=" * 60)

  # 각 배열의 정렬 결과 비교
  print("\n정렬 결과 비교:")
  print(f"랜덤 배열 정렬 후: {sorted(random_arr)}")
  print(f"거의 정렬된 배열 정렬 후: {sorted(nearly_sorted_arr)}")
  print(f"역순 배열 정렬 후: {sorted(reversed_arr)}")
  print(f"중복이 많은 배열 정렬 후: {sorted(few_unique_arr)}")

  # 비교 애니메이션 생성
  print(f"\n" + "=" * 60)
  print("비교 애니메이션 생성 중...")
  print("=" * 60)

  try:
    from comparison_animation import create_comparison_animation
    create_comparison_animation()
    print("✅ 비교 애니메이션 생성 완료!")
    print("파일: img/comparison_animation.gif")
  except ImportError:
    print("❌ comparison_animation.py 파일을 찾을 수 없습니다.")
  except Exception as e:
    print(f"❌ 비교 애니메이션 생성 중 오류: {e}")


def create_step_by_step_demo():
  """단계별 병합 정렬 데모"""
  print(f"\n" + "=" * 60)
  print("단계별 병합 정렬 데모")
  print("=" * 60)

  # 작은 배열로 단계별 설명
  demo_arr = [8, 3, 5, 4, 7, 6, 1, 2]
  print(f"데모 배열: {demo_arr}")

  print("\n병합 정렬의 분할-정복 과정:")
  print("1. 분할(Divide): 배열을 반으로 나눔")
  print("2. 정복(Conquer): 각 부분을 재귀적으로 정렬")
  print("3. 결합(Combine): 정렬된 부분들을 병합")

  create_animation_for_data(demo_arr, 'img/step_by_step_demo.gif')
  print("✅ 단계별 데모 애니메이션 생성 완료!")
  print("파일: img/step_by_step_demo.gif")


def create_complexity_demo():
  """시간 복잡도 데모"""
  print(f"\n" + "=" * 60)
  print("시간 복잡도 데모 (O(n log n))")
  print("=" * 60)

  # 다양한 크기의 배열로 복잡도 시연
  sizes = [4, 8]

  for size in sizes:
    print(f"\n크기 {size}인 배열:")
    arr = list(range(size, 0, -1))  # 역순 배열
    print(f"배열: {arr}")

    filename = f'img/complexity_demo_size_{size}.gif'
    create_animation_for_data(arr, filename)
    print(f"✅ 크기 {size} 데모 애니메이션 생성 완료!")
    print(f"파일: {filename}")


if __name__ == "__main__":
  # 기본 애니메이션들 생성
  create_animations_with_same_data()

  # 단계별 데모
  create_step_by_step_demo()

  # 복잡도 데모
  create_complexity_demo()

  print(f"\n" + "=" * 60)
  print("모든 애니메이션 생성이 완료되었습니다!")
  print("=" * 60)
