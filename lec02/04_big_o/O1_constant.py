# O1_constant.py
# O(1) - 상수 시간복잡도
# 입력 크기와 관계없이 항상 일정한 시간이 걸림

def get_first_element(arr):
  """배열의 첫 번째 요소 반환 - O(1)"""
  if len(arr) > 0:
    return arr[0]
  return None


def add_numbers(a, b):
  """두 숫자 더하기 - O(1)"""
  return a + b


def check_if_even(n):
  """짝수인지 확인 - O(1)"""
  return n % 2 == 0


# 사용 예시
if __name__ == "__main__":
  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

  print("O(1) 예시들:")
  print(f"첫 번째 요소: {get_first_element(numbers)}")
  print(f"5 + 3 = {add_numbers(5, 3)}")
  print(f"7은 짝수인가? {check_if_even(7)}")
  print(f"8은 짝수인가? {check_if_even(8)}")
