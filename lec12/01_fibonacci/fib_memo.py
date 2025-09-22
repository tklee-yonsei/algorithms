def fib_memo(n, memo={}):
  if n <= 1:
    return n

  if n in memo:
    return memo[n]

  print(f"💭 Memo 계산: F({n})")
  memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
  return memo[n]


def main():
  print(fib_memo(6))


if __name__ == "__main__":
  main()
