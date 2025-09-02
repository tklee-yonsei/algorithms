# comparison_animation.py
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import os


def bubble_sort_with_steps(arr):
  """버블 정렬 과정을 단계별로 기록 (기본 버전)"""
  steps = []
  arr = arr.copy()
  n = len(arr)

  steps.append(('start', arr.copy(), -1, -1))

  # 모든 패스를 수행 (n-1번)
  for i in range(n - 1):
    for j in range(0, n - i - 1):
      steps.append(('comparing', arr.copy(), j, j + 1))

      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        steps.append(('swapping', arr.copy(), j, j + 1))

  steps.append(('completed', arr.copy(), -1, -1))
  return steps


def selection_sort_with_steps(arr):
  """선택 정렬 과정을 단계별로 기록"""
  steps = []
  arr = arr.copy()
  n = len(arr)

  steps.append(('start', arr.copy(), -1, -1))

  for i in range(n):
    min_idx = i
    steps.append(('finding_min', arr.copy(), i, min_idx))

    for j in range(i + 1, n):
      steps.append(('comparing', arr.copy(), j, min_idx))
      if arr[j] < arr[min_idx]:
        min_idx = j
        steps.append(('new_min', arr.copy(), j, min_idx))

    if min_idx != i:
      arr[i], arr[min_idx] = arr[min_idx], arr[i]
      steps.append(('swapping', arr.copy(), i, min_idx))

  steps.append(('completed', arr.copy(), -1, -1))
  return steps


def insertion_sort_with_steps(arr):
  """삽입 정렬 과정을 단계별로 기록"""
  steps = []
  arr = arr.copy()
  n = len(arr)

  steps.append(('start', arr.copy(), -1, -1))

  for i in range(1, n):
    key = arr[i]
    j = i - 1

    steps.append(('key_to_insert', arr.copy(), i, -1))

    while j >= 0 and arr[j] > key:
      steps.append(('comparing', arr.copy(), j, j + 1))
      arr[j + 1] = arr[j]
      steps.append(('moving', arr.copy(), j, j + 1))
      j = j - 1

    arr[j + 1] = key
    steps.append(('inserting', arr.copy(), j + 1, -1))

  steps.append(('completed', arr.copy(), -1, -1))
  return steps


