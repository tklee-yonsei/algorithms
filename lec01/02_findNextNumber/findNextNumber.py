# findNextNumber.py
def find_next_number(previous_number, my_sequence):
  """내가 적어둔 수열에서 다음 수를 찾는 함수"""
  try:
    # 앞 사람이 말한 수의 인덱스 찾기
    current_index = my_sequence.index(previous_number)

    # 마지막 수가 아니라면 다음 수 반환
    if current_index < len(my_sequence) - 1:
      return my_sequence[current_index + 1]
    else:
      return None  # 마지막 수인 경우

  except ValueError:
    return None  # 수열에서 찾을 수 없는 경우


# 사용 예시
if __name__ == "__main__":
  # 내가 미리 적어둔 수열
  my_sequence = [
      1,         2,         4,          8,        16,       32,       64,
      128,       256,       512,        1024,     2048,     4096,     8192,
      16384,     32768,     65536,      131072,   262144,   524288,   1048576,
      2097152,   4194304,   8388608,    16777216, 33554432, 67108864, 134217728,
      268435456, 536870912, 1073741824,
  ]

  prev_num = 8
  result = find_next_number(prev_num, my_sequence)

  if result is not None:
    print(f"앞 사람이 {prev_num}를 말했으니, 나는 {result}를 말한다.")
  else:
    print(f"내 수열에서 {prev_num}를 찾을 수 없거나 마지막 수입니다.")
