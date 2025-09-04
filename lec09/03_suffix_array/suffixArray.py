# suffixArray.py

class SuffixEntry:
  """Naive 방법용 클래스"""

  def __init__(self, index, suffix):
    self.index = index
    self.suffix = suffix

  def __lt__(self, other):
    return self.suffix < other.suffix


class SuffixRank:
  """Doubling 알고리즘용 클래스"""

  def __init__(self, rank0, rank1, index):
    self.rank = [rank0, rank1]
    self.index = index

  def __lt__(self, other):
    if self.rank[0] != other.rank[0]:
      return self.rank[0] < other.rank[0]
    return self.rank[1] < other.rank[1]


def build_suffix_array_naive(text):
  """
  Naive 방법으로 Suffix Array 구축

  Args:
      text: 입력 문자열

  Returns:
      suffix array 리스트

  시간 복잡도: O(n^2 log n)
  공간 복잡도: O(n)
  """
  n = len(text)
  suffixes = []

  # 모든 suffix 생성
  for i in range(n):
    suffixes.append(SuffixEntry(i, text[i:]))

  # 사전순 정렬
  suffixes.sort()

  # 결과를 suffix array로 반환
  return [suffix.index for suffix in suffixes]


def build_suffix_array_doubling(text):
  """
  Doubling 알고리즘으로 Suffix Array 구축

  Args:
      text: 입력 문자열

  Returns:
      suffix array 리스트

  시간 복잡도: O(n log^2 n)
  공간 복잡도: O(n)
  """
  n = len(text)
  suffixes = []

  # 초기 rank 설정 (각 문자)
  for i in range(n):
    rank0 = ord(text[i])
    rank1 = ord(text[i + 1]) if i + 1 < n else -1
    suffixes.append(SuffixRank(rank0, rank1, i))

  # 정렬
  suffixes.sort()

  # 각 단계마다 길이를 2배씩 증가
  k = 4
  while k < 2 * n:
    # 새로운 rank 할당
    rank = 0
    prev_rank0 = suffixes[0].rank[0]
    prev_rank1 = suffixes[0].rank[1]
    suffixes[0].rank[0] = rank

    index = [0] * n
    index[suffixes[0].index] = 0

    for i in range(1, n):
      if (suffixes[i].rank[0] != prev_rank0 or
              suffixes[i].rank[1] != prev_rank1):
        rank += 1

      prev_rank0 = suffixes[i].rank[0]
      prev_rank1 = suffixes[i].rank[1]
      suffixes[i].rank[0] = rank
      index[suffixes[i].index] = i

    # 다음 위치의 rank 업데이트
    for i in range(n):
      next_index = suffixes[i].index + k // 2
      suffixes[i].rank[1] = (suffixes[index[next_index]].rank[0]
                             if next_index < n else -1)

    # 다시 정렬
    suffixes.sort()

    k *= 2

  # 최종 suffix array 생성
  return [suffix.index for suffix in suffixes]


def print_suffix_array(text, suffix_array):
  """
  Suffix Array 출력 함수

  Args:
      text: 원본 문자열
      suffix_array: suffix array
  """
  print("Index\tSuffix")
  print("-----\t------")
  for i, idx in enumerate(suffix_array):
    print(f"{idx}\t{text[idx:]}")


def search_pattern(text, suffix_array, pattern):
  """
  패턴 검색 함수 (이진 탐색 사용)

  Args:
      text: 원본 문자열
      suffix_array: suffix array
      pattern: 검색할 패턴

  Returns:
      패턴이 발견된 위치, 없으면 -1
  """
  left = 0
  right = len(suffix_array) - 1
  pattern_len = len(pattern)

  while left <= right:
    mid = (left + right) // 2
    suffix = text[suffix_array[mid]:]

    # 패턴 길이만큼만 비교
    suffix_prefix = suffix[:pattern_len] if len(suffix) >= pattern_len else suffix

    if pattern == suffix_prefix:
      return suffix_array[mid]  # 패턴 발견
    elif pattern < suffix_prefix:
      right = mid - 1
    else:
      left = mid + 1

  return -1  # 패턴을 찾지 못함


def compute_lcp(text, i, j):
  """
  두 위치의 LCP (Longest Common Prefix) 계산

  Args:
      text: 원본 문자열
      i: 첫 번째 위치
      j: 두 번째 위치

  Returns:
      LCP 길이
  """
  lcp = 0
  n = len(text)
  while (i + lcp < n and j + lcp < n and
         text[i + lcp] == text[j + lcp]):
    lcp += 1
  return lcp


def build_lcp_array(text, suffix_array):
  """
  LCP 배열 구축 (Kasai 알고리즘)

  Args:
      text: 원본 문자열
      suffix_array: suffix array

  Returns:
      LCP 배열
  """
  n = len(text)
  lcp_array = [0] * n
  rank = [0] * n

  # suffix array의 역순 배열 생성
  for i in range(n):
    rank[suffix_array[i]] = i

  h = 0
  for i in range(n):
    if rank[i] > 0:
      j = suffix_array[rank[i] - 1]
      while (i + h < n and j + h < n and
             text[i + h] == text[j + h]):
        h += 1
      lcp_array[rank[i]] = h
      if h > 0:
        h -= 1

  return lcp_array


