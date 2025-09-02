# coinChangeGreedy.py

def coin_change_greedy(coins, amount):
  """탐욕 알고리즘을 사용하여 동전 교환 문제를 해결하는 함수"""
  coins.sort(reverse=True)  # 내림차순 정렬
  result = []

  for coin in coins:
    count = amount // coin
    if count > 0:
      result.extend([coin] * count)
      amount %= coin

  return result, len(result)


# 사용 예시
if __name__ == "__main__":
  coins = [500, 100, 50, 10]
  amount = 1260
  result, count = coin_change_greedy(coins, amount)
  print(f"사용된 동전: {result}")
  print(f"총 동전 개수: {count}")

  # 추가 테스트 케이스
  print("\n--- 추가 테스트 케이스 ---")
  test_cases = [
      ([500, 100, 50, 10], 380),
      ([500, 100, 50, 10], 1000),
      ([1, 5, 10, 25], 67)
  ]

  for coins_test, amount_test in test_cases:
    result_test, count_test = coin_change_greedy(coins_test.copy(), amount_test)
    print(f"동전: {coins_test}, 금액: {amount_test} -> 사용된 동전: {result_test}, 개수: {count_test}")
