# sequentialSearch.py
# TODO: 배열에서 특정 값을 순차적으로 탐색하는 함수를 작성하세요.
def sequential_search(arr, target):
  """순차 탐색 함수"""
  # 여기에 코드를 작성하세요
  return -1


# 사용 예시
if __name__ == "__main__":
  arr = [64, 34, 25, 12, 22, 11, 90]
  target = 22

  result = sequential_search(arr, target)

  if result != -1:
    print(f"값 {target}를 인덱스 {result}에서 찾았습니다.")
  else:
    print(f"값 {target}를 찾을 수 없습니다.")
