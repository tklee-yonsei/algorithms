# binarySearch.py
# TODO: 정렬된 배열에서 특정 값을 이진 탐색으로 찾는 함수를 작성하세요.
def binary_search(arr, target):
  """이진 탐색 함수"""
  # 여기에 코드를 작성하세요
  # 힌트: left, right, mid 변수를 사용하세요
  return -1


# 사용 예시
if __name__ == "__main__":
  arr = [11, 12, 22, 25, 34, 64, 90]  # 정렬된 배열
  target = 22

  result = binary_search(arr, target)

  if result != -1:
    print(f"값 {target}를 인덱스 {result}에서 찾았습니다.")
  else:
    print(f"값 {target}를 찾을 수 없습니다.")
