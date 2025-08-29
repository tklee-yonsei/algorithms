# Onlogn_linearithmic.py
# O(n log n) - 선형로그 시간복잡도
# 입력 크기와 로그의 곱에 비례하여 시간이 증가

def merge_sort(arr):
  """병합 정렬 - O(n log n)"""
  if len(arr) <= 1:
    return arr

  mid = len(arr) // 2
  left = merge_sort(arr[:mid])
  right = merge_sort(arr[mid:])

  return merge(left, right)


def merge(left, right):
  """병합 함수"""
  result = []
  i = j = 0

  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  result.extend(left[i:])
  result.extend(right[j:])
  return result


def quick_sort(arr):
  """퀵 정렬 - O(n log n) 평균"""
  if len(arr) <= 1:
    return arr

  pivot = arr[len(arr) // 2]
  left = [x for x in arr if x < pivot]
  middle = [x for x in arr if x == pivot]
  right = [x for x in arr if x > pivot]

  return quick_sort(left) + middle + quick_sort(right)


def heap_sort(arr):
  """힙 정렬 - O(n log n)"""
  def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
      largest = left

    if right < n and arr[right] > arr[largest]:
      largest = right

    if largest != i:
      arr[i], arr[largest] = arr[largest], arr[i]
      heapify(arr, n, largest)

  n = len(arr)

  # 힙 구성
  for i in range(n // 2 - 1, -1, -1):
    heapify(arr, n, i)

  # 힙에서 요소 추출
  for i in range(n - 1, 0, -1):
    arr[0], arr[i] = arr[i], arr[0]
    heapify(arr, i, 0)

  return arr


# 사용 예시
if __name__ == "__main__":
  print("O(n log n) 예시들:")

  # 병합 정렬
  arr1 = [64, 34, 25, 12, 22, 11, 90]
  print(f"원본 배열: {arr1}")
  print(f"병합 정렬: {merge_sort(arr1.copy())}")

  # 퀵 정렬
  arr2 = [38, 27, 43, 3, 9, 82, 10]
  print(f"퀵 정렬: {quick_sort(arr2.copy())}")

  # 힙 정렬
  arr3 = [12, 11, 13, 5, 6, 7]
  print(f"힙 정렬: {heap_sort(arr3.copy())}")
