# comprehensive_comparison_animation.py
from insertion_sort_animation import insertion_sort_with_animation
from selection_sort_animation import selection_sort_with_animation
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import os
import sys

# 상위 디렉토리의 모듈들을 import하기 위해 경로 추가
sys.path.append('../01_selection_sort')
sys.path.append('../02_insertion_sort')


def create_comprehensive_comparison_animation():
  """4가지 케이스에 대한 insertion sort와 selection sort의 종합 비교 애니메이션"""
  print("=" * 60)
  print("Insertion Sort vs Selection Sort 종합 비교 애니메이션 생성")
  print("=" * 60)

  # 기본 데이터 생성 (1-10까지의 숫자)
  base_data = list(range(1, 11))
  print(f"기본 데이터: {base_data}")

  # 4가지 케이스 생성
  cases = {}

  # 1. 랜덤 배열
  random.seed(42)  # 재현 가능한 결과를 위해 시드 설정
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
  selection_steps = {}
  selection_colors = {}
  insertion_steps = {}
  insertion_colors = {}
  max_steps = 0

  for case_name, case_info in cases.items():
    print(f"\n{case_info['name']} 처리 중...")

    # Selection Sort 과정 기록
    sel_steps, sel_colors = selection_sort_with_animation(case_info['data'].copy())
    selection_steps[case_name] = sel_steps
    selection_colors[case_name] = sel_colors

    # Insertion Sort 과정 기록
    ins_steps, ins_colors = insertion_sort_with_animation(case_info['data'].copy())
    insertion_steps[case_name] = ins_steps
    insertion_colors[case_name] = ins_colors

    max_steps = max(max_steps, len(sel_steps), len(ins_steps))

  # 애니메이션 생성
  create_comprehensive_comparison_frames(selection_steps, selection_colors,
                                         insertion_steps, insertion_colors,
                                         cases, max_steps)

  print(f"\n종합 비교 애니메이션이 생성되었습니다!")
  print("파일: img/comprehensive_comparison.gif")


