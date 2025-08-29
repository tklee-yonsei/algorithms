# speed_comparison_animation.py
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


def create_speed_comparison_animation():
  """랜덤 배열에 대한 insertion sort와 selection sort의 속도 비교 애니메이션"""
  print("=" * 60)
  print("Insertion Sort vs Selection Sort 속도 비교 애니메이션 생성")
  print("=" * 60)

  # 동일한 랜덤 배열 생성
  random.seed(42)  # 재현 가능한 결과를 위해 시드 설정
  base_data = list(range(1, 11))
  random_arr = base_data.copy()
  random.shuffle(random_arr)

  print(f"테스트 배열: {random_arr}")

  # Selection Sort 과정 기록
  print("\nSelection Sort 처리 중...")
  selection_steps, selection_colors = selection_sort_with_animation(random_arr.copy())

  # Insertion Sort 과정 기록
  print("Insertion Sort 처리 중...")
  insertion_steps, insertion_colors = insertion_sort_with_animation(random_arr.copy())

  # 애니메이션 생성
  create_speed_comparison_frames(selection_steps, selection_colors,
                                 insertion_steps, insertion_colors)

  print(f"\n속도 비교 애니메이션이 생성되었습니다!")
  print("파일: img/speed_comparison.gif")


def create_speed_comparison_frames(selection_steps, selection_colors,
                                   insertion_steps, insertion_colors):
  """속도 비교 애니메이션 프레임 생성"""
  # 스타일 설정
  plt.style.use('seaborn-v0_8')
  fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 12))
  fig.suptitle('Insertion Sort vs Selection Sort - Speed Comparison',
               fontsize=18, fontweight='bold', color='#2C3E50')

  # 배경색 설정
  fig.patch.set_facecolor('#F8F9FA')
  ax1.set_facecolor('#F8F9FA')
  ax2.set_facecolor('#F8F9FA')

  # 최대 프레임 수 계산
  max_steps = max(len(selection_steps), len(insertion_steps))

  def animate(frame):
    # Selection Sort (위쪽)
    ax1.clear()
    ax1.set_facecolor('#F8F9FA')

    # 현재 프레임에 해당하는 데이터 가져오기
    current_frame = min(frame, len(selection_steps) - 1)
    current_data = selection_steps[current_frame]
    current_colors = selection_colors[current_frame]

    # 바형 그래프 그리기
    bars1 = ax1.bar(range(len(current_data)), current_data,
                    color=current_colors, edgecolor='#2C3E50', linewidth=2,
                    alpha=0.8, width=0.7)

    # 그래프 설정
    ax1.set_xlim(-0.5, len(current_data) - 0.5)
    ax1.set_ylim(0, 11)
    ax1.set_title(f"Selection Sort - Step {current_frame + 1}/{len(selection_steps)}",
                  fontsize=14, fontweight='bold', color='#2C3E50')

    # 값 표시
    for i, bar in enumerate(bars1):
      height = bar.get_height()
      ax1.text(bar.get_x() + bar.get_width()/2., height + 0.2,
               f'{int(height)}', ha='center', va='bottom',
               fontweight='bold', fontsize=11, color='#2C3E50')

    # 그리드 설정
    ax1.grid(True, alpha=0.2, linestyle='-', linewidth=0.5, color='#95A5A6')

    # 축 스타일링
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['left'].set_color('#BDC3C7')
    ax1.spines['bottom'].set_color('#BDC3C7')

    # 축 눈금 설정
    ax1.tick_params(axis='both', colors='#7F8C8D', labelsize=11)

    # Insertion Sort (아래쪽)
    ax2.clear()
    ax2.set_facecolor('#F8F9FA')

    # 현재 프레임에 해당하는 데이터 가져오기
    current_frame = min(frame, len(insertion_steps) - 1)
    current_data = insertion_steps[current_frame]
    current_colors = insertion_colors[current_frame]

    # 바형 그래프 그리기
    bars2 = ax2.bar(range(len(current_data)), current_data,
                    color=current_colors, edgecolor='#2C3E50', linewidth=2,
                    alpha=0.8, width=0.7)

    # 그래프 설정
    ax2.set_xlim(-0.5, len(current_data) - 0.5)
    ax2.set_ylim(0, 11)
    ax2.set_title(f"Insertion Sort - Step {current_frame + 1}/{len(insertion_steps)}",
                  fontsize=14, fontweight='bold', color='#2C3E50')
    ax2.set_xlabel('Array Index', fontsize=12, fontweight='bold', color='#2C3E50')

    # 값 표시
    for i, bar in enumerate(bars2):
      height = bar.get_height()
      ax2.text(bar.get_x() + bar.get_width()/2., height + 0.2,
               f'{int(height)}', ha='center', va='bottom',
               fontweight='bold', fontsize=11, color='#2C3E50')

    # 그리드 설정
    ax2.grid(True, alpha=0.2, linestyle='-', linewidth=0.5, color='#95A5A6')

    # 축 스타일링
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['left'].set_color('#BDC3C7')
    ax2.spines['bottom'].set_color('#BDC3C7')

    # 축 눈금 설정
    ax2.tick_params(axis='both', colors='#7F8C8D', labelsize=11)

    # 진행률 표시
    selection_progress = ((current_frame + 1) / len(selection_steps)) * 100
    insertion_progress = ((current_frame + 1) / len(insertion_steps)) * 100

    ax1.text(0.02, 0.98, f'Progress: {selection_progress:.0f}%',
             transform=ax1.transAxes, fontsize=10, fontweight='bold',
             verticalalignment='top', color='#2C3E50',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))

    ax2.text(0.02, 0.98, f'Progress: {insertion_progress:.0f}%',
             transform=ax2.transAxes, fontsize=10, fontweight='bold',
             verticalalignment='top', color='#2C3E50',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))

    # 스텝 수 비교 표시
    ax1.text(0.98, 0.98, f'Total Steps: {len(selection_steps)}',
             transform=ax1.transAxes, fontsize=10, fontweight='bold',
             verticalalignment='top', horizontalalignment='right', color='#2C3E50',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))

    ax2.text(0.98, 0.98, f'Total Steps: {len(insertion_steps)}',
             transform=ax2.transAxes, fontsize=10, fontweight='bold',
             verticalalignment='top', horizontalalignment='right', color='#2C3E50',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))

    return []

  # 애니메이션 생성
  anim = animation.FuncAnimation(fig, animate, frames=max_steps,
                                 interval=400, repeat=True, blit=False)

  # GIF로 저장
  script_dir = os.path.dirname(os.path.abspath(__file__))
  gif_path = os.path.join(script_dir, 'img', 'speed_comparison.gif')
  anim.save(gif_path, writer='pillow', fps=2.5, dpi=150)
  plt.close()

  print(f"Animation saved as '{gif_path}'")
  print(f"Selection Sort steps: {len(selection_steps)}")
  print(f"Insertion Sort steps: {len(insertion_steps)}")


if __name__ == "__main__":
  create_speed_comparison_animation()
