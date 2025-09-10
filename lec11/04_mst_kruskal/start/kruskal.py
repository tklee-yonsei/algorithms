"""
Kruskal MST (Minimum Spanning Tree) 알고리즘 구현 - Union-Find 기반
그래프에서 최소 신장 트리를 찾습니다.

시간 복잡도: O(E log E) - 간선 정렬이 지배적
공간 복잡도: O(V + E) - 그래프 저장과 Union-Find 자료구조
"""

from typing import List, Tuple, Optional


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

  def __lt__(self, other):
    """정렬을 위한 비교 연산자"""
    return self.weight < other.weight


class Graph:
  """
  그래프 클래스 (간선 리스트로 표현)
  """

  def __init__(self, num_vertices: int):
    """
    그래프 초기화

    Args:
        num_vertices: 정점의 개수
    """
    self.num_vertices = num_vertices
    self.edges: List[Edge] = []

  def add_edge(self, src: int, dest: int, weight: int) -> None:
    """
    간선 추가 (무방향 가중치 그래프)

    Args:
        src: 시작 정점
        dest: 도착 정점
        weight: 간선의 가중치
    """
    # 무방향 그래프이므로 한 번만 추가 (중복 방지)
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


class ComponentTracker:
  """연결 성분을 추적하는 간단한 클래스"""

  def __init__(self, vertices: int):
    """
    연결 성분 추적기 초기화

    Args:
        vertices: 정점의 개수
    """
    # 각 정점을 자기 자신만의 연결 성분으로 초기화
    self.component = list(range(vertices))
    self.vertices = vertices

  def is_connected(self, u: int, v: int) -> bool:
    """
    두 정점이 같은 연결 성분에 속하는지 확인

    Args:
        u: 첫 번째 정점
        v: 두 번째 정점

    Returns:
        같은 연결 성분에 속하면 True, 아니면 False
    """
    return self.component[u] == self.component[v]

  def merge_components(self, u: int, v: int) -> None:
    """
    두 연결 성분을 합치기 (간선 추가 시)

    Args:
        u: 첫 번째 정점
        v: 두 번째 정점
    """
    old_component = self.component[v]
    new_component = self.component[u]

    # v의 연결 성분에 속한 모든 정점을 u의 연결 성분으로 변경
    for i in range(self.vertices):
      if self.component[i] == old_component:
        self.component[i] = new_component


class MST:
  """MST 결과 클래스"""

  def __init__(self):
    self.edges: List[Edge] = []
    self.total_weight = 0

  def add_edge(self, edge: Edge) -> None:
    """MST에 간선 추가"""
    self.edges.append(edge)
    self.total_weight += edge.weight

  def print_mst(self) -> None:
    """MST 결과 출력"""
    if not self.edges:
      print("No MST found!")
      return

    print("=== MST Result ===")
    print("MST Edges:")
    for edge in self.edges:
      print(f"  {edge.src} - {edge.dest} : {edge.weight}")
    print(f"Total Weight: {self.total_weight}\n")


def kruskal_mst(graph: Graph) -> Optional[MST]:
  """
  Kruskal MST 알고리즘

  Args:
      graph: 가중치 그래프

  Returns:
      MST 결과 객체 (연결되지 않은 그래프인 경우 None)
  """
  vertices = graph.num_vertices
  num_edges = len(graph.edges)

  if vertices <= 0 or num_edges <= 0:
    print("Invalid graph!")
    return None

  # TODO: 이 함수를 완성하세요!
  #
  # 힌트:
  # 1. MST 결과 객체 생성 (MST())
  # 2. 간선들을 가중치 오름차순으로 정렬 (sorted() 함수 사용)
  # 3. ComponentTracker 초기화
  # 4. 정렬된 간선들을 순서대로 검사하면서:
  #    - is_connected로 사이클 검사
  #    - 사이클이 없으면 MST에 추가하고 merge_components로 합치기
  #    - MST가 완성되면 (V-1개 간선) 종료
  # 5. MST 반환

  print("=== Kruskal MST Algorithm ===")
  print("Processing edges in order of increasing weight:\n")

  # 여기에 코드를 작성하세요!

  return None


def main():
  """
  메인 함수 - 예제 실행
  """
  print("=== Kruskal MST Algorithm ===\n")

  # 그래프 생성 (8개 정점: 0-7)
  graph = Graph(8)

  # 간선 추가 (가중치 그래프) - 이미지의 그래프 기준
  # 정점: 0, 1, 2, 3, 4, 5, 6, 7
  graph.add_edge(0, 7, 16)   # 0.16 * 100
  graph.add_edge(2, 3, 17)   # 0.17 * 100
  graph.add_edge(1, 7, 19)   # 0.19 * 100
  graph.add_edge(0, 2, 26)   # 0.26 * 100
  graph.add_edge(5, 7, 28)   # 0.28 * 100
  graph.add_edge(1, 3, 29)   # 0.29 * 100
  graph.add_edge(1, 5, 32)   # 0.32 * 100
  graph.add_edge(2, 7, 34)   # 0.34 * 100
  graph.add_edge(4, 5, 35)   # 0.35 * 100
  graph.add_edge(1, 2, 36)   # 0.36 * 100
  graph.add_edge(4, 7, 37)   # 0.37 * 100
  graph.add_edge(0, 4, 38)   # 0.38 * 100
  graph.add_edge(6, 2, 40)   # 0.40 * 100
  graph.add_edge(3, 6, 52)   # 0.52 * 100
  graph.add_edge(6, 0, 58)   # 0.58 * 100
  graph.add_edge(6, 4, 93)   # 0.93 * 100

  # 그래프 구조 출력
  graph.print_graph()

  # Kruskal MST 실행
  mst = kruskal_mst(graph)
  if mst:
    mst.print_mst()


if __name__ == "__main__":
  main()
