# comprehensive_three_way_comparison.py
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import os
import sys

# 상위 디렉토리의 모듈들을 import하기 위해 경로 추가
sys.path.append('../01_selection_sort')
sys.path.append('../02_insertion_sort')
sys.path.append('../05_shell_sort')


def insertion_sort_for_gap_with_steps(arr, start, gap, steps, base_step_count):
  """특정 gap 그룹에 대해 삽입 정렬을 수행하는 함수 (단계 추적 포함)"""
  n = len(arr)

  # 현재 gap 그룹의 요소들을 삽입 정렬
  for i in range(start + gap, n, gap):
    temp = arr[i]
    j = i

    # 현재 처리할 요소를 표시
    steps.append({
        'array': arr.copy(),
        'gap': gap,
        'start': start,
        'current_i': i,
        'current_j': j,
        'temp': temp,
        'algorithm': 'shell',
        'description': f'Shell Sort - Gap: {gap}, Current: {temp}',
        'step_count': base_step_count + len(steps)
    })

    while j >= start + gap and arr[j - gap] > temp:
      # 비교 중인 요소들 표시
      steps.append({
          'array': arr.copy(),
          'gap': gap,
          'start': start,
          'current_i': i,
          'current_j': j,
          'temp': temp,
          'algorithm': 'shell',
          'description': f'Shell Sort - Comparing',
          'step_count': base_step_count + len(steps)
      })

      arr[j] = arr[j - gap]
      j -= gap

    # temp를 올바른 위치에 삽입
    arr[j] = temp

    # 삽입 후 상태 표시
    steps.append({
        'array': arr.copy(),
        'gap': gap,
        'start': start,
        'current_i': i,
        'current_j': j,
        'temp': temp,
        'algorithm': 'shell',
        'description': f'Shell Sort - Inserted',
        'step_count': base_step_count + len(steps)
    })


def shell_sort_with_steps_local(arr):
  """Shell Sort with step tracking"""
  n = len(arr)
  gap = n // 2
  steps = []
  base_step_count = 0

  # 초기 상태 저장
  steps.append({
      'array': arr.copy(),
      'gap': gap,
      'start': -1,
      'current_i': -1,
      'current_j': -1,
      'temp': None,
      'algorithm': 'shell',
      'description': 'Shell Sort - Initial State',
      'step_count': base_step_count
  })

  while gap > 0:
    # 각 gap 그룹에 대해 삽입 정렬 수행
    for start in range(gap):
      insertion_sort_for_gap_with_steps(arr, start, gap, steps, base_step_count)
      base_step_count = len(steps)

    gap //= 2

  # 최종 정렬 완료 상태
  steps.append({
      'array': arr.copy(),
      'gap': 0,
      'start': -1,
      'current_i': -1,
      'current_j': -1,
      'temp': None,
      'algorithm': 'shell',
      'description': 'Shell Sort - Completed',
      'step_count': base_step_count
  })

  return steps


def create_comprehensive_three_way_comparison():
  """4가지 케이스에 대한 3개 정렬 알고리즘의 종합 비교 애니메이션"""
  print("=" * 80)
  print("Insertion Sort vs Selection Sort vs Shell Sort 종합 비교 애니메이션 생성")
  print("=" * 80)

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
  shell_steps = {}
  shell_colors = {}
  max_steps = 0

  for case_name, case_info in cases.items():
    print(f"\n{case_info['name']} 처리 중...")

    # Selection Sort 과정 기록
    try:
      from selection_sort_animation import selection_sort_with_animation
      sel_steps, sel_colors = selection_sort_with_animation(case_info['data'].copy())
      selection_steps[case_name] = sel_steps
      selection_colors[case_name] = sel_colors
    except Exception as e:
      print(f"Selection Sort 오류: {e}")
      selection_steps[case_name] = []
      selection_colors[case_name] = []

    # Insertion Sort 과정 기록
    try:
      from insertion_sort_animation import insertion_sort_with_animation
      ins_steps, ins_colors = insertion_sort_with_animation(case_info['data'].copy())
      insertion_steps[case_name] = ins_steps
      insertion_colors[case_name] = ins_colors
    except Exception as e:
      print(f"Insertion Sort 오류: {e}")
      insertion_steps[case_name] = []
      insertion_colors[case_name] = []

    # Shell Sort 과정 기록
    try:
      shell_steps_data = shell_sort_with_steps_local(case_info['data'].copy())
      shell_steps[case_name] = shell_steps_data
      shell_colors[case_name] = [['#FFD93D' if i == step.get('current_i', -1) else
                                 '#FF6B6B' if i == step.get('current_j', -1) else
                                  '#4ECDC4' for i in range(len(step['array']))]
                                 for step in shell_steps_data]
    except Exception as e:
      print(f"Shell Sort 오류: {e}")
      shell_steps[case_name] = []
      shell_colors[case_name] = []

    max_steps = max(max_steps, len(selection_steps[case_name]),
                    len(insertion_steps[case_name]), len(shell_steps[case_name]))

  # 애니메이션 생성
  create_comprehensive_three_way_comparison_frames(selection_steps, selection_colors,
                                                   insertion_steps, insertion_colors,
                                                   shell_steps, shell_colors,
                                                   cases, max_steps)

  print(f"\n종합 비교 애니메이션이 생성되었습니다!")
  print("파일: img/comprehensive_three_way_comparison.gif")


