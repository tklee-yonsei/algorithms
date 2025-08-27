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
  colors.append(['#E3F2FD'] * n)  # 연한 파란색

  for i in range(n - 1):
    min_index = i

    # 현재 선택된 위치를 표시
    current_colors = ['#E3F2FD'] * n
    current_colors[i] = '#FFD54F'  # 노란색 - 현재 선택
    colors.append(current_colors.copy())
    steps.append(arr.copy())

    # i번째 위치부터 끝까지 최솟값 찾기
    for j in range(i + 1, n):
      current_colors = ['#E3F2FD'] * n
      current_colors[i] = '#FFD54F'  # 현재 선택된 위치
      current_colors[j] = '#FF8A80'  # 비교 중인 요소 (빨간색)

      # 현재까지의 최솟값 위치 표시
      if min_index != i:
        current_colors[min_index] = '#FFB74D'  # 주황색 - 현재 최솟값

      if arr[j] < arr[min_index]:
        min_index = j
        current_colors[j] = '#FF5722'  # 진한 주황색 - 새로운 최솟값

      colors.append(current_colors.copy())
      steps.append(arr.copy())

    # 교환 과정 표시
    if min_index != i:
      # 교환 전 상태
      current_colors = ['#E3F2FD'] * n
      current_colors[i] = '#FFD54F'  # 현재 위치
      current_colors[min_index] = '#FF5722'  # 교환할 최솟값
      colors.append(current_colors.copy())
      steps.append(arr.copy())

      # 교환 실행
      arr[i], arr[min_index] = arr[min_index], arr[i]

      # 교환 후 상태
      current_colors = ['#E3F2FD'] * n
      current_colors[i] = '#4CAF50'  # 정렬 완료된 위치
      colors.append(current_colors.copy())
      steps.append(arr.copy())
    else:
      # 교환이 필요 없는 경우
      current_colors = ['#E3F2FD'] * n
      current_colors[i] = '#4CAF50'  # 정렬 완료된 위치
      colors.append(current_colors.copy())
      steps.append(arr.copy())

  # 마지막 요소도 정렬 완료로 표시
  final_colors = ['#4CAF50'] * n
  colors.append(final_colors)
  steps.append(arr.copy())

  return steps, colors


def create_animation(steps, colors, filename='selection_sort.gif'):
  """애니메이션 GIF 생성"""
  # 스타일 설정
  plt.style.use('seaborn-v0_8')
  fig, ax = plt.subplots(figsize=(16, 10))

  # 배경색 설정
  fig.patch.set_facecolor('#F8F9FA')
  ax.set_facecolor('#F8F9FA')

  def animate(frame):
    ax.clear()
    ax.set_facecolor('#F8F9FA')

    # 바형 그래프 그리기
    bars = ax.bar(range(len(steps[frame])), steps[frame],
                  color=colors[frame], edgecolor='#2C3E50', linewidth=2,
                  alpha=0.8, width=0.7)

    # 그래프 설정
    ax.set_xlim(-0.5, len(steps[frame]) - 0.5)
    ax.set_ylim(0, max(max(step) for step in steps) * 1.15)

    # 축 레이블과 제목
    ax.set_xlabel('Array Index', fontsize=14, fontweight='bold', color='#2C3E50')
    ax.set_ylabel('Value', fontsize=14, fontweight='bold', color='#2C3E50')
    ax.set_title(f'Selection Sort Visualization - Step {frame + 1}/{len(steps)}',
                 fontsize=16, fontweight='bold', color='#2C3E50', pad=20)

    # 값 표시
    for i, bar in enumerate(bars):
      height = bar.get_height()
      ax.text(bar.get_x() + bar.get_width()/2., height + 0.5,
              f'{int(height)}', ha='center', va='bottom',
              fontweight='bold', fontsize=12, color='#2C3E50')

    # 그리드 설정
    ax.grid(True, alpha=0.2, linestyle='-', linewidth=0.5, color='#95A5A6')

    # 축 스타일링
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#BDC3C7')
    ax.spines['bottom'].set_color('#BDC3C7')

    # 축 눈금 설정
    ax.tick_params(axis='both', colors='#7F8C8D', labelsize=12)

    # 범례 추가
    legend_elements = [
        plt.Rectangle((0, 0), 1, 1, facecolor='#E3F2FD',
                      edgecolor='#2C3E50', label='Unsorted'),
        plt.Rectangle((0, 0), 1, 1, facecolor='#FFD54F',
                      edgecolor='#2C3E50', label='Current Position'),
        plt.Rectangle((0, 0), 1, 1, facecolor='#FF8A80',
                      edgecolor='#2C3E50', label='Comparing'),
        plt.Rectangle((0, 0), 1, 1, facecolor='#FFB74D',
                      edgecolor='#2C3E50', label='Current Min'),
        plt.Rectangle((0, 0), 1, 1, facecolor='#FF5722',
                      edgecolor='#2C3E50', label='New Min'),
        plt.Rectangle((0, 0), 1, 1, facecolor='#4CAF50',
                      edgecolor='#2C3E50', label='Sorted')
    ]
    ax.legend(handles=legend_elements, loc='upper right', frameon=True,
              fancybox=True, shadow=True, fontsize=11)

    return bars

    # 애니메이션 생성
  anim = animation.FuncAnimation(fig, animate, frames=len(steps),
                                 interval=500, repeat=True, blit=False)

  # GIF로 저장 (고해상도)
  anim.save(filename, writer='pillow', fps=2, dpi=150)
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
