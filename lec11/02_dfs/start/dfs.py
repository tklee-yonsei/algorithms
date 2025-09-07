"""
DFS (Depth-First Search) 알고리즘 구현 - 시작 템플릿
그래프에서 깊이 우선 탐색을 수행합니다.

TODO: 아래 함수들을 완성하세요.
"""

from collections import defaultdict
from typing import List, Set


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


def dfs_recursive(graph: Graph, start_vertex: int) -> List[int]:
  """
  DFS 알고리즘 구현 (재귀적)

  TODO: 재귀를 이용한 DFS 알고리즘을 구현하세요.

  구현 단계:
  1. 시작 정점이 유효한지 확인
  2. 방문 상태를 추적하는 집합(explored) 생성
  3. DFS 탐색 결과를 저장할 리스트 생성
  4. 재귀 보조 함수 dfs_visit 구현:
     - 현재 정점을 방문 처리
     - 현재 정점을 결과에 추가
     - 인접 정점들에 대해 재귀 호출
  5. 시작 정점부터 dfs_visit 호출

  Args:
      graph: 탐색할 그래프
      start_vertex: 시작 정점

  Returns:
      DFS 탐색 순서의 정점 리스트
  """
  # TODO: 구현하세요
  if start_vertex not in graph.get_vertices():
    print(f"Invalid start vertex: {start_vertex}")
    return []

  explored = set()
  dfs_order = []

  def dfs_visit(vertex: int) -> None:
    """
    DFS 재귀 보조 함수

    TODO: 이 함수를 구현하세요.
    """
    # TODO: 구현하세요
    pass

  print(f"DFS Recursive Traversal starting from vertex {start_vertex}: ", end="")

  # TODO: 재귀 DFS 시작

  print(" ".join(map(str, dfs_order)))
  return dfs_order


def dfs_iterative(graph: Graph, start_vertex: int) -> List[int]:
  """
  DFS 알고리즘 구현 (반복적)

  TODO: 스택을 이용한 반복적 DFS 알고리즘을 구현하세요.

  구현 단계:
  1. 시작 정점이 유효한지 확인
  2. 방문 상태를 추적하는 집합(explored) 생성
  3. 스택 초기화 (리스트 사용, 시작 정점 추가)
  4. 스택이 비어있지 않은 동안 반복:
     - 스택에서 정점을 하나 꺼냄 (pop)
     - 아직 탐색되지 않은 정점이라면 방문 처리
     - 인접 정점들을 스택에 추가 (역순으로)

  Args:
      graph: 탐색할 그래프
      start_vertex: 시작 정점

  Returns:
      DFS 탐색 순서의 정점 리스트
  """
  # TODO: 구현하세요
  if start_vertex not in graph.get_vertices():
    print(f"Invalid start vertex: {start_vertex}")
    return []

  explored = set()
  stack = []
  dfs_order = []

  print(f"DFS Iterative Traversal starting from vertex {start_vertex}: ", end="")

  # TODO: DFS 메인 루프를 구현하세요

  print(" ".join(map(str, dfs_order)))
  return dfs_order


def main():
  """
  메인 함수 - 예제 실행
  """
  print("=== DFS (Depth-First Search) Algorithm ===\n")

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

  # DFS 실행
  dfs_recursive(graph, 0)
  dfs_iterative(graph, 0)


if __name__ == "__main__":
  main()