def search_pattern_advanced(text, suffix_array, pattern):
  """
  고급 패턴 검색 함수 (더 효율적인 버전)

  Args:
      text: 원본 문자열
      suffix_array: suffix array
      pattern: 검색할 패턴

  Returns:
      패턴이 발견된 위치, 없으면 -1
  """
  left, right = 0, len(suffix_array) - 1
  m = len(pattern)

  while left <= right:
    mid = (left + right) // 2
    suffix = text[suffix_array[mid]:]

    # 패턴 길이만큼만 비교
    suffix_prefix = suffix[:m] if len(suffix) >= m else suffix

    if pattern == suffix_prefix:
      return suffix_array[mid]  # 패턴 찾음
    elif pattern > suffix_prefix:
      left = mid + 1
    else:
      right = mid - 1

  return -1  # 패턴 없음


def find_all_patterns(text, suffix_array, pattern):
  """
  패턴의 모든 출현 위치를 찾는 함수 (개선된 버전)

  Args:
      text: 원본 문자열
      suffix_array: suffix array
      pattern: 검색할 패턴

  Returns:
      패턴이 발견된 모든 위치의 리스트
  """
  results = []
  n = len(suffix_array)
  m = len(pattern)

  # 첫 번째 출현 위치 찾기
  left, right = 0, n - 1
  first = -1

  # 이진 탐색으로 첫 번째 출현 위치 찾기
  while left <= right:
    mid = (left + right) // 2
    suffix = text[suffix_array[mid]:]
    suffix_prefix = suffix[:m] if len(suffix) >= m else suffix

    if suffix_prefix >= pattern:
      if suffix_prefix == pattern:
        first = mid
      right = mid - 1
    else:
      left = mid + 1

  if first == -1:
    return results

  # 첫 번째 위치부터 연속된 모든 출현 위치 찾기
  for i in range(first, n):
    suffix = text[suffix_array[i]:]
    if suffix.startswith(pattern):
      results.append(suffix_array[i])
    else:
      break

  return sorted(results)


def find_longest_repeated_substring(text, suffix_array, lcp_array):
  """
  가장 긴 반복 부분 문자열 찾기

  Args:
      text: 원본 문자열
      suffix_array: suffix array
      lcp_array: LCP 배열

  Returns:
      (시작 위치, 길이) 튜플
  """
  max_lcp = max(lcp_array[1:]) if len(lcp_array) > 1 else 0
  if max_lcp == 0:
    return (-1, 0)

  for i in range(1, len(lcp_array)):
    if lcp_array[i] == max_lcp:
      return (suffix_array[i], max_lcp)

  return (-1, 0)


def find_all_occurrences(text, suffix_array, pattern):
  """
  패턴의 모든 출현 위치를 찾는 함수 (기존 버전 유지)

  Args:
      text: 원본 문자열
      suffix_array: suffix array
      pattern: 검색할 패턴

  Returns:
      패턴이 발견된 모든 위치의 리스트
  """
  return find_all_patterns(text, suffix_array, pattern)


