# shellSort.py

def get_shell_gap(n):
  """
  Shell's original sequence: n/2, n/4, n/8, ...
  """
  return n // 2


def get_knuth_gap(n):
  """
  Knuth's sequence: 1, 4, 13, 40, 121, ...
  """
  gap = 1
  while gap < n // 3:
    gap = 3 * gap + 1
  return gap


def get_next_gap(gap, sequence_type):
  """
  다음 gap 값을 계산
  """
  if sequence_type == "knuth":
    return gap // 3
  else:
    return gap // 2  # shell's original (기본값)


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

    while j >= start + gap and arr[j - gap] > temp:
      arr[j] = arr[j - gap]
      j -= gap

    arr[j] = temp


def shell_sort(arr, sequence_type="shell"):
  """
  Shell Sort 알고리즘 구현
  sequence_type: "shell" (기본값) 또는 "knuth"
  """
  n = len(arr)

  # 초기 gap 설정
  if sequence_type == "knuth":
    gap = get_knuth_gap(n)
  else:
    gap = get_shell_gap(n)  # 기본값

  while gap > 0:
    # 각 gap 그룹에 대해 삽입 정렬 수행
    for start in range(gap):
      insertion_sort_for_gap(arr, start, gap)

    # 다음 gap 계산
    gap = get_next_gap(gap, sequence_type)

  return arr


def print_array(arr):
  """배열을 출력하는 함수"""
  print(" ".join(map(str, arr)))


if __name__ == "__main__":
  # 테스트 배열
  arr = [64, 34, 25, 12, 22, 11, 90]

  print("정렬 전 배열:", end=" ")
  print_array(arr)

  # Shell's original sequence 사용
  print("\nShell's original sequence 사용:", end=" ")
  arr_copy = arr.copy()
  shell_sort(arr_copy, "shell")
  print_array(arr_copy)

  # Knuth's sequence 사용
  print("Knuth's sequence 사용:", end=" ")
  arr_copy = arr.copy()
  shell_sort(arr_copy, "knuth")
  print_array(arr_copy)
