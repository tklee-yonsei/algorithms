# suffixArray.py - Suffix Array (START CODE)

class SuffixEntry:
  """Naive 방법용 클래스 (완성됨)"""

  def __init__(self, index, suffix):
    self.index = index
    self.suffix = suffix

  def __lt__(self, other):
    return self.suffix < other.suffix


class SuffixRank:
  """Doubling 알고리즘용 클래스 (완성됨)"""

  def __init__(self, rank0, rank1, index):
    self.rank = [rank0, rank1]
    self.index = index

  def __lt__(self, other):
    if self.rank[0] != other.rank[0]:
      return self.rank[0] < other.rank[0]
    return self.rank[1] < other.rank[1]


def build_suffix_array_naive(text):
  """
  TODO: Naive 방법으로 Suffix Array 구축

  Args:
      text: 입력 문자열

  Returns:
      suffix array 리스트

  시간 복잡도: O(n^2 log n)
  공간 복잡도: O(n)
  """
  # TODO: Naive 방법으로 Suffix Array를 구축하세요
  # 힌트:
  # 1. n = len(text), suffixes = [] 선언
  # 2. 모든 suffix 생성: suffixes.append(SuffixEntry(i, text[i:]))
  # 3. 사전순 정렬: suffixes.sort()
  # 4. 결과를 suffix array로 반환: [suffix.index for suffix in suffixes]

  print("build_suffix_array_naive 구현 필요")
  return []  # 임시 반환값


def build_suffix_array_doubling(text):
  """
  TODO: Doubling 알고리즘으로 Suffix Array 구축

  Args:
      text: 입력 문자열

  Returns:
      suffix array 리스트

  시간 복잡도: O(n log^2 n)
  공간 복잡도: O(n)
  """
  # TODO: Doubling 알고리즘으로 Suffix Array를 구축하세요
  # 힌트:
  # 1. n = len(text), suffixes = [] 선언
  # 2. 초기 rank 설정 (각 문자와 다음 문자):
  #    - rank0 = ord(text[i]), rank1 = ord(text[i+1]) if i+1 < n else -1
  #    - suffixes.append(SuffixRank(rank0, rank1, i))
  # 3. 정렬: suffixes.sort()
  # 4. k = 4부터 시작해서 2배씩 증가하며 반복:
  #    - 새로운 rank 할당
  #    - index 배열로 위치 추적
  #    - 다음 위치의 rank 업데이트
  #    - 다시 정렬
  # 5. 최종 suffix array 생성: [suffix.index for suffix in suffixes]

  print("build_suffix_array_doubling 구현 필요")
  return []  # 임시 반환값


def print_suffix_array(text, suffix_array):
  """
  Suffix Array 출력 함수 (완성됨)

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
  패턴 검색 함수 (이진 탐색 사용) (완성됨)

  Args:
      text: 원본 문자열
      suffix_array: suffix array
      pattern: 검색할 패턴

  Returns:
      패턴이 발견된 위치, 없으면 -1
  """
  # 빈 suffix_array인 경우 처리
  if not suffix_array or len(suffix_array) == 0:
    return -1

  left = 0
  right = len(suffix_array) - 1
  pattern_len = len(pattern)

  while left <= right:
    mid = (left + right) // 2
    suffix = text[suffix_array[mid]:]

    # 패턴 길이만큼만 비교
    suffix_prefix = suffix[:pattern_len]

    if pattern == suffix_prefix:
      return suffix_array[mid]
    elif pattern > suffix_prefix:
      left = mid + 1
    else:
      right = mid - 1

  return -1


def find_all_patterns(text, suffix_array, pattern):
  """
  모든 패턴 출현 위치 찾기 (완성됨)

  Args:
      text: 원본 문자열
      suffix_array: suffix array
      pattern: 검색할 패턴

  Returns:
      패턴이 발견된 모든 위치의 리스트
  """
  results = []

  # 빈 suffix_array인 경우 처리
  if not suffix_array or len(suffix_array) == 0:
    return results

  n = len(suffix_array)
  m = len(pattern)

  # 첫 번째 출현 위치 찾기
  left, right = 0, n - 1
  first = -1

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

  # 연속된 모든 매칭 찾기
  for i in range(first, n):
    suffix = text[suffix_array[i]:]
    if suffix.startswith(pattern):
      results.append(suffix_array[i])
    else:
      break

  return sorted(results)