def create_comprehensive_comparison_frames(selection_steps, selection_colors,
                                           insertion_steps, insertion_colors,
                                           cases, max_steps):
  """종합 비교 애니메이션 프레임 생성"""
  # 스타일 설정
  plt.style.use('seaborn-v0_8')
  fig, axes = plt.subplots(2, 4, figsize=(20, 10))
  fig.suptitle('Insertion Sort vs Selection Sort - Comprehensive Comparison',
               fontsize=18, fontweight='bold', color='#2C3E50')

  # 배경색 설정
  fig.patch.set_facecolor('#F8F9FA')
  for ax in axes.flat:
    ax.set_facecolor('#F8F9FA')

  case_names = list(cases.keys())

  def animate(frame):
    # 모든 서브플롯 초기화
    for i, case_name in enumerate(case_names):
      # Selection Sort (위쪽 행)
      ax1 = axes[0, i]
      ax1.clear()
      ax1.set_facecolor('#F8F9FA')

      # 현재 프레임에 해당하는 데이터 가져오기
      current_frame = min(frame, len(selection_steps[case_name]) - 1)
      current_data = selection_steps[case_name][current_frame]
      current_colors = selection_colors[case_name][current_frame]

      # 바형 그래프 그리기
      bars1 = ax1.bar(range(len(current_data)), current_data,
                      color=current_colors, edgecolor='#2C3E50', linewidth=1.5,
                      alpha=0.8, width=0.7)

      # 그래프 설정
      ax1.set_xlim(-0.5, len(current_data) - 0.5)
      ax1.set_ylim(0, 11)
      ax1.set_title(f"Selection Sort\n{cases[case_name]['name']}\nStep {current_frame + 1}/{len(selection_steps[case_name])}",
                    fontsize=10, fontweight='bold', color='#2C3E50')

      # 값 표시
      for j, bar in enumerate(bars1):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 0.2,
                 f'{int(height)}', ha='center', va='bottom',
                 fontweight='bold', fontsize=8, color='#2C3E50')

      # 그리드 설정
      ax1.grid(True, alpha=0.2, linestyle='-', linewidth=0.5, color='#95A5A6')

      # 축 스타일링
      ax1.spines['top'].set_visible(False)
      ax1.spines['right'].set_visible(False)
      ax1.spines['left'].set_color('#BDC3C7')
      ax1.spines['bottom'].set_color('#BDC3C7')

      # 축 눈금 설정
      ax1.tick_params(axis='both', colors='#7F8C8D', labelsize=8)

      # Insertion Sort (아래쪽 행)
      ax2 = axes[1, i]
      ax2.clear()
      ax2.set_facecolor('#F8F9FA')

      # 현재 프레임에 해당하는 데이터 가져오기
      current_frame = min(frame, len(insertion_steps[case_name]) - 1)
      current_data = insertion_steps[case_name][current_frame]
      current_colors = insertion_colors[case_name][current_frame]

      # 바형 그래프 그리기
      bars2 = ax2.bar(range(len(current_data)), current_data,
                      color=current_colors, edgecolor='#2C3E50', linewidth=1.5,
                      alpha=0.8, width=0.7)

      # 그래프 설정
      ax2.set_xlim(-0.5, len(current_data) - 0.5)
      ax2.set_ylim(0, 11)
      ax2.set_title(f"Insertion Sort\n{cases[case_name]['name']}\nStep {current_frame + 1}/{len(insertion_steps[case_name])}",
                    fontsize=10, fontweight='bold', color='#2C3E50')

      # 값 표시
      for j, bar in enumerate(bars2):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 0.2,
                 f'{int(height)}', ha='center', va='bottom',
                 fontweight='bold', fontsize=8, color='#2C3E50')

      # 그리드 설정
      ax2.grid(True, alpha=0.2, linestyle='-', linewidth=0.5, color='#95A5A6')

      # 축 스타일링
      ax2.spines['top'].set_visible(False)
      ax2.spines['right'].set_visible(False)
      ax2.spines['left'].set_color('#BDC3C7')
      ax2.spines['bottom'].set_color('#BDC3C7')

      # 축 눈금 설정
      ax2.tick_params(axis='both', colors='#7F8C8D', labelsize=8)

      # 진행률 표시
      selection_progress = ((current_frame + 1) / len(selection_steps[case_name])) * 100
      insertion_progress = ((current_frame + 1) / len(insertion_steps[case_name])) * 100

      ax1.text(0.02, 0.98, f'Progress: {selection_progress:.0f}%',
               transform=ax1.transAxes, fontsize=8, fontweight='bold',
               verticalalignment='top', color='#2C3E50',
               bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8))

      ax2.text(0.02, 0.98, f'Progress: {insertion_progress:.0f}%',
               transform=ax2.transAxes, fontsize=8, fontweight='bold',
               verticalalignment='top', color='#2C3E50',
               bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8))

      # 스텝 수 비교 표시
      ax1.text(0.98, 0.98, f'Steps: {len(selection_steps[case_name])}',
               transform=ax1.transAxes, fontsize=8, fontweight='bold',
               verticalalignment='top', horizontalalignment='right', color='#2C3E50',
               bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8))

      ax2.text(0.98, 0.98, f'Steps: {len(insertion_steps[case_name])}',
               transform=ax2.transAxes, fontsize=8, fontweight='bold',
               verticalalignment='top', horizontalalignment='right', color='#2C3E50',
               bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8))

    return []

  # 애니메이션 생성
  anim = animation.FuncAnimation(fig, animate, frames=max_steps,
                                 interval=300, repeat=True, blit=False)

  # GIF로 저장
  script_dir = os.path.dirname(os.path.abspath(__file__))
  gif_path = os.path.join(script_dir, 'img', 'comprehensive_comparison.gif')
  anim.save(gif_path, writer='pillow', fps=3, dpi=150)
  plt.close()

  print(f"Animation saved as '{gif_path}'")


if __name__ == "__main__":
  create_comprehensive_comparison_animation()
