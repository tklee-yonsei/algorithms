# fsa_simple.py - 교육용 간단 버전
from enum import Enum


class State(Enum):
  """
  FSA 상태 정의
  """
  S0 = 0  # 시작 상태
  S1 = 1  # 'a'를 읽은 상태
  S2 = 2  # b* 시작 상태 (0개의 'b' 허용)
  S3 = 3  # 'b'를 1개 이상 읽은 상태
  S4 = 4  # 'c'를 읽어서 패턴 매칭 완료 (Accept 상태)


def accept_pattern(input_string):
  """
  간단한 FSA: a(b)*c 패턴 인식

  상태:
  - S0: 시작 상태
  - S1: 'a'를 읽은 상태
  - S2: b* 시작 상태 (0개의 'b' 허용)
  - S3: 'b'를 1개 이상 읽은 상태
  - S4: 'c'를 읽어서 패턴 매칭 완료 (Accept 상태)

  상태 다이어그램:
  S0 --'a'--> S1 --ε--> S2 --'b'--> S3 --'b'--> S2 (loop)
                        S2 --'c'--> S4 (accept)
                        S3 --'c'--> S4 (accept)
  """
  current_state = State.S0
  print(f"시작 상태: {current_state.name}")

  for char in input_string:
    next_state = current_state

    # 상태 전이 규칙
    if current_state == State.S0:  # 시작 상태
      if char == 'a':
        next_state = State.S1
        print(f"'{char}' 입력 -> {next_state.name}")
        # S1에서 epsilon 전이로 S2로 자동 이동
        current_state = State.S2
        print(f"ε 전이 -> {current_state.name}")
        continue  # 다음 루프로 이동
      else:
        return False  # 거부

    elif current_state == State.S2:  # b* 시작 상태
      if char == 'b':
        next_state = State.S3
      elif char == 'c':
        next_state = State.S4
      else:
        return False  # 거부

    elif current_state == State.S3:  # 'b'를 1개 이상 읽은 상태
      if char == 'b':
        next_state = State.S2  # S2로 돌아가서 루프
      elif char == 'c':
        next_state = State.S4
      else:
        return False  # 거부

    elif current_state == State.S4:  # 수락 상태
      return False  # 수락 후에는 더 이상 입력 불가

    print(f"'{char}' 입력 -> {next_state.name}")
    current_state = next_state

  # 최종 상태가 수락 상태(S4)인지 확인
  result = (current_state == State.S4)
  print(f"최종 상태: {current_state.name} -> {'수락' if result else '거부'}")
  return result


def main():
  print("=== 간단한 FSA 예시: a(b)*c 패턴 ===\n")

  # 테스트 케이스들
  test_cases = ["ac", "abc", "abbc", "abbbc", "ab", "bc", "aac"]

  for test_case in test_cases:
    print(f"테스트: '{test_case}'")
    result = accept_pattern(test_case)
    print(f"결과: {'✓ 수락' if result else '✗ 거부'}\n")


if __name__ == "__main__":
  main()
