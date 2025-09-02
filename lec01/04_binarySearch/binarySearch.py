# binarySearch.py
def binary_search(arr, target):
  """이진 탐색 함수"""
  left = 0
  right = len(arr) - 1

  while left <= right:
    mid = left + (right - left) // 2  # 정수 나눗셈

    if arr[mid] == target:
      return mid  # 찾은 인덱스 반환
    elif arr[mid] < target:
      left = mid + 1  # 오른쪽 절반 탐색
    else:
      right = mid - 1  # 왼쪽 절반 탐색

  return -1  # 찾지 못한 경우


# 사용 예시
if __name__ == "__main__":
  arr = [11, 12, 22, 25, 34, 64, 90]  # 정렬된 배열
  target = 22

  result = binary_search(arr, target)

  if result != -1:
    print(f"값 {target}를 인덱스 {result}에서 찾았습니다.")
  else:
    print(f"값 {target}를 찾을 수 없습니다.")