def compute_lcp(text, i, j):
  """
  LCP (Longest Common Prefix) 계산 (완성됨)

  Args:
      text: 문자열
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
  LCP 배열 구축 (Kasai 알고리즘) (완성됨)

  Args:
      text: 문자열
      suffix_array: suffix array

  Returns:
      LCP 배열
  """
  n = len(text)
  lcp_array = [0] * n

  # 빈 suffix_array인 경우 처리
  if not suffix_array or len(suffix_array) == 0:
    return lcp_array

  rank = [0] * n

  for i in range(n):
    if i < len(suffix_array):  # 안전성 체크 추가
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


def find_longest_repeated_substring(text, suffix_array, lcp_array):
  """
  가장 긴 반복 부분 문자열 찾기 (완성됨)

  Args:
      text: 원본 문자열
      suffix_array: suffix array
      lcp_array: LCP 배열

  Returns:
      (시작 위치, 길이) 튜플
  """
  # 빈 배열인 경우 처리
  if not lcp_array or len(lcp_array) <= 1:
    return (-1, 0)

  max_lcp = max(lcp_array[1:])
  if max_lcp == 0:
    return (-1, 0)

  for i in range(1, len(lcp_array)):
    if lcp_array[i] == max_lcp and i < len(suffix_array):
      return (suffix_array[i], max_lcp)
  return (-1, 0)


def test_suffix_array():
  """테스트 함수 (완성됨)"""
  print("=== Suffix Array 테스트 ===\n")

  # 테스트 케이스 1: Naive 방법
  print("=== Naive 방법 테스트 ===")
  text1 = "banana"
  print(f"문자열: {text1}")

  suffix_array1 = build_suffix_array_naive(text1)
  print_suffix_array(text1, suffix_array1)

  # 패턴 검색 테스트
  pattern1 = "ana"
  pos1 = search_pattern(text1, suffix_array1, pattern1)
  print(f"패턴 '{pattern1}' 검색 결과: {pos1}")
  print()

  # 테스트 케이스 2: Doubling 방법
  print("=== Doubling 알고리즘 테스트 ===")
  text2 = "mississippi"
  print(f"문자열: {text2}")

  suffix_array2 = build_suffix_array_doubling(text2)
  print_suffix_array(text2, suffix_array2)

  # LCP 배열 구축
  lcp_array2 = build_lcp_array(text2, suffix_array2)
  print(f"LCP Array: {lcp_array2}")

  # 패턴 검색 테스트
  pattern2 = "issi"
  pos2 = search_pattern(text2, suffix_array2, pattern2)
  print(f"패턴 '{pattern2}' 검색 결과: {pos2}")

  # 모든 패턴 찾기
  pattern3 = "si"
  results = find_all_patterns(text2, suffix_array2, pattern3)
  print(f"패턴 '{pattern3}'의 모든 출현 위치: {results}")

  # 가장 긴 반복 부분 문자열
  longest_pos, longest_len = find_longest_repeated_substring(
      text2, suffix_array2, lcp_array2)
  print(f"가장 긴 반복 부분 문자열: 위치 {longest_pos}, 길이 {longest_len}")
  if longest_len > 0:
    print(f"문자열: '{text2[longest_pos:longest_pos+longest_len]}'")
  print()

  # 테스트 케이스 3: 비교 테스트
  print("=== 방법 비교 테스트 ===")
  text3 = "abcabc"
  print(f"문자열: {text3}")

  sa_naive = build_suffix_array_naive(text3)
  sa_doubling = build_suffix_array_doubling(text3)

  print(f"Naive 결과:    {sa_naive}")
  print(f"Doubling 결과: {sa_doubling}")

  # 결과 일치 확인
  match = sa_naive == sa_doubling
  print(f"결과 일치: {'예' if match else '아니오'}")
  print()

  # 테스트 케이스 4: 특수 케이스
  print("=== 특수 케이스 테스트 ===")
  test_cases = [
      "",          # 빈 문자열
      "a",         # 단일 문자
      "aa",        # 반복 문자
      "abc",       # 서로 다른 문자
      "abcabc",    # 반복 패턴
  ]

  for text in test_cases:
    if text:  # 빈 문자열이 아닌 경우만
      print(f"문자열: '{text}'")
      sa_naive = build_suffix_array_naive(text)
      print(f"Suffix Array: {sa_naive}")
    else:
      print("빈 문자열 테스트 스킵")


# 메인 실행 (완성됨)
if __name__ == "__main__":
  test_suffix_array()
