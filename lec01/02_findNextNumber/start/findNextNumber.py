# findNextNumber.py
# TODO: 내가 적어둔 수열에서 다음 수를 찾는 함수를 작성하세요.
def find_next_number(previous_number, my_sequence):
  """내가 적어둔 수열에서 다음 수를 찾는 함수"""
  # 여기에 코드를 작성하세요
  return None


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
