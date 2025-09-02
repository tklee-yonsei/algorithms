# performance_comparison.py
import random
import time
import copy
import numpy as np


def partition(arr, low, high):
  """Partition function (Hoare partition scheme)"""
  # Select first element as pivot
  pivot = arr[low]

  i = low - 1
  j = high + 1

  while True:
    # Find element greater than or equal to pivot from left
    i += 1
    while i <= high and arr[i] < pivot:
      i += 1

    # Find element smaller than or equal to pivot from right
    j -= 1
    while j >= low and arr[j] > pivot:
      j -= 1

    # If no elements to swap, terminate
    if i >= j:
      return j

    # Swap elements
    arr[i], arr[j] = arr[j], arr[i]


def quick_sort(arr, low=None, high=None):
  """Quick sort function (Hoare partition)"""
  if low is None:
    low = 0
  if high is None:
    high = len(arr) - 1

  if low < high:
    # Partition
    pivot_index = partition(arr, low, high)

    # Conquer
    quick_sort(arr, low, pivot_index)
    quick_sort(arr, pivot_index + 1, high)


def generate_random_array(size):
  """Generate random array"""
  return [random.randint(1, 1000) for _ in range(size)]


def generate_nearly_sorted_array(size):
  """Generate nearly sorted array (about 10% random)"""
  arr = list(range(1, size + 1))
  # Randomly shuffle 10% of elements
  num_swaps = size // 10
  for _ in range(num_swaps):
    i = random.randint(0, size - 1)
    j = random.randint(0, size - 1)
    arr[i], arr[j] = arr[j], arr[i]
  return arr


def generate_reversed_array(size):
  """Generate reversed array"""
  return list(range(size, 0, -1))


def generate_few_unique_array(size):
  """Generate array with many duplicates (values only between 1-10)"""
  return [random.randint(1, 10) for _ in range(size)]


def generate_sorted_array(size):
  """Generate already sorted array"""
  return list(range(1, size + 1))


def measure_sorting_time(sort_func, arr):
  """Measure sorting time"""
  arr_copy = copy.deepcopy(arr)
  start_time = time.time()
  sort_func(arr_copy)
  end_time = time.time()
  return end_time - start_time


def test_performance():
  """Performance test on various data patterns"""
  sizes = [100, 500, 1000, 2000, 5000]

  print("Quick Sort Performance Comparison")
  print("=" * 60)

  for size in sizes:
    print(f"\nArray size: {size}")
    print("-" * 40)

    # Random array
    random_arr = generate_random_array(size)
    random_time = measure_sorting_time(quick_sort, random_arr)
    print(f"Random array:     {random_time:.6f}s")

    # Nearly sorted array
    nearly_sorted_arr = generate_nearly_sorted_array(size)
    nearly_sorted_time = measure_sorting_time(quick_sort, nearly_sorted_arr)
    print(f"Nearly sorted:    {nearly_sorted_time:.6f}s")

    # Reversed array (worst case)
    reversed_arr = generate_reversed_array(size)
    reversed_time = measure_sorting_time(quick_sort, reversed_arr)
    print(f"Reversed array:   {reversed_time:.6f}s")

    # Array with many duplicates
    few_unique_arr = generate_few_unique_array(size)
    few_unique_time = measure_sorting_time(quick_sort, few_unique_arr)
    print(f"Many duplicates:  {few_unique_time:.6f}s")

    # Already sorted array (worst case)
    sorted_arr = generate_sorted_array(size)
    sorted_time = measure_sorting_time(quick_sort, sorted_arr)
    print(f"Already sorted:   {sorted_time:.6f}s")


def verify_sorting():
  """Verify that sorting works correctly"""
  print("\nSorting Verification")
  print("=" * 30)

  # Test cases
  test_cases = [
      ([64, 34, 25, 12, 22, 11, 90], "Basic test"),
      ([1], "Single element"),
      ([], "Empty array"),
      ([3, 3, 3, 3], "All elements same"),
      ([5, 4, 3, 2, 1], "Reversed"),
      ([1, 2, 3, 4, 5], "Already sorted"),
      ([1, 3, 2, 5, 4, 7, 6, 8], "Partially sorted")
  ]

  for arr, description in test_cases:
    original = arr.copy()
    if len(arr) > 0:
      quick_sort(arr)
    is_sorted = arr == sorted(original)
    print(f"{description}: {'✓' if is_sorted else '✗'} {arr}")


