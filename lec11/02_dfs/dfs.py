"""
DFS (Depth-First Search) 알고리즘 구현
그래프에서 깊이 우선 탐색을 수행합니다.

시간 복잡도: O(V + E) - V는 정점 수, E는 간선 수
공간 복잡도: O(V) - 스택과 방문 집합을 위한 공간
"""

from collections import defaultdict
from typing import List, Set


class Graph:
  """
  그래프 클래스 (인접 리스트로 표현)
  """

  def __init__(self, num_vertices: int = 0):
    """
    그래프 초기화

    Args:
        num_vertices: 정점의 개수 (옵션)
    """
    self.num_vertices = num_vertices
    self.adj_list = defaultdict(list)

  def add_edge(self, src: int, dest: int) -> None:
    """
    간선 추가 (무방향 그래프)

    Args:
        src: 시작 정점
        dest: 도착 정점
    """
    self.adj_list[src].append(dest)
    self.adj_list[dest].append(src)  # 무방향 그래프

  def add_directed_edge(self, src: int, dest: int) -> None:
    """
    방향 간선 추가 (방향 그래프)

    Args:
        src: 시작 정점
        dest: 도착 정점
    """
    self.adj_list[src].append(dest)

  def get_vertices(self) -> Set[int]:
    """
    그래프의 모든 정점 반환

    Returns:
        모든 정점의 집합
    """
    vertices = set()
    for vertex in self.adj_list:
      vertices.add(vertex)
      vertices.update(self.adj_list[vertex])
    return vertices

  def print_graph(self) -> None:
    """
    그래프 구조 출력 (디버깅용)
    """
    print("\nGraph representation (adjacency list):")
    vertices = sorted(self.get_vertices())
    for vertex in vertices:
      neighbors = self.adj_list[vertex]
      print(f"Vertex {vertex}: {neighbors}")
    print()


def dfs_recursive(graph: Graph, start_vertex: int) -> List[int]:
  """
  DFS 알고리즘 구현 (재귀적)

  Args:
      graph: 탐색할 그래프
      start_vertex: 시작 정점

  Returns:
      DFS 탐색 순서의 정점 리스트
  """
  if start_vertex not in graph.get_vertices():
    print(f"Invalid start vertex: {start_vertex}")
    return []

  # 방문 상태를 추적하는 집합
  explored = set()

  # DFS 탐색 결과를 저장할 리스트
  dfs_order = []

  def dfs_visit(vertex: int) -> None:
    """
    DFS 재귀 보조 함수

    Args:
        vertex: 현재 방문할 정점
    """
    # 현재 정점을 방문 처리
    explored.add(vertex)
    dfs_order.append(vertex)

    # 현재 정점의 모든 인접 정점에 대해 재귀 호출
    # 정렬해서 일관된 순서로 탐색
    neighbors = sorted(graph.adj_list[vertex])
    for neighbor in neighbors:
      if neighbor not in explored:
        dfs_visit(neighbor)

  print(f"DFS Recursive Traversal starting from vertex {start_vertex}: ", end="")

  # 재귀 DFS 시작
  dfs_visit(start_vertex)

  # 결과 출력
  print(" ".join(map(str, dfs_order)))
  return dfs_order


