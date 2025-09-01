# quickSort.py
def partition(arr, low, high):
  """배열을 분할하는 함수 (Hoare partition scheme)"""
  # 첫 번째 요소를 피벗으로 선택
  pivot = arr[low]

  i = low - 1
  j = high + 1

  while True:
    # 왼쪽에서 피벗보다 큰 요소 찾기
    i += 1
    while i <= high and arr[i] < pivot:
      i += 1

    # 오른쪽에서 피벗보다 작은 요소 찾기
    j -= 1
    while j >= low and arr[j] > pivot:
      j -= 1

    # 교환할 요소가 없으면 종료
    if i >= j:
      return j

    # 요소 교환
    arr[i], arr[j] = arr[j], arr[i]


def quick_sort(arr, low=None, high=None):
  """퀵 정렬 함수 (Hoare partition)"""
  if low is None:
    low = 0
  if high is None:
    high = len(arr) - 1

  if low < high:
    # 분할
    pivot_index = partition(arr, low, high)

    # 정복
    quick_sort(arr, low, pivot_index)
    quick_sort(arr, pivot_index + 1, high)


# 사용 예시
if __name__ == "__main__":
  arr = [64, 34, 25, 12, 22, 11, 90]

  print("정렬 전 배열:", arr)

  # Hoare 방식 퀵 정렬
  quick_sort(arr)
  print("정렬 후 배열:", arr)
