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

  # 4가지 케이스 비교 애니메이션 생성
  print("\n" + "="*60)
  print("4가지 케이스 비교 애니메이션 생성")
  print("="*60)

  try:
    create_four_case_comparison_animation()
    print("✅ 4가지 케이스 비교 애니메이션 생성 완료!")
  except Exception as e:
    print(f"❌ 4가지 케이스 비교 애니메이션 생성 중 오류: {e}")


def create_four_case_comparison_animation():
  """4가지 케이스를 한 화면에 동시에 표시하는 셸 정렬 비교 애니메이션 생성"""
  print("=" * 60)
  print("셸 정렬 비교 애니메이션 생성")
  print("=" * 60)

  # 기본 데이터 생성 (1-12까지의 숫자)
  base_data = list(range(1, 13))
  print(f"기본 데이터: {base_data}")

  # 4가지 케이스 생성
  cases = {}

  # 1. 랜덤 배열
  random.seed(42)  # 일관된 결과를 위해 시드 고정
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
    i = random.randint(0, 11)
    j = random.randint(0, 11)
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

  # 4. 셸 정렬에 유리한 배열 (큰 값들이 앞쪽에, 작은 값들이 뒤쪽에)
  shell_favorable_arr = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
                         1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
  cases['shell_favorable'] = {
      'data': shell_favorable_arr,
      'name': 'Shell Favorable',
      'color': '#96CEB4'
  }

  # 각 케이스의 정렬 과정 기록
  all_steps = {}
  all_colors = {}
  max_steps = 0

  for case_name, case_info in cases.items():
    print(f"\n{case_info['name']} 처리 중...")
    steps, colors = shell_sort_with_animation(case_info['data'].copy())
    all_steps[case_name] = steps
    all_colors[case_name] = colors
    max_steps = max(max_steps, len(steps))

  # 애니메이션 생성
  create_comparison_animation_frames(all_steps, all_colors, cases, max_steps)

  print(f"\n비교 애니메이션이 생성되었습니다!")
  print("파일: img/comparison_animation.gif")


def shell_sort_with_animation(arr):
  """셸 정렬 애니메이션용 함수 (shell_sort_animation.py와 호환)"""
  from shell_sort_animation import shell_sort_with_animation as shell_anim
  return shell_anim(arr)


def create_comparison_animation_frames(all_steps, all_colors, cases, max_steps):
  """비교 애니메이션 프레임 생성"""
  # 스타일 설정
  plt.style.use('seaborn-v0_8')
  fig, axes = plt.subplots(2, 2, figsize=(16, 12))
  fig.suptitle('Shell Sort Comparison - Different Data Patterns',
               fontsize=18, fontweight='bold', color='#2C3E50')

  # 배경색 설정
  fig.patch.set_facecolor('#F8F9FA')
  for ax in axes.flat:
    ax.set_facecolor('#F8F9FA')

  case_names = list(cases.keys())
  case_positions = [(0, 0), (0, 1), (1, 0), (1, 1)]

  def animate(frame):
    # 각 케이스의 완료 상태 추적
    completion_status = {}

    # 모든 서브플롯 초기화
    for i, (case_name, (row, col)) in enumerate(zip(case_names, case_positions)):
      ax = axes[row, col]
      ax.clear()
      ax.set_facecolor('#F8F9FA')

      # 현재 프레임에 해당하는 데이터 가져오기
      current_frame = min(frame, len(all_steps[case_name]) - 1)
      current_data = all_steps[case_name][current_frame]
      current_colors = all_colors[case_name][current_frame]

      # 바형 그래프 그리기
      bars = ax.bar(range(len(current_data)), current_data,
                    color=current_colors, edgecolor='#2C3E50', linewidth=1.5,
                    alpha=0.8, width=0.7)

      # 그래프 설정
      ax.set_xlim(-0.5, len(current_data) - 0.5)
      ax.set_ylim(0, max(current_data) * 1.1)
      ax.set_title(f"{cases[case_name]['name']}\nStep {current_frame + 1}/{len(all_steps[case_name])}",
                   fontsize=12, fontweight='bold', color='#2C3E50')

      # 값 표시
      for j, bar in enumerate(bars):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.2,
                f'{int(height)}', ha='center', va='bottom',
                fontweight='bold', fontsize=9, color='#2C3E50')

      # 그리드 설정
      ax.grid(True, alpha=0.2, linestyle='-', linewidth=0.5, color='#95A5A6')

      # 축 스타일링
      ax.spines['top'].set_visible(False)
      ax.spines['right'].set_visible(False)
      ax.spines['left'].set_color('#BDC3C7')
      ax.spines['bottom'].set_color('#BDC3C7')

      # 축 눈금 설정
      ax.tick_params(axis='both', colors='#7F8C8D', labelsize=9)

      # 정렬 진행률 계산 (실제 정렬된 요소 수 기반)
      sorted_count = 0
      for k in range(len(current_data)):
        if k < len(current_data) - 1:  # 마지막 요소가 아닌 경우
          # 현재 위치까지 정렬이 완료되었는지 확인
          is_sorted = True
          for m in range(k + 1):
            if current_data[m] != m + 1:  # 1부터 시작하는 정렬된 배열과 비교
              is_sorted = False
              break
          if is_sorted:
            sorted_count = k + 1
        else:  # 마지막 요소
          # 전체 배열이 정렬되었는지 확인
          if all(current_data[i] == i + 1 for i in range(len(current_data))):
            sorted_count = len(current_data)

      progress = (sorted_count / len(current_data)) * 100
      completion_status[case_name] = {
          'progress': progress,
          'completed': sorted_count == len(current_data),
          'step': current_frame + 1
      }

      # 진행률 표시
      ax.text(0.02, 0.98, f'Progress: {progress:.0f}%',
              transform=ax.transAxes, fontsize=10, fontweight='bold',
              verticalalignment='top', color='#2C3E50',
              bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))

    return []

  # 애니메이션 생성
  anim = animation.FuncAnimation(fig, animate, frames=max_steps,
                                 interval=300, repeat=True, blit=False)

  # GIF로 저장
  import os
  script_dir = os.path.dirname(os.path.abspath(__file__))
  gif_path = os.path.join(script_dir, 'img', 'comparison_animation.gif')
  anim.save(gif_path, writer='pillow', fps=3, dpi=150)
  plt.close()

  print(f"Animation saved as '{gif_path}'")


if __name__ == "__main__":
  main()
