def lis_tab(arr):
  n = len(arr)
  dp = [1] * n  # 각 원소로 끝나는 LIS의 길이

  for i in range(1, n):
    print(f"📊 계산: index {i} (값: {arr[i]})")
    for j in range(i):
      if arr[j] < arr[i]:
        dp[i] = max(dp[i], dp[j] + 1)

  return max(dp)


if __name__ == "__main__":
  arr = [10, 9, 2, 5, 3, 7, 101, 18]
  print(lis_tab(arr))
