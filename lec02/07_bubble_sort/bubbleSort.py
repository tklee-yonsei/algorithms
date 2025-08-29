# bubbleSort.py
def bubble_sort(arr):
  """버블 정렬 함수 (기본 버전)"""
  n = len(arr)

  # 모든 패스를 수행 (n-1번)
  for i in range(n - 1):
    # 마지막 i개 요소는 이미 정렬됨
    for j in range(0, n - i - 1):
      # 인접한 요소들을 비교
      if arr[j] > arr[j + 1]:
        # 큰 요소를 뒤로 보내기 (swap)
        arr[j], arr[j + 1] = arr[j + 1], arr[j]


# 사용 예시
if __name__ == "__main__":
  arr = [64, 34, 25, 12, 22, 11, 90]

  print("정렬 전 배열:", arr)

  bubble_sort(arr)

  print("정렬 후 배열:", arr)
