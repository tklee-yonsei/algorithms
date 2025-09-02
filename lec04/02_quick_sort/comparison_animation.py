# comparison_animation.py
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random
import copy
import os


def partition(arr, low, high):
  """Hoare partition scheme"""
  pivot = arr[low]
  i = low - 1
  j = high + 1

  while True:
    i += 1
    while arr[i] < pivot:
      i += 1

    j -= 1
    while arr[j] > pivot:
      j -= 1

    if i >= j:
      return j

    arr[i], arr[j] = arr[j], arr[i]


def quick_sort_steps(arr):
  """Quick sort with step recording"""
  steps = []
  work_arr = arr.copy()
  steps.append(work_arr.copy())

  def quick_sort_recursive(arr, low, high):
    if low < high:
      pivot_index = partition(arr, low, high)
      steps.append(arr.copy())
      quick_sort_recursive(arr, low, pivot_index)
      quick_sort_recursive(arr, pivot_index + 1, high)

  quick_sort_recursive(work_arr, 0, len(work_arr) - 1)
  return steps


def merge_sort_steps(arr):
  """Merge sort with step recording"""
  steps = []
  work_arr = arr.copy()
  steps.append(work_arr.copy())

  def merge(arr, left, mid, right):
    left_arr = arr[left:mid+1]
    right_arr = arr[mid+1:right+1]

    i = j = 0
    k = left

    while i < len(left_arr) and j < len(right_arr):
      if left_arr[i] <= right_arr[j]:
        arr[k] = left_arr[i]
        i += 1
      else:
        arr[k] = right_arr[j]
        j += 1
      k += 1
      steps.append(arr.copy())

    while i < len(left_arr):
      arr[k] = left_arr[i]
      i += 1
      k += 1
      steps.append(arr.copy())

    while j < len(right_arr):
      arr[k] = right_arr[j]
      j += 1
      k += 1
      steps.append(arr.copy())

  def merge_sort_recursive(arr, left, right):
    if left < right:
      mid = (left + right) // 2
      merge_sort_recursive(arr, left, mid)
      merge_sort_recursive(arr, mid + 1, right)
      merge(arr, left, mid, right)

  merge_sort_recursive(work_arr, 0, len(work_arr) - 1)
  return steps


def bubble_sort_steps(arr):
  """Bubble sort with step recording"""
  steps = []
  work_arr = arr.copy()
  steps.append(work_arr.copy())
  n = len(work_arr)

  for i in range(n):
    for j in range(0, n - i - 1):
      if work_arr[j] > work_arr[j + 1]:
        work_arr[j], work_arr[j + 1] = work_arr[j + 1], work_arr[j]
        steps.append(work_arr.copy())

  return steps


def selection_sort_steps(arr):
  """Selection sort with step recording"""
  steps = []
  work_arr = arr.copy()
  steps.append(work_arr.copy())
  n = len(work_arr)

  for i in range(n):
    min_idx = i
    for j in range(i + 1, n):
      if work_arr[j] < work_arr[min_idx]:
        min_idx = j

    if min_idx != i:
      work_arr[i], work_arr[min_idx] = work_arr[min_idx], work_arr[i]
      steps.append(work_arr.copy())

  return steps


