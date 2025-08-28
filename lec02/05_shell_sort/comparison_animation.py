import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random
import time


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


def shell_sort_with_steps(arr):
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
      'step_count': len(steps)
  })

  return arr, steps


def shell_sort_optimized(arr):
  """최적화된 Shell Sort (Knuth's sequence)"""
  n = len(arr)

  # Knuth's sequence: 1, 4, 13, 40, 121, ...
  gap = 1
  while gap < n // 3:
    gap = 3 * gap + 1

  while gap > 0:
    for i in range(gap, n):
      temp = arr[i]
      j = i

      while j >= gap and arr[j - gap] > temp:
        arr[j] = arr[j - gap]
        j -= gap

      arr[j] = temp

    gap //= 3

  return arr


def insertion_sort_optimized(arr):
  """최적화된 Insertion Sort"""
  for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
      arr[j + 1] = arr[j]
      j -= 1

    arr[j + 1] = key

  return arr


def performance_comparison(arr):
  """실제 성능 비교"""
  print(f"\n실제 성능 비교 (배열 크기: {len(arr)})")
  print("-" * 50)

  # Shell Sort 성능 측정
  arr_copy = arr.copy()
  start_time = time.time()
  shell_sort_optimized(arr_copy)
  shell_time = time.time() - start_time

  # Insertion Sort 성능 측정
  arr_copy = arr.copy()
  start_time = time.time()
  insertion_sort_optimized(arr_copy)
  insertion_time = time.time() - start_time

  print(f"Shell Sort (Knuth): {shell_time:.6f}초")
  print(f"Insertion Sort:     {insertion_time:.6f}초")

  if shell_time < insertion_time:
    print("✅ Shell Sort가 더 빠름!")
  else:
    print("❌ Insertion Sort가 더 빠름")

  return shell_time, insertion_time


def insertion_sort_with_steps(arr):
  """Insertion Sort with step tracking"""
  steps = []

  # 초기 상태 저장
  steps.append({
      'array': arr.copy(),
      'current_i': -1,
      'current_j': -1,
      'key': None,
      'algorithm': 'insertion',
      'description': 'Insertion Sort - Initial State'
  })

  for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    # 현재 처리할 요소 표시
    steps.append({
        'array': arr.copy(),
        'current_i': i,
        'current_j': j,
        'key': key,
        'algorithm': 'insertion',
        'description': f'Insertion Sort - Current: {key}'
    })

    while j >= 0 and arr[j] > key:
      # 비교 중인 요소들 표시
      steps.append({
          'array': arr.copy(),
          'current_i': i,
          'current_j': j,
          'key': key,
          'algorithm': 'insertion',
          'description': f'Insertion Sort - Comparing'
      })

      arr[j + 1] = arr[j]
      j -= 1

    arr[j + 1] = key

    # 삽입 후 상태 표시
    steps.append({
        'array': arr.copy(),
        'current_i': i,
        'current_j': j,
        'key': key,
        'algorithm': 'insertion',
        'description': f'Insertion Sort - Inserted'
    })

  # 최종 정렬 완료 상태
  steps.append({
      'array': arr.copy(),
      'current_i': -1,
      'current_j': -1,
      'key': None,
      'algorithm': 'insertion',
      'description': 'Insertion Sort - Completed'
  })

  return arr, steps


def get_shell_colors(arr, step):
  """셸 정렬용 색상 배열 생성"""
  n = len(arr)
  colors = ['#E3F2FD'] * n  # 기본: 연한 파란색 (Unsorted)

  gap = step.get('gap', 0)
  start = step.get('start', -1)
  current_i = step.get('current_i', -1)
  current_j = step.get('current_j', -1)
  temp = step.get('temp', None)

  if current_i >= 0:
    colors[current_i] = '#FFD54F'  # 노란색 - 현재 처리할 요소

    # 같은 gap 그룹의 요소들 표시
    if gap > 0 and start >= 0:
      for k in range(start, n, gap):
        if k != current_i and k != current_j:
          colors[k] = '#FFB74D'  # 주황색 - 같은 gap 그룹

  if current_j >= 0:
    colors[current_j] = '#FF8A80'  # 빨간색 - 비교 중인 요소

  # 정렬된 요소들 표시 (gap이 0이거나 완료된 경우)
  if gap == 0 or step.get('description', '').find('Completed') >= 0:
    colors = ['#4CAF50'] * n  # 초록색 - 정렬 완료

  return colors


def get_insertion_colors(arr, step):
  """삽입 정렬용 색상 배열 생성"""
  n = len(arr)
  colors = ['#E3F2FD'] * n  # 기본: 연한 파란색 (Unsorted)

  current_i = step.get('current_i', -1)
  current_j = step.get('current_j', -1)
  key = step.get('key', None)

  if current_i >= 0:
    colors[current_i] = '#FFD54F'  # 노란색 - 현재 처리할 요소

  if current_j >= 0:
    colors[current_j] = '#FF8A80'  # 빨간색 - 비교 중인 요소

  # 정렬된 부분 표시
  if current_i > 0:
    for k in range(current_i):
      colors[k] = '#4CAF50'  # 초록색 - 정렬된 요소

  # 완료된 경우
  if step.get('description', '').find('Completed') >= 0:
    colors = ['#4CAF50'] * n  # 초록색 - 정렬 완료

  return colors


