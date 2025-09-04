# lsdRadixSort.py - LSD Radix Sort (START CODE)

def get_max(arr):
  """
  배열에서 최대값 찾기 (완성됨)

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
  TODO: 특정 자릿수(exp)를 기준으로 counting sort 수행

  Args:
      arr: 정렬할 배열
      exp: 현재 자릿수 (1, 10, 100, ...)
  """
  # TODO: Counting sort를 구현하세요
  # 힌트:
  # 1. n = len(arr), output = [0] * n, count = [0] * 10 선언
  # 2. 각 자릿수의 빈도 계산: digit = (arr[i] // exp) % 10
  # 3. 누적 카운트로 변경 (위치 정보 생성)
  # 4. 뒤에서부터 처리하여 안정성 보장
  # 5. 결과를 원본 배열로 복사

  print(f"  counting_sort_by_digit 구현 필요 (exp = {exp})")


def lsd_radix_sort(arr):
  """
  TODO: LSD (Least Significant Digit) Radix Sort 구현

  Args:
      arr: 정렬할 배열

  시간 복잡도: O(d * (n + k))
  공간 복잡도: O(n + k)

  d: 자릿수의 개수
  n: 원소의 개수
  k: 진법 (여기서는 10진법이므로 k=10)
  """
  # TODO: LSD Radix Sort를 구현하세요
  # 힌트:
  # 1. 빈 배열이나 원소가 1개 이하면 early return
  # 2. get_max()를 사용해서 최대값 찾기
  # 3. exp = 1부터 시작해서 최고 자릿수까지 반복
  # 4. 각 자릿수에 대해 counting_sort_by_digit 호출
  # 5. 중간 과정 출력 (디버깅용)
  # 6. exp *= 10으로 다음 자릿수로 이동

  print("lsd_radix_sort 구현 필요")


def test_lsd_radix_sort():
  """테스트 함수 (완성됨)"""
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

  print("\n=== 빈 배열 및 특수 케이스 ===")
  arr6 = []
  print(f"빈 배열: {arr6}")
  lsd_radix_sort(arr6)
  print(f"정렬 후: {arr6}")

  arr7 = [42]
  print(f"단일 원소: {arr7}")
  lsd_radix_sort(arr7)
  print(f"정렬 후: {arr7}")

  print("\n=== 큰 숫자들 테스트 ===")
  arr8 = [9999, 1000, 5555, 3333, 7777, 1111]
  print(f"정렬 전: {arr8}")
  lsd_radix_sort(arr8)
  print(f"최종 정렬 후: {arr8}")


# 메인 실행 (완성됨)
if __name__ == "__main__":
  test_lsd_radix_sort()
