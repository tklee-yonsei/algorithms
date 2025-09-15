"""
최소 힙 (Min Heap) 자료구조 구현 - 배열 기반 이진 힙
완전 이진 트리의 성질을 만족하며, 부모 노드가 자식 노드보다 작거나 같습니다.

시간 복잡도:
- 삽입 (insert): O(log n)
- 최솟값 추출 (extract_min): O(log n)  
- 최솟값 조회 (peek): O(1)

공간 복잡도: O(n)
"""

from typing import List, Optional


class MinHeap:
  """최소 힙 클래스"""

  def __init__(self, capacity: int = 100):
    """
    힙 초기화

    Args:
        capacity: 힙의 최대 용량
    """
    self.array: List[int] = [0] * capacity
    self.size = 0
    self.capacity = capacity

  def get_parent_index(self, index: int) -> int:
    """부모 인덱스 계산"""
    return (index - 1) // 2

  def get_left_child_index(self, index: int) -> int:
    """왼쪽 자식 인덱스 계산"""
    return 2 * index + 1

  def get_right_child_index(self, index: int) -> int:
    """오른쪽 자식 인덱스 계산"""
    return 2 * index + 2

  def swap(self, index1: int, index2: int) -> None:
    """두 원소 교환"""
    self.array[index1], self.array[index2] = self.array[index2], self.array[index1]

  def insert(self, element: int) -> bool:
    """
    원소 삽입

    Args:
        element: 삽입할 원소

    Returns:
        성공 여부
    """
    # 1. 힙이 가득 찬 경우 확인
    if self.size >= self.capacity:
      print("Heap is full!")
      return False

    # 2. 힙의 마지막에 새 원소 추가
    self.array[self.size] = element
    last_index = self.size
    self.size += 1

    print(f"Inserted {element} at index {last_index}")

    # 3. 힙 속성 복구 (상향 이동)
    self._heapify_up(last_index)

    return True

  def _heapify_up(self, index: int) -> None:
    """
    상향 힙 정리 (Heapify Up)

    Args:
        index: 정리를 시작할 인덱스
    """
    # 루트에 도달하면 종료
    if index == 0:
      return

    parent_index = self.get_parent_index(index)

    print(
        f"Comparing {self.array[index]} (index {index}) with parent {self.array[parent_index]} (index {parent_index})")

    # 현재 노드가 부모보다 작으면 교환
    if self.array[index] < self.array[parent_index]:
      print(f"Swapping {self.array[index]} with {self.array[parent_index]}")
      self.swap(index, parent_index)

      # 재귀적으로 부모 방향으로 계속 정리
      self._heapify_up(parent_index)

  def extract_min(self) -> Optional[int]:
    """
    최솟값 추출

    Returns:
        최솟값 (힙이 비어있으면 None)
    """
    # 1. 빈 힙 확인
    if self.size == 0:
      print("Heap is empty!")
      return None

    # 2. 최솟값 저장 (루트)
    min_value = self.array[0]

    # 3. 마지막 원소를 루트로 이동
    self.array[0] = self.array[self.size - 1]
    self.size -= 1

    print(f"Extracted min value: {min_value}")

    # 4. 힙이 비어있지 않으면 힙 속성 복구 (하향 이동)
    if self.size > 0:
      print(f"Moving {self.array[0]} to root, heapifying down")
      self._heapify_down(0)

    return min_value

  def _heapify_down(self, index: int) -> None:
    """
    하향 힙 정리 (Heapify Down)

    Args:
        index: 정리를 시작할 인덱스
    """
    min_index = index
    left_child = self.get_left_child_index(index)
    right_child = self.get_right_child_index(index)

    # 왼쪽 자식과 비교
    if left_child < self.size and self.array[left_child] < self.array[min_index]:
      min_index = left_child

    # 오른쪽 자식과 비교
    if right_child < self.size and self.array[right_child] < self.array[min_index]:
      min_index = right_child

    # 최솟값이 현재 노드가 아니면 교환 후 재귀
    if min_index != index:
      print(
          f"Swapping {self.array[index]} (index {index}) with {self.array[min_index]} (index {min_index})")
      self.swap(index, min_index)

      # 재귀적으로 자식 방향으로 계속 정리
      self._heapify_down(min_index)

  def peek(self) -> Optional[int]:
    """
    최솟값 조회 (추출하지 않고)

    Returns:
        최솟값 (힙이 비어있으면 None)
    """
    if self.size == 0:
      print("Heap is empty!")
      return None

    return self.array[0]

  def is_empty(self) -> bool:
    """힙이 비어있는지 확인"""
    return self.size == 0

  def print_heap(self) -> None:
    """힙 출력"""
    if self.size == 0:
      print("Heap is empty")
      return

    elements = [str(self.array[i]) for i in range(self.size)]
    print(f"Heap contents: [{', '.join(elements)}]")
    print(f"Size: {self.size}")

  def print_tree_structure(self) -> None:
    """트리 구조로 힙 출력 (시각화)"""
    if self.size == 0:
      print("Heap is empty")
      return

    print("\n=== Heap Tree Structure ===")
    level = 0
    index = 0

    while index < self.size:
      level_size = 2 ** level
      level_elements = []

      for i in range(level_size):
        if index + i < self.size:
          level_elements.append(str(self.array[index + i]))
        else:
          break

      # 들여쓰기로 레벨 표현
      indent = "  " * (3 - level) if level < 3 else ""
      print(f"Level {level}: {indent}{' '.join(level_elements)}")

      index += level_size
      level += 1


def main():
  """메인 함수 - 힙 데모"""
  print("=== Min Heap Demo ===")

  # 힙 생성
  heap = MinHeap(10)

  # 원소들 삽입
  elements = [4, 7, 2, 9, 1, 5, 8]

  print("\n--- Insertion Phase ---")
  for element in elements:
    print(f"\nInserting: {element}")
    heap.insert(element)
    heap.print_heap()
    heap.print_tree_structure()

  print("\n--- Extraction Phase ---")
  while not heap.is_empty():
    min_val = heap.extract_min()
    print(f"Extracted: {min_val}")
    heap.print_heap()
    if not heap.is_empty():
      heap.print_tree_structure()
    print()


if __name__ == "__main__":
  main()