def create_comprehensive_three_way_comparison_frames(selection_steps, selection_colors,
                                                     insertion_steps, insertion_colors,
                                                     shell_steps, shell_colors,
                                                     cases, max_steps):
  """3개 정렬 알고리즘의 종합 비교 프레임 생성"""
  # 스타일 설정
  plt.style.use('seaborn-v0_8')
  fig, axes = plt.subplots(3, 4, figsize=(20, 15))
  fig.suptitle('Insertion Sort vs Selection Sort vs Shell Sort - Comprehensive Comparison',
               fontsize=18, fontweight='bold', color='#2C3E50')

  # 배경색 설정
  fig.patch.set_facecolor('#F8F9FA')
  for ax in axes.flat:
    ax.set_facecolor('#F8F9FA')

  case_names = list(cases.keys())

  def animate(frame):
    # 모든 서브플롯 초기화
    for i, case_name in enumerate(case_names):
      # Selection Sort (첫 번째 행)
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

      # Insertion Sort (두 번째 행)
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

      # Shell Sort (세 번째 행)
      ax3 = axes[2, i]
      ax3.clear()
      ax3.set_facecolor('#F8F9FA')

      # 현재 프레임에 해당하는 데이터 가져오기
      current_frame = min(frame, len(shell_steps[case_name]) - 1)
      current_data = shell_steps[case_name][current_frame]['array'] if isinstance(
          shell_steps[case_name][current_frame], dict) else shell_steps[case_name][current_frame]
      current_colors = shell_colors[case_name][current_frame] if current_frame < len(
          shell_colors[case_name]) else ['#FFD93D'] * len(current_data)

      # 바형 그래프 그리기
      bars3 = ax3.bar(range(len(current_data)), current_data,
                      color=current_colors, edgecolor='#2C3E50', linewidth=1.5,
                      alpha=0.8, width=0.7)

      # 그래프 설정
      ax3.set_xlim(-0.5, len(current_data) - 0.5)
      ax3.set_ylim(0, 11)
      ax3.set_title(f"Shell Sort\n{cases[case_name]['name']}\nStep {current_frame + 1}/{len(shell_steps[case_name])}",
                    fontsize=10, fontweight='bold', color='#2C3E50')

      # 값 표시
      for j, bar in enumerate(bars3):
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height + 0.2,
                 f'{int(height)}', ha='center', va='bottom',
                 fontweight='bold', fontsize=8, color='#2C3E50')

      # 그리드 설정
      ax3.grid(True, alpha=0.2, linestyle='-', linewidth=0.5, color='#95A5A6')

      # 축 스타일링
      ax3.spines['top'].set_visible(False)
      ax3.spines['right'].set_visible(False)
      ax3.spines['left'].set_color('#BDC3C7')
      ax3.spines['bottom'].set_color('#BDC3C7')

      # 축 눈금 설정
      ax3.tick_params(axis='both', colors='#7F8C8D', labelsize=8)

      # 진행률 표시
      selection_progress = ((current_frame + 1) / len(
          selection_steps[case_name])) * 100 if len(selection_steps[case_name]) > 0 else 0
      insertion_progress = ((current_frame + 1) / len(
          insertion_steps[case_name])) * 100 if len(insertion_steps[case_name]) > 0 else 0
      shell_progress = (
          (current_frame + 1) / len(shell_steps[case_name])) * 100 if len(shell_steps[case_name]) > 0 else 0

      ax1.text(0.02, 0.98, f'Progress: {selection_progress:.0f}%',
               transform=ax1.transAxes, fontsize=8, fontweight='bold',
               verticalalignment='top', color='#2C3E50',
               bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8))

      ax2.text(0.02, 0.98, f'Progress: {insertion_progress:.0f}%',
               transform=ax2.transAxes, fontsize=8, fontweight='bold',
               verticalalignment='top', color='#2C3E50',
               bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8))

      ax3.text(0.02, 0.98, f'Progress: {shell_progress:.0f}%',
               transform=ax3.transAxes, fontsize=8, fontweight='bold',
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

      ax3.text(0.98, 0.98, f'Steps: {len(shell_steps[case_name])}',
               transform=ax3.transAxes, fontsize=8, fontweight='bold',
               verticalalignment='top', horizontalalignment='right', color='#2C3E50',
               bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8))

    return []

  # 애니메이션 생성
  anim = animation.FuncAnimation(fig, animate, frames=max_steps,
                                 interval=300, repeat=True, blit=False)

  # GIF로 저장
  script_dir = os.path.dirname(os.path.abspath(__file__))
  img_dir = os.path.join(script_dir, 'img')
  os.makedirs(img_dir, exist_ok=True)

  gif_path = os.path.join(img_dir, 'comprehensive_three_way_comparison.gif')
  anim.save(gif_path, writer='pillow', fps=3, dpi=150)
  plt.close()

  print(f"Animation saved as '{gif_path}'")


if __name__ == "__main__":
  create_comprehensive_three_way_comparison()
