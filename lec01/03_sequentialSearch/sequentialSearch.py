# sequentialSearch.py
def sequential_search(arr, target):
  """순차 탐색 함수"""
  for i in range(len(arr)):
    if arr[i] == target:
      return i  # 찾은 인덱스 반환
  return -1  # 찾지 못한 경우


# 사용 예시
if __name__ == "__main__":
  arr = [64, 34, 25, 12, 22, 11, 90]
  target = 22

  result = sequential_search(arr, target)

  if result != -1:
    print(f"값 {target}를 인덱스 {result}에서 찾았습니다.")
  else:
    print(f"값 {target}를 찾을 수 없습니다.")