def create_comparison_animation(data, filename='comparison_animation.gif'):
  """세 정렬 알고리즘 비교 애니메이션"""

  # 각 정렬 알고리즘의 단계 기록
  bubble_steps = bubble_sort_with_steps(data)
  selection_steps = selection_sort_with_steps(data)
  insertion_steps = insertion_sort_with_steps(data)

  # 최대 단계 수
  max_steps = max(len(bubble_steps), len(selection_steps), len(insertion_steps))

  # 스타일 설정
  plt.style.use('seaborn-v0_8')
  fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(16, 12))
  fig.patch.set_facecolor('#F8F9FA')

  # 축 설정
  axes = [ax1, ax2, ax3]
  titles = ['Bubble Sort', 'Selection Sort', 'Insertion Sort']
  steps_list = [bubble_steps, selection_steps, insertion_steps]

  for ax in axes:
    ax.set_facecolor('#F8F9FA')

  def get_colors(arr, action, idx1, idx2, sort_type):
    """액션에 따른 색상 배정"""
    colors = ['#E3F2FD'] * len(arr)  # 기본 색상

    if sort_type == 'bubble':
      if action == 'comparing':
        colors[idx1] = '#FFD54F'  # 노란색
        colors[idx2] = '#FF8A80'  # 빨간색
      elif action == 'swapping':
        colors[idx1] = '#9C27B0'  # 보라색
        colors[idx2] = '#9C27B0'  # 보라색
      elif action == 'completed':
        colors = ['#4CAF50'] * len(arr)  # 초록색

    elif sort_type == 'selection':
      if action == 'finding_min' or action == 'new_min':
        colors[idx1] = '#FFD54F'  # 노란색
        if idx2 >= 0:
          colors[idx2] = '#FF8A80'  # 빨간색
      elif action == 'comparing':
        colors[idx1] = '#FFD54F'  # 노란색
        colors[idx2] = '#FF8A80'  # 빨간색
      elif action == 'swapping':
        colors[idx1] = '#9C27B0'  # 보라색
        colors[idx2] = '#9C27B0'  # 보라색
      elif action == 'completed':
        colors = ['#4CAF50'] * len(arr)  # 초록색

    elif sort_type == 'insertion':
      if action == 'key_to_insert':
        colors[idx1] = '#FFD54F'  # 노란색
      elif action == 'comparing' or action == 'moving':
        colors[idx1] = '#FF8A80'  # 빨간색
        colors[idx2] = '#FFB74D'  # 주황색
      elif action == 'inserting':
        colors[idx1] = '#9C27B0'  # 보라색
      elif action == 'completed':
        colors = ['#4CAF50'] * len(arr)  # 초록색

    return colors

  def animate(frame):
    for i, (ax, title, steps, sort_type) in enumerate(zip(axes, titles, steps_list, ['bubble', 'selection', 'insertion'])):
      ax.clear()
      ax.set_facecolor('#F8F9FA')

      # 현재 단계 가져오기
      if frame < len(steps):
        action, arr, idx1, idx2 = steps[frame]
        colors = get_colors(arr, action, idx1, idx2, sort_type)
        step_text = f"Step {frame + 1}: {action.replace('_', ' ').title()}"
      else:
        # 완료된 경우 마지막 상태 유지
        action, arr, idx1, idx2 = steps[-1]
        colors = ['#4CAF50'] * len(arr)
        step_text = "Completed"

      # 바 그래프 그리기
      bars = ax.bar(range(len(arr)), arr, color=colors,
                    edgecolor='#2C3E50', linewidth=1.5, alpha=0.8)

      # 축 설정
      ax.set_xlim(-0.5, len(arr) - 0.5)
      ax.set_ylim(0, max(data) * 1.1)
      ax.set_title(f'{title} - {step_text}',
                   fontsize=14, fontweight='bold', color='#2C3E50')

      # 값 표시
      for j, bar in enumerate(bars):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.3,
                f'{int(height)}', ha='center', va='bottom',
                fontweight='bold', fontsize=10, color='#2C3E50')

      # 축 스타일링
      ax.spines['top'].set_visible(False)
      ax.spines['right'].set_visible(False)
      ax.spines['left'].set_color('#BDC3C7')
      ax.spines['bottom'].set_color('#BDC3C7')
      ax.tick_params(axis='both', colors='#7F8C8D', labelsize=10)

      if i == 2:  # 마지막 subplot에만 x축 라벨 추가
        ax.set_xlabel('Array Index', fontsize=12, fontweight='bold', color='#2C3E50')

      if i == 1:  # 중간 subplot에 y축 라벨 추가
        ax.set_ylabel('Value', fontsize=12, fontweight='bold', color='#2C3E50')

  # 전체 제목
  fig.suptitle(f'Sorting Algorithm Comparison - Data: {data}',
               fontsize=16, fontweight='bold', color='#2C3E50', y=0.98)

  # 애니메이션 생성
  anim = animation.FuncAnimation(fig, animate, frames=max_steps,
                                 interval=800, repeat=True, blit=False)

  # 레이아웃 조정
  plt.tight_layout()
  plt.subplots_adjust(top=0.94)

  # GIF로 저장
  anim.save(filename, writer='pillow', fps=1.25, dpi=120)
  plt.close()

  print(f"Comparison animation saved as '{filename}'")


def main():
  # 테스트 데이터
  test_data = [64, 34, 25, 12, 22, 11, 90]

  print(f"Creating comparison animation for: {test_data}")

  # img 폴더에 GIF 저장
  script_dir = os.path.dirname(os.path.abspath(__file__))
  img_dir = os.path.join(script_dir, 'img')

  # img 디렉토리가 없으면 생성
  if not os.path.exists(img_dir):
    os.makedirs(img_dir)

  gif_path = os.path.join(img_dir, 'comparison_animation.gif')

  create_comparison_animation(test_data, gif_path)


def create_comparison_for_data(data, filename='comparison_animation.gif'):
  """주어진 데이터로 비교 애니메이션 생성"""
  print(f"Creating comparison animation for: {data}")

  script_dir = os.path.dirname(os.path.abspath(__file__))

  # filename이 절대경로가 아니면 img 폴더에 저장
  if not os.path.isabs(filename):
    img_dir = os.path.join(script_dir, 'img')
    # img 디렉토리가 없으면 생성
    if not os.path.exists(img_dir):
      os.makedirs(img_dir)
    gif_path = os.path.join(img_dir, filename)
  else:
    gif_path = filename

  create_comparison_animation(data, gif_path)

  print(f"Comparison animation saved as '{gif_path}'")


if __name__ == "__main__":
  main()
