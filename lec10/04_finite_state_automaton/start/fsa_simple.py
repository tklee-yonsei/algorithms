# fsa_simple.py - 시작 코드 (교육용 간단 버전)
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

  상태 전이 규칙:
  - S0에서 'a' 입력 시 -> S1, 그리고 epsilon 전이로 S2
  - S2에서 'b' 입력 시 -> S3
  - S2에서 'c' 입력 시 -> S4
  - S3에서 'b' 입력 시 -> S2 (루프백)
  - S3에서 'c' 입력 시 -> S4
  - S4에서 어떤 입력이든 -> 거부 (더 이상 입력 불가)
  - 정의되지 않은 전이는 거부
  """
  current_state = State.S0
  print(f"시작 상태: {current_state.name}")

  # TODO: FSA 구현
  # 1. 입력 문자열의 각 문자에 대해 반복
  # 2. 현재 상태와 입력 문자에 따라 다음 상태 결정
  # 3. 상태 전이 규칙에 따라 if/elif 문으로 구현
  # 4. S0에서 'a' 입력 시 epsilon 전이도 함께 처리
  # 5. 정의되지 않은 전이가 있으면 False 반환 (거부)
  # 6. 최종 상태가 S4인지 확인하여 결과 반환

  for char in input_string:
    # 여기에 구현하세요
    pass

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
