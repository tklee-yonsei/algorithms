"""
Dijkstra 최단 경로 알고리즘 구현 - 우선순위 큐 기반
가중치 있는 방향 그래프에서 한 정점으로부터 모든 정점까지의 최단 경로를 찾습니다.

전제조건: 모든 간선의 가중치는 0 이상이어야 함 (음의 가중치 불허)

시간 복잡도: O(E log V) - 우선순위 큐 사용
공간 복잡도: O(V + E) - 그래프 저장과 우선순위 큐
"""

import heapq
from typing import List, Tuple, Optional, Dict


class Edge:
  """간선 클래스"""

  def __init__(self, src: int, dest: int, weight: int):
    self.src = src
    self.dest = dest
    self.weight = weight

  def __str__(self):
    return f"({self.src}, {self.dest}, {self.weight})"

  def __repr__(self):
    return self.__str__()


class Graph:
  """
  그래프 클래스 (인접 리스트로 표현)
  """

  def __init__(self, num_vertices: int):
    """
    그래프 초기화

    Args:
        num_vertices: 정점의 개수
    """
    self.num_vertices = num_vertices
    # 인접 리스트: {vertex: [(neighbor, weight), ...]}
    self.adj_list: Dict[int, List[Tuple[int, int]]] = {
        i: [] for i in range(num_vertices)}
    self.edges: List[Edge] = []

  def add_edge(self, src: int, dest: int, weight: int) -> None:
    """
    간선 추가 (방향 가중치 그래프)

    Args:
        src: 시작 정점
        dest: 도착 정점
        weight: 간선의 가중치
    """
    # 방향 그래프이므로 한 방향만 추가
    self.adj_list[src].append((dest, weight))

    # 간선 리스트에도 추가 (출력용)
    edge = Edge(src, dest, weight)
    self.edges.append(edge)

  def print_graph(self) -> None:
    """
    그래프 구조 출력 (디버깅용)
    """
    print("Graph representation (edge list):")
    print(f"Vertices: {self.num_vertices}, Edges: {len(self.edges)}")
    for i, edge in enumerate(self.edges):
      print(f"  Edge {i}: {edge}")
    print()


class ShortestPath:
  """최단 경로 결과 클래스"""

  def __init__(self, num_vertices: int):
    self.num_vertices = num_vertices
    self.distances: List[float] = [float('inf')] * num_vertices
    self.parents: List[int] = [-1] * num_vertices

  def print_shortest_paths(self, start_vertex: int) -> None:
    """최단 경로 결과 출력"""
    print("=== Shortest Path Results ===")
    print(f"Shortest distances from vertex {start_vertex}:")
    for i in range(self.num_vertices):
      if self.distances[i] == float('inf'):
        print(f"  Vertex {i}: unreachable")
      else:
        print(f"  Vertex {i}: {int(self.distances[i])}")
    print()

  def print_path(self, start_vertex: int, target_vertex: int) -> None:
    """특정 정점까지의 경로 출력"""
    if self.distances[target_vertex] == float('inf'):
      print(f"No path from vertex {start_vertex} to vertex {target_vertex}")
      return

    print(f"Shortest path from vertex {start_vertex} to vertex {target_vertex}:")
    print(f"Distance: {int(self.distances[target_vertex])}")

    # 경로 재구성
    path = []
    current = target_vertex

    while current != -1:
      path.append(current)
      current = self.parents[current]

    # 경로 출력
    path.reverse()
    print(f"Path: {' -> '.join(map(str, path))}")
    print()


def dijkstra(graph: Graph, start_vertex: int = 0) -> Optional[ShortestPath]:
  """
  Dijkstra 최단 경로 알고리즘

  Args:
      graph: 가중치 그래프
      start_vertex: 시작 정점 (기본값: 0)

  Returns:
      최단 경로 결과 객체 (연결되지 않은 그래프인 경우 None)
  """
  vertices = graph.num_vertices

  if vertices <= 0:
    print("Invalid graph!")
    return None

  # TODO: 이 함수를 완성하세요!
  #
  # 힌트 (우선순위 큐 기반):
  # 1. 최단 경로 결과 객체 생성 (ShortestPath(vertices))
  # 2. visited, distances, parents 배열들 초기화
  #    - visited[i]: 정점 i가 방문되었는지 (초기값: False)
  #    - distances[i]: 정점 i까지의 최단 거리 (초기값: float('inf'))
  #    - parents[i]: 최단 경로에서 정점 i의 부모 (초기값: -1)
  # 3. 시작 정점의 distances를 0으로 설정
  # 4. 우선순위 큐 초기화 (heapq 사용)
  #    - 모든 정점을 (거리, 정점번호) 튜플로 큐에 추가
  # 5. 우선순위 큐가 빌 때까지 반복:
  #    - heappop으로 최소 거리를 가진 정점 선택
  #    - 이미 방문했거나 더 좋은 경로가 있으면 스킵
  #    - 정점을 visited로 표시
  #    - 인접한 정점들의 distances 값 업데이트 (heappush로 큐에 추가)
  # 6. 최단 경로 결과 반환

  print("=== Dijkstra Shortest Path Algorithm (Priority Queue) ===")
  print(f"Starting from vertex {start_vertex}")
  print("Processing vertices in order of minimum distances:\n")

  # 여기에 코드를 작성하세요!

  return None


def main():
  """
  메인 함수 - 예제 실행
  """
  print("=== Dijkstra Shortest Path Algorithm (Priority Queue) ===\n")

  # 그래프 생성 (8개 정점: 0-7)
  graph = Graph(8)

  # 간선 추가 (방향 가중치 그래프) - 이미지 데이터 사용
  # 정점: 0, 1, 2, 3, 4, 5, 6, 7
  graph.add_edge(0, 1, 5)   # 0→1
  graph.add_edge(0, 4, 9)   # 0→4
  graph.add_edge(0, 7, 8)   # 0→7
  graph.add_edge(1, 2, 12)  # 1→2
  graph.add_edge(1, 3, 15)  # 1→3
  graph.add_edge(1, 7, 4)   # 1→7
  graph.add_edge(2, 3, 3)   # 2→3
  graph.add_edge(2, 6, 11)  # 2→6
  graph.add_edge(3, 6, 9)   # 3→6
  graph.add_edge(4, 5, 4)   # 4→5
  graph.add_edge(4, 6, 20)  # 4→6
  graph.add_edge(4, 7, 5)   # 4→7
  graph.add_edge(5, 2, 1)   # 5→2
  graph.add_edge(5, 6, 13)  # 5→6
  graph.add_edge(7, 5, 6)   # 7→5
  graph.add_edge(7, 2, 7)   # 7→2

  # 그래프 구조 출력
  graph.print_graph()

  # Dijkstra 최단 경로 실행 (정점 0에서 시작)
  result = dijkstra(graph, 0)
  if result:
    result.print_shortest_paths(0)

    # 특정 정점까지의 경로 출력
    result.print_path(0, 6)
    result.print_path(0, 3)
    result.print_path(0, 7)


if __name__ == "__main__":
  main()
