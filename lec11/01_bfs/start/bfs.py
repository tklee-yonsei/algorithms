"""
BFS (Breadth-First Search) 알고리즘 구현 - 시작 템플릿
그래프에서 너비 우선 탐색을 수행합니다.

TODO: 아래 함수들을 완성하세요.
"""

from collections import deque, defaultdict
from typing import List, Dict, Set


class Graph:
  """
  그래프 클래스 (인접 리스트로 표현)
  """

  def __init__(self, num_vertices: int = 0):
    """그래프 초기화"""
    self.num_vertices = num_vertices
    self.adj_list = defaultdict(list)

  def add_edge(self, src: int, dest: int) -> None:
    """
    간선 추가 (무방향 그래프)

    TODO: 무방향 그래프에 간선을 추가하는 코드를 작성하세요.
    src -> dest와 dest -> src 모두 추가해야 합니다.

    Args:
        src: 시작 정점
        dest: 도착 정점
    """
    # TODO: 구현하세요
    pass

  def get_vertices(self) -> Set[int]:
    """
    그래프의 모든 정점 반환

    TODO: 그래프에 포함된 모든 정점을 집합으로 반환하세요.

    Returns:
        모든 정점의 집합
    """
    # TODO: 구현하세요
    return set()

  def print_graph(self) -> None:
    """그래프 구조 출력 (디버깅용)"""
    print("\nGraph representation (adjacency list):")
    vertices = sorted(self.get_vertices())
    for vertex in vertices:
      neighbors = self.adj_list[vertex]
      print(f"Vertex {vertex}: {neighbors}")
    print()


def bfs(graph: Graph, start_vertex: int) -> List[int]:
  """
  BFS 알고리즘 구현

  TODO: BFS 알고리즘을 구현하세요.

  구현 단계:
  1. 시작 정점이 유효한지 확인
  2. 방문 상태를 추적하는 집합(explored) 생성
  3. 큐 초기화 (deque 사용)
  4. 시작 정점을 explored에 추가하고 큐에 삽입
  5. 큐가 비어있지 않은 동안 반복:
     - 큐에서 정점을 하나 꺼냄 (popleft)
     - 현재 정점을 결과에 추가
     - 현재 정점의 모든 인접 정점을 확인
     - 아직 탐색되지 않은 인접 정점을 explored에 추가하고 큐에 삽입

  Args:
      graph: 탐색할 그래프
      start_vertex: 시작 정점

  Returns:
      BFS 탐색 순서의 정점 리스트
  """
  # TODO: 구현하세요
  if start_vertex not in graph.get_vertices():
    print(f"Invalid start vertex: {start_vertex}")
    return []

  # TODO: BFS 알고리즘을 구현하세요
  explored = set()
  queue = deque()
  bfs_order = []

  print(f"BFS Traversal starting from vertex {start_vertex}: ", end="")

  # TODO: BFS 메인 루프를 구현하세요

  print()  # 줄바꿈
  return bfs_order


def main():
  """
  메인 함수 - 예제 실행
  """
  print("=== BFS (Breadth-First Search) Algorithm ===\n")

  # 그래프 생성
  graph = Graph()

  # 간선 추가
  graph.add_edge(0, 1)
  graph.add_edge(0, 2)
  graph.add_edge(1, 3)
  graph.add_edge(1, 4)
  graph.add_edge(2, 5)
  graph.add_edge(2, 6)

  # 그래프 구조 출력
  graph.print_graph()

  # BFS 실행
  result = bfs(graph, 0)
  print(f"BFS result: {result}")


if __name__ == "__main__":
  main()
