# shell_sort_animation.py
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from PIL import Image
import os


def shell_sort_with_animation(arr):
  """셸 정렬 과정을 단계별로 기록"""
  n = len(arr)
  steps = []
  colors = []
  gap = n // 2

  # 초기 상태 저장
  steps.append(arr.copy())
  colors.append(['#E3F2FD'] * n)  # 연한 파란색

  while gap > 0:
    # 각 gap 그룹에 대해 삽입 정렬 수행
    for start in range(gap):
      # 현재 gap 그룹의 요소들을 삽입 정렬
      for i in range(start + gap, n, gap):
        temp = arr[i]
        j = i

        # 현재 처리할 요소를 표시
        current_colors = ['#E3F2FD'] * n
        current_colors[i] = '#FFD54F'  # 노란색 - 현재 처리할 요소

        # 같은 gap 그룹의 요소들을 표시
        for k in range(start, n, gap):
          if k != i:
            current_colors[k] = '#FFB74D'  # 주황색 - 같은 gap 그룹

        colors.append(current_colors.copy())
        steps.append(arr.copy())

        # gap만큼 떨어진 요소들과 비교하여 삽입
        while j >= start + gap and arr[j - gap] > temp:
          current_colors = ['#E3F2FD'] * n
          current_colors[i] = '#FFD54F'  # 현재 처리할 요소
          current_colors[j] = '#FF8A80'  # 비교 중인 요소 (빨간색)
          current_colors[j - gap] = '#FF8A80'  # 비교 중인 요소 (빨간색)

          # 같은 gap 그룹의 다른 요소들 표시
          for k in range(start, n, gap):
            if k != i and k != j and k != j - gap:
              current_colors[k] = '#FFB74D'  # 주황색

          colors.append(current_colors.copy())
          steps.append(arr.copy())

          # 요소 이동
          arr[j] = arr[j - gap]
          j = j - gap

        # temp를 올바른 위치에 삽입
        arr[j] = temp

        # 삽입 후 상태 표시
        current_colors = ['#E3F2FD'] * n
        current_colors[j] = '#4CAF50'  # 삽입된 요소 (초록색)

        # 같은 gap 그룹의 다른 요소들 표시
        for k in range(start, n, gap):
          if k != j:
            current_colors[k] = '#FFB74D'  # 주황색

        colors.append(current_colors.copy())
        steps.append(arr.copy())

    gap //= 2

  # 최종 정렬 완료 상태
  final_colors = ['#4CAF50'] * n
  colors.append(final_colors)
  steps.append(arr.copy())

  return steps, colors


def create_animation(steps, colors, filename='shell_sort.gif'):
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

    # 현재 gap 값 계산 (단계별로 gap 추적)
    current_gap = 0
    if frame > 0:
      # gap이 변경되는 시점을 찾기 위해 단계를 역추적
      n = len(steps[0])
      gap_sequence = []
      temp_n = n
      while temp_n > 0:
        gap_sequence.append(temp_n // 2)
        temp_n //= 2

      # 현재 프레임에서 사용 중인 gap 계산
      step_count = 0
      for gap in gap_sequence:
        if gap == 0:
          continue
        for i in range(gap, n):
          step_count += 3  # 각 요소당 3단계 (시작, 비교, 삽입)
          if step_count >= frame:
            current_gap = gap
            break
        if current_gap > 0:
          break

    ax.set_title(f'Shell Sort Visualization - Step {frame + 1}/{len(steps)} (Gap: {current_gap})',
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
                      edgecolor='#2C3E50', label='Current Element'),
        plt.Rectangle((0, 0), 1, 1, facecolor='#FFB74D',
                      edgecolor='#2C3E50', label='Same Gap Group'),
        plt.Rectangle((0, 0), 1, 1, facecolor='#FF8A80',
                      edgecolor='#2C3E50', label='Comparing'),
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
  steps, colors = shell_sort_with_animation(data.copy())

  # 애니메이션 생성
  # 스크립트가 있는 디렉토리에 GIF 저장
  script_dir = os.path.dirname(os.path.abspath(__file__))
  gif_path = os.path.join(script_dir, 'shell_sort.gif')
  create_animation(steps, colors, gif_path)

  # 정렬된 결과 출력 (마지막 단계에서 가져옴)
  sorted_data = steps[-1] if steps else data
  print("Sorting completed:", sorted_data)


def create_animation_for_data(data, filename='shell_sort.gif'):
  """주어진 데이터로 애니메이션 생성"""
  print(f"Creating animation for: {data}")

  # 정렬 과정 기록
  steps, colors = shell_sort_with_animation(data.copy())

  # 애니메이션 생성
  script_dir = os.path.dirname(os.path.abspath(__file__))
  gif_path = os.path.join(script_dir, filename)
  create_animation(steps, colors, gif_path)

  print(f"Animation saved as '{filename}'")
  return data


if __name__ == "__main__":
  main()
