"""
Greedy MST (Minimum Spanning Tree) 알고리즘 구현 - Cut Property 기반 (시작 템플릿)
그래프에서 최소 신장 트리를 찾습니다.

TODO: 아래 함수들을 완성하세요.
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


class Graph:
  """
  그래프 클래스 (간선 리스트로 표현)
  """

  def __init__(self, num_vertices: int):
    """그래프 초기화"""
    self.num_vertices = num_vertices
    self.edges: List[Edge] = []

  def add_edge(self, src: int, dest: int, weight: int) -> None:
    """
    간선 추가 (무방향 가중치 그래프)

    TODO: 무방향 그래프에 간선을 추가하는 코드를 작성하세요.
    무방향 그래프이므로 한 번만 추가하면 됩니다.

    Args:
        src: 시작 정점
        dest: 도착 정점
        weight: 간선의 가중치
    """
    # TODO: 구현하세요
    pass

  def print_graph(self) -> None:
    """그래프 구조 출력 (디버깅용)"""
    print("Graph representation (edge list):")
    print(f"Vertices: {self.num_vertices}, Edges: {len(self.edges)}")
    for i, edge in enumerate(self.edges):
      print(f"  Edge {i}: {edge}")
    print()


class MST:
  """MST 결과 클래스"""

  def __init__(self):
    self.edges: List[Edge] = []
    self.total_weight = 0

  def add_edge(self, edge: Edge) -> None:
    """
    MST에 간선 추가

    TODO: MST에 간선을 추가하고 총 가중치를 업데이트하세요.
    """
    # TODO: 구현하세요
    pass

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


def greedy_mst(graph: Graph) -> Optional[MST]:
  """
  Cut Property 기반 Greedy MST 알고리즘

  TODO: Cut Property를 이용한 Greedy MST 알고리즘을 구현하세요.

  구현 단계:
  1. MST 결과 객체와 MST에 포함된 정점들을 추적하는 집합 생성
  2. 시작 정점 선택 (예: 정점 0)
  3. MST 구성 메인 루프 (vertices-1개의 간선 필요):
     - Cut을 가로지르는 모든 간선 검사
     - 최소 가중치 간선 선택
     - 선택된 간선을 MST에 추가
     - 새로운 정점을 MST 집합에 추가

  Args:
      graph: 가중치 그래프

  Returns:
      MST 결과 객체 (연결되지 않은 그래프인 경우 None)
  """
  vertices = graph.num_vertices

  if vertices <= 0:
    print("Invalid graph!")
    return None

  # TODO: MST 결과 객체 생성
  mst = MST()

  # TODO: MST에 포함된 정점들을 추적하는 집합 생성
  mst_vertices = set()

  # TODO: 시작 정점 선택 및 추가
  start_vertex = 0

  print("=== Greedy MST Algorithm (Cut Property) ===")
  print(f"Starting from vertex {start_vertex}\n")

  # TODO: MST 구성 메인 루프 구현
  for step in range(vertices - 1):
    print(f"Step {step + 1}: Finding cut between MST and remaining vertices")

    # TODO: Cut을 가로지르는 최소 가중치 간선 찾기
    min_weight = float('inf')
    min_edge = None

    # TODO: 현재 MST 정점들과 나머지 정점들 출력

    # TODO: 모든 간선을 검사하여 Cut을 가로지르는 간선 찾기
    for edge in graph.edges:
      src, dest = edge.src, edge.dest

      # TODO: Cut을 가로지르는 간선인지 확인
      # (한쪽은 MST에, 다른 쪽은 MST에 없어야 함)
      pass

    # TODO: 최소 가중치 간선을 MST에 추가
    if min_edge is not None:
      # TODO: MST에 간선 추가
      # TODO: 새로운 정점을 MST에 추가
      pass
    else:
      print("  No valid edge found - graph is not connected!")
      return None

    print()

  return mst


def main():
  """
  메인 함수 - 예제 실행
  """
  print("=== Greedy MST (Cut Property) Algorithm ===\n")

  # 그래프 생성 (6개 정점)
  graph = Graph(6)

  # 간선 추가
  graph.add_edge(0, 1, 2)
  graph.add_edge(0, 3, 6)
  graph.add_edge(1, 2, 3)
  graph.add_edge(1, 3, 8)
  graph.add_edge(1, 4, 5)
  graph.add_edge(2, 5, 7)
  graph.add_edge(3, 4, 9)
  graph.add_edge(4, 5, 4)

  # 그래프 구조 출력
  graph.print_graph()

  # Greedy MST 실행
  mst = greedy_mst(graph)
  if mst:
    mst.print_mst()


if __name__ == "__main__":
  main()
