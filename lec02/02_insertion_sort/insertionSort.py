# insertionSort.py
def insertion_sort(arr):
  """삽입 정렬 함수"""
  n = len(arr)

  for i in range(1, n):
    key = arr[i]
    j = i - 1

    # key보다 큰 원소들을 오른쪽으로 이동
    while j >= 0 and arr[j] > key:
      arr[j + 1] = arr[j]
      j = j - 1

    # key를 올바른 위치에 삽입
    arr[j + 1] = key


# 사용 예시
if __name__ == "__main__":
  arr = [64, 34, 25, 12, 22, 11, 90]

  print("정렬 전 배열:", arr)

  insertion_sort(arr)

  print("정렬 후 배열:", arr)
