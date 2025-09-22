def lis_memo(arr):
  def helper(i, prev_idx, memo={}):
    # TODO: 실제 계산을 수행하는 도우미 함수
    # i: 현재 검사할 인덱스
    # prev_idx: 이전에 선택한 원소의 인덱스 (-1이면 아직 선택 안함)
    pass

  return helper(0, -1)


if __name__ == "__main__":
  arr = [10, 9, 2, 5, 3, 7, 101, 18]
  print(lis_memo(arr))
