#!/usr/bin/env python3
"""
Improved Quick Sort Animation with Cumulative Recursion Stack and Visual Pointer Markers
Features:
- Cumulative recursion stack showing ALL active calls
- Visual pointer markers (i, j, P) directly on array bars
- Enhanced color coding and layout
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import os


def quick_sort_with_improved_animation(arr):
  """Improved quick sort animation with cumulative recursion stack and pointer visualization"""
  steps = []
  colors = []
  descriptions = []
  recursion_stack = []  # Cumulative recursion stack
  pivot_info = []      # Track pivot information
  pointer_info = []    # Track i, j pointers
  n = len(arr)

  # Copy array to work with (preserve original)
  work_arr = arr.copy()

  # Save initial state
  steps.append(work_arr.copy())
  colors.append(['#E8F5E8'] * n)  # Very light green - unsorted
  descriptions.append("Initial unsorted array")
  recursion_stack.append([])
  pivot_info.append({})
  pointer_info.append({})

  def partition_with_improved_animation(arr, low, high, depth, current_stack, steps, colors, descriptions,
                                        recursion_stack, pivot_info, pointer_info):
    """Improved partition with detailed visualization and pointer markers"""
    pivot = arr[low]
    pivot_original_pos = low  # Track original pivot position

    # Show current recursion level and range
    current_colors = ['#F5F5F5'] * n  # Light gray - not in current scope
    for i in range(low, high + 1):
      current_colors[i] = '#E3F2FD'  # Light blue - current partition range
    current_colors[low] = '#FF5722'  # Orange - pivot

    steps.append(arr.copy())
    colors.append(current_colors.copy())
    descriptions.append(f"Depth {depth}: Partition [{low}..{high}], Pivot = {pivot}")
    recursion_stack.append(current_stack.copy())
    pivot_info.append({'index': low, 'value': pivot, 'range': [low, high]})
    pointer_info.append({})

    # Initialize Hoare partition pointers
    i = low - 1
    j = high + 1

    while True:
      # Move i to the right
      i += 1
      while i <= high and arr[i] < pivot:
        # Show left pointer movement
        current_colors = ['#F5F5F5'] * n
        for idx in range(low, high + 1):
          current_colors[idx] = '#E3F2FD'  # Partition range

        # Find where pivot is currently located
        pivot_current_pos = low
        for idx in range(low, high + 1):
          if arr[idx] == pivot:
            pivot_current_pos = idx
            break
        current_colors[pivot_current_pos] = '#FF5722'  # Pivot (orange)
        current_colors[i] = '#2196F3'    # Left pointer (blue)

        steps.append(arr.copy())
        colors.append(current_colors.copy())
        descriptions.append(f"Left pointer i={i}: {arr[i]} < {pivot}")
        recursion_stack.append(current_stack.copy())
        pivot_info.append({'index': pivot_current_pos,
                          'value': pivot, 'range': [low, high]})
        pointer_info.append({'i': i, 'j': j, 'comparing': 'left',
                            'pivot_pos': pivot_current_pos})
        i += 1

      # Move j to the left
      j -= 1
      while j >= low and arr[j] > pivot:
        # Show right pointer movement
        current_colors = ['#F5F5F5'] * n
        for idx in range(low, high + 1):
          current_colors[idx] = '#E3F2FD'  # Partition range

        # Find where pivot is currently located
        pivot_current_pos = low
        for idx in range(low, high + 1):
          if arr[idx] == pivot:
            pivot_current_pos = idx
            break
        current_colors[pivot_current_pos] = '#FF5722'  # Pivot (orange)
        current_colors[j] = '#9C27B0'    # Right pointer (purple)
        if i <= high:
          current_colors[i] = '#2196F3'  # Left pointer (blue)

        steps.append(arr.copy())
        colors.append(current_colors.copy())
        descriptions.append(f"Right pointer j={j}: {arr[j]} > {pivot}")
        recursion_stack.append(current_stack.copy())
        pivot_info.append({'index': pivot_current_pos,
                          'value': pivot, 'range': [low, high]})
        pointer_info.append({'i': i, 'j': j, 'comparing': 'right',
                            'pivot_pos': pivot_current_pos})
        j -= 1

      # Check if pointers crossed
      if i >= j:
        # Show final pointer positions
        current_colors = ['#F5F5F5'] * n
        for idx in range(low, high + 1):
          current_colors[idx] = '#E3F2FD'  # Partition range

        # Find where pivot is currently located
        pivot_current_pos = low
        for idx in range(low, high + 1):
          if arr[idx] == pivot:
            pivot_current_pos = idx
            break
        current_colors[pivot_current_pos] = '#FF5722'  # Pivot
        if i <= high:
          current_colors[i] = '#2196F3'  # Left pointer
        if j >= low:
          current_colors[j] = '#9C27B0'  # Right pointer

        steps.append(arr.copy())
        colors.append(current_colors.copy())
        descriptions.append(f"Pointers crossed: i={i}, j={j} - Partition complete")
        recursion_stack.append(current_stack.copy())
        pivot_info.append({'index': pivot_current_pos,
                          'value': pivot, 'range': [low, high]})
        pointer_info.append({'i': i, 'j': j, 'crossed': True,
                            'pivot_pos': pivot_current_pos})

        return j

      # Show elements to be swapped
      current_colors = ['#F5F5F5'] * n
      for idx in range(low, high + 1):
        current_colors[idx] = '#E3F2FD'  # Partition range

      # Find where pivot is currently located
      pivot_current_pos = low
      for idx in range(low, high + 1):
        if arr[idx] == pivot:
          pivot_current_pos = idx
          break
      current_colors[pivot_current_pos] = '#FF5722'  # Pivot
      current_colors[i] = '#FFEB3B'    # Yellow - will swap
      current_colors[j] = '#FFEB3B'    # Yellow - will swap

      steps.append(arr.copy())
      colors.append(current_colors.copy())
      descriptions.append(f"Swap {arr[i]} <-> {arr[j]} at positions {i}, {j}")
      recursion_stack.append(current_stack.copy())
      pivot_info.append({'index': pivot_current_pos,
                        'value': pivot, 'range': [low, high]})
      pointer_info.append({'i': i, 'j': j, 'swapping': True,
                          'pivot_pos': pivot_current_pos})

      # Execute swap
      arr[i], arr[j] = arr[j], arr[i]

      # Show after swap with partitioned colors
      current_colors = ['#F5F5F5'] * n
      for idx in range(low, j + 1):
        current_colors[idx] = '#4CAF50'  # Green - <= pivot
      for idx in range(j + 1, high + 1):
        current_colors[idx] = '#F44336'  # Red - > pivot

      # Find where pivot is currently located after swap
      pivot_current_pos = low
      for idx in range(low, high + 1):
        if arr[idx] == pivot:
          pivot_current_pos = idx
          break
      current_colors[pivot_current_pos] = '#FF5722'  # Pivot
      current_colors[i] = '#81C784'  # Light green - just swapped
      current_colors[j] = '#FFCDD2'  # Light red - just swapped

      steps.append(arr.copy())
      colors.append(current_colors.copy())
      descriptions.append(f"After swap: Left part <= {pivot}, Right part > {pivot}")
      recursion_stack.append(current_stack.copy())
      pivot_info.append({'index': pivot_current_pos,
                        'value': pivot, 'range': [low, high]})
      pointer_info.append({'i': i, 'j': j, 'swapped': True,
                          'pivot_pos': pivot_current_pos})

  def quick_sort_recursive_improved(arr, low, high, depth, current_stack, steps, colors, descriptions,
                                    recursion_stack, pivot_info, pointer_info):
    """Improved recursive quick sort with cumulative stack tracking"""
    if low < high:
      # Add current call to stack (only if not already there)
      new_stack = current_stack.copy()
      # Check if current range is not already in the stack
      current_range = f"[{low}..{high}]"
      if not any(call['range'] == current_range for call in new_stack):
        new_stack.append({'range': current_range, 'depth': depth, 'status': 'active'})

      # Show current sorting range with depth indication
      current_colors = ['#F5F5F5'] * n  # Gray - not in scope
      for i in range(low, high + 1):
        # Use different shades based on depth
        if depth == 0:
          current_colors[i] = '#E1F5FE'  # Very light cyan
        elif depth == 1:
          current_colors[i] = '#E8F5E8'  # Very light green
        elif depth == 2:
          current_colors[i] = '#FFF3E0'  # Very light orange
        else:
          current_colors[i] = '#F3E5F5'  # Very light purple

      steps.append(arr.copy())
      colors.append(current_colors.copy())
      descriptions.append(f"Depth {depth}: Start sorting range [{low}..{high}]")
      recursion_stack.append(new_stack.copy())
      pivot_info.append({})
      pointer_info.append({})

      # Update status to partitioning
      partition_stack = new_stack.copy()
      if partition_stack:
        partition_stack[-1]['status'] = 'partitioning'

      # Partition
      pivot_index = partition_with_improved_animation(arr, low, high, depth, partition_stack, steps, colors,
                                                      descriptions, recursion_stack, pivot_info, pointer_info)

      # Update stack - mark partition as completed
      completed_stack = new_stack.copy()
      if completed_stack:
        completed_stack[-1]['status'] = 'partitioned'
        completed_stack[-1]['pivot_index'] = pivot_index

      # Show partition result with clear boundaries
      current_colors = ['#F5F5F5'] * n
      for i in range(low, pivot_index + 1):
        current_colors[i] = '#4CAF50'  # Green - left partition
      if pivot_index >= low and pivot_index <= high:
        current_colors[pivot_index] = '#FF9800'  # Orange - pivot final position
      for i in range(pivot_index + 1, high + 1):
        current_colors[i] = '#F44336'  # Red - right partition

      steps.append(arr.copy())
      colors.append(current_colors.copy())
      descriptions.append(
          f"Partition result: Pivot at {pivot_index}, Left: [{low}..{pivot_index}], Right: [{pivot_index+1}..{high}]")
      recursion_stack.append(completed_stack.copy())
      pivot_info.append(
          {'index': pivot_index, 'value': arr[pivot_index] if pivot_index >= low else None, 'final': True})
      pointer_info.append({})

      # Recursively sort left part
      if low < pivot_index:
        # Show preparing left recursion
        current_colors = ['#F5F5F5'] * n
        for i in range(low, pivot_index):
          current_colors[i] = '#C8E6C9'  # Light green - left subarray
        if pivot_index >= low and pivot_index <= high:
          current_colors[pivot_index] = '#FF9800'  # Pivot

        steps.append(arr.copy())
        colors.append(current_colors.copy())
        descriptions.append(
            f"Depth {depth+1}: Recursively sort left part [{low}..{pivot_index-1}]")
        recursion_stack.append(completed_stack.copy())
        pivot_info.append(
            {'index': pivot_index, 'value': arr[pivot_index] if pivot_index >= low else None})
        pointer_info.append({})

        quick_sort_recursive_improved(arr, low, pivot_index, depth + 1, completed_stack, steps, colors,
                                      descriptions, recursion_stack, pivot_info, pointer_info)

      # Recursively sort right part
      if pivot_index + 1 < high:
        # Show preparing right recursion
        current_colors = ['#F5F5F5'] * n
        if pivot_index >= low and pivot_index <= high:
          current_colors[pivot_index] = '#FF9800'  # Pivot
        for i in range(pivot_index + 1, high + 1):
          current_colors[i] = '#FFCDD2'  # Light red - right subarray

        steps.append(arr.copy())
        colors.append(current_colors.copy())
        descriptions.append(
            f"Depth {depth+1}: Recursively sort right part [{pivot_index+1}..{high}]")
        recursion_stack.append(completed_stack.copy())
        pivot_info.append(
            {'index': pivot_index, 'value': arr[pivot_index] if pivot_index >= low else None})
        pointer_info.append({})

        quick_sort_recursive_improved(arr, pivot_index + 1, high, depth + 1, completed_stack, steps, colors,
                                      descriptions, recursion_stack, pivot_info, pointer_info)

      # Mark current call as completed
      final_stack = new_stack.copy()
      if final_stack:
        final_stack[-1]['status'] = 'completed'

      # Show completed section
      current_colors = ['#F5F5F5'] * n
      for i in range(low, high + 1):
        current_colors[i] = '#4CAF50'  # Green - sorted section

      steps.append(arr.copy())
      colors.append(current_colors.copy())
      descriptions.append(f"Depth {depth}: Section [{low}..{high}] completely sorted")
      recursion_stack.append(final_stack.copy())
      pivot_info.append({})
      pointer_info.append({})

  # Execute improved quick sort
  quick_sort_recursive_improved(work_arr, 0, n - 1, 0, [], steps, colors, descriptions,
                                recursion_stack, pivot_info, pointer_info)

  # Update original array
  for i in range(n):
    arr[i] = work_arr[i]

  # Final sorted state
  final_colors = ['#4CAF50'] * n  # All green - completely sorted
  colors.append(final_colors)
  steps.append(work_arr.copy())
  descriptions.append("Quick sort complete - Array fully sorted!")
  recursion_stack.append([])
  pivot_info.append({})
  pointer_info.append({})

  return steps, colors, descriptions, recursion_stack, pivot_info, pointer_info


def create_improved_animation(steps, colors, descriptions, recursion_stack, pivot_info, pointer_info,
                              filename='quick_sort_improved.gif'):
  """Create improved animation with cumulative recursion stack and pointer markers"""
  # Style settings
  plt.style.use('seaborn-v0_8')
  fig = plt.figure(figsize=(22, 16))

  # Create layout: main array + info panels
  gs = fig.add_gridspec(3, 2, height_ratios=[3, 1.2, 0.8], width_ratios=[3, 1],
                        hspace=0.35, wspace=0.3)

  ax_main = fig.add_subplot(gs[0, :])    # Main array visualization
  ax_recursion = fig.add_subplot(gs[1, 0])  # Recursion stack
  ax_info = fig.add_subplot(gs[1, 1])       # Pivot and pointer info
  ax_legend = fig.add_subplot(gs[2, :])     # Legend and description

  # Background colors
  fig.patch.set_facecolor('#F8F9FA')
  for ax in [ax_main, ax_recursion, ax_info, ax_legend]:
    ax.set_facecolor('#F8F9FA')

  def animate(frame):
    # Clear all axes
    for ax in [ax_main, ax_recursion, ax_info, ax_legend]:
      ax.clear()
      ax.set_facecolor('#F8F9FA')

    # Main array visualization
    bars = ax_main.bar(range(len(steps[frame])), steps[frame],
                       color=colors[frame], edgecolor='#2C3E50', linewidth=2,
                       alpha=0.9, width=0.8)

    ax_main.set_xlim(-0.5, len(steps[frame]) - 0.5)
    ax_main.set_ylim(0, max(max(step) for step in steps) * 1.3)
    ax_main.set_xlabel('Array Index', fontsize=14, fontweight='bold', color='#2C3E50')
    ax_main.set_ylabel('Value', fontsize=14, fontweight='bold', color='#2C3E50')
    ax_main.set_title(f'Improved Quick Sort Visualization - Step {frame + 1}/{len(steps)}',
                      fontsize=16, fontweight='bold', color='#2C3E50', pad=20)

    # Add values on bars
    for i, bar in enumerate(bars):
      height = bar.get_height()
      ax_main.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                   f'{int(height)}', ha='center', va='bottom',
                   fontweight='bold', fontsize=11, color='#2C3E50')

    # Add pointer markers (i, j) as arrows
    if frame < len(pointer_info) and pointer_info[frame]:
      ptr_info = pointer_info[frame]
      max_height = max(max(step) for step in steps) * 1.25

      if 'i' in ptr_info and ptr_info['i'] < len(steps[frame]):
        i_pos = ptr_info['i']
        # Blue arrow for i pointer
        ax_main.annotate('i', xy=(i_pos, steps[frame][i_pos] + 1),
                         xytext=(i_pos, max_height * 0.9),
                         arrowprops=dict(arrowstyle='->', color='#2196F3', lw=3),
                         fontsize=14, fontweight='bold', color='#2196F3',
                         ha='center')

      if 'j' in ptr_info and ptr_info['j'] < len(steps[frame]) and ptr_info['j'] >= 0:
        j_pos = ptr_info['j']
        # Purple arrow for j pointer
        ax_main.annotate('j', xy=(j_pos, steps[frame][j_pos] + 1),
                         xytext=(j_pos, max_height * 0.85),
                         arrowprops=dict(arrowstyle='->', color='#9C27B0', lw=3),
                         fontsize=14, fontweight='bold', color='#9C27B0',
                         ha='center')

      # Mark pivot position
      if 'pivot_pos' in ptr_info and ptr_info['pivot_pos'] < len(steps[frame]):
        pivot_pos = ptr_info['pivot_pos']
        ax_main.annotate('P', xy=(pivot_pos, steps[frame][pivot_pos] + 1),
                         xytext=(pivot_pos, max_height * 0.95),
                         arrowprops=dict(arrowstyle='->', color='#FF5722', lw=3),
                         fontsize=14, fontweight='bold', color='#FF5722',
                         ha='center')

    ax_main.grid(True, alpha=0.2)

    # Cumulative recursion stack visualization
    if frame < len(recursion_stack) and recursion_stack[frame]:
      ax_recursion.set_title(
          'Cumulative Recursion Stack (All Active Calls)', fontweight='bold', fontsize=12)

      stack = recursion_stack[frame]
      max_depth = max([call['depth'] for call in stack]) if stack else 0

      for i, call_info in enumerate(stack):
        depth = call_info['depth']
        range_str = call_info['range']
        side = call_info.get('side', '')
        status = call_info.get('status', 'active')

        # Color based on status - only the LAST item in stack should be active (green)
        if status == 'completed':
          color = '#9E9E9E'  # Gray - completed
        elif (status == 'partitioning' or status == 'active') and i == len(stack) - 1:
          color = '#4CAF50'  # Green - currently active (only the last/top call)
        else:
          color = '#E0E0E0'  # Light gray - pending/waiting

        # Draw horizontal bar for each call
        bar_height = 0.6
        ax_recursion.barh(i, depth + 1, height=bar_height, color=color, alpha=0.7,
                          edgecolor='black', linewidth=1)

        # Add text label
        label = f"D{depth}: {range_str}"
        if side:
          label += f" ({side})"
        if status != 'active':
          label += f" [{status}]"

        ax_recursion.text(0.1, i, label, va='center', fontweight='bold', fontsize=9)

      ax_recursion.set_xlim(0, max_depth + 2)
      ax_recursion.set_ylim(-0.5, len(stack) - 0.5)
      ax_recursion.set_xlabel('Recursion Depth', fontsize=10, fontweight='bold')
    else:
      ax_recursion.text(0.5, 0.5, 'No active recursion calls', transform=ax_recursion.transAxes,
                        ha='center', va='center', fontsize=12, fontweight='bold')
      ax_recursion.set_xlim(0, 1)
      ax_recursion.set_ylim(0, 1)

    # Pivot and pointer information
    ax_info.set_title('Current State Details', fontweight='bold', fontsize=12)
    info_text = []

    if frame < len(pivot_info) and pivot_info[frame]:
      piv_info = pivot_info[frame]
      if 'value' in piv_info and piv_info['value'] is not None:
        info_text.append(f"Pivot: {piv_info['value']} at index {piv_info['index']}")
        if 'range' in piv_info:
          info_text.append(f"Range: {piv_info['range']}")

    if frame < len(pointer_info) and pointer_info[frame]:
      ptr_info = pointer_info[frame]
      if 'i' in ptr_info and 'j' in ptr_info:
        info_text.append(f"Pointers: i={ptr_info['i']}, j={ptr_info['j']}")
        if ptr_info.get('comparing') == 'left':
          info_text.append("→ Searching from left (i)")
        elif ptr_info.get('comparing') == 'right':
          info_text.append("← Searching from right (j)")
        elif ptr_info.get('swapping'):
          info_text.append("⟷ Swapping elements")
        elif ptr_info.get('crossed'):
          info_text.append("✗ Pointers crossed - partition done!")

    # Add active recursion count
    if frame < len(recursion_stack) and recursion_stack[frame]:
      active_calls = len([call for call in recursion_stack[frame]
                         if call.get('status') != 'completed'])
      info_text.append(f"Active calls: {active_calls}")

    if info_text:
      for i, text in enumerate(info_text):
        ax_info.text(0.05, 0.9 - i*0.15, text, transform=ax_info.transAxes,
                     fontsize=11, fontweight='bold', va='top')
    else:
      ax_info.text(0.5, 0.5, 'No current state info', transform=ax_info.transAxes,
                   ha='center', va='center', fontsize=11)

    ax_info.set_xlim(0, 1)
    ax_info.set_ylim(0, 1)

    # Description and legend
    if frame < len(descriptions):
      ax_legend.text(0.02, 0.85, descriptions[frame], transform=ax_legend.transAxes,
                     fontsize=13, fontweight='bold', va='top',
                     bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.9))

    # Color legend
    legend_elements = [
        plt.Rectangle((0, 0), 1, 1, facecolor='#F5F5F5', label='Out of scope'),
        plt.Rectangle((0, 0), 1, 1, facecolor='#E3F2FD', label='Current range'),
        plt.Rectangle((0, 0), 1, 1, facecolor='#FF5722', label='Pivot (P)'),
        plt.Rectangle((0, 0), 1, 1, facecolor='#4CAF50', label='<= Pivot'),
        plt.Rectangle((0, 0), 1, 1, facecolor='#F44336', label='> Pivot'),
        plt.Rectangle((0, 0), 1, 1, facecolor='#FFEB3B', label='Swapping')
    ]

    # Add pointer legend
    ax_legend.text(0.02, 0.4, 'Pointers: i (blue ↓), j (purple ↓), P (orange ↓)',
                   transform=ax_legend.transAxes, fontsize=11, fontweight='bold', va='top')

    ax_legend.legend(handles=legend_elements, loc='lower center', ncol=6,
                     frameon=True, fancybox=True, shadow=True, fontsize=9)
    ax_legend.set_xlim(0, 1)
    ax_legend.set_ylim(0, 1)

    return bars

  # Create animation
  anim = animation.FuncAnimation(fig, animate, frames=len(steps),
                                 interval=2500, repeat=True, blit=False)

  # Save as GIF
  anim.save(filename, writer='pillow', fps=0.4, dpi=100)
  plt.close()

  print(f"Improved quick sort animation saved as '{filename}'")


def main():
  # Test with a small array
  data = [6, 2, 8, 1, 5, 3]
  print("Initial array:", data)

  # Generate improved animation
  steps, colors, descriptions, recursion_stack, pivot_info, pointer_info = quick_sort_with_improved_animation(
      data)

  # Create improved animation
  script_dir = os.path.dirname(os.path.abspath(__file__))
  gif_path = os.path.join(script_dir, 'quick_sort_improved.gif')
  create_improved_animation(steps, colors, descriptions,
                            recursion_stack, pivot_info, pointer_info, gif_path)

  print("Sorting completed:", data)


def create_animation_for_data_improved(data, filename='quick_sort_improved.gif'):
  """Create improved animation for given data"""
  print(f"Creating improved quick sort animation for: {data}")

  # Generate animation data
  steps, colors, descriptions, recursion_stack, pivot_info, pointer_info = quick_sort_with_improved_animation(
      data.copy())

  # Create animation
  script_dir = os.path.dirname(os.path.abspath(__file__))
  gif_path = os.path.join(script_dir, filename)
  create_improved_animation(steps, colors, descriptions,
                            recursion_stack, pivot_info, pointer_info, gif_path)

  print(f"Improved animation saved as '{filename}'")
  return data


if __name__ == "__main__":
  main()
