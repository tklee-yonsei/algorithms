"""
BFS (Breadth-First Search) 알고리즘 구현
그래프에서 너비 우선 탐색을 수행합니다.

시간 복잡도: O(V + E) - V는 정점 수, E는 간선 수
공간 복잡도: O(V) - 큐와 방문 집합을 위한 공간
"""

from collections import deque, defaultdict
from typing import List, Dict, Set


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


def bfs(graph: Graph, start_vertex: int) -> List[int]:
  """
  BFS 알고리즘 구현

  Args:
      graph: 탐색할 그래프
      start_vertex: 시작 정점

  Returns:
      BFS 탐색 순서의 정점 리스트
  """
  if start_vertex not in graph.get_vertices():
    print(f"Invalid start vertex: {start_vertex}")
    return []

  # 방문 상태를 추적하는 집합
  explored = set()

  # 큐 초기화 (deque 사용)
  queue = deque()

  # 시작 정점을 explored로 표시하고 큐에 추가
  explored.add(start_vertex)
  queue.append(start_vertex)

  # BFS 탐색 결과를 저장할 리스트
  bfs_order = []

  print(f"BFS Traversal starting from vertex {start_vertex}: ", end="")

  # BFS 메인 루프
  while queue:
    # 큐에서 정점을 하나 꺼냄
    current_vertex = queue.popleft()
    bfs_order.append(current_vertex)
    print(current_vertex, end=" ")

    # 현재 정점의 모든 인접 정점을 확인
    # 정렬해서 일관된 순서로 탐색
    neighbors = sorted(graph.adj_list[current_vertex])
    for neighbor in neighbors:
      # 인접 정점이 아직 탐색되지 않았다면
      if neighbor not in explored:
        explored.add(neighbor)
        queue.append(neighbor)

  print()  # 줄바꿈
  return bfs_order


def bfs_with_levels(graph: Graph, start_vertex: int) -> Dict[int, int]:
  """
  레벨 정보와 함께 BFS 실행
  각 정점까지의 최단 거리(레벨)를 계산

  Args:
      graph: 탐색할 그래프
      start_vertex: 시작 정점

  Returns:
      각 정점의 레벨을 담은 딕셔너리
  """
  if start_vertex not in graph.get_vertices():
    print(f"Invalid start vertex: {start_vertex}")
    return {}

  explored = set()
  queue = deque()
  levels = {}

  # 시작 정점 초기화
  explored.add(start_vertex)
  queue.append(start_vertex)
  levels[start_vertex] = 0

  print(f"BFS with levels from vertex {start_vertex}:")

  while queue:
    current_vertex = queue.popleft()
    current_level = levels[current_vertex]

    print(f"Vertex {current_vertex} (level {current_level})")

    # 인접 정점들 처리
    neighbors = sorted(graph.adj_list[current_vertex])
    for neighbor in neighbors:
      if neighbor not in explored:
        explored.add(neighbor)
        queue.append(neighbor)
        levels[neighbor] = current_level + 1

  return levels


def bfs_shortest_path(graph: Graph, start: int, target: int) -> List[int]:
  """
  BFS를 이용한 최단 경로 찾기 (무가중 그래프)

  Args:
      graph: 탐색할 그래프
      start: 시작 정점
      target: 목표 정점

  Returns:
      최단 경로를 나타내는 정점 리스트
  """
  if start not in graph.get_vertices() or target not in graph.get_vertices():
    return []

  if start == target:
    return [start]

  explored = set()
  queue = deque()
  parent = {}

  explored.add(start)
  queue.append(start)
  parent[start] = None

  while queue:
    current_vertex = queue.popleft()

    neighbors = graph.adj_list[current_vertex]
    for neighbor in neighbors:
      if neighbor not in explored:
        explored.add(neighbor)
        queue.append(neighbor)
        parent[neighbor] = current_vertex

        # 목표 정점에 도달했으면 경로 재구성
        if neighbor == target:
          path = []
          current = target
          while current is not None:
            path.append(current)
            current = parent[current]
          return path[::-1]  # 역순으로 반환

  return []  # 경로가 없음


def main():
  """
  메인 함수 - 예제 실행
  """
  print("=== BFS (Breadth-First Search) Algorithm ===\n")

  # 그래프 생성 (7개 정점)
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

  # 각 정점에서 시작하는 BFS 실행
  print("BFS traversals:")
  for vertex in sorted(graph.get_vertices()):
    bfs(graph, vertex)

  print("\n=== BFS with different graph ===")

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
  bfs(graph2, 0)


if __name__ == "__main__":
  main()