def create_comparison_animation():
  """Create comparison animation of different sorting algorithms"""
  # Test data
  data = [8, 3, 5, 4, 7, 6, 1, 2]

  # Get steps for each algorithm
  quick_steps = quick_sort_steps(data)
  merge_steps = merge_sort_steps(data)
  bubble_steps = bubble_sort_steps(data)
  selection_steps = selection_sort_steps(data)

  # Normalize step counts (pad shorter ones)
  max_steps = max(len(quick_steps), len(merge_steps),
                  len(bubble_steps), len(selection_steps))

  # Pad shorter step lists
  while len(quick_steps) < max_steps:
    quick_steps.append(quick_steps[-1])
  while len(merge_steps) < max_steps:
    merge_steps.append(merge_steps[-1])
  while len(bubble_steps) < max_steps:
    bubble_steps.append(bubble_steps[-1])
  while len(selection_steps) < max_steps:
    selection_steps.append(selection_steps[-1])

  # Create animation
  fig, axes = plt.subplots(2, 2, figsize=(16, 12))
  fig.suptitle('Sorting Algorithm Comparison', fontsize=16, fontweight='bold')

  # Flatten axes for easier indexing
  axes = axes.flatten()

  algorithms = ['Quick Sort', 'Merge Sort', 'Bubble Sort', 'Selection Sort']
  steps_list = [quick_steps, merge_steps, bubble_steps, selection_steps]
  colors = ['#FF5722', '#4CAF50', '#2196F3', '#9C27B0']

  def animate(frame):
    for i, (ax, algorithm, steps, color) in enumerate(zip(axes, algorithms, steps_list, colors)):
      ax.clear()

      # Create bar chart
      bars = ax.bar(range(len(data)), steps[frame],
                    color=color, alpha=0.7, edgecolor='black', linewidth=1)

      # Styling
      ax.set_title(f'{algorithm} - Step {frame + 1}', fontweight='bold')
      ax.set_ylim(0, max(data) * 1.1)
      ax.set_xlim(-0.5, len(data) - 0.5)

      # Add values on bars
      for j, bar in enumerate(bars):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                f'{int(height)}', ha='center', va='bottom', fontweight='bold')

      # Grid
      ax.grid(True, alpha=0.3)
      ax.set_axisbelow(True)

  # Create animation
  anim = animation.FuncAnimation(fig, animate, frames=max_steps,
                                 interval=500, repeat=True, blit=False)

  # Save animation
  script_dir = os.path.dirname(os.path.abspath(__file__))
  gif_path = os.path.join(script_dir, 'img', 'comparison_animation.gif')
  anim.save(gif_path, writer='pillow', fps=2, dpi=100)
  plt.close()

  print(f"Comparison animation saved as '{gif_path}'")


def create_performance_comparison():
  """Create performance comparison visualization"""
  algorithms = ['Quick Sort\n(Average)', 'Quick Sort\n(Worst)',
                'Merge Sort', 'Bubble Sort', 'Selection Sort']

  # Theoretical time complexities (normalized)
  sizes = [10, 20, 50, 100, 200, 500]

  # Calculate theoretical times (normalized to show relative performance)
  quick_avg = [n * np.log2(n) for n in sizes]  # O(n log n)
  quick_worst = [n * n for n in sizes]  # O(n²)
  merge_times = [n * np.log2(n) for n in sizes]  # O(n log n)
  bubble_times = [n * n for n in sizes]  # O(n²)
  selection_times = [n * n for n in sizes]  # O(n²)

  # Normalize to make comparison clearer
  base = quick_avg[-1]
  quick_avg = [t / base for t in quick_avg]
  quick_worst = [t / base for t in quick_worst]
  merge_times = [t / base for t in merge_times]
  bubble_times = [t / base for t in bubble_times]
  selection_times = [t / base for t in selection_times]

  plt.figure(figsize=(12, 8))
  plt.plot(sizes, quick_avg, 'o-', label='Quick Sort (Average: O(n log n))',
           linewidth=2, markersize=6)
  plt.plot(sizes, quick_worst, 's-', label='Quick Sort (Worst: O(n²))',
           linewidth=2, markersize=6)
  plt.plot(sizes, merge_times, '^-', label='Merge Sort (O(n log n))',
           linewidth=2, markersize=6)
  plt.plot(sizes, bubble_times, 'v-',
           label='Bubble Sort (O(n²))', linewidth=2, markersize=6)
  plt.plot(sizes, selection_times, 'd-',
           label='Selection Sort (O(n²))', linewidth=2, markersize=6)

  plt.xlabel('Input Size (n)', fontsize=12, fontweight='bold')
  plt.ylabel('Relative Time (normalized)', fontsize=12, fontweight='bold')
  plt.title('Sorting Algorithm Time Complexity Comparison',
            fontsize=14, fontweight='bold')
  plt.legend(fontsize=10)
  plt.grid(True, alpha=0.3)
  plt.yscale('log')

  # Save plot
  script_dir = os.path.dirname(os.path.abspath(__file__))
  plot_path = os.path.join(script_dir, 'img', 'performance_comparison.png')
  plt.savefig(plot_path, dpi=150, bbox_inches='tight')
  plt.close()

  print(f"Performance comparison plot saved as '{plot_path}'")


