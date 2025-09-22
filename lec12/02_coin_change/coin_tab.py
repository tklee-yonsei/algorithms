def coin_tab(amount, coins):
  dp = [float('inf')] * (amount + 1)
  dp[0] = 0

  for i in range(1, amount + 1):
    print(f"📊 계산: 금액 {i}")
    for coin in coins:
      if i >= coin:
        dp[i] = min(dp[i], dp[i - coin] + 1)

  return dp[amount] if dp[amount] != float('inf') else -1


def main():
  print(coin_tab(6, [1, 3, 4]))


if __name__ == "__main__":
  main()
