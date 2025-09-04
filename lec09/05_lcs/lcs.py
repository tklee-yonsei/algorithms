# lcs.py

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


def find_longest_common_substring(lcp):
  """
  LCP 배열에서 가장 긴 공통 부분 문자열 찾기

  Args:
      lcp: LCP 배열

  Returns:
      최대 LCP 길이
  """
  max_lcp = 0
  for i in range(1, len(lcp)):  # LCP[0]은 보통 0이므로 1부터 시작
    if lcp[i] > max_lcp:
      max_lcp = lcp[i]
  return max_lcp


def find_longest_common_substring_with_index(lcp):
  """
  최대 LCP와 해당 인덱스 찾기

  Args:
      lcp: LCP 배열

  Returns:
      (최대 LCP 길이, 인덱스) 튜플
  """
  max_lcp = 0
  max_index = -1

  for i in range(1, len(lcp)):
    if lcp[i] > max_lcp:
      max_lcp = lcp[i]
      max_index = i

  return max_lcp, max_index


def find_all_longest_common_substrings(lcp):
  """
  최대 LCP와 같은 모든 인덱스 찾기

  Args:
      lcp: LCP 배열

  Returns:
      (최대 LCP 길이, 인덱스 리스트) 튜플
  """
  max_lcp = find_longest_common_substring(lcp)
  indices = []

  for i in range(1, len(lcp)):
    if lcp[i] == max_lcp:
      indices.append(i)

  return max_lcp, indices


def find_longest_common_substring_with_suffix_array(text, suffix_array, lcp):
  """
  Suffix Array와 LCP 배열을 이용해 가장 긴 공통 부분 문자열 찾기

  Args:
      text: 원본 문자열
      suffix_array: suffix array
      lcp: LCP 배열

  Returns:
      (공통 부분 문자열, 길이, 위치1, 위치2) 튜플
  """
  max_lcp, max_index = find_longest_common_substring_with_index(lcp)

  if max_lcp == 0:
    return "", 0, -1, -1

  # 가장 긴 공통 부분 문자열이 나타나는 두 suffix의 시작 위치
  pos1 = suffix_array[max_index - 1]
  pos2 = suffix_array[max_index]

  # 실제 부분 문자열 추출
  common_substring = text[pos1:pos1 + max_lcp]

  return common_substring, max_lcp, pos1, pos2


def find_all_occurrences_of_lcs(text, lcp, suffix_array):
  """
  가장 긴 공통 부분 문자열의 모든 출현 위치 찾기

  Args:
      text: 원본 문자열
      lcp: LCP 배열
      suffix_array: suffix array

  Returns:
      (출현 위치 리스트, 최대 LCP 길이) 튜플
  """
  max_lcp, indices = find_all_longest_common_substrings(lcp)

  if max_lcp == 0:
    return [], 0

  positions = []

  for index in indices:
    pos1 = suffix_array[index - 1]
    pos2 = suffix_array[index]
    positions.extend([pos1, pos2])

  # 중복 제거 및 정렬
  unique_positions = sorted(list(set(positions)))

  return unique_positions, max_lcp


def find_top_k_longest_common_substrings(lcp, suffix_array, text, k=3):
  """
  상위 k개의 가장 긴 공통 부분 문자열 찾기

  Args:
      lcp: LCP 배열
      suffix_array: suffix array
      text: 원본 문자열
      k: 찾을 개수

  Returns:
      [(부분 문자열, 길이, 위치1, 위치2), ...] 리스트
  """
  lcp_with_index = []

  for i in range(1, len(lcp)):
    if lcp[i] > 0:
      lcp_with_index.append((lcp[i], i))

  # LCP 길이로 내림차순 정렬
  lcp_with_index.sort(reverse=True)

  results = []
  seen = set()

  for lcp_length, index in lcp_with_index[:k]:
    pos1 = suffix_array[index - 1]
    pos2 = suffix_array[index]
    substring = text[pos1:pos1 + lcp_length]

    if substring not in seen:
      seen.add(substring)
      results.append((substring, lcp_length, pos1, pos2))

  return results


def compute_lcp_statistics(lcp):
  """
  LCP 배열의 통계 정보 계산

  Args:
      lcp: LCP 배열

  Returns:
      (최대 LCP, 최소 LCP, 평균 LCP, 총 공통 문자 수) 튜플
  """
  valid_lcp = [x for x in lcp[1:] if x > 0]

  if not valid_lcp:
    return 0, 0, 0.0, 0

  max_lcp = max(valid_lcp)
  min_lcp = min(valid_lcp)
  avg_lcp = sum(valid_lcp) / len(valid_lcp)
  total_common = sum(valid_lcp)

  return max_lcp, min_lcp, avg_lcp, total_common


