# huffmanCode.py
import heapq
from collections import defaultdict


class Node:
  """허프만 트리 노드 클래스"""

  def __init__(self, character=None, frequency=0, left=None, right=None):
    self.character = character
    self.frequency = frequency
    self.left = left
    self.right = right

  # 우선순위 큐에서 사용하기 위한 비교 연산자
  def __lt__(self, other):
    return self.frequency < other.frequency

  def __eq__(self, other):
    return self.frequency == other.frequency


def build_huffman_tree(characters, frequencies):
  """허프만 트리를 구축하는 함수"""
  # 1. 우선순위 큐(최소 힙) 생성
  heap = []

  # 2. 각 문자에 대해 노드 생성하여 힙에 삽입
  for i in range(len(characters)):
    node = Node(characters[i], frequencies[i])
    heapq.heappush(heap, node)

  # 3. 허프만 트리 구성
  while len(heap) > 1:
    # 빈도가 가장 작은 두 노드 추출
    left = heapq.heappop(heap)
    right = heapq.heappop(heap)

    # 새 내부 노드 생성 (문자는 None, 빈도는 두 노드의 합)
    merged = Node(None, left.frequency + right.frequency, left, right)

    # 합쳐진 노드를 다시 힙에 삽입
    heapq.heappush(heap, merged)

  # 4. 루트 노드 반환
  return heap[0] if heap else None


def generate_codes(root, code="", codes=None):
  """허프만 코드를 생성하는 함수"""
  if codes is None:
    codes = {}

  if root is not None:
    # 리프 노드인 경우 (문자 노드)
    if root.left is None and root.right is None:
      codes[root.character] = code if code else "0"  # 단일 문자인 경우 "0"
      return codes

    # 내부 노드인 경우 재귀 호출
    generate_codes(root.left, code + "1", codes)
    generate_codes(root.right, code + "0", codes)

  return codes


def huffman_coding(characters, frequencies):
  """허프만 코딩 메인 함수"""
  # 1. 허프만 트리 구축
  root = build_huffman_tree(characters, frequencies)

  # 2. 허프만 코드 생성
  codes = generate_codes(root)

  # 3. 결과 출력
  print("=== 허프만 코딩 결과 ===")
  for i, char in enumerate(characters):
    print(f"문자: {char}, 빈도: {frequencies[i]}, 코드: {codes.get(char, 'N/A')}")

  return codes, root


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


def calculate_compression_ratio(characters, frequencies, codes):
  """압축률을 계산하는 함수"""
  # 원본 크기 계산 (각 문자당 8비트 가정)
  original_size = sum(freq * 8 for freq in frequencies)

  # 허프만 코드 크기 계산
  huffman_size = sum(frequencies[i] * len(codes[characters[i]])
                     for i in range(len(characters)))

  # 압축률 계산
  compression_ratio = (1 - huffman_size / original_size) * \
      100 if original_size > 0 else 0

  print(f"\n=== 압축률 분석 ===")
  print(f"원본 크기 (8비트 고정 길이): {original_size} 비트")
  print(f"허프만 코드 크기: {huffman_size} 비트")
  print(f"압축률: {compression_ratio:.2f}%")

  return compression_ratio


def encode_text(text, codes):
  """텍스트를 허프만 코드로 인코딩하는 함수"""
  encoded = ""
  for char in text:
    if char in codes:
      encoded += codes[char]
    else:
      print(f"경고: 문자 '{char}'에 대한 코드가 없습니다.")
  return encoded


def decode_text(encoded_text, root):
  """허프만 코드를 텍스트로 디코딩하는 함수"""
  decoded = ""
  current = root

  for bit in encoded_text:
    if bit == '1':
      current = current.left
    else:
      current = current.right

    # 리프 노드에 도달한 경우
    if current.left is None and current.right is None:
      decoded += current.character
      current = root

  return decoded


# 사용 예시
if __name__ == "__main__":
  # 예제 데이터 (문제에서 제시된 빈도표)
  characters = ['A', 'B', 'C', 'D']
  frequencies = [60, 25, 10, 5]

  print("입력 데이터:")
  for i, char in enumerate(characters):
    print(f"문자: {char}, 빈도: {frequencies[i]}")
  print()

  # 허프만 코딩 수행
  codes, root = huffman_coding(characters, frequencies)

  # 트리 구조 출력
  print(f"\n=== 허프만 트리 구조 ===")
  print_tree(root)

  # 압축률 계산
  calculate_compression_ratio(characters, frequencies, codes)

  # 인코딩/디코딩 예시
  print(f"\n=== 인코딩/디코딩 예시 ===")
  sample_text = "ABCD"
  encoded = encode_text(sample_text, codes)
  decoded = decode_text(encoded, root)
  print(f"원본 텍스트: {sample_text}")
  print(f"인코딩된 텍스트: {encoded}")
  print(f"디코딩된 텍스트: {decoded}")

  # 추가 테스트 케이스
  print(f"\n--- 추가 테스트 케이스 ---")
  characters2 = ['a', 'b', 'c', 'd', 'e', 'f']
  frequencies2 = [5, 9, 12, 13, 16, 45]

  print("테스트 케이스 2:")
  codes2, root2 = huffman_coding(characters2, frequencies2)
  calculate_compression_ratio(characters2, frequencies2, codes2)

  # 더 복잡한 예시
  print(f"\n--- 실제 텍스트 예시 ---")
  text = "AAAAAAAAAABBBBBCCCDD"
  char_freq = defaultdict(int)
  for char in text:
    char_freq[char] += 1

  chars = list(char_freq.keys())
  freqs = list(char_freq.values())

  print(f"텍스트: {text}")
  print("문자 빈도:")
  for i, char in enumerate(chars):
    print(f"  {char}: {freqs[i]}")

  codes3, root3 = huffman_coding(chars, freqs)
  encoded_text = encode_text(text, codes3)
  print(f"인코딩 결과: {encoded_text}")
  calculate_compression_ratio(chars, freqs, codes3)
