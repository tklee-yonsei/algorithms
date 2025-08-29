# create_animations.py
from comparison_animation import create_comparison_for_data
from bubble_sort_animation import create_animation_for_data
import os
import sys

# 현재 디렉토리를 Python 경로에 추가
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)


def create_all_animations():
  """다양한 데이터 패턴에 대한 모든 애니메이션 생성"""

  print("버블 정렬 애니메이션 생성 시작...")
  print("=" * 50)

  # 다양한 테스트 데이터 패턴
  test_patterns = {
      'random_array': [64, 34, 25, 12, 22, 11, 90],
      'nearly_sorted': [11, 12, 25, 22, 34, 64, 90],
      'reversed_array': [90, 64, 34, 25, 22, 12, 11],
      'few_unique': [3, 1, 3, 2, 1, 2, 3, 1, 2]
  }

  # 이미지 저장 디렉토리 확인/생성
  img_dir = os.path.join(current_dir, 'img')
  if not os.path.exists(img_dir):
    os.makedirs(img_dir)
    print(f"Created directory: {img_dir}")

  print("\n1. 버블 정렬 단독 애니메이션 생성...")
  print("-" * 40)

  for pattern_name, data in test_patterns.items():
    print(f"생성 중: {pattern_name} - 데이터: {data}")

    # 버블 정렬 애니메이션
    bubble_filename = os.path.join(img_dir, f'{pattern_name}.gif')
    create_animation_for_data(data, bubble_filename)

    print(f"✓ 저장됨: {bubble_filename}")

  print("\n2. 정렬 알고리즘 비교 애니메이션 생성...")
  print("-" * 40)

  for pattern_name, data in test_patterns.items():
    print(f"생성 중: {pattern_name} 비교 - 데이터: {data}")

    # 비교 애니메이션
    comparison_filename = os.path.join(img_dir, f'comparison_{pattern_name}.gif')
    create_comparison_for_data(data, comparison_filename)

    print(f"✓ 저장됨: {comparison_filename}")

  print("\n3. 기본 애니메이션 생성...")
  print("-" * 40)

  # 기본 데이터로 메인 애니메이션 생성
  main_data = [64, 34, 25, 12, 22, 11, 90]

  # 메인 버블 정렬 애니메이션
  main_bubble_path = os.path.join(current_dir, 'bubble_sort.gif')
  create_animation_for_data(main_data, main_bubble_path)
  print(f"✓ 메인 버블 정렬 애니메이션: {main_bubble_path}")

  # 메인 비교 애니메이션
  main_comparison_path = os.path.join(current_dir, 'comparison_animation.gif')
  create_comparison_for_data(main_data, main_comparison_path)
  print(f"✓ 메인 비교 애니메이션: {main_comparison_path}")

  print("\n" + "=" * 50)
  print("모든 애니메이션 생성 완료!")
  print("=" * 50)

  # 생성된 파일 목록 출력
  print("\n생성된 파일들:")

  print("\n📁 메인 디렉토리:")
  main_files = ['bubble_sort.gif', 'comparison_animation.gif']
  for file in main_files:
    file_path = os.path.join(current_dir, file)
    if os.path.exists(file_path):
      print(f"  ✓ {file}")

  print("\n📁 img/ 디렉토리:")
  if os.path.exists(img_dir):
    img_files = sorted([f for f in os.listdir(img_dir) if f.endswith('.gif')])
    for file in img_files:
      print(f"  ✓ {file}")


def main():
  """메인 함수"""
  try:
    create_all_animations()
  except ImportError as e:
    print(f"모듈 import 오류: {e}")
    print("필요한 라이브러리가 설치되어 있는지 확인해주세요:")
    print("pip install matplotlib numpy pillow")
  except Exception as e:
    print(f"애니메이션 생성 중 오류 발생: {e}")


if __name__ == "__main__":
  main()