def test_suffix_array():
  """테스트 함수"""
  print("=== Suffix Array 테스트 ===\n")

  # 테스트 케이스 1: Naive 방법
  print("=== Naive 방법 테스트 ===")
  text1 = "banana"
  print(f"문자열: {text1}")
  suffix_array1 = build_suffix_array_naive(text1)
  print_suffix_array(text1, suffix_array1)

  # 테스트 케이스 2: Doubling 알고리즘
  print("\n=== Doubling 알고리즘 테스트 ===")
  text2 = "abcdef"
  print(f"문자열: {text2}")
  suffix_array2 = build_suffix_array_doubling(text2)
  print_suffix_array(text2, suffix_array2)

  # 테스트 케이스 3: 복잡한 문자열
  print("\n=== 복잡한 문자열 테스트 ===")
  text3 = "mississippi"
  print(f"문자열: {text3}")
  suffix_array3 = build_suffix_array_doubling(text3)
  print_suffix_array(text3, suffix_array3)

  # 테스트 케이스 4: 패턴 검색
  print("\n=== 패턴 검색 테스트 ===")
  patterns = ["iss", "ana", "xyz"]

  for pattern in patterns:
    result1 = search_pattern(text3, suffix_array3, pattern)
    result2 = search_pattern(text1, suffix_array1, pattern)

    print(f"패턴 '{pattern}':")
    if result1 != -1:
      print(f"  '{text3}'에서 위치 {result1}에서 발견")
    if result2 != -1:
      print(f"  '{text1}'에서 위치 {result2}에서 발견")
    if result1 == -1 and result2 == -1:
      print(f"  찾을 수 없음")

  # 테스트 케이스 5: 모든 출현 위치 찾기
  print("\n=== 모든 출현 위치 찾기 테스트 ===")
  pattern = "is"
  all_occurrences = find_all_occurrences(text3, suffix_array3, pattern)
  print(f"패턴 '{pattern}'의 모든 출현 위치: {all_occurrences}")

  # 테스트 케이스 6: 반복 문자
  print("\n=== 반복 문자 테스트 ===")
  text4 = "aaaa"
  print(f"문자열: {text4}")
  suffix_array4 = build_suffix_array_doubling(text4)
  print_suffix_array(text4, suffix_array4)

  # 테스트 케이스 7: 알파벳 순서
  print("\n=== 알파벳 순서 테스트 ===")
  text5 = "dcba"
  print(f"문자열: {text5}")
  suffix_array5 = build_suffix_array_naive(text5)
  print_suffix_array(text5, suffix_array5)

  # 테스트 케이스 8: 성능 비교 (작은 문자열)
  print("\n=== 성능 비교 테스트 ===")
  text6 = "abracadabra"
  print(f"문자열: {text6}")

  print("Naive 방법:")
  suffix_array6_naive = build_suffix_array_naive(text6)
  print(f"결과: {suffix_array6_naive}")

  print("Doubling 알고리즘:")
  suffix_array6_doubling = build_suffix_array_doubling(text6)
  print(f"결과: {suffix_array6_doubling}")

  print(f"결과 일치: {suffix_array6_naive == suffix_array6_doubling}")

  # 테스트 케이스 9: LCP 배열 테스트
  print("\n=== LCP 배열 테스트 ===")
  text7 = "abcabxabcd"
  print(f"문자열: {text7}")
  suffix_array7 = build_suffix_array_doubling(text7)
  lcp_array7 = build_lcp_array(text7, suffix_array7)

  print_suffix_array(text7, suffix_array7)
  print(f"LCP Array: {lcp_array7}")

  # 테스트 케이스 10: 고급 패턴 검색
  print("\n=== 고급 패턴 검색 테스트 ===")
  pattern_adv = "abc"
  result_adv = search_pattern_advanced(text7, suffix_array7, pattern_adv)
  print(f"고급 검색 - 패턴 '{pattern_adv}': ", end="")
  if result_adv != -1:
    print(f"위치 {result_adv}에서 발견")
  else:
    print("찾을 수 없음")

  # 테스트 케이스 11: 모든 패턴 출현 위치 찾기 (개선된 버전)
  print("\n=== 모든 패턴 출현 위치 테스트 (개선된 버전) ===")
  all_patterns = find_all_patterns(text7, suffix_array7, pattern_adv)
  print(f"패턴 '{pattern_adv}'의 모든 출현 위치: {all_patterns}")

  # 테스트 케이스 12: 가장 긴 반복 부분 문자열
  print("\n=== 가장 긴 반복 부분 문자열 테스트 ===")
  longest_pos, longest_len = find_longest_repeated_substring(
      text7, suffix_array7, lcp_array7)
  if longest_pos != -1:
    substring = text7[longest_pos:longest_pos + longest_len]
    print(f"가장 긴 반복 부분 문자열: '{substring}' (위치 {longest_pos}, 길이 {longest_len})")
  else:
    print("반복 부분 문자열이 없습니다.")

  # 테스트 케이스 13: LCP를 이용한 두 suffix 비교
  print("\n=== LCP 계산 테스트 ===")
  pos1, pos2 = 0, 3  # "abcabxabcd"에서 0번째와 3번째 위치
  lcp_direct = compute_lcp(text7, pos1, pos2)
  print(f"위치 {pos1}('{text7[pos1:]}')와 위치 {pos2}('{text7[pos2:]}')의 LCP: {lcp_direct}")

  # 테스트 케이스 14: 복잡한 문자열에서의 고급 기능
  print("\n=== 복잡한 문자열 고급 기능 테스트 ===")
  text8 = "mississippi"
  print(f"문자열: {text8}")
  suffix_array8 = build_suffix_array_doubling(text8)
  lcp_array8 = build_lcp_array(text8, suffix_array8)

  # 가장 긴 반복 부분 문자열
  longest_pos8, longest_len8 = find_longest_repeated_substring(
      text8, suffix_array8, lcp_array8)
  if longest_pos8 != -1:
    substring8 = text8[longest_pos8:longest_pos8 + longest_len8]
    print(f"가장 긴 반복 부분 문자열: '{substring8}' (위치 {longest_pos8}, 길이 {longest_len8})")

  # 다양한 패턴 검색
  patterns_test = ["is", "ss", "ssi"]
  for pattern in patterns_test:
    occurrences = find_all_patterns(text8, suffix_array8, pattern)
    print(f"패턴 '{pattern}': {occurrences}")

  print(f"\nLCP Array for '{text8}': {lcp_array8}")


# 사용 예시
if __name__ == "__main__":
  test_suffix_array()