def create_space_complexity_comparison():
  """Create space complexity comparison"""
  algorithms = ['Quick Sort', 'Merge Sort',
                'Bubble Sort', 'Selection Sort', 'Heap Sort']
  space_complexities = ['O(log n)', 'O(n)', 'O(1)', 'O(1)', 'O(1)']
  colors = ['#FF5722', '#4CAF50', '#2196F3', '#9C27B0', '#FF9800']

  # Simulate space usage for visualization
  sizes = [10, 50, 100, 500, 1000]

  quick_space = [np.log2(n) for n in sizes]  # O(log n) - recursion stack
  merge_space = sizes  # O(n) - auxiliary arrays
  bubble_space = [1] * len(sizes)  # O(1) - constant space
  selection_space = [1] * len(sizes)  # O(1) - constant space
  heap_space = [1] * len(sizes)  # O(1) - constant space

  plt.figure(figsize=(12, 8))
  plt.plot(sizes, quick_space, 'o-', label='Quick Sort O(log n)',
           linewidth=2, markersize=6, color=colors[0])
  plt.plot(sizes, merge_space, 's-', label='Merge Sort O(n)',
           linewidth=2, markersize=6, color=colors[1])
  plt.plot(sizes, bubble_space, '^-', label='Bubble Sort O(1)',
           linewidth=2, markersize=6, color=colors[2])
  plt.plot(sizes, selection_space, 'v-', label='Selection Sort O(1)',
           linewidth=2, markersize=6, color=colors[3])
  plt.plot(sizes, heap_space, 'd-', label='Heap Sort O(1)',
           linewidth=2, markersize=6, color=colors[4])

  plt.xlabel('Input Size (n)', fontsize=12, fontweight='bold')
  plt.ylabel('Space Usage (relative)', fontsize=12, fontweight='bold')
  plt.title('Sorting Algorithm Space Complexity Comparison',
            fontsize=14, fontweight='bold')
  plt.legend(fontsize=10)
  plt.grid(True, alpha=0.3)

  # Save plot
  script_dir = os.path.dirname(os.path.abspath(__file__))
  plot_path = os.path.join(script_dir, 'img', 'space_complexity_comparison.png')
  plt.savefig(plot_path, dpi=150, bbox_inches='tight')
  plt.close()

  print(f"Space complexity comparison plot saved as '{plot_path}'")


def create_stability_comparison():
  """Create sorting algorithm stability comparison table"""
  print("\nSorting Algorithm Comparison Table")
  print("=" * 80)
  print(f"{'Algorithm':<15} {'Time (Best)':<12} {'Time (Avg)':<12} {'Time (Worst)':<12} {'Space':<8} {'Stable':<8}")
  print("-" * 80)

  algorithms_data = [
      ("Quick Sort", "O(n log n)", "O(n log n)", "O(n²)", "O(log n)", "No"),
      ("Merge Sort", "O(n log n)", "O(n log n)", "O(n log n)", "O(n)", "Yes"),
      ("Heap Sort", "O(n log n)", "O(n log n)", "O(n log n)", "O(1)", "No"),
      ("Bubble Sort", "O(n)", "O(n²)", "O(n²)", "O(1)", "Yes"),
      ("Selection Sort", "O(n²)", "O(n²)", "O(n²)", "O(1)", "No"),
      ("Insertion Sort", "O(n)", "O(n²)", "O(n²)", "O(1)", "Yes"),
      ("Shell Sort", "O(n log n)", "O(n^1.25)", "O(n²)", "O(1)", "No"),
      ("Counting Sort", "O(n+k)", "O(n+k)", "O(n+k)", "O(k)", "Yes"),
      ("Radix Sort", "O(nk)", "O(nk)", "O(nk)", "O(n+k)", "Yes"),
      ("Bucket Sort", "O(n+k)", "O(n+k)", "O(n²)", "O(n)", "Yes")
  ]

  for algo_data in algorithms_data:
    print(
        f"{algo_data[0]:<15} {algo_data[1]:<12} {algo_data[2]:<12} {algo_data[3]:<12} {algo_data[4]:<8} {algo_data[5]:<8}")

  print("-" * 80)
  print("\nNotes:")
  print("- k: range of input values")
  print("- n: number of elements")
  print("- Quick Sort worst case occurs with already sorted/reverse sorted arrays")
  print("- Merge Sort guarantees O(n log n) in all cases but uses O(n) extra space")
  print("- Stable algorithms maintain relative order of equal elements")


if __name__ == "__main__":
  print("Creating sorting algorithm comparison visualizations...")

  # Create comparison animation
  create_comparison_animation()

  # Create performance comparison plot
  create_performance_comparison()

  # Create space complexity comparison plot
  create_space_complexity_comparison()

  # Print stability comparison table
  create_stability_comparison()

  print("\n✅ All comparison visualizations created!")
  print("Files generated:")
  print("- img/comparison_animation.gif")
  print("- img/performance_comparison.png")
  print("- img/space_complexity_comparison.png")