def create_comparison_animation(shell_steps, insertion_steps, filename="comparison.gif", title="Shell Sort vs Insertion Sort"):
  """비교 애니메이션 생성"""
  fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

  # 두 알고리즘의 최대 단계 수 계산
  max_steps = max(len(shell_steps), len(insertion_steps))

  def animate(frame):
    ax1.clear()
    ax2.clear()

    bars1 = None
    bars2 = None

    # Shell Sort 애니메이션
    if frame < len(shell_steps):
      step = shell_steps[frame]
      arr = step['array']
      colors = get_shell_colors(arr, step)
      description = step['description']

      bars1 = ax1.bar(range(len(arr)), arr, color=colors,
                      edgecolor='#2C3E50', linewidth=2, alpha=0.8, width=0.7)

      ax1.set_title(f'Shell Sort\n{description}',
                    fontsize=12, fontweight='bold', color='#2C3E50')
      ax1.set_xlabel('Array Index', fontsize=10, color='#2C3E50')
      ax1.set_ylabel('Value', fontsize=10, color='#2C3E50')
      ax1.set_ylim(0, max(arr) * 1.15)

      # 값 표시
      for i, bar in enumerate(bars1):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                 f'{int(height)}', ha='center', va='bottom',
                 fontweight='bold', fontsize=10, color='#2C3E50')

      # 그리드 설정
      ax1.grid(True, alpha=0.2, linestyle='-', linewidth=0.5, color='#95A5A6')

    # Insertion Sort 애니메이션
    if frame < len(insertion_steps):
      step = insertion_steps[frame]
      arr = step['array']
      colors = get_insertion_colors(arr, step)
      description = step['description']

      bars2 = ax2.bar(range(len(arr)), arr, color=colors,
                      edgecolor='#2C3E50', linewidth=2, alpha=0.8, width=0.7)

      ax2.set_title(f'Insertion Sort\n{description}',
                    fontsize=12, fontweight='bold', color='#2C3E50')
      ax2.set_xlabel('Array Index', fontsize=10, color='#2C3E50')
      ax2.set_ylabel('Value', fontsize=10, color='#2C3E50')
      ax2.set_ylim(0, max(arr) * 1.15)

      # 값 표시
      for i, bar in enumerate(bars2):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                 f'{int(height)}', ha='center', va='bottom',
                 fontweight='bold', fontsize=10, color='#2C3E50')

      # 그리드 설정
      ax2.grid(True, alpha=0.2, linestyle='-', linewidth=0.5, color='#95A5A6')

    plt.suptitle(f'{title} - Step {frame + 1}/{max_steps}',
                 fontsize=14, fontweight='bold', color='#2C3E50')

    return bars1, bars2

  # 애니메이션 생성
  anim = animation.FuncAnimation(fig, animate, frames=max_steps,
                                 interval=800, repeat=True, blit=False)

  # GIF로 저장
  anim.save(filename, writer='pillow', fps=2, dpi=150)
  plt.close()

  print(f"Comparison animation saved as '{filename}'")

  return anim


def create_test_cases():
  """Insertion sort가 이기는 케이스와 Shell sort가 이기는 케이스 생성"""

  # 케이스 1: Insertion sort가 유리한 케이스 (부분적으로 정렬된 배열)
  insertion_favorable = [1, 2, 3, 4, 5, 15, 16,
                         17, 18, 19, 20, 6, 7, 8, 9, 10, 11, 12, 13, 14]

  # 케이스 2: Shell sort가 유리한 케이스 (중간 정도로 뒤섞인 배열)
  shell_favorable = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44,
                     1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

  return insertion_favorable, shell_favorable


def main():
  print("Creating comparison animations for different cases...")

  # 테스트 케이스 생성
  insertion_case, shell_case = create_test_cases()

  print("\nCase 1: Insertion Sort Favorable")
  print("Array:", insertion_case[:10], "...")

  # Insertion sort가 유리한 케이스
  shell_sorted1, shell_steps1 = shell_sort_with_steps(insertion_case.copy())
  insertion_sorted1, insertion_steps1 = insertion_sort_with_steps(insertion_case.copy())

  print(f"Shell Sort steps: {len(shell_steps1)}")
  print(f"Insertion Sort steps: {len(insertion_steps1)}")

  if len(insertion_steps1) < len(shell_steps1):
    print("✅ Insertion Sort wins!")
  else:
    print("❌ Shell Sort wins")

  # 실제 성능 비교
  performance_comparison(insertion_case)

  # 첫 번째 비교 애니메이션 생성
  print("Creating insertion_favorable.gif...")
  create_comparison_animation(shell_steps1, insertion_steps1,
                              "img/insertion_favorable.gif")

  print("\nCase 2: Shell Sort Favorable")
  print("Array:", shell_case[:10], "...")

  # Shell sort가 유리한 케이스
  shell_sorted2, shell_steps2 = shell_sort_with_steps(shell_case.copy())
  insertion_sorted2, insertion_steps2 = insertion_sort_with_steps(shell_case.copy())

  print(f"Shell Sort steps: {len(shell_steps2)}")
  print(f"Insertion Sort steps: {len(insertion_steps2)}")

  if len(shell_steps2) < len(insertion_steps2):
    print("✅ Shell Sort wins!")
  else:
    print("❌ Insertion Sort wins")

  # 실제 성능 비교
  performance_comparison(shell_case)

  # 두 번째 비교 애니메이션 생성
  print("Creating shell_favorable.gif...")
  create_comparison_animation(shell_steps2, insertion_steps2, "img/shell_favorable.gif")

  # 더 큰 배열로 성능 테스트
  print("\n" + "="*60)
  print("대용량 배열 성능 테스트")
  print("="*60)

  random.seed(42)
  large_array = [random.randint(1, 1000) for _ in range(1000)]
  performance_comparison(large_array)

  print("\nBoth animations created successfully!")


if __name__ == "__main__":
  main()
