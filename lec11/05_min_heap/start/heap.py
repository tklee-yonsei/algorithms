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
    # TODO: 이 함수를 완성하세요!
    #
    # 힌트:
    # 1. 힙이 가득 찼는지 확인 (self.size >= self.capacity)
    # 2. 새 원소를 배열 끝에 추가
    # 3. size 증가
    # 4. _heapify_up으로 힙 속성 복구
    # 5. 성공 시 True 반환

    print("=== Insert Function - TODO ===")
    return False

  def _heapify_up(self, index: int) -> None:
    """
    상향 힙 정리 (Heapify Up)

    Args:
        index: 정리를 시작할 인덱스
    """
    # TODO: 이 함수를 완성하세요!
    #
    # 힌트:
    # 1. 루트(index == 0)에 도달하면 종료
    # 2. 부모 인덱스 계산: self.get_parent_index(index)
    # 3. 현재 노드가 부모보다 작으면:
    #    - self.swap으로 교환
    #    - 재귀적으로 self._heapify_up(parent_index) 호출
    # 4. 과정을 print로 출력하여 디버깅

    pass

  def extract_min(self) -> Optional[int]:
    """
    최솟값 추출

    Returns:
        최솟값 (힙이 비어있으면 None)
    """
    # TODO: 이 함수를 완성하세요!
    #
    # 힌트:
    # 1. 빈 힙 확인 (self.size == 0)
    # 2. 최솟값(루트) 저장
    # 3. 마지막 원소를 루트로 이동
    # 4. size 감소
    # 5. _heapify_down으로 힙 속성 복구
    # 6. 최솟값 반환

    print("=== ExtractMin Function - TODO ===")
    return None

  def _heapify_down(self, index: int) -> None:
    """
    하향 힙 정리 (Heapify Down)

    Args:
        index: 정리를 시작할 인덱스
    """
    # TODO: 이 함수를 완성하세요!
    #
    # 힌트:
    # 1. 현재 인덱스를 최소값으로 초기화
    # 2. 왼쪽/오른쪽 자식 인덱스 계산
    # 3. 자식들과 비교하여 가장 작은 값의 인덱스 찾기
    # 4. 최소값이 현재 노드가 아니면:
    #    - self.swap으로 교환
    #    - 재귀적으로 self._heapify_down 호출

    pass

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


def main():
  """메인 함수 - 힙 데모"""
  print("=== Min Heap Demo (TODO Implementation) ===")

  # 힙 생성
  heap = MinHeap(10)

  # 원소들 삽입
  elements = [4, 7, 2, 9, 1, 5, 8]

  print("\n--- Insertion Phase ---")
  for element in elements:
    print(f"\nInserting: {element}")
    if heap.insert(element):
      heap.print_heap()

  print("\n--- Extraction Phase ---")
  while not heap.is_empty():
    min_val = heap.extract_min()
    if min_val is not None:
      print(f"Extracted: {min_val}")
      heap.print_heap()
    print()


if __name__ == "__main__":
  main()
