# speed_comparison_animation.py
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import os
import sys
import time

# 상위 디렉토리의 모듈들을 import하기 위해 경로 추가
sys.path.append('../01_selection_sort')
sys.path.append('../02_insertion_sort')
sys.path.append('../05_shell_sort')


def create_speed_comparison_animation():
  """3개 정렬 알고리즘의 속도 비교 애니메이션"""
  print("=" * 80)
  print("Insertion Sort vs Selection Sort vs Shell Sort 속도 비교 애니메이션 생성")
  print("=" * 80)

  # 다양한 크기의 데이터 생성
  sizes = [5, 10, 15, 20]
  algorithms = [
      {'name': 'Selection Sort', 'color': '#FF6B6B', 'func': 'selection_sort'},
      {'name': 'Insertion Sort', 'color': '#4ECDC4', 'func': 'insertion_sort'},
      {'name': 'Shell Sort', 'color': '#45B7D1', 'func': 'shell_sort'}
  ]

  # 각 크기별로 정렬 시간 측정
  results = {}

  for size in sizes:
    print(f"\n크기 {size} 배열 처리 중...")
    results[size] = {}

    # 각 알고리즘별로 시간 측정
    for algorithm in algorithms:
      times = []

      # 여러 번 실행하여 평균 시간 계산
      for _ in range(5):
        # 랜덤 데이터 생성
        random.seed(42 + _)  # 재현 가능한 결과를 위해 시드 설정
        data = list(range(1, size + 1))
        random.shuffle(data)

        # 정렬 시간 측정
        start_time = time.time()

        if algorithm['func'] == 'selection_sort':
          selection_sort(data.copy())
        elif algorithm['func'] == 'insertion_sort':
          insertion_sort(data.copy())
        elif algorithm['func'] == 'shell_sort':
          shell_sort(data.copy())

        end_time = time.time()
        times.append(end_time - start_time)

      # 평균 시간 저장
      results[size][algorithm['name']] = np.mean(times)
      print(f"  {algorithm['name']}: {np.mean(times):.6f}초")

  # 애니메이션 생성
  create_speed_comparison_frames(results, algorithms, sizes)

  print(f"\n속도 비교 애니메이션이 생성되었습니다!")
  print("파일: img/speed_comparison.gif")


def selection_sort(arr):
  """Selection Sort 구현"""
  n = len(arr)
  for i in range(n):
    min_idx = i
    for j in range(i + 1, n):
      if arr[j] < arr[min_idx]:
        min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
  return arr


def insertion_sort(arr):
  """Insertion Sort 구현"""
  for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key
  return arr


def shell_sort(arr):
  """Shell Sort 구현"""
  n = len(arr)
  gap = n // 2

  while gap > 0:
    for i in range(gap, n):
      temp = arr[i]
      j = i
      while j >= gap and arr[j - gap] > temp:
        arr[j] = arr[j - gap]
        j -= gap
      arr[j] = temp
    gap //= 2
  return arr


def create_speed_comparison_frames(results, algorithms, sizes):
  """속도 비교 애니메이션 프레임 생성"""

  fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
  fig.suptitle('Insertion Sort vs Selection Sort vs Shell Sort\n속도 비교',
               fontsize=16, fontweight='bold')

  frames = []

  # 애니메이션 단계별로 프레임 생성
  for step in range(len(sizes) + 1):
    ax1.clear()
    ax2.clear()

    # 현재까지의 데이터만 사용
    current_sizes = sizes[:step]
    current_results = {size: results[size] for size in current_sizes}

    if current_sizes:
      # 막대 그래프 (ax1)
      x = np.arange(len(current_sizes))
      width = 0.25

      for i, algorithm in enumerate(algorithms):
        values = [current_results[size][algorithm['name']]
                  * 1000 for size in current_sizes]  # 밀리초 단위
        bars = ax1.bar(x + i * width, values, width,
                       label=algorithm['name'], color=algorithm['color'], alpha=0.8)

        # 값 표시
        for bar, value in zip(bars, values):
          ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.001,
                   f'{value:.2f}ms', ha='center', va='bottom', fontsize=8)

      ax1.set_xlabel('배열 크기')
      ax1.set_ylabel('실행 시간 (밀리초)')
      ax1.set_title('실행 시간 비교')
      ax1.set_xticks(x + width)
      ax1.set_xticklabels(current_sizes)
      ax1.legend()
      ax1.grid(True, alpha=0.3)

      # 선 그래프 (ax2)
      for algorithm in algorithms:
        values = [current_results[size][algorithm['name']]
                  * 1000 for size in current_sizes]
        ax2.plot(current_sizes, values, marker='o', linewidth=2,
                 label=algorithm['name'], color=algorithm['color'])

      ax2.set_xlabel('배열 크기')
      ax2.set_ylabel('실행 시간 (밀리초)')
      ax2.set_title('실행 시간 추이')
      ax2.legend()
      ax2.grid(True, alpha=0.3)

    # 단계 정보 표시
    if current_sizes:
      step_info = f"단계: {step}/{len(sizes)}"
      ax1.text(0.02, 0.98, step_info, transform=ax1.transAxes,
               fontsize=12, verticalalignment='top',
               bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    frames.append([ax1, ax2])

  # 애니메이션 생성
  anim = animation.ArtistAnimation(fig, frames, interval=1000, repeat=True, blit=False)

  # 저장
  img_dir = os.path.join(os.path.dirname(__file__), 'img')
  os.makedirs(img_dir, exist_ok=True)

  output_path = os.path.join(img_dir, 'speed_comparison.gif')
  anim.save(output_path, writer='pillow', fps=1, dpi=100)

  plt.close()
  print(f"애니메이션이 저장되었습니다: {output_path}")


if __name__ == "__main__":
  create_speed_comparison_animation()
