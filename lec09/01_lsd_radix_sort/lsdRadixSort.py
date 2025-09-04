# lsdRadixSort.py

def get_max(arr):
  """
  배열에서 최대값 찾기

  Args:
      arr: 입력 배열

  Returns:
      배열의 최대값
  """
  max_val = arr[0]
  for num in arr:
    if num > max_val:
      max_val = num
  return max_val


def counting_sort_by_digit(arr, exp):
  """
  특정 자릿수(exp)를 기준으로 counting sort 수행

  Args:
      arr: 정렬할 배열
      exp: 현재 자릿수 (1, 10, 100, ...)
  """
  n = len(arr)
  output = [0] * n  # 출력 배열
  count = [0] * 10  # 0~9까지 카운트

  # 각 자릿수의 빈도 계산
  for i in range(n):
    digit = (arr[i] // exp) % 10
    count[digit] += 1

  # 누적 카운트로 변경 (위치 정보)
  for i in range(1, 10):
    count[i] += count[i - 1]

  # 뒤에서부터 처리하여 안정성 보장
  for i in range(n - 1, -1, -1):
    digit = (arr[i] // exp) % 10
    output[count[digit] - 1] = arr[i]
    count[digit] -= 1

  # 결과를 원본 배열로 복사
  for i in range(n):
    arr[i] = output[i]


def lsd_radix_sort(arr):
  """
  LSD (Least Significant Digit) Radix Sort 구현

  Args:
      arr: 정렬할 배열

  시간 복잡도: O(d * (n + k))
  공간 복잡도: O(n + k)

  d: 자릿수의 개수
  n: 원소의 개수
  k: 진법 (여기서는 10진법이므로 k=10)
  """
  if not arr or len(arr) <= 1:
    return

  # 최대값 찾기
  max_val = get_max(arr)

  # 각 자릿수에 대해 counting sort 수행
  exp = 1
  while max_val // exp > 0:
    counting_sort_by_digit(arr, exp)

    # 중간 과정 출력 (디버깅용)
    print(f"자릿수 {exp} 정렬 후: {arr}")

    exp *= 10


def test_lsd_radix_sort():
  """테스트 함수"""
  print("=== LSD Radix Sort 테스트 1 ===")
  arr1 = [170, 45, 75, 90, 2, 802, 24, 66]
  print(f"정렬 전: {arr1}")
  lsd_radix_sort(arr1)
  print(f"최종 정렬 후: {arr1}")

  print("\n=== LSD Radix Sort 테스트 2 ===")
  arr2 = [329, 457, 657, 839, 436, 720, 355]
  print(f"정렬 전: {arr2}")
  lsd_radix_sort(arr2)
  print(f"최종 정렬 후: {arr2}")

  print("\n=== 작은 숫자들 테스트 ===")
  arr3 = [9, 5, 1, 8, 3, 7, 2, 6, 4]
  print(f"정렬 전: {arr3}")
  lsd_radix_sort(arr3)
  print(f"최종 정렬 후: {arr3}")

  print("\n=== 중복값 포함 테스트 ===")
  arr4 = [123, 456, 123, 789, 456, 123]
  print(f"정렬 전: {arr4}")
  lsd_radix_sort(arr4)
  print(f"최종 정렬 후: {arr4}")

  print("\n=== 단일 자릿수 테스트 ===")
  arr5 = [4, 2, 7, 1, 9, 3]
  print(f"정렬 전: {arr5}")
  lsd_radix_sort(arr5)
  print(f"최종 정렬 후: {arr5}")

  print("\n=== 0이 포함된 테스트 ===")
  arr6 = [102, 0, 5, 10, 1]
  print(f"정렬 전: {arr6}")
  lsd_radix_sort(arr6)
  print(f"최종 정렬 후: {arr6}")

  print("\n=== 더 큰 숫자들 테스트 ===")
  arr7 = [1234, 5678, 9012, 3456, 7890]
  print(f"정렬 전: {arr7}")
  lsd_radix_sort(arr7)
  print(f"최종 정렬 후: {arr7}")


# 사용 예시
if __name__ == "__main__":
  test_lsd_radix_sort()
