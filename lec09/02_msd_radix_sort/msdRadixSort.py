# msdRadixSort.py

RADIX = 10


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


def counting_sort_by_digit_msd(arr, start, end, exp):
  """
  MSD용 카운팅 정렬 함수 (특정 자릿수 기준)

  Args:
      arr: 정렬할 배열
      start: 정렬 범위 시작 인덱스
      end: 정렬 범위 끝 인덱스
      exp: 현재 자릿수

  Returns:
      각 버킷의 크기를 담은 리스트
  """
  n = end - start + 1
  output = [0] * n
  count = [0] * RADIX

  # 현재 자릿수(exp)에 대한 각 자릿수의 빈도 계산
  for i in range(start, end + 1):
    digit = (arr[i] // exp) % RADIX
    count[digit] += 1

  # 버킷 크기 저장 (재귀 호출을 위해)
  bucket_sizes = count[:]

  # 누적 카운트로 변경 (위치 정보 생성)
  for i in range(1, RADIX):
    count[i] += count[i - 1]

  # 뒤에서부터 처리하여 안정성 보장
  for i in range(end, start - 1, -1):
    digit = (arr[i] // exp) % RADIX
    output[count[digit] - 1] = arr[i]
    count[digit] -= 1

  # 결과를 원본 배열의 해당 구간으로 복사
  for i in range(n):
    arr[start + i] = output[i]

  return bucket_sizes


def msd_radix_sort_recursive(arr, start, end, exp):
  """
  MSD Radix Sort 재귀 함수

  Args:
      arr: 정렬할 배열
      start: 정렬 범위 시작 인덱스
      end: 정렬 범위 끝 인덱스
      exp: 현재 자릿수 (가장 높은 자릿수부터 시작)
  """
  if start >= end or exp <= 0:
    return

  # 현재 자릿수에 대해 카운팅 정렬 수행
  bucket_sizes = counting_sort_by_digit_msd(arr, start, end, exp)

  # 중간 과정 출력 (디버깅용)
  print(f"자릿수 {exp} 정렬 후 ({start}~{end}): {arr[start:end+1]}")

  # 각 버킷에 대해 재귀적으로 정렬
  current_start = start
  for i in range(RADIX):
    if bucket_sizes[i] > 1:
      msd_radix_sort_recursive(arr, current_start,
                               current_start + bucket_sizes[i] - 1,
                               exp // RADIX)
    current_start += bucket_sizes[i]


def msd_radix_sort(arr):
  """
  MSD (Most Significant Digit) Radix Sort 구현

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

  # 최대 자릿수의 exp 값 계산
  exp = 1
  while max_val // exp >= RADIX:
    exp *= RADIX

  msd_radix_sort_recursive(arr, 0, len(arr) - 1, exp)


def test_msd_radix_sort():
  """테스트 함수"""
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

  print("\n=== 큰 숫자들 테스트 ===")
  arr4 = [1234, 5678, 9012, 3456, 7890]
  print(f"정렬 전: {arr4}")
  msd_radix_sort(arr4)
  print(f"최종 정렬 후: {arr4}")

  print("\n=== 중복값 포함 테스트 ===")
  arr5 = [123, 456, 123, 789, 456, 123]
  print(f"정렬 전: {arr5}")
  msd_radix_sort(arr5)
  print(f"최종 정렬 후: {arr5}")

  print("\n=== 다양한 자릿수 테스트 ===")
  arr6 = [5, 50, 500, 5000, 55, 555]
  print(f"정렬 전: {arr6}")
  msd_radix_sort(arr6)
  print(f"최종 정렬 후: {arr6}")

  print("\n=== 0이 포함된 테스트 ===")
  arr7 = [102, 0, 5, 10, 1]
  print(f"정렬 전: {arr7}")
  msd_radix_sort(arr7)
  print(f"최종 정렬 후: {arr7}")

  print("\n=== 더 복잡한 테스트 ===")
  arr8 = [3141, 592, 6535, 897, 932, 384, 626, 433]
  print(f"정렬 전: {arr8}")
  msd_radix_sort(arr8)
  print(f"최종 정렬 후: {arr8}")

  print("\n=== 단일 자릿수와 다중 자릿수 혼합 ===")
  arr9 = [1, 23, 456, 7, 89, 1234]
  print(f"정렬 전: {arr9}")
  msd_radix_sort(arr9)
  print(f"최종 정렬 후: {arr9}")


# 사용 예시
if __name__ == "__main__":
  test_msd_radix_sort()
