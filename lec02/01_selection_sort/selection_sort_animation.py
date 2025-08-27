# selection_sort_animation.py
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from PIL import Image
import os


def selection_sort_with_animation(arr):
  """선택 정렬 과정을 단계별로 기록"""
  n = len(arr)
  steps = []
  colors = []

  # 초기 상태 저장
  steps.append(arr.copy())
  colors.append(['lightblue'] * n)

  for i in range(n - 1):
    min_index = i

    # 현재 비교 중인 요소를 노란색으로 표시
    current_colors = ['lightblue'] * n
    current_colors[i] = 'yellow'
    colors.append(current_colors.copy())
    steps.append(arr.copy())

    # i번째 위치부터 끝까지 최솟값 찾기
    for j in range(i + 1, n):
      # 비교 중인 요소를 빨간색으로 표시
      current_colors = ['lightblue'] * n
      current_colors[i] = 'yellow'  # 현재 선택된 위치
      current_colors[j] = 'red'     # 비교 중인 요소
      if arr[j] < arr[min_index]:
        min_index = j
        current_colors[j] = 'orange'  # 새로운 최솟값
      colors.append(current_colors.copy())
      steps.append(arr.copy())

    # 최솟값을 i번째 위치로 교환
    if min_index != i:
      arr[i], arr[min_index] = arr[min_index], arr[i]

      # 교환 후 상태 저장
      current_colors = ['lightblue'] * n
      current_colors[i] = 'green'  # 정렬 완료된 위치
      colors.append(current_colors.copy())
      steps.append(arr.copy())
    else:
      # 교환이 필요 없는 경우
      current_colors = ['lightblue'] * n
      current_colors[i] = 'green'  # 정렬 완료된 위치
      colors.append(current_colors.copy())
      steps.append(arr.copy())

  # 마지막 요소도 정렬 완료로 표시
  final_colors = ['green'] * n
  colors.append(final_colors)
  steps.append(arr.copy())

  return steps, colors


def create_animation(steps, colors, filename='selection_sort.gif'):
  """애니메이션 GIF 생성"""
  fig, ax = plt.subplots(figsize=(12, 6))

  def animate(frame):
    ax.clear()

    # 바형 그래프 그리기
    bars = ax.bar(range(len(steps[frame])), steps[frame],
                  color=colors[frame], edgecolor='black', linewidth=1)

    # 그래프 설정
    ax.set_xlim(-0.5, len(steps[frame]) - 0.5)
    ax.set_ylim(0, max(max(step) for step in steps) * 1.1)
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    ax.set_title(f'Selection Sort Process - Step {frame + 1}/{len(steps)}')

    # 값 표시
    for i, bar in enumerate(bars):
      height = bar.get_height()
      ax.text(bar.get_x() + bar.get_width()/2., height + 0.5,
              f'{int(height)}', ha='center', va='bottom', fontweight='bold')

    # 그리드 추가
    ax.grid(True, alpha=0.3)

    return bars

  # 애니메이션 생성
  anim = animation.FuncAnimation(fig, animate, frames=len(steps),
                                 interval=500, repeat=True, blit=False)

  # GIF로 저장
  anim.save(filename, writer='pillow', fps=2)
  plt.close()

  print(f"Animation saved as '{filename}'")


def create_random_data(size=10):
  """랜덤 데이터 생성"""
  return np.random.randint(1, 50, size)


def main():
  # 랜덤 데이터 생성
  data = create_random_data(10)
  print("Initial array:", data)

  # 정렬 과정 기록
  steps, colors = selection_sort_with_animation(data.copy())

  # 애니메이션 생성
  # 스크립트가 있는 디렉토리에 GIF 저장
  script_dir = os.path.dirname(os.path.abspath(__file__))
  gif_path = os.path.join(script_dir, 'selection_sort.gif')
  create_animation(steps, colors, gif_path)

  print("Sorting completed:", data)


if __name__ == "__main__":
  main()
