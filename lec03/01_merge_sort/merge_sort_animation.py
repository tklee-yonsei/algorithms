# merge_sort_animation.py
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from PIL import Image
import os


def merge_sort_with_animation(arr):
  """병합 정렬 과정을 단계별로 기록 (메모리 사용량 포함)"""
  steps = []
  colors = []
  memory_usage = []  # 메모리 사용량 기록
  memory_details = []  # 메모리 세부 정보
  n = len(arr)

  # 배열을 복사해서 작업 (원본 보존)
  work_arr = arr.copy()

  # 초기 상태 저장
  steps.append(work_arr.copy())
  colors.append(['#E3F2FD'] * n)  # 연한 파란색
  memory_usage.append(0)  # 초기 메모리 사용량
  memory_details.append([])  # 초기 메모리 세부 정보

  def merge(arr, left, mid, right, steps, colors, memory_usage, memory_details):
    """두 개의 정렬된 부분 배열을 합치는 함수 (애니메이션용)"""
    # 병합할 범위 표시
    current_colors = ['#E3F2FD'] * n
    for i in range(left, right + 1):
      if i <= mid:
        current_colors[i] = '#FFD54F'  # 노란색 - 왼쪽 부분
      else:
        current_colors[i] = '#FF8A80'  # 빨간색 - 오른쪽 부분

    colors.append(current_colors.copy())
    steps.append(arr.copy())
    memory_usage.append(0)  # 분할 단계에서는 추가 메모리 없음
    memory_details.append([])

    # 임시 배열 생성 (메모리 사용 시작)
    left_arr = arr[left:mid+1]
    right_arr = arr[mid+1:right+1]
    temp_memory_size = len(left_arr) + len(right_arr)

    # 메모리 할당 상태 표시
    current_colors = ['#E3F2FD'] * n
    for i in range(left, right + 1):
      if i <= mid:
        current_colors[i] = '#FFD54F'  # 노란색 - 왼쪽 부분 (메모리에 복사됨)
      else:
        current_colors[i] = '#FF8A80'  # 빨간색 - 오른쪽 부분 (메모리에 복사됨)

    colors.append(current_colors.copy())
    steps.append(arr.copy())
    memory_usage.append(temp_memory_size)
    memory_details.append([
        f"Left temp: {left_arr}",
        f"Right temp: {right_arr}"
    ])

    # 인덱스 초기화
    i = j = 0
    k = left

    # 두 배열을 비교하며 작은 값부터 원본 배열에 복사
    while i < len(left_arr) and j < len(right_arr):
      current_colors = ['#E3F2FD'] * n

      # 현재 비교 중인 요소들 표시
      if left + i < n:
        current_colors[left + i] = '#FFD54F'  # 왼쪽 배열에서 비교 중
      if mid + 1 + j < n:
        current_colors[mid + 1 + j] = '#FF8A80'  # 오른쪽 배열에서 비교 중
      current_colors[k] = '#4CAF50'  # 병합될 위치 (초록색)

      colors.append(current_colors.copy())
      steps.append(arr.copy())
      memory_usage.append(temp_memory_size)
      memory_details.append([
          f"Comparing: {left_arr[i]} vs {right_arr[j]}",
          f"Left temp: {left_arr[i:]}",
          f"Right temp: {right_arr[j:]}"
      ])

      if left_arr[i] <= right_arr[j]:
        arr[k] = left_arr[i]
        i += 1
      else:
        arr[k] = right_arr[j]
        j += 1

      # 병합 후 상태 표시
      current_colors = ['#E3F2FD'] * n
      current_colors[k] = '#81C784'  # 연한 초록색 - 방금 병합된 요소
      for idx in range(left, k):
        current_colors[idx] = '#4CAF50'  # 이미 병합된 부분

      colors.append(current_colors.copy())
      steps.append(arr.copy())
      memory_usage.append(temp_memory_size)
      memory_details.append([
          f"Merged: {arr[k]}",
          f"Left temp: {left_arr[i:] if i < len(left_arr) else '[]'}",
          f"Right temp: {right_arr[j:] if j < len(right_arr) else '[]'}"
      ])

      k += 1

    # 남은 요소들 복사
    while i < len(left_arr):
      current_colors = ['#E3F2FD'] * n
      current_colors[k] = '#4CAF50'  # 복사될 위치
      if left + i < n:
        current_colors[left + i] = '#FFD54F'  # 복사할 요소

      colors.append(current_colors.copy())
      steps.append(arr.copy())
      memory_usage.append(temp_memory_size)
      memory_details.append([
          f"Copying remaining left: {left_arr[i]}",
          f"Left temp: {left_arr[i:]}"
      ])

      arr[k] = left_arr[i]
      i += 1
      k += 1

      # 복사 후 상태
      current_colors = ['#E3F2FD'] * n
      for idx in range(left, k):
        current_colors[idx] = '#4CAF50'
      colors.append(current_colors.copy())
      steps.append(arr.copy())
      memory_usage.append(temp_memory_size)
      memory_details.append([
          f"Copied: {arr[k-1]}",
          f"Left temp: {left_arr[i:] if i < len(left_arr) else '[]'}"
      ])

    while j < len(right_arr):
      current_colors = ['#E3F2FD'] * n
      current_colors[k] = '#4CAF50'  # 복사될 위치
      if mid + 1 + j < n:
        current_colors[mid + 1 + j] = '#FF8A80'  # 복사할 요소

      colors.append(current_colors.copy())
      steps.append(arr.copy())
      memory_usage.append(temp_memory_size)
      memory_details.append([
          f"Copying remaining right: {right_arr[j]}",
          f"Right temp: {right_arr[j:]}"
      ])

      arr[k] = right_arr[j]
      j += 1
      k += 1

      # 복사 후 상태
      current_colors = ['#E3F2FD'] * n
      for idx in range(left, k):
        current_colors[idx] = '#4CAF50'
      colors.append(current_colors.copy())
      steps.append(arr.copy())
      memory_usage.append(temp_memory_size)
      memory_details.append([
          f"Copied: {arr[k-1]}",
          f"Right temp: {right_arr[j:] if j < len(right_arr) else '[]'}"
      ])

    # 병합 완료 상태 표시 (메모리 해제)
    current_colors = ['#E3F2FD'] * n
    for idx in range(left, right + 1):
      current_colors[idx] = '#4CAF50'  # 초록색 - 병합 완료
    colors.append(current_colors.copy())
    steps.append(arr.copy())
    memory_usage.append(0)  # 메모리 해제됨
    memory_details.append(["Memory freed - merge complete"])

  def merge_sort_recursive(arr, left, right, steps, colors, memory_usage, memory_details):
    """재귀적 병합 정렬 (애니메이션용)"""
    if left < right:
      # 분할 표시
      mid = (left + right) // 2
      current_colors = ['#E3F2FD'] * n
      for i in range(left, right + 1):
        if i <= mid:
          current_colors[i] = '#FFE082'  # 연한 노란색 - 왼쪽 부분
        else:
          current_colors[i] = '#FFAB91'  # 연한 주황색 - 오른쪽 부분

      colors.append(current_colors.copy())
      steps.append(arr.copy())
      memory_usage.append(0)
      memory_details.append([f"Dividing: [{left}..{mid}] and [{mid+1}..{right}]"])

      # 왼쪽 부분 정렬
      merge_sort_recursive(arr, left, mid, steps, colors, memory_usage, memory_details)

      # 오른쪽 부분 정렬
      merge_sort_recursive(arr, mid + 1, right, steps, colors,
                           memory_usage, memory_details)

      # 병합
      merge(arr, left, mid, right, steps, colors, memory_usage, memory_details)

  # 병합 정렬 실행
  merge_sort_recursive(work_arr, 0, n - 1, steps, colors, memory_usage, memory_details)

  # 원본 배열을 정렬된 결과로 업데이트
  for i in range(n):
    arr[i] = work_arr[i]

  # 최종 정렬 완료 상태
  final_colors = ['#4CAF50'] * n
  colors.append(final_colors)
  steps.append(work_arr.copy())
  memory_usage.append(0)
  memory_details.append(["Sorting complete"])

  return steps, colors, memory_usage, memory_details


