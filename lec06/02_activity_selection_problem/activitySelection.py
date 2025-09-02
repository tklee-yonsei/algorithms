# activitySelection.py

def activity_selection(activities):
  """탐욕 알고리즘을 사용하여 활동 선택 문제를 해결하는 함수"""
  # 끝나는 시간으로 정렬
  activities.sort(key=lambda x: x[1])

  selected = [activities[0]]  # 첫 번째 활동 선택
  last_end_time = activities[0][1]

  for i in range(1, len(activities)):
    start_time, end_time = activities[i]
    if start_time >= last_end_time:  # 겹치지 않으면
      selected.append(activities[i])
      last_end_time = end_time

  return selected


# 사용 예시
if __name__ == "__main__":
  activities = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 8), (8, 9)]
  result = activity_selection(activities)
  print(f"선택된 활동들: {result}")
  print(f"선택된 활동 개수: {len(result)}")

  # 추가 테스트 케이스
  print("\n--- 추가 테스트 케이스 ---")
  test_cases = [
      [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9),
       (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)],
      [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)],
      [(0, 5), (1, 2), (3, 4)]
  ]

  for i, test_activities in enumerate(test_cases, 1):
    result_test = activity_selection(test_activities.copy())
    print(f"테스트 {i}: {test_activities}")
    print(f"선택된 활동: {result_test}, 개수: {len(result_test)}")
    print()