def dfs_iterative(graph: Graph, start_vertex: int) -> List[int]:
  """
  DFS 알고리즘 구현 (반복적) - 스택 상태 시각화 포함

  Args:
      graph: 탐색할 그래프
      start_vertex: 시작 정점

  Returns:
      DFS 탐색 순서의 정점 리스트
  """
  if start_vertex not in graph.get_vertices():
    print(f"Invalid start vertex: {start_vertex}")
    return []

  # 방문 상태를 추적하는 집합
  explored = set()

  # 스택 초기화 (리스트 사용)
  stack = [start_vertex]
  print(f"Initial stack: {stack}")

  # DFS 탐색 결과를 저장할 리스트
  dfs_order = []

  print(f"DFS Iterative Traversal starting from vertex {start_vertex}:")

  # DFS 메인 루프
  while stack:
    print(f"  Stack before pop: {stack}", end="")

    # 스택에서 정점을 하나 꺼냄
    current_vertex = stack.pop()
    print(f" -> Pop {current_vertex} -> Stack after pop: {stack}")

    # 아직 탐색되지 않은 정점이라면
    if current_vertex not in explored:
      explored.add(current_vertex)
      dfs_order.append(current_vertex)
      print(f"  Visit: {current_vertex}")

      # 현재 정점의 모든 인접 정점을 스택에 추가 (역순으로)
      # 일관된 순서를 위해 정렬 후 역순으로 추가
      neighbors = sorted(graph.adj_list[current_vertex], reverse=True)
      for neighbor in neighbors:
        if neighbor not in explored:
          stack.append(neighbor)
          print(f"  Push {neighbor} -> Stack: {stack}")
    else:
      print(f"  {current_vertex} already visited, skip")

    print()  # 빈 줄

  print(f"Final traversal order: {' '.join(map(str, dfs_order))}")
  return dfs_order


def dfs_find_path(graph: Graph, start: int, target: int) -> List[int]:
  """
  DFS를 이용한 경로 찾기

  Args:
      graph: 탐색할 그래프
      start: 시작 정점
      target: 목표 정점

  Returns:
      경로를 나타내는 정점 리스트 (경로가 없으면 빈 리스트)
  """
  if start not in graph.get_vertices() or target not in graph.get_vertices():
    return []

  if start == target:
    return [start]

  explored = set()
  parent = {}

  def dfs_visit(vertex: int) -> bool:
    """
    DFS로 목표 정점을 찾는 재귀 함수

    Args:
        vertex: 현재 정점

    Returns:
        목표 정점을 찾았으면 True, 아니면 False
    """
    explored.add(vertex)

    if vertex == target:
      return True

    neighbors = graph.adj_list[vertex]
    for neighbor in neighbors:
      if neighbor not in explored:
        parent[neighbor] = vertex
        if dfs_visit(neighbor):
          return True

    return False

  # DFS로 경로 찾기
  if dfs_visit(start):
    # 경로 재구성
    path = []
    current = target
    while current is not None:
      path.append(current)
      current = parent.get(current)
    return path[::-1]  # 역순으로 반환

  return []  # 경로가 없음


def main():
  """
  메인 함수 - 예제 실행
  """
  print("=== DFS (Depth-First Search) Algorithm ===\n")

  # 그래프 생성 (7개 정점)
  graph = Graph()

  # 간선 추가 (C 코드와 동일한 그래프)
  graph.add_edge(0, 1)
  graph.add_edge(0, 2)
  graph.add_edge(0, 5)
  graph.add_edge(0, 6)
  graph.add_edge(3, 4)
  graph.add_edge(3, 5)
  graph.add_edge(4, 5)
  graph.add_edge(4, 6)

  # 그래프 구조 출력
  graph.print_graph()

  # DFS 실행 (한 개 예제만)
  print("=== DFS Recursive ===")
  dfs_recursive(graph, 0)

  print("\n=== DFS Iterative (with stack visualization) ===")
  dfs_iterative(graph, 0)

  print("\n=== DFS with different graph ===")

  # 다른 그래프 예제
  graph2 = Graph()
  graph2.add_edge(0, 1)
  graph2.add_edge(0, 4)
  graph2.add_edge(1, 2)
  graph2.add_edge(1, 3)
  graph2.add_edge(1, 4)
  graph2.add_edge(2, 3)
  graph2.add_edge(3, 4)

  graph2.print_graph()
  print("=== DFS Recursive ===")
  dfs_recursive(graph2, 0)
  print("\n=== DFS Iterative (with stack visualization) ===")
  dfs_iterative(graph2, 0)


if __name__ == "__main__":
  main()
