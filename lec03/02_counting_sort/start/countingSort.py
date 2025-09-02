# countingSort.py

# TODO: 최대값과 최소값을 찾는 함수를 구현하세요
def find_min_max(arr):
  """최대값과 최소값 찾기"""
  # 여기에 코드를 작성하세요
  # 힌트:
  # 1. 첫 번째 원소로 min_val, max_val 초기화
  # 2. 배열을 순회하며 최소값과 최대값 업데이트
  # 3. min_val, max_val 반환
  return 0, 0


# TODO: 카운팅 정렬 함수를 구현하세요
def counting_sort(arr):
  """
  카운팅 정렬 알고리즘

  Args:
      arr: 정렬할 정수 배열

  Returns:
      정렬된 배열

  시간 복잡도: O(n + k) - n은 원소 개수, k는 값의 범위
  공간 복잡도: O(k) - 카운팅 배열을 위한 공간
  """
  # 여기에 코드를 작성하세요
  # 힌트:
  # 1. 빈 배열 처리
  # 2. 최대값과 최소값 찾기
  # 3. 카운팅 배열 초기화 (범위 크기만큼)
  # 4. 각 원소의 개수 세기
  # 5. 카운팅 배열을 누적합으로 변환
  # 6. 결과 배열에 배치 (뒤에서부터)
  # 7. 정렬된 배열 반환
  return []


# 사용 예시
if __name__ == "__main__":
  # 기본 예시
  print("=== 기본 카운팅 정렬 예시 ===")
  arr1 = [4, 2, 2, 8, 3, 3, 1]
  print(f"정렬 전: {arr1}")
  sorted_arr1 = counting_sort(arr1)
  print(f"정렬 후: {sorted_arr1}")

  print("\n=== 중복값 포함 예시 ===")
  arr2 = [1, 4, 1, 2, 7, 5, 2]
  print(f"정렬 전: {arr2}")
  sorted_arr2 = counting_sort(arr2)
  print(f"정렬 후: {sorted_arr2}")

  print("\n=== 음수 포함 예시 ===")
  arr3 = [-2, 1, -1, 3, 0, 2]
  print(f"정렬 전: {arr3}")
  sorted_arr3 = counting_sort(arr3)
  print(f"정렬 후: {sorted_arr3}")