def compare_with_builtin():
  """Performance comparison with built-in sort function"""
  print("\nPerformance Comparison with Built-in Sort")
  print("=" * 50)

  sizes = [1000, 5000, 10000]

  for size in sizes:
    print(f"\nArray size: {size}")
    print("-" * 30)

    # Generate random array
    random_arr = generate_random_array(size)

    # Measure quick sort time
    quick_time = measure_sorting_time(quick_sort, random_arr.copy())

    # Measure built-in sort time
    builtin_time = measure_sorting_time(lambda arr: arr.sort(), random_arr.copy())

    print(f"Quick sort:   {quick_time:.6f}s")
    print(f"Built-in sort: {builtin_time:.6f}s")
    print(f"Ratio:        {quick_time / builtin_time:.2f}x")


def analyze_worst_case():
  """Analyze worst case scenarios"""
  print("\nWorst Case Analysis")
  print("=" * 40)

  print("Quick sort worst cases:")
  print("1. Already sorted array")
  print("2. Reverse sorted array")
  print("3. Arrays where pivot is always min/max")

  sizes = [100, 200, 400, 800]

  print("\nSize\tRandom(s)\tSorted(s)\tReversed(s)\tWorst/Avg Ratio")
  print("-" * 65)

  for size in sizes:
    # Random array (average case)
    random_arr = generate_random_array(size)
    random_time = measure_sorting_time(quick_sort, random_arr)

    # Sorted array (worst case)
    sorted_arr = generate_sorted_array(size)
    sorted_time = measure_sorting_time(quick_sort, sorted_arr)

    # Reversed array (worst case)
    reversed_arr = generate_reversed_array(size)
    reversed_time = measure_sorting_time(quick_sort, reversed_arr)

    worst_ratio = max(sorted_time, reversed_time) / random_time

    print(f"{size}\t{random_time:.6f}\t{sorted_time:.6f}\t{reversed_time:.6f}\t{worst_ratio:.2f}")


def analyze_time_complexity():
  """Time complexity analysis"""
  print("\nTime Complexity Analysis")
  print("=" * 40)

  sizes = [100, 200, 400, 800, 1600, 3200]
  times = []

  print("Size\tTime(s)\t\tTheoretical\tActual")
  print("\t\t\tRatio\t\tRatio")
  print("-" * 50)

  prev_time = None
  prev_size = None

  for size in sizes:
    random_arr = generate_random_array(size)
    time_taken = measure_sorting_time(quick_sort, random_arr)
    times.append(time_taken)

    # Theoretical ratio: O(n log n) average case, so 2x size ≈ 2.2x time
    theoretical_ratio = (size * np.log2(size)) / (prev_size *
                                                  np.log2(prev_size)) if prev_size else 1
    actual_ratio = time_taken / prev_time if prev_time else 1

    print(f"{size}\t{time_taken:.6f}\t{theoretical_ratio:.2f}\t\t{actual_ratio:.2f}")

    prev_time = time_taken
    prev_size = size


def compare_pivot_strategies():
  """Compare different pivot selection strategies (conceptual)"""
  print("\nPivot Selection Strategy Analysis")
  print("=" * 50)

  print("Current implementation: First element as pivot (Hoare partition)")
  print("\nPivot strategy comparison:")
  print("1. First element (current):")
  print("   - Pros: Simple implementation")
  print("   - Cons: O(n²) on sorted/reverse sorted arrays")
  print("\n2. Last element (Lomuto):")
  print("   - Pros: Easy to understand")
  print("   - Cons: O(n²) on sorted arrays")
  print("\n3. Random element:")
  print("   - Pros: Expected O(n log n) performance")
  print("   - Cons: Random number generation overhead")
  print("\n4. Median-of-three:")
  print("   - Pros: Better performance on partially sorted data")
  print("   - Cons: More complex implementation")

  # Demonstrate current strategy performance on different inputs
  size = 1000
  print(f"\nPerformance comparison (size {size}):")

  # Random array (good case)
  random_arr = generate_random_array(size)
  random_time = measure_sorting_time(quick_sort, random_arr)
  print(f"Random array:     {random_time:.6f}s")

  # Sorted array (worst case for first-element pivot)
  sorted_arr = generate_sorted_array(size)
  sorted_time = measure_sorting_time(quick_sort, sorted_arr)
  print(f"Sorted array:     {sorted_time:.6f}s ({sorted_time/random_time:.1f}x slower)")


if __name__ == "__main__":
  # Sorting verification
  verify_sorting()

  # Performance test
  test_performance()

  # Comparison with built-in sort
  compare_with_builtin()

  # Worst case analysis
  analyze_worst_case()

  # Time complexity analysis
  analyze_time_complexity()

  # Pivot strategy comparison
  compare_pivot_strategies()
