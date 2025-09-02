# huffmanCode.py
import heapq
from collections import defaultdict

# TODO: 허프만 트리 노드 클래스를 구현하세요


class Node:
  """허프만 트리 노드 클래스"""

  def __init__(self, character=None, frequency=0, left=None, right=None):
    # TODO: 노드 초기화
    pass

  # TODO: 우선순위 큐에서 사용하기 위한 비교 연산자를 구현하세요
  def __lt__(self, other):
    # 빈도를 기준으로 비교
    pass

  def __eq__(self, other):
    # 빈도가 같은지 비교
    pass

# TODO: 허프만 트리를 구축하는 함수를 구현하세요


def build_huffman_tree(characters, frequencies):
  """허프만 트리를 구축하는 함수"""
  # 1. 우선순위 큐(최소 힙) 생성
  # 2. 각 문자에 대해 노드 생성하여 힙에 삽입
  # 3. 허프만 트리 구성 (두 개씩 합치기)
  # 4. 루트 노드 반환
  return None

# TODO: 허프만 코드를 생성하는 함수를 구현하세요


def generate_codes(root, code="", codes=None):
  """허프만 코드를 생성하는 함수"""
  # 재귀적으로 트리를 순회하며 각 문자의 코드 생성
  # 왼쪽: '0', 오른쪽: '1'
  # 리프 노드에서 코드 저장
  if codes is None:
    codes = {}

  # TODO: 구현

  return codes

# TODO: 허프만 코딩 메인 함수를 구현하세요


def huffman_coding(characters, frequencies):
  """허프만 코딩 메인 함수"""
  # 1. 허프만 트리 구축
  # 2. 허프만 코드 생성
  # 3. 결과 출력

  print("=== 허프만 코딩 결과 ===")
  # TODO: 구현

  return {}, None  # TODO: 실제 codes와 root 반환

# 트리 구조 출력 함수 (참고용)


def print_tree(root, depth=0, prefix="루트: "):
  """트리 구조를 시각적으로 출력하는 함수"""
  if root is not None:
    print("  " * depth + prefix, end="")
    if root.character is None:
      print(f"내부노드 (빈도: {root.frequency})")
    else:
      print(f"리프노드: {root.character} (빈도: {root.frequency})")

    if root.left or root.right:
      if root.left:
        print_tree(root.left, depth + 1, "L--- ")
      if root.right:
        print_tree(root.right, depth + 1, "R--- ")

# TODO: 압축률을 계산하는 함수를 구현하세요


def calculate_compression_ratio(characters, frequencies, codes):
  """압축률을 계산하는 함수"""
  # 원본 크기와 허프만 코드 크기를 계산하여 압축률 산출
  pass


# 사용 예시
if __name__ == "__main__":
  # 예제 데이터
  characters = ['A', 'B', 'C', 'D']
  frequencies = [60, 25, 10, 5]

  print("입력 데이터:")
  for i, char in enumerate(characters):
    print(f"문자: {char}, 빈도: {frequencies[i]}")
  print()

  # TODO: 허프만 코딩 수행
  # codes, root = huffman_coding(characters, frequencies)

  print("TODO: 허프만 코딩을 구현하세요!")
