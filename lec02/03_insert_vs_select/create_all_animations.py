# create_all_animations.py
import os
import sys

# 상위 디렉토리의 모듈들을 import하기 위해 경로 추가
sys.path.append('../01_selection_sort')
sys.path.append('../02_insertion_sort')


def create_all_animations():
  """모든 비교 애니메이션 생성"""
  print("=" * 60)
  print("Insertion Sort vs Selection Sort 모든 애니메이션 생성")
  print("=" * 60)

  # 1. 속도 비교 애니메이션 생성
  print("\n1. 속도 비교 애니메이션 생성 중...")
  try:
    from speed_comparison_animation import create_speed_comparison_animation
    create_speed_comparison_animation()
    print("✅ 속도 비교 애니메이션 생성 완료!")
  except Exception as e:
    print(f"❌ 속도 비교 애니메이션 생성 중 오류: {e}")

  # 2. 종합 비교 애니메이션 생성
  print("\n2. 종합 비교 애니메이션 생성 중...")
  try:
    from comprehensive_comparison_animation import create_comprehensive_comparison_animation
    create_comprehensive_comparison_animation()
    print("✅ 종합 비교 애니메이션 생성 완료!")
  except Exception as e:
    print(f"❌ 종합 비교 애니메이션 생성 중 오류: {e}")

  print(f"\n" + "=" * 60)
  print("모든 애니메이션 생성 완료!")
  print("=" * 60)
  print("생성된 파일들:")
  print("- img/speed_comparison.gif")
  print("- img/comprehensive_comparison.gif")
  print("- complexity_analysis.md")
  print("=" * 60)

  # 생성된 파일 목록 확인
  script_dir = os.path.dirname(os.path.abspath(__file__))
  img_dir = os.path.join(script_dir, 'img')

  if os.path.exists(img_dir):
    files = os.listdir(img_dir)
    print(f"\nimg/ 디렉토리의 파일들:")
    for file in files:
      if file.endswith('.gif'):
        file_path = os.path.join(img_dir, file)
        file_size = os.path.getsize(file_path) / (1024 * 1024)  # MB
        print(f"- {file} ({file_size:.1f} MB)")


def show_complexity_summary():
  """복잡도 요약 정보 출력"""
  print(f"\n" + "=" * 60)
  print("복잡도 비교 요약")
  print("=" * 60)

  print("\n📊 시간 복잡도 (Time Complexity):")
  print("┌─────────────────┬─────────────┬───────────────┬─────────────┐")
  print("│   알고리즘      │  Best Case  │ Average Case  │ Worst Case  │")
  print("├─────────────────┼─────────────┼───────────────┼─────────────┤")
  print("│ Selection Sort  │    O(n²)    │    O(n²)      │    O(n²)    │")
  print("│ Insertion Sort  │    O(n)     │    O(n²)      │    O(n²)    │")
  print("└─────────────────┴─────────────┴───────────────┴─────────────┘")

  print("\n💾 공간 복잡도 (Space Complexity):")
  print("┌─────────────────┬─────────────┬─────────────────────────────┐")
  print("│   알고리즘      │ 공간 복잡도 │           설명              │")
  print("├─────────────────┼─────────────┼─────────────────────────────┤")
  print("│ Selection Sort  │    O(1)     │    제자리 정렬 (In-place)   │")
  print("│ Insertion Sort  │    O(1)     │    제자리 정렬 (In-place)   │")
  print("└─────────────────┴─────────────┴─────────────────────────────┘")

  print("\n🔒 안정성 (Stability):")
  print("┌─────────────────┬─────────────┬─────────────────────────────┐")
  print("│   알고리즘      │   안정성    │           설명              │")
  print("├─────────────────┼─────────────┼─────────────────────────────┤")
  print("│ Selection Sort  │   불안정    │  동일 값 순서 변경 가능     │")
  print("│ Insertion Sort  │    안정     │  동일 값 순서 유지          │")
  print("└─────────────────┴─────────────┴─────────────────────────────┘")

  print("\n💡 주요 차이점:")
  print("• Selection Sort: 데이터 상태와 관계없이 일정한 성능")
  print("• Insertion Sort: 이미 정렬된 데이터에서는 매우 효율적")
  print("• Insertion Sort: 적응형 알고리즘으로 실시간 데이터에 유리")


if __name__ == "__main__":
  create_all_animations()
  show_complexity_summary()
