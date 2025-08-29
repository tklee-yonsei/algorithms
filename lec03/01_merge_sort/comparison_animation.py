# comparison_animation.py
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import os
from merge_sort_animation import merge_sort_with_animation


def create_comparison_animation():
  """다양한 데이터 패턴에 대한 병합 정렬 비교 애니메이션"""

  # 4가지 데이터 패턴
  base_data = [8, 7, 6, 5, 4, 3, 2, 1]  # 작은 크기로 시작

  patterns = {
      'Random': [8, 3, 6, 1, 5, 2, 7, 4],
      'Nearly Sorted': [1, 2, 4, 3, 5, 6, 8, 7],  # 몇 개만 바뀜
      'Reversed': [8, 7, 6, 5, 4, 3, 2, 1],
      'Few Unique': [1, 1, 2, 2, 1, 2, 1, 2]
  }

  # 각 패턴에 대한 정렬 과정 기록
  all_steps = {}
  all_colors = {}
  max_steps = 0

  for name, data in patterns.items():
    print(f"Processing {name}: {data}")
    steps, colors, memory_usage, memory_details = merge_sort_with_animation(data.copy())
    all_steps[name] = steps
    all_colors[name] = colors
    max_steps = max(max_steps, len(steps))

  # 모든 패턴의 스텝 수를 동일하게 맞추기 (마지막 상태 반복)
  for name in patterns.keys():
    while len(all_steps[name]) < max_steps:
      all_steps[name].append(all_steps[name][-1])
      all_colors[name].append(all_colors[name][-1])

  # 애니메이션 생성
  fig, axes = plt.subplots(2, 2, figsize=(20, 16))
  fig.suptitle('Merge Sort Comparison: Different Data Patterns',
               fontsize=20, fontweight='bold', y=0.95)

  # 배경색 설정
  fig.patch.set_facecolor('#F8F9FA')

  # 서브플롯 위치
  positions = [(0, 0), (0, 1), (1, 0), (1, 1)]
  pattern_names = list(patterns.keys())

  def animate(frame):
    for idx, (name, pos) in enumerate(zip(pattern_names, positions)):
      ax = axes[pos[0]][pos[1]]
      ax.clear()
      ax.set_facecolor('#F8F9FA')

      # 현재 프레임의 데이터
      current_data = all_steps[name][frame]
      current_colors = all_colors[name][frame]

      # 바 차트 생성
      bars = ax.bar(range(len(current_data)), current_data,
                    color=current_colors, edgecolor='#2C3E50',
                    linewidth=1.5, alpha=0.8)

      # 그래프 설정
      ax.set_xlim(-0.5, len(current_data) - 0.5)
      ax.set_ylim(0, max(max(step) for step in all_steps[name]) * 1.1)

      # 제목과 레이블
      ax.set_title(f'{name} Array', fontsize=14, fontweight='bold',
                   color='#2C3E50', pad=15)
      ax.set_xlabel('Index', fontsize=12, color='#2C3E50')
      ax.set_ylabel('Value', fontsize=12, color='#2C3E50')

      # 값 표시
      for i, bar in enumerate(bars):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                f'{int(height)}', ha='center', va='bottom',
                fontweight='bold', fontsize=10, color='#2C3E50')

      # 그리드
      ax.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)

      # 축 스타일링
      ax.spines['top'].set_visible(False)
      ax.spines['right'].set_visible(False)
      ax.spines['left'].set_color('#BDC3C7')
      ax.spines['bottom'].set_color('#BDC3C7')
      ax.tick_params(axis='both', colors='#7F8C8D', labelsize=10)

  # 범례 추가 (전체 그림에 대해)
  legend_elements = [
      plt.Rectangle((0, 0), 1, 1, facecolor='#E3F2FD',
                    edgecolor='#2C3E50', label='Unsorted'),
      plt.Rectangle((0, 0), 1, 1, facecolor='#FFE082',
                    edgecolor='#2C3E50', label='Left Subarray'),
      plt.Rectangle((0, 0), 1, 1, facecolor='#FFAB91',
                    edgecolor='#2C3E50', label='Right Subarray'),
      plt.Rectangle((0, 0), 1, 1, facecolor='#FFD54F',
                    edgecolor='#2C3E50', label='Comparing Left'),
      plt.Rectangle((0, 0), 1, 1, facecolor='#FF8A80',
                    edgecolor='#2C3E50', label='Comparing Right'),
      plt.Rectangle((0, 0), 1, 1, facecolor='#4CAF50',
                    edgecolor='#2C3E50', label='Merged/Sorted')
  ]

  fig.legend(handles=legend_elements, loc='lower center',
             ncol=6, fontsize=12, frameon=True, fancybox=True, shadow=True,
             bbox_to_anchor=(0.5, 0.02))

  # 진행 상황 표시
  def animate_with_progress(frame):
    animate(frame)
    fig.suptitle(f'Merge Sort Comparison - Step {frame + 1}/{max_steps}',
                 fontsize=20, fontweight='bold', y=0.95)
    return []

  # 애니메이션 생성
  anim = animation.FuncAnimation(fig, animate_with_progress, frames=max_steps,
                                 interval=1000, repeat=True, blit=False)

  # GIF로 저장
  script_dir = os.path.dirname(os.path.abspath(__file__))
  gif_path = os.path.join(script_dir, 'img', 'comparison_animation.gif')
  anim.save(gif_path, writer='pillow', fps=1, dpi=100)
  plt.close()

  print(f"Comparison animation saved as '{gif_path}'")

  # 성능 분석 출력
  print("\n성능 분석:")
  print("=" * 50)
  print("병합 정렬의 특징:")
  print("- 시간 복잡도: O(n log n) - 모든 경우에 동일")
  print("- 공간 복잡도: O(n) - 추가 메모리 필요")
  print("- 안정 정렬: 동일한 값의 상대적 순서 유지")
  print("- 분할-정복 알고리즘")
  print("\n데이터 패턴별 특징:")
  print("- 랜덤 배열: 표준적인 성능")
  print("- 거의 정렬된 배열: 여전히 O(n log n)")
  print("- 역순 배열: 여전히 O(n log n)")
  print("- 중복이 많은 배열: 여전히 O(n log n)")
  print("\n병합 정렬은 입력 데이터의 패턴에 관계없이")
  print("항상 일정한 성능을 보입니다!")


