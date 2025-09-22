def lis_memo(arr):
  def helper(i, prev_idx, memo={}):
    if i == len(arr):
      return 0

    key = (i, prev_idx)
    if key in memo:
      return memo[key]

    # 현재 원소를 포함하지 않는 경우
    exclude = helper(i + 1, prev_idx, memo)

    # 현재 원소를 포함하는 경우
    include = 0
    if prev_idx == -1 or arr[i] > arr[prev_idx]:
      include = 1 + helper(i + 1, i, memo)

    memo[key] = max(include, exclude)
    return memo[key]

  return helper(0, -1)


if __name__ == "__main__":
  arr = [10, 9, 2, 5, 3, 7, 101, 18]
  print(lis_memo(arr))
