# shellSort.py

# TODO: 특정 gap 그룹에 대해 삽입 정렬을 수행하는 함수를 구현하세요
def insertion_sort_for_gap(arr, start, gap):
  """
  특정 gap 그룹에 대해 삽입 정렬을 수행하는 함수
  arr: 정렬할 배열
  start: 그룹의 시작 인덱스
  gap: 간격
  """
  # 여기에 코드를 작성하세요
  # 힌트: gap만큼 떨어진 요소들 사이에서 삽입 정렬 수행
  pass


# TODO: Shell Sort 메인 함수를 구현하세요
def shell_sort(arr):
  """
  Shell Sort 알고리즘 구현 (Shell's original sequence 사용)
  """
  # 여기에 코드를 작성하세요
  # 힌트:
  # 1. 초기 gap을 len(arr)//2로 설정
  # 2. gap을 점진적으로 줄여가며 (gap = gap//2) 각 그룹에 대해 삽입 정렬 수행
  # 3. gap이 0이 될 때까지 반복
  # Shell's original sequence: n/2, n/4, n/8, ..., 1
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
