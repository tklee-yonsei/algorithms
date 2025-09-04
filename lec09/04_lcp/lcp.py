# lcp.py

def compute_lcp(s, i, j):
  """
  두 위치의 LCP (Longest Common Prefix) 계산

  Args:
      s: 문자열
      i: 첫 번째 위치
      j: 두 번째 위치

  Returns:
      LCP 길이
  """
  lcp = 0
  n = len(s)
  while (i + lcp < n and j + lcp < n and
         s[i + lcp] == s[j + lcp]):
    lcp += 1
  return lcp


def compute_all_lcp(s, positions):
  """
  주어진 모든 위치 쌍에 대해 LCP 계산

  Args:
      s: 문자열
      positions: 위치 리스트

  Returns:
      2차원 LCP 매트릭스
  """
  n = len(s)
  pos_count = len(positions)
  results = []

  for i in range(pos_count):
    row = []
    for j in range(pos_count):
      if i != j:
        lcp = compute_lcp(s, positions[i], positions[j])
        row.append(lcp)
      else:
        # 자기 자신과의 LCP는 남은 문자열 길이
        row.append(n - positions[i])
    results.append(row)

  return results


def find_max_lcp(s, positions):
  """
  모든 위치 쌍 중 최대 LCP 찾기

  Args:
      s: 문자열
      positions: 위치 리스트

  Returns:
      (최대 LCP 길이, 첫 번째 위치, 두 번째 위치) 튜플
  """
  max_lcp = 0
  best_i = -1
  best_j = -1

  for i in range(len(positions)):
    for j in range(i + 1, len(positions)):
      current_lcp = compute_lcp(s, positions[i], positions[j])
      if current_lcp > max_lcp:
        max_lcp = current_lcp
        best_i = positions[i]
        best_j = positions[j]

  return max_lcp, best_i, best_j


def build_lcp_kasai(text, sa):
  """
  Suffix Array로부터 LCP 배열 구축 (Kasai 알고리즘)

  Args:
      text: 문자열
      sa: suffix array

  Returns:
      LCP 배열
  """
  n = len(text)
  lcp = [0] * n
  rank = [0] * n

  # Step 1: SA의 역함수 구성
  for i in range(n):
    rank[sa[i]] = i

  h = 0  # 현재 LCP 길이
  lcp[0] = 0

  # Step 2: 텍스트 순서로 각 suffix 처리
  for i in range(n):
    if rank[i] > 0:
      j = sa[rank[i] - 1]  # 이전 suffix의 시작 위치

      # h값부터 시작하여 공통 접두사 길이 계산
      while (i + h < n and j + h < n and
             text[i + h] == text[j + h]):
        h += 1

      lcp[rank[i]] = h

      # 다음 iteration을 위해 h를 1 감소
      if h > 0:
        h -= 1

  return lcp


def print_lcp_comparison(s, i, j, lcp):
  """
  LCP 비교 결과 출력

  Args:
      s: 문자열
      i: 첫 번째 위치
      j: 두 번째 위치
      lcp: LCP 길이
  """
  print(f"위치 {i}: {s[i:]}")
  print(f"위치 {j}: {s[j:]}")
  print(f"LCP 길이: {lcp}")
  if lcp > 0:
    print(f"공통 접두사: {s[i:i+lcp]}")
  else:
    print("공통 접두사: 없음")


def print_lcp_matrix(matrix, positions):
  """
  LCP 매트릭스 출력

  Args:
      matrix: LCP 매트릭스
      positions: 위치 리스트
  """
  print("LCP 매트릭스:")
  print("    ", end="")
  for j in range(len(positions)):
    print(f"{j:3d}", end="")
  print()

  for i in range(len(positions)):
    print(f"{i:2d}: ", end="")
    for j in range(len(positions)):
      print(f"{matrix[i][j]:3d}", end="")
    print()


