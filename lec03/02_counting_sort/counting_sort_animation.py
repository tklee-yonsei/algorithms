#!/usr/bin/env python3
"""
Counting Sort Animation Script

This script visualizes the counting sort algorithm process.
Uses matplotlib to create animations and save them as GIF files.
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from typing import List, Tuple
import argparse

# Font settings
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False


class CountingSortAnimator:
  def __init__(self, arr: List[int], interval: int = 800):
    """
    Counting sort animator initialization

    Args:
        arr: Array to be sorted
        interval: Animation frame interval (ms)
    """
    self.original_array = arr.copy()
    self.interval = interval

    # Store animation step data
    self.steps = []
    self.step_descriptions = []

    # Calculate array-related information
    self.min_val = min(arr)
    self.max_val = max(arr)
    self.offset = -self.min_val  # Fixed offset calculation
    self.range_size = self.max_val - self.min_val + 1

    # Create animation steps
    self._create_animation_steps()

    # Graph setup
    self.fig, self.axes = plt.subplots(2, 2, figsize=(15, 10))
    self.fig.suptitle('Counting Sort Animation', fontsize=16, fontweight='bold')

    # Current step
    self.current_step = 0

  def _create_animation_steps(self):
    """Create animation step data"""
    arr = self.original_array.copy()
    n = len(arr)

    # Step 1: Initial array
    self.steps.append({
        'original_array': arr.copy(),
        'counting_array': [0] * self.range_size,
        'cumulative_array': [0] * self.range_size,
        'result_array': [0] * n,
        'current_element': -1,
        'phase': 'initial'
    })
    self.step_descriptions.append("Initial state: Array to be sorted")

    # Step 2: Create counting array - count each element
    counting_array = [0] * self.range_size
    for i, value in enumerate(arr):
      counting_array[value + self.offset] += 1
      self.steps.append({
          'original_array': arr.copy(),
          'counting_array': counting_array.copy(),
          'cumulative_array': [0] * self.range_size,
          'result_array': [0] * n,
          'current_element': i,
          'phase': 'counting'
      })
      self.step_descriptions.append(
          f"Counting: Process value {value} at index {i}")

    # Step 3: Calculate cumulative sum
    cumulative_array = counting_array.copy()
    for i in range(1, self.range_size):
      cumulative_array[i] += cumulative_array[i-1]
      self.steps.append({
          'original_array': arr.copy(),
          'counting_array': counting_array.copy(),
          'cumulative_array': cumulative_array.copy(),
          'result_array': [0] * n,
          'current_element': i,
          'phase': 'cumulative'
      })
      self.step_descriptions.append(f"Cumulative sum: Up to index {i}")

    # Step 4: Place elements in result array
    result_array = [0] * n
    working_cumulative = cumulative_array.copy()

    for i in range(n-1, -1, -1):
      value = arr[i]
      position = working_cumulative[value + self.offset] - 1
      result_array[position] = value
      working_cumulative[value + self.offset] -= 1

      self.steps.append({
          'original_array': arr.copy(),
          'counting_array': counting_array.copy(),
          'cumulative_array': working_cumulative.copy(),
          'result_array': result_array.copy(),
          'current_element': i,
          'placed_position': position,
          'phase': 'placement'
      })
      self.step_descriptions.append(
          f"Place: value {value} from index {i} → result position {position}")

    # Final step
    self.steps.append({
        'original_array': arr.copy(),
        'counting_array': counting_array.copy(),
        'cumulative_array': working_cumulative.copy(),
        'result_array': result_array.copy(),
        'current_element': -1,
        'phase': 'complete'
    })
    self.step_descriptions.append("Sorting complete!")

  def _draw_array(self, ax, array: List[int], title: str, highlight_idx: int = -1,
                  colors: List[str] = None, placed_position: int = -1):
    """Draw array as bar chart with appropriate labels for each array type"""
    ax.clear()

    if not array or max(array) == 0:
      ax.set_title(title)
      return

    positions = range(len(array))

    # Color settings
    if colors is None:
      colors = ['lightblue'] * len(array)

    # Highlight current element being processed
    if highlight_idx >= 0 and highlight_idx < len(colors):
      colors[highlight_idx] = 'red'

    # Highlight placed position
    if placed_position >= 0 and placed_position < len(colors):
      colors[placed_position] = 'green'

    bars = ax.bar(positions, array, color=colors)

    # Display values with optional index information
    for i, (bar, value) in enumerate(zip(bars, array)):
      if value > 0 or title == "Result Array":  # Show even zero values for result array
        if title == "Cumulative Array" and value > 0:
          # Show cumulative_value(position) where position = cumulative_value - 1
          position = value - 1
          label = f"{value}({position})"
        else:
          # Original Array and Result Array: show only values
          # Counting Array: show only counts
          label = str(value)

        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                label, ha='center', va='bottom', fontsize=10, fontweight='bold')

    ax.set_title(title, fontsize=12, fontweight='bold')

    # Set axis labels based on array type
    if title in ["Counting Array", "Cumulative Array"]:
      ax.set_xlabel('Value Range')
      ax.set_ylabel('Count')
      # Set custom x-axis labels for counting arrays to show actual values
      if hasattr(self, 'min_val') and hasattr(self, 'max_val'):
        value_labels = [str(self.min_val + i) for i in range(len(array))]
        ax.set_xticks(range(len(array)))
        ax.set_xticklabels(value_labels)
    else:
      ax.set_xlabel('Index')
      ax.set_ylabel('Value')

    # Set y-axis range
    if max(array) > 0:
      ax.set_ylim(0, max(array) * 1.2)

  def _get_value_colors(self, array: List[int]) -> List[str]:
    """Generate colors based on values"""
    if not array:
      return []

    unique_values = list(set(array))
    colors_map = plt.cm.Set3(np.linspace(0, 1, len(unique_values)))
    value_to_color = {val: colors_map[i] for i, val in enumerate(unique_values)}

    return [value_to_color.get(val, 'lightblue') for val in array]

  def animate(self, frame):
    """Update animation frame"""
    if frame >= len(self.steps):
      return

    step_data = self.steps[frame]
    description = self.step_descriptions[frame]

    # Update subplot title
    self.fig.suptitle(f'Counting Sort - Step {frame + 1}/{len(self.steps)}: {description}',
                      fontsize=14, fontweight='bold')

    # 1. Original array (top left) - show only values
    highlight_idx = step_data.get('current_element', -1)
    original_colors = self._get_value_colors(step_data['original_array'])
    self._draw_array(self.axes[0, 0], step_data['original_array'],
                     "Original Array", highlight_idx, original_colors)

    # 2. Counting array (top right)
    counting_highlight = -1
    if step_data['phase'] == 'counting' and highlight_idx >= 0:
      value = step_data['original_array'][highlight_idx]
      counting_highlight = value + self.offset

    self._draw_array(self.axes[0, 1], step_data['counting_array'],
                     "Counting Array", counting_highlight)

    # 3. Cumulative array (bottom left)
    cumulative_highlight = step_data.get(
        'current_element', -1) if step_data['phase'] == 'cumulative' else -1
    self._draw_array(self.axes[1, 0], step_data['cumulative_array'],
                     "Cumulative Array", cumulative_highlight)

    # 4. Result array (bottom right)
    placed_position = step_data.get('placed_position', -1)
    result_colors = self._get_value_colors(
        step_data['result_array']) if any(step_data['result_array']) else None
    self._draw_array(self.axes[1, 1], step_data['result_array'],
                     "Result Array", -1, result_colors, placed_position)

    # Adjust layout
    plt.tight_layout()
    plt.subplots_adjust(top=0.92)

  def create_animation(self, filename: str = "counting_sort.gif", save_gif: bool = True):
    """Create and save animation"""
    anim = animation.FuncAnimation(
        self.fig, self.animate, frames=len(self.steps),
        interval=self.interval, repeat=True, blit=False
    )

    if save_gif:
      print(f"Saving animation as {filename}...")
      anim.save(filename, writer='pillow', fps=1000//self.interval)
      print(f"Saved: {filename}")

    plt.show()
    return anim


def create_step_by_step_demo():
  """Create step-by-step demo"""
  test_arrays = [
      ([4, 2, 2, 8, 3, 3, 1], "Basic example"),
      ([1, 4, 1, 2, 7, 5, 2], "With duplicates"),
      ([5, 4, 3, 2, 1], "Reverse order"),
      ([1, 1, 1, 1], "All same values"),
      ([3, 1, 4, 1, 5, 9, 2, 6, 5], "Longer array")
  ]

  for i, (arr, description) in enumerate(test_arrays):
    print(f"\n=== {description} ===")
    print(f"Input array: {arr}")

    animator = CountingSortAnimator(arr, interval=1000)
    filename = f"counting_sort_demo_{i+1}.gif"
    animator.create_animation(filename, save_gif=False)


def create_comparison_demo():
  """Create comparison demo with other sorting algorithms"""
  import time
  import random

  def bubble_sort(arr):
    """Bubble sort (for comparison)"""
    n = len(arr)
    for i in range(n):
      for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
          arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

  def counting_sort_simple(arr):
    """Simple counting sort"""
    if not arr:
      return []

    min_val, max_val = min(arr), max(arr)
    offset = -min_val
    range_size = max_val - min_val + 1

    count = [0] * range_size
    for num in arr:
      count[num + offset] += 1

    for i in range(1, range_size):
      count[i] += count[i - 1]

    result = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
      value = arr[i]
      position = count[value + offset] - 1
      result[position] = value
      count[value + offset] -= 1

    return result

  # Performance comparison
  sizes = [10, 50, 100, 500]

  print("=== Sorting Algorithm Performance Comparison ===")
  print(f"{'Size':<6} {'Counting Sort':<12} {'Bubble Sort':<12} {'Improvement':<10}")
  print("-" * 50)

  for size in sizes:
    # Random data in range 0~20 (favorable for counting sort)
    test_data = [random.randint(0, 20) for _ in range(size)]

    # Measure counting sort time
    start_time = time.time()
    counting_result = counting_sort_simple(test_data.copy())
    counting_time = time.time() - start_time

    # Measure bubble sort time
    start_time = time.time()
    bubble_result = bubble_sort(test_data.copy())
    bubble_time = time.time() - start_time

    # Verify results
    assert counting_result == bubble_result, "Sorting results differ!"

    improvement = bubble_time / counting_time if counting_time > 0 else float('inf')

    print(f"{size:<6} {counting_time:<12.6f} {bubble_time:<12.6f} {improvement:<10.1f}x")


def main():
  """Main function"""
  parser = argparse.ArgumentParser(description='Create counting sort animation')
  parser.add_argument('--array', nargs='+', type=int, default=[4, 2, 2, 8, 3, 3, 1],
                      help='Array to sort (default: [4, 2, 2, 8, 3, 3, 1])')
  parser.add_argument('--interval', type=int, default=1000,
                      help='Animation frame interval (ms, default: 1000)')
  parser.add_argument('--output', type=str, default='counting_sort.gif',
                      help='Output filename (default: counting_sort.gif)')
  parser.add_argument('--demo', action='store_true',
                      help='Run demo with various examples')
  parser.add_argument('--comparison', action='store_true',
                      help='Run performance comparison')
  parser.add_argument('--no-save', action='store_true',
                      help='Do not save as GIF file')

  args = parser.parse_args()

  if args.demo:
    create_step_by_step_demo()
  elif args.comparison:
    create_comparison_demo()
  else:
    print(f"Creating counting sort animation")
    print(f"Input array: {args.array}")

    animator = CountingSortAnimator(args.array, args.interval)
    animator.create_animation(args.output, not args.no_save)


if __name__ == "__main__":
  main()
