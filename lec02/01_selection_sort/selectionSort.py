# selectionSort.py
def selection_sort(arr):
  """선택 정렬 함수"""
  n = len(arr)

  for i in range(n - 1):
    min_index = i

    # i번째 위치부터 끝까지 최솟값 찾기
    for j in range(i + 1, n):
      if arr[j] < arr[min_index]:
        min_index = j

    # 최솟값을 i번째 위치로 교환
    if min_index != i:
      arr[i], arr[min_index] = arr[min_index], arr[i]


# 사용 예시
if __name__ == "__main__":
  arr = [64, 34, 25, 12, 22, 11, 90]

  print("정렬 전 배열:", arr)

  selection_sort(arr)

  print("정렬 후 배열:", arr)
