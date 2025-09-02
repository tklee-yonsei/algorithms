# shellSort.py

# 특정 gap 그룹에 대해 삽입 정렬을 수행하는 함수
def insertion_sort_for_gap(arr, start, gap):
  """
  특정 gap 그룹에 대해 삽입 정렬을 수행하는 함수
  arr: 정렬할 배열
  start: 그룹의 시작 인덱스
  gap: 간격
  """
  n = len(arr)

  # 현재 gap 그룹의 요소들을 삽입 정렬
  for i in range(start + gap, n, gap):
    temp = arr[i]
    j = i

    # gap만큼 떨어진 요소들과 비교하여 삽입
    while j >= start + gap and arr[j - gap] > temp:
      arr[j] = arr[j - gap]
      j -= gap

    arr[j] = temp


# Shell Sort 메인 함수 (Shell's original sequence 사용)
def shell_sort(arr):
  """
  Shell Sort 알고리즘 구현 (Shell's original sequence 사용)
  """
  n = len(arr)

  # Shell's original sequence: n/2, n/4, n/8, ..., 1
  gap = n // 2
  while gap > 0:
    # 각 gap 그룹에 대해 삽입 정렬 수행
    for start in range(gap):
      insertion_sort_for_gap(arr, start, gap)

    # 다음 gap으로 줄이기
    gap = gap // 2

  return arr


def print_array(arr):
  """배열을 출력하는 함수"""
  print(" ".join(map(str, arr)))


if __name__ == "__main__":
  # 테스트 배열
  arr = [64, 34, 25, 12, 22, 11, 90]

  print("정렬 전 배열:", end=" ")
  print_array(arr)

  shell_sort(arr)

  print("정렬 후 배열:", end=" ")
  print_array(arr)
