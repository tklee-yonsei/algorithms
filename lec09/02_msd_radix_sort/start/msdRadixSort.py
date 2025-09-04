# msdRadixSort.py - MSD Radix Sort (START CODE)

RADIX = 10


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


def counting_sort_by_digit_msd(arr, start, end, exp):
  """
  TODO: MSD용 카운팅 정렬 함수 (특정 자릿수 기준)

  Args:
      arr: 정렬할 배열
      start: 정렬 범위 시작 인덱스
      end: 정렬 범위 끝 인덱스
      exp: 현재 자릿수

  Returns:
      각 버킷의 크기를 담은 리스트
  """
  # TODO: MSD용 카운팅 정렬을 구현하세요
  # 힌트:
  # 1. n = end - start + 1 계산
  # 2. output = [0] * n, count = [0] * RADIX 선언
  # 3. 현재 자릿수에 대한 빈도 계산: digit = (arr[i] // exp) % RADIX
  # 4. bucket_sizes = count[:] 로 버킷 크기 저장
  # 5. 누적 카운트로 변경 (위치 정보 생성)
  # 6. 뒤에서부터 처리하여 안정성 보장
  # 7. 결과를 원본 배열의 해당 구간으로 복사
  # 8. bucket_sizes 반환

  print(f"  counting_sort_by_digit_msd 구현 필요 (start={start}, end={end}, exp={exp})")
  return [0] * RADIX  # 임시 반환값


def msd_radix_sort_recursive(arr, start, end, exp):
  """
  TODO: MSD Radix Sort 재귀 함수

  Args:
      arr: 정렬할 배열
      start: 정렬 범위 시작 인덱스
      end: 정렬 범위 끝 인덱스
      exp: 현재 자릿수 (가장 높은 자릿수부터 시작)
  """
  # TODO: MSD Radix Sort 재귀 함수를 구현하세요
  # 힌트:
  # 1. 기저 조건 확인 (start >= end or exp <= 0)
  # 2. counting_sort_by_digit_msd 호출하여 bucket_sizes 받기
  # 3. 중간 과정 출력 (디버깅용)
  # 4. 각 버킷에 대해 재귀적으로 정렬:
  #    - current_start부터 시작
  #    - bucket_sizes[i] > 1인 경우만 재귀 호출
  #    - 다음 자릿수로 (exp // RADIX)
  #    - current_start += bucket_sizes[i]로 업데이트

  print(f"msd_radix_sort_recursive 구현 필요 (start={start}, end={end}, exp={exp})")


def msd_radix_sort(arr):
  """
  MSD (Most Significant Digit) Radix Sort 구현 (완성됨)

  Args:
      arr: 정렬할 배열

  시간 복잡도: O(d * (n + k)) (평균), O(n^2) (최악)
  공간 복잡도: O(n + k)

  d: 자릿수의 개수
  n: 원소의 개수
  k: 진법 (여기서는 10진법이므로 k=10)
  """
  if not arr or len(arr) <= 1:
    return

  # 최대값 찾기
  max_val = get_max(arr)

  # 최대 자릿수 계산
  max_exp = 1
  while max_val // max_exp >= 10:
    max_exp *= 10

  print(f"최대값: {max_val}, 최대 자릿수: {max_exp}")

  # 가장 높은 자릿수부터 시작하여 재귀적으로 정렬
  msd_radix_sort_recursive(arr, 0, len(arr) - 1, max_exp)


def test_msd_radix_sort():
  """테스트 함수 (완성됨)"""
  print("=== MSD Radix Sort 테스트 1 ===")
  arr1 = [170, 45, 75, 90, 2, 802, 24, 66]
  print(f"정렬 전: {arr1}")
  msd_radix_sort(arr1)
  print(f"최종 정렬 후: {arr1}")

  print("\n=== MSD Radix Sort 테스트 2 ===")
  arr2 = [329, 457, 657, 839, 436, 720, 355]
  print(f"정렬 전: {arr2}")
  msd_radix_sort(arr2)
  print(f"최종 정렬 후: {arr2}")

  print("\n=== 작은 숫자들 테스트 ===")
  arr3 = [9, 5, 1, 8, 3, 7, 2, 6, 4]
  print(f"정렬 전: {arr3}")
  msd_radix_sort(arr3)
  print(f"최종 정렬 후: {arr3}")

  print("\n=== 중복값 포함 테스트 ===")
  arr4 = [123, 456, 123, 789, 456, 123]
  print(f"정렬 전: {arr4}")
  msd_radix_sort(arr4)
  print(f"최종 정렬 후: {arr4}")

  print("\n=== 단일 자릿수 테스트 ===")
  arr5 = [4, 2, 7, 1, 9, 3]
  print(f"정렬 전: {arr5}")
  msd_radix_sort(arr5)
  print(f"최종 정렬 후: {arr5}")

  print("\n=== 빈 배열 및 특수 케이스 ===")
  arr6 = []
  print(f"빈 배열: {arr6}")
  msd_radix_sort(arr6)
  print(f"정렬 후: {arr6}")

  arr7 = [42]
  print(f"단일 원소: {arr7}")
  msd_radix_sort(arr7)
  print(f"정렬 후: {arr7}")

  print("\n=== 큰 숫자들 테스트 ===")
  arr8 = [9999, 1000, 5555, 3333, 7777, 1111]
  print(f"정렬 전: {arr8}")
  msd_radix_sort(arr8)
  print(f"최종 정렬 후: {arr8}")

  print("\n=== 역순 정렬 테스트 ===")
  arr9 = [987, 654, 321, 111]
  print(f"정렬 전: {arr9}")
  msd_radix_sort(arr9)
  print(f"최종 정렬 후: {arr9}")


# 메인 실행 (완성됨)
if __name__ == "__main__":
  test_msd_radix_sort()
