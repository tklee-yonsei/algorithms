# coinChangeGreedy.py
# TODO: 탐욕 알고리즘을 사용하여 동전 교환 문제를 해결하는 함수를 작성하세요.

def coin_change_greedy(coins, amount):
  """탐욕 알고리즘을 사용하여 동전 교환 문제를 해결하는 함수"""
  # TODO: 여기에 탐욕 알고리즘을 구현하세요
  # 1. 동전을 내림차순으로 정렬
  coins.sort(reverse=True)  # 내림차순 정렬
  # 2. 가장 큰 동전부터 가능한 많이 사용
  # 3. 남은 금액에 대해 다음 큰 동전으로 반복
  return [], 0


# 사용 예시
if __name__ == "__main__":
  coins = [500, 100, 50, 10]
  amount = 1260
  result, count = coin_change_greedy(coins, amount)
  print(f"사용된 동전: {result}")
  print(f"총 동전 개수: {count}")