def create_merge_vs_other_sorts():
  """병합 정렬과 다른 정렬 알고리즘 비교"""
  print("\n병합 정렬 vs 다른 정렬 알고리즘")
  print("=" * 50)

  comparison_data = {
      "알고리즘": ["Merge Sort", "Quick Sort", "Heap Sort", "Insertion Sort", "Selection Sort"],
      "최선 시간복잡도": ["O(n log n)", "O(n log n)", "O(n log n)", "O(n)", "O(n²)"],
      "평균 시간복잡도": ["O(n log n)", "O(n log n)", "O(n log n)", "O(n²)", "O(n²)"],
      "최악 시간복잡도": ["O(n log n)", "O(n²)", "O(n log n)", "O(n²)", "O(n²)"],
      "공간복잡도": ["O(n)", "O(log n)", "O(1)", "O(1)", "O(1)"],
      "안정성": ["안정", "불안정", "불안정", "안정", "불안정"]
  }

  print(f"{'알고리즘':<15} {'최선':<12} {'평균':<12} {'최악':<12} {'공간':<8} {'안정성'}")
  print("-" * 80)

  for i in range(len(comparison_data["알고리즘"])):
    print(f"{comparison_data['알고리즘'][i]:<15} "
          f"{comparison_data['최선 시간복잡도'][i]:<12} "
          f"{comparison_data['평균 시간복잡도'][i]:<12} "
          f"{comparison_data['최악 시간복잡도'][i]:<12} "
          f"{comparison_data['공간복잡도'][i]:<8} "
          f"{comparison_data['안정성'][i]}")


if __name__ == "__main__":
  # 비교 애니메이션 생성
  create_comparison_animation()

  # 다른 정렬 알고리즘과 비교
  create_merge_vs_other_sorts()
