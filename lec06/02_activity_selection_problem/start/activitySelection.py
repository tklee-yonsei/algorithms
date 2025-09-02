# activitySelection.py
# TODO: 탐욕 알고리즘을 사용하여 활동 선택 문제를 해결하는 함수를 작성하세요.

def activity_selection(activities):
  """탐욕 알고리즘을 사용하여 활동 선택 문제를 해결하는 함수"""
  # TODO: 여기에 활동 선택 알고리즘을 구현하세요
  # 1. 활동들을 끝나는 시간 기준으로 오름차순 정렬
  # 2. 첫 번째 활동을 선택
  # 3. 나머지 활동들 중에서 이전에 선택한 활동과 겹치지 않는 활동들을 순서대로 선택
  # 4. 선택된 활동들의 리스트를 반환
  return []


# 사용 예시
if __name__ == "__main__":
  activities = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 8), (8, 9)]
  result = activity_selection(activities)
  print(f"선택된 활동들: {result}")
  print(f"선택된 활동 개수: {len(result)}")
