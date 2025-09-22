def fib_tab(n):
  if n <= 1:
    return n

  dp = [0] * (n + 1)
  dp[1] = 1

  for i in range(2, n + 1):
    print(f"📊 Tab 계산: F({i})")
    dp[i] = dp[i-1] + dp[i-2]

  return dp[n]


def main():
  print(fib_tab(6))


if __name__ == "__main__":
  main()
