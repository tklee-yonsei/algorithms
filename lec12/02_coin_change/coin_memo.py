def coin_memo(amount, coins, memo={}):
  if amount == 0:
    return 0
  if amount < 0:
    return float('inf')

  if amount in memo:
    return memo[amount]

  print(f"💭 계산: 금액 {amount}")

  min_coins = float('inf')
  for coin in coins:
    result = coin_memo(amount - coin, coins, memo)
    if result != float('inf'):
      min_coins = min(min_coins, result + 1)

  memo[amount] = min_coins
  return min_coins


def main():
  print(coin_memo(6, [1, 3, 4]))


if __name__ == "__main__":
  main()
