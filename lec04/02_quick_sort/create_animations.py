#!/usr/bin/env python3
"""
Create various Quick Sort animations with different data patterns
Using 12 elements for better visualization
"""

import os
import sys
import numpy as np

# Import the animation function
from quick_sort_animation import create_animation_for_data_improved


def create_animations():
  """Create various Quick Sort animations"""
  print("=" * 70)
  print("Quick Sort Animation Generator")
  print("Creating animations with 12 elements for better visualization")
  print("=" * 70)

  # Create img directory if it doesn't exist
  if not os.path.exists('img'):
    os.makedirs('img')

  # 1. Random array
  print("\n1. Creating random array animation...")
  random_data = [8, 3, 12, 6, 1, 9, 4, 11, 7, 2, 10, 5]
  create_animation_for_data_improved(random_data, 'img/quick_sort_random.gif')

  # 2. Nearly sorted array
  print("\n2. Creating nearly sorted array animation...")
  nearly_sorted = [1, 2, 3, 5, 4, 6, 7, 9, 8, 10, 11, 12]
  create_animation_for_data_improved(nearly_sorted, 'img/quick_sort_nearly_sorted.gif')

  # 3. Reversed array (worst case for Hoare with first pivot)
  print("\n3. Creating reversed array animation (worst case)...")
  reversed_data = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
  create_animation_for_data_improved(reversed_data, 'img/quick_sort_reversed.gif')

  # 4. Array with duplicates
  print("\n4. Creating array with duplicates animation...")
  duplicates = [5, 2, 8, 2, 9, 1, 5, 5, 3, 8, 1, 7]
  create_animation_for_data_improved(duplicates, 'img/quick_sort_duplicates.gif')

  # 5. Already sorted array (also worst case)
  print("\n5. Creating already sorted array animation...")
  sorted_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
  create_animation_for_data_improved(sorted_data, 'img/quick_sort_sorted.gif')

  # 6. Balanced case (good pivots)
  print("\n6. Creating balanced case animation...")
  balanced = [6, 3, 9, 1, 4, 8, 11, 2, 5, 7, 10, 12]
  create_animation_for_data_improved(balanced, 'img/quick_sort_balanced.gif')

  # 7. Zigzag pattern
  print("\n7. Creating zigzag pattern animation...")
  zigzag = [1, 12, 2, 11, 3, 10, 4, 9, 5, 8, 6, 7]
  create_animation_for_data_improved(zigzag, 'img/quick_sort_zigzag.gif')

  # 8. Demo case (mixed)
  print("\n8. Creating demo case animation...")
  demo = [7, 2, 10, 4, 8, 1, 12, 5, 9, 3, 11, 6]
  create_animation_for_data_improved(demo, 'img/quick_sort_demo.gif')

  print("\n" + "=" * 70)
  print("✅ ALL ANIMATIONS CREATED SUCCESSFULLY!")
  print("=" * 70)
  print("\n📁 Generated files in img/:")
  print("  ├── quick_sort_random.gif      (Random distribution)")
  print("  ├── quick_sort_nearly_sorted.gif (Nearly sorted)")
  print("  ├── quick_sort_reversed.gif    (Worst case - reversed)")
  print("  ├── quick_sort_duplicates.gif  (With duplicate values)")
  print("  ├── quick_sort_sorted.gif      (Already sorted)")
  print("  ├── quick_sort_balanced.gif    (Good pivot selection)")
  print("  ├── quick_sort_zigzag.gif      (Zigzag pattern)")
  print("  └── quick_sort_demo.gif        (General demonstration)")
  print("\n💡 Each animation shows:")
  print("  • 12 elements for clear visualization")
  print("  • Hoare partition with first element as pivot")
  print("  • Cumulative recursion stack")
  print("  • Visual pointer markers (i, j, P)")
  print("  • Step-by-step partitioning process")
  print("=" * 70)


if __name__ == "__main__":
  create_animations()