def create_animation_with_memory(steps, colors, memory_usage, memory_details, filename='merge_sort.gif'):
  """메모리 내용을 실제 요소들로 표시하는 애니메이션 GIF 생성"""
  # 스타일 설정
  plt.style.use('seaborn-v0_8')
  fig = plt.figure(figsize=(20, 12))

  # 서브플롯 생성 (2행 1열)
  gs = fig.add_gridspec(2, 1, height_ratios=[3, 1], hspace=0.3)
  ax1 = fig.add_subplot(gs[0])  # 메인 정렬 시각화
  ax2 = fig.add_subplot(gs[1])  # 메모리 내용

  # 배경색 설정
  fig.patch.set_facecolor('#F8F9FA')
  ax1.set_facecolor('#F8F9FA')
  ax2.set_facecolor('#F8F9FA')

  def animate(frame):
    ax1.clear()
    ax2.clear()
    ax1.set_facecolor('#F8F9FA')
    ax2.set_facecolor('#F8F9FA')

    # 메인 정렬 시각화
    bars = ax1.bar(range(len(steps[frame])), steps[frame],
                   color=colors[frame], edgecolor='#2C3E50', linewidth=2,
                   alpha=0.8, width=0.7)

    # 그래프 설정
    ax1.set_xlim(-0.5, len(steps[frame]) - 0.5)
    ax1.set_ylim(0, max(max(step) for step in steps) * 1.15)

    # 축 레이블과 제목
    ax1.set_xlabel('Array Index', fontsize=14, fontweight='bold', color='#2C3E50')
    ax1.set_ylabel('Value', fontsize=14, fontweight='bold', color='#2C3E50')
    ax1.set_title(f'Merge Sort with Memory Visualization - Step {frame + 1}/{len(steps)}',
                  fontsize=16, fontweight='bold', color='#2C3E50', pad=20)

    # 값 표시
    for i, bar in enumerate(bars):
      height = bar.get_height()
      ax1.text(bar.get_x() + bar.get_width()/2., height + 0.5,
               f'{int(height)}', ha='center', va='bottom',
               fontweight='bold', fontsize=12, color='#2C3E50')

    # 그리드 설정
    ax1.grid(True, alpha=0.2, linestyle='-', linewidth=0.5, color='#95A5A6')

    # 축 스타일링
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['left'].set_color('#BDC3C7')
    ax1.spines['bottom'].set_color('#BDC3C7')
    ax1.tick_params(axis='both', colors='#7F8C8D', labelsize=12)

    # 범례 추가
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
    ax1.legend(handles=legend_elements, loc='upper right', frameon=True,
               fancybox=True, shadow=True, fontsize=10)

    # 메모리 시각화 - 실제 요소들을 칸으로 표시
    if frame < len(memory_details) and memory_details[frame]:
      # 메모리 세부 정보에서 실제 배열 데이터 추출
      left_temp = []
      right_temp = []

      for detail in memory_details[frame]:
        if detail.startswith("Left temp:"):
          try:
            # "Left temp: [1, 2, 3]" 형태에서 리스트 추출
            temp_str = detail.split(": ", 1)[1]
            if temp_str != "[]" and temp_str != "":
              left_temp = eval(temp_str) if temp_str.startswith("[") else []
          except:
            left_temp = []
        elif detail.startswith("Right temp:"):
          try:
            # "Right temp: [4, 5, 6]" 형태에서 리스트 추출
            temp_str = detail.split(": ", 1)[1]
            if temp_str != "[]" and temp_str != "":
              right_temp = eval(temp_str) if temp_str.startswith("[") else []
          except:
            right_temp = []

      # 메모리 요소들을 시각화
      if left_temp or right_temp:
        # 왼쪽 임시 배열 시각화
        if left_temp:
          left_positions = range(len(left_temp))
          left_bars = ax2.bar([x - 0.2 for x in left_positions], left_temp,
                              width=0.35, color='#FFD54F', alpha=0.8,
                              edgecolor='#2C3E50', linewidth=1.5,
                              label='Left Temp Array')

          # 값 표시
          for i, (pos, val) in enumerate(zip(left_positions, left_temp)):
            ax2.text(pos - 0.2, val + max(left_temp) * 0.05, str(val),
                     ha='center', va='bottom', fontweight='bold',
                     fontsize=10, color='#2C3E50')

        # 오른쪽 임시 배열 시각화
        if right_temp:
          right_start = len(left_temp) if left_temp else 0
          right_positions = range(right_start, right_start + len(right_temp))
          right_bars = ax2.bar([x + 0.2 for x in right_positions], right_temp,
                               width=0.35, color='#FF8A80', alpha=0.8,
                               edgecolor='#2C3E50', linewidth=1.5,
                               label='Right Temp Array')

          # 값 표시
          for i, (pos, val) in enumerate(zip(right_positions, right_temp)):
            ax2.text(pos + 0.2, val + max(right_temp) * 0.05, str(val),
                     ha='center', va='bottom', fontweight='bold',
                     fontsize=10, color='#2C3E50')

        # 축 설정
        total_elements = len(left_temp) + len(right_temp)
        max_val = max((left_temp + right_temp) if (left_temp + right_temp) else [1])

        ax2.set_xlim(-0.5, max(total_elements - 1, 0) + 0.5)
        ax2.set_ylim(0, max_val * 1.2)
        ax2.set_xlabel('Memory Position', fontsize=12,
                       fontweight='bold', color='#2C3E50')
        ax2.set_ylabel('Element Value', fontsize=12, fontweight='bold', color='#2C3E50')
        ax2.set_title(f'Temporary Memory Contents (Total: {total_elements} elements)',
                      fontsize=14, fontweight='bold', color='#2C3E50')

        # 범례 추가
        if left_temp and right_temp:
          ax2.legend(loc='upper right', fontsize=10)

      else:
        # 메모리가 비어있을 때
        ax2.text(0.5, 0.5, 'No temporary memory in use',
                 transform=ax2.transAxes, ha='center', va='center',
                 fontsize=14, fontweight='bold', color='#4CAF50',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8F5E8', alpha=0.8))
        ax2.set_xlim(0, 1)
        ax2.set_ylim(0, 1)
        ax2.set_xlabel('Memory Position', fontsize=12,
                       fontweight='bold', color='#2C3E50')
        ax2.set_ylabel('Element Value', fontsize=12, fontweight='bold', color='#2C3E50')
        ax2.set_title('Temporary Memory Contents (Empty)',
                      fontsize=14, fontweight='bold', color='#2C3E50')
    else:
      # 메모리 정보가 없을 때
      ax2.text(0.5, 0.5, 'No memory information available',
               transform=ax2.transAxes, ha='center', va='center',
               fontsize=14, fontweight='bold', color='#757575')
      ax2.set_xlim(0, 1)
      ax2.set_ylim(0, 1)
      ax2.set_xlabel('Memory Position', fontsize=12, fontweight='bold', color='#2C3E50')
      ax2.set_ylabel('Element Value', fontsize=12, fontweight='bold', color='#2C3E50')
      ax2.set_title('Temporary Memory Contents',
                    fontsize=14, fontweight='bold', color='#2C3E50')

    # 메모리 축 스타일링
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['left'].set_color('#BDC3C7')
    ax2.spines['bottom'].set_color('#BDC3C7')
    ax2.tick_params(axis='both', colors='#7F8C8D', labelsize=10)
    ax2.grid(True, alpha=0.2, linestyle='-', linewidth=0.5, color='#95A5A6')

    return bars

  # 애니메이션 생성
  anim = animation.FuncAnimation(fig, animate, frames=len(steps),
                                 interval=1000, repeat=True, blit=False)

  # GIF로 저장 (고해상도)
  anim.save(filename, writer='pillow', fps=1, dpi=120)
  plt.close()

  print(f"Animation with memory visualization saved as '{filename}'")


def create_animation(steps, colors, filename='merge_sort.gif'):
  """기존 애니메이션 GIF 생성 (호환성 유지)"""
  if len(steps) > 0 and len(steps[0]) > 0:
    # 메모리 정보가 없는 경우를 위한 더미 데이터
    dummy_memory = [0] * len(steps)
    dummy_details = [[]] * len(steps)
    create_animation_with_memory(steps, colors, dummy_memory, dummy_details, filename)
  else:
    print(f"Warning: Empty steps data, skipping animation creation")


def create_random_data(size=8):
  """랜덤 데이터 생성"""
  return np.random.randint(1, 50, size).tolist()  # numpy 배열을 리스트로 변환


def main():
  # 랜덤 데이터 생성 (작은 크기로 시작)
  data = create_random_data(8)
  print("Initial array:", data)

  # 정렬 과정 기록 (원본 배열을 직접 전달)
  steps, colors, memory_usage, memory_details = merge_sort_with_animation(data)

  # 애니메이션 생성
  # 스크립트가 있는 디렉토리에 GIF 저장
  script_dir = os.path.dirname(os.path.abspath(__file__))
  gif_path = os.path.join(script_dir, 'merge_sort.gif')
  create_animation_with_memory(steps, colors, memory_usage, memory_details, gif_path)

  print("Sorting completed:", data)


def create_animation_for_data(data, filename='merge_sort.gif'):
  """주어진 데이터로 애니메이션 생성"""
  print(f"Creating animation for: {data}")

  # 정렬 과정 기록
  steps, colors, memory_usage, memory_details = merge_sort_with_animation(data.copy())

  # 애니메이션 생성
  script_dir = os.path.dirname(os.path.abspath(__file__))
  gif_path = os.path.join(script_dir, filename)
  create_animation_with_memory(steps, colors, memory_usage, memory_details, gif_path)

  print(f"Animation saved as '{filename}'")
  return data


if __name__ == "__main__":
  main()
