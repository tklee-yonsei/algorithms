# fractionalKnapsack.py

def fractional_knapsack(capacity, items):
  """탐욕 알고리즘을 사용하여 분할 배낭 문제를 해결하는 함수"""
  # 단위 무게당 가치로 정렬 (내림차순)
  items.sort(key=lambda x: x[1]/x[0], reverse=True)

  total_value = 0
  selected = []

  for weight, value in items:
    if capacity >= weight:
      # 물건 전체를 가져갈 수 있는 경우
      selected.append((weight, value, 1.0))  # 100% 선택
      total_value += value
      capacity -= weight
    else:
      # 물건의 일부만 가져갈 수 있는 경우
      fraction = capacity / weight
      selected.append((weight, value, fraction))
      total_value += value * fraction
      break

  return selected, total_value


# 사용 예시
if __name__ == "__main__":
  capacity = 15
  items = [(10, 60), (20, 100), (30, 120)]  # (무게, 가치)
  result, max_value = fractional_knapsack(capacity, items)

  print(f"최대 가치: {max_value}")
  for weight, value, fraction in result:
    print(f"무게 {weight}, 가치 {value}, 선택 비율: {fraction:.2f}")

  # 추가 테스트 케이스
  print("\n--- 추가 테스트 케이스 ---")
  test_cases = [
      (50, [(10, 60), (20, 100), (30, 120)]),
      (25, [(15, 20), (10, 30), (5, 40)]),
      (7, [(2, 1), (3, 4), (5, 7), (1, 1)])
  ]

  for i, (cap, test_items) in enumerate(test_cases, 1):
    result_test, max_value_test = fractional_knapsack(cap, test_items.copy())
    print(f"\n테스트 {i}: 용량 {cap}, 물건들 {test_items}")
    print(f"최대 가치: {max_value_test:.2f}")
    for weight, value, fraction in result_test:
      print(f"  무게 {weight}, 가치 {value}, 선택 비율: {fraction:.2f}")