def test_lcp():
  """테스트 함수"""
  print("=== LCP 계산 테스트 ===\n")

  # 테스트 케이스 1: 기본 LCP 계산
  print("=== LCP 계산 테스트 1 ===")
  text1 = "banana"
  print(f"문자열: {text1}\n")

  # 몇 가지 위치 쌍에 대해 LCP 계산
  pairs = [(0, 1), (0, 3), (1, 3), (2, 4)]

  for i, j in pairs:
    lcp = compute_lcp(text1, i, j)
    print_lcp_comparison(text1, i, j, lcp)
    print()

  # 테스트 케이스 2: 반복 패턴에서 최대 LCP 찾기
  print("=== LCP 계산 테스트 2 ===")
  text2 = "abcabcab"
  print(f"문자열: {text2}")

  positions = [0, 1, 2, 3, 4, 5]
  max_lcp, best_i, best_j = find_max_lcp(text2, positions)

  print(f"최대 LCP: {max_lcp} (위치 {best_i}와 {best_j})")
  if max_lcp > 0:
    print(f"공통 접두사: {text2[best_i:best_i+max_lcp]}")
  print()

  # 테스트 케이스 3: Suffix Array와 LCP 배열
  print("=== Suffix Array와 LCP 배열 테스트 ===")
  text3 = "mississippi"
  print(f"문자열: {text3}")

  # 미리 계산된 suffix array (실제로는 다른 알고리즘으로 구축)
  suffix_array3 = [10, 7, 4, 1, 0, 9, 8, 6, 3, 5, 2]
  lcp_array3 = build_lcp_kasai(text3, suffix_array3)

  print(f"Suffix Array: {suffix_array3}")
  print(f"LCP Array: {lcp_array3}")
  print()

  # LCP 배열의 각 값이 의미하는 바 설명
  print("LCP 배열 상세 분석:")
  for i in range(1, len(text3)):
    pos1 = suffix_array3[i-1]
    pos2 = suffix_array3[i]
    print(f"SA[{i-1}] = {pos1}, SA[{i}] = {pos2}")
    print(f"LCP[{i}] = {lcp_array3[i]}")
    if lcp_array3[i] > 0:
      print(f"공통 접두사: {text3[pos1:pos1+lcp_array3[i]]}")
    print(f"suffix[{pos1}]: {text3[pos1:]}")
    print(f"suffix[{pos2}]: {text3[pos2:]}")
    print()

  # 테스트 케이스 4: 모든 LCP 매트릭스
  print("=== 모든 위치 쌍 LCP 매트릭스 ===")
  text4 = "ababa"
  print(f"문자열: {text4}")

  positions4 = [0, 1, 2, 3, 4]
  results = compute_all_lcp(text4, positions4)

  print_lcp_matrix(results, positions4)
  print()

  # 테스트 케이스 5: 특별한 경우들
  print("=== 특별한 경우들 테스트 ===")

  # 완전히 같은 문자열
  text5 = "aaaa"
  print(f"문자열: {text5}")
  lcp_same = compute_lcp(text5, 0, 1)
  print(f"위치 0과 1의 LCP: {lcp_same}")

  # 완전히 다른 문자열
  text6 = "abcd"
  lcp_diff = compute_lcp(text6, 0, 1)
  print(f"'{text6}'에서 위치 0과 1의 LCP: {lcp_diff}")

  # 한 suffix가 다른 suffix의 접두사인 경우
  text7 = "abcabc"
  lcp_prefix = compute_lcp(text7, 0, 3)
  print(f"'{text7}'에서 위치 0과 3의 LCP: {lcp_prefix}")
  print()

  # 테스트 케이스 6: 성능 비교 (작은 규모)
  print("=== 다양한 패턴에서의 LCP ===")
  test_strings = [
      "abcdefg",
      "ababab",
      "aaaaaa",
      "abcdcba",
      "mississippi"
  ]

  for text in test_strings:
    print(f"문자열: '{text}'")
    positions = list(range(min(4, len(text))))  # 처음 4개 위치만
    max_lcp, best_i, best_j = find_max_lcp(text, positions)
    print(f"  최대 LCP: {max_lcp}", end="")
    if max_lcp > 0:
      print(f" (위치 {best_i}와 {best_j}: '{text[best_i:best_i+max_lcp]}')")
    else:
      print(" (공통 접두사 없음)")


# 사용 예시
if __name__ == "__main__":
  test_lcp()
