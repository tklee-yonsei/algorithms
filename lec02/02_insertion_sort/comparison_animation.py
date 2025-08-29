# comparison_animation.py
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import os
from insertion_sort_animation import insertion_sort_with_animation


def create_comparison_animation():
  """4가지 케이스를 한 화면에 동시에 표시하는 애니메이션 생성"""
  print("=" * 60)
  print("삽입 정렬 비교 애니메이션 생성")
  print("=" * 60)

  # 기본 데이터 생성 (1-10까지의 숫자)
  base_data = list(range(1, 11))
  print(f"기본 데이터: {base_data}")

  # 4가지 케이스 생성
  cases = {}

  # 1. 랜덤 배열
  random_arr = base_data.copy()
  random.shuffle(random_arr)
  cases['random'] = {
      'data': random_arr,
      'name': 'Random Array',
      'color': '#FF6B6B'
  }

  # 2. 거의 정렬된 배열
  nearly_sorted_arr = base_data.copy()
  for _ in range(2):
    i = random.randint(0, 9)
    j = random.randint(0, 9)
    nearly_sorted_arr[i], nearly_sorted_arr[j] = nearly_sorted_arr[j], nearly_sorted_arr[i]
  cases['nearly_sorted'] = {
      'data': nearly_sorted_arr,
      'name': 'Nearly Sorted',
      'color': '#4ECDC4'
  }

  # 3. 역순 배열
  reversed_arr = base_data.copy()
  reversed_arr.reverse()
  cases['reversed'] = {
      'data': reversed_arr,
      'name': 'Reversed Array',
      'color': '#45B7D1'
  }

  # 4. 중복이 많은 배열
  few_unique_arr = base_data.copy()
  for i in range(3, 6):
    few_unique_arr[i] = 1
  for i in range(7, 10):
    few_unique_arr[i] = 2
  cases['few_unique'] = {
      'data': few_unique_arr,
      'name': 'Few Unique',
      'color': '#96CEB4'
  }

  # 각 케이스의 정렬 과정 기록
  all_steps = {}
  all_colors = {}
  max_steps = 0

  for case_name, case_info in cases.items():
    print(f"\n{case_info['name']} 처리 중...")
    steps, colors = insertion_sort_with_animation(case_info['data'].copy())
    all_steps[case_name] = steps
    all_colors[case_name] = colors
    max_steps = max(max_steps, len(steps))

  # 애니메이션 생성
  create_comparison_animation_frames(all_steps, all_colors, cases, max_steps)

  print(f"\n비교 애니메이션이 생성되었습니다!")
  print("파일: img/comparison_animation.gif")


def create_comparison_animation_frames(all_steps, all_colors, cases, max_steps):
  """비교 애니메이션 프레임 생성"""
  # 스타일 설정
  plt.style.use('seaborn-v0_8')
  fig, axes = plt.subplots(2, 2, figsize=(16, 12))
  fig.suptitle('Insertion Sort Comparison - Different Data Patterns',
               fontsize=18, fontweight='bold', color='#2C3E50')

  # 배경색 설정
  fig.patch.set_facecolor('#F8F9FA')
  for ax in axes.flat:
    ax.set_facecolor('#F8F9FA')

  case_names = list(cases.keys())
  case_positions = [(0, 0), (0, 1), (1, 0), (1, 1)]

  def animate(frame):
    # 각 케이스의 완료 상태 추적
    completion_status = {}

    # 모든 서브플롯 초기화
    for i, (case_name, (row, col)) in enumerate(zip(case_names, case_positions)):
      ax = axes[row, col]
      ax.clear()
      ax.set_facecolor('#F8F9FA')

      # 현재 프레임에 해당하는 데이터 가져오기
      current_frame = min(frame, len(all_steps[case_name]) - 1)
      current_data = all_steps[case_name][current_frame]
      current_colors = all_colors[case_name][current_frame]

      # 바형 그래프 그리기
      bars = ax.bar(range(len(current_data)), current_data,
                    color=current_colors, edgecolor='#2C3E50', linewidth=1.5,
                    alpha=0.8, width=0.7)

      # 그래프 설정
      ax.set_xlim(-0.5, len(current_data) - 0.5)
      ax.set_ylim(0, 11)
      ax.set_title(f"{cases[case_name]['name']}\nStep {current_frame + 1}/{len(all_steps[case_name])}",
                   fontsize=12, fontweight='bold', color='#2C3E50')

      # 값 표시
      for j, bar in enumerate(bars):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.2,
                f'{int(height)}', ha='center', va='bottom',
                fontweight='bold', fontsize=9, color='#2C3E50')

      # 그리드 설정
      ax.grid(True, alpha=0.2, linestyle='-', linewidth=0.5, color='#95A5A6')

      # 축 스타일링
      ax.spines['top'].set_visible(False)
      ax.spines['right'].set_visible(False)
      ax.spines['left'].set_color('#BDC3C7')
      ax.spines['bottom'].set_color('#BDC3C7')

      # 축 눈금 설정
      ax.tick_params(axis='both', colors='#7F8C8D', labelsize=9)

      # 정렬 진행률 계산 (실제 정렬된 요소 수 기반)
      sorted_count = 0
      for k in range(len(current_data)):
        if k < len(current_data) - 1:  # 마지막 요소가 아닌 경우
          # 현재 위치까지 정렬이 완료되었는지 확인
          is_sorted = True
          for m in range(k + 1):
            if current_data[m] != m + 1:  # 1부터 시작하는 정렬된 배열과 비교
              is_sorted = False
              break
          if is_sorted:
            sorted_count = k + 1
        else:  # 마지막 요소
          # 전체 배열이 정렬되었는지 확인
          if all(current_data[i] == i + 1 for i in range(len(current_data))):
            sorted_count = len(current_data)

      progress = (sorted_count / len(current_data)) * 100
      completion_status[case_name] = {
          'progress': progress,
          'completed': sorted_count == len(current_data),
          'step': current_frame + 1
      }

      # 진행률 표시
      ax.text(0.02, 0.98, f'Progress: {progress:.0f}%',
              transform=ax.transAxes, fontsize=10, fontweight='bold',
              verticalalignment='top', color='#2C3E50',
              bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))

    return []

  # 애니메이션 생성
  anim = animation.FuncAnimation(fig, animate, frames=max_steps,
                                 interval=300, repeat=True, blit=False)

  # GIF로 저장
  script_dir = os.path.dirname(os.path.abspath(__file__))
  gif_path = os.path.join(script_dir, 'img', 'comparison_animation.gif')
  anim.save(gif_path, writer='pillow', fps=3, dpi=150)
  plt.close()

  print(f"Animation saved as '{gif_path}'")


if __name__ == "__main__":
  create_comparison_animation()