def print_lcs_analysis(text, suffix_array, lcp):
  """
  LCS 분석 결과 출력

  Args:
      text: 원본 문자열
      suffix_array: suffix array
      lcp: LCP 배열
  """
  print("=== 가장 긴 공통 부분 문자열 분석 ===")
  print(f"문자열: {text}")
  print(f"Suffix Array: {suffix_array}")
  print(f"LCP Array: {lcp}")
  print()

  # 기본 통계
  max_lcp, min_lcp, avg_lcp, total_common = compute_lcp_statistics(lcp)

  print("LCP 통계:")
  print(f"  최대 LCP: {max_lcp}")
  print(f"  최소 LCP (0 제외): {min_lcp}")
  print(f"  평균 LCP: {avg_lcp:.2f}")
  print(f"  총 공통 문자 수: {total_common}")
  print()

  # 가장 긴 공통 부분 문자열
  common_str, length, pos1, pos2 = find_longest_common_substring_with_suffix_array(
      text, suffix_array, lcp)

  if length > 0:
    print("가장 긴 공통 부분 문자열:")
    print(f"  문자열: {common_str}")
    print(f"  길이: {length}")
    print(f"  출현 위치: {pos1}과 {pos2}")
    print(f"  suffix[{pos1}]: {text[pos1:]}")
    print(f"  suffix[{pos2}]: {text[pos2:]}")
  else:
    print("공통 부분 문자열이 없습니다.")
  print()

  # 모든 출현 위치
  positions, max_len = find_all_occurrences_of_lcs(text, lcp, suffix_array)
  if max_len > 0:
    print(f"가장 긴 공통 부분 문자열의 모든 출현 위치: {positions}")
  print()

  # 상위 3개 LCS
  top_lcs = find_top_k_longest_common_substrings(lcp, suffix_array, text, 3)
  print("상위 3개 가장 긴 공통 부분 문자열:")
  for i, (substring, length, p1, p2) in enumerate(top_lcs):
    print(f"  {i+1}: '{substring}' (길이 {length}, 위치 {p1}과 {p2})")


def test_lcs():
  """테스트 함수"""
  print("=== LCS 테스트 ===\n")

  # 테스트 케이스 1: 기본 예제
  print("=== LCS 테스트 1: banana ===")
  text1 = "banana"
  suffix_array1 = [5, 3, 1, 0, 4, 2]  # 미리 계산된 값
  lcp1 = [0, 1, 3, 0, 0, 2]  # 미리 계산된 값

  print_lcs_analysis(text1, suffix_array1, lcp1)

  # 테스트 케이스 2: 복잡한 예제
  print("=== LCS 테스트 2: mississippi ===")
  text2 = "mississippi"
  suffix_array2 = [10, 7, 4, 1, 0, 9, 8, 6, 3, 5, 2]  # 미리 계산된 값
  lcp2 = [0, 1, 1, 4, 0, 0, 1, 0, 2, 1, 3]  # 미리 계산된 값

  print_lcs_analysis(text2, suffix_array2, lcp2)

  # 테스트 케이스 3: 반복 패턴
  print("=== LCS 테스트 3: abcabcabc ===")
  text3 = "abcabcabc"
  suffix_array3 = [0, 3, 6, 1, 4, 7, 2, 5, 8]  # 가정된 값
  lcp3 = [0, 6, 3, 0, 3, 0, 0, 0, 0]  # 가정된 값

  print_lcs_analysis(text3, suffix_array3, lcp3)

  # 테스트 케이스 4: 단순 통계 테스트
  print("=== 단순 LCP 배열 테스트 ===")
  lcp_simple = [0, 2, 1, 4, 0, 3, 1]

  max_lcp, max_index = find_longest_common_substring_with_index(lcp_simple)
  print(f"LCP 배열: {lcp_simple}")
  print(f"최대 LCP: {max_lcp} (위치: {max_index})")

  all_max, indices = find_all_longest_common_substrings(lcp_simple)
  print(f"최대값과 같은 모든 위치: {indices}")
  print()

  # 테스트 케이스 5: 특별한 경우들
  print("=== 특별한 경우들 ===")

  # 모든 LCP가 0인 경우
  lcp_zero = [0, 0, 0, 0]
  max_zero = find_longest_common_substring(lcp_zero)
  print(f"모든 LCP가 0인 경우 최대값: {max_zero}")

  # 단일 최대값
  lcp_single = [0, 1, 5, 2, 1]
  max_single = find_longest_common_substring(lcp_single)
  print(f"단일 최대값 경우: {max_single}")

  # 여러 최대값
  lcp_multiple = [0, 3, 1, 3, 2, 3]
  max_mult, indices_mult = find_all_longest_common_substrings(lcp_multiple)
  print(f"여러 최대값 ({max_mult})의 위치들: {indices_mult}")
  print()

  # 테스트 케이스 6: 실제 문자열 패턴 분석
  print("=== 다양한 패턴 분석 ===")
  test_cases = [
      ("aaa", [2, 1, 0], [0, 2, 1]),
      ("abab", [3, 1, 0, 2], [0, 0, 2, 0]),
      ("abcabc", [5, 2, 0, 3, 1, 4], [0, 0, 0, 3, 0, 0])
  ]

  for text, sa, lcp in test_cases:
    print(f"패턴 '{text}':")
    max_lcp = find_longest_common_substring(lcp)
    if max_lcp > 0:
      common_str, length, pos1, pos2 = find_longest_common_substring_with_suffix_array(
          text, sa, lcp)
      print(f"  가장 긴 공통 부분 문자열: '{common_str}' (길이 {length})")
    else:
      print("  공통 부분 문자열 없음")
  print()

  # 테스트 케이스 7: 성능 관련 통계
  print("=== LCP 통계 비교 ===")
  stat_cases = [
      [0, 1, 2, 3, 4],
      [0, 5, 1, 1, 1],
      [0, 0, 0, 0, 0],
      [0, 2, 4, 1, 3, 2]
  ]

  for i, lcp in enumerate(stat_cases):
    max_lcp, min_lcp, avg_lcp, total = compute_lcp_statistics(lcp)
    print(f"케이스 {i+1}: LCP={lcp}")
    print(f"  최대={max_lcp}, 최소={min_lcp}, 평균={avg_lcp:.2f}, 총합={total}")


# 사용 예시
if __name__ == "__main__":
  test_lcs()
