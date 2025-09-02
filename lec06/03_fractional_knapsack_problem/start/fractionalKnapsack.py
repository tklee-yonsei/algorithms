# fractionalKnapsack.py
# TODO: 탐욕 알고리즘을 사용하여 분할 배낭 문제를 해결하는 함수를 작성하세요.

def fractional_knapsack(capacity, items):
  """탐욕 알고리즘을 사용하여 분할 배낭 문제를 해결하는 함수"""
  # TODO: 여기에 분할 배낭 알고리즘을 구현하세요
  # 1. 물건들을 단위 무게당 가치 기준으로 내림차순 정렬
  # 2. 가치 밀도가 높은 물건부터 우선적으로 선택
  # 3. 배낭 용량이 부족하면 물건의 일부만 선택 (분할 가능)
  # 4. 선택된 물건들과 총 가치를 반환
  return [], 0


# 사용 예시
if __name__ == "__main__":
  capacity = 15
  items = [(10, 60), (20, 100), (30, 120)]  # (무게, 가치)
  result, max_value = fractional_knapsack(capacity, items)

  print(f"최대 가치: {max_value}")
  for weight, value, fraction in result:
    print(f"무게 {weight}, 가치 {value}, 선택 비율: {fraction:.2f}")
