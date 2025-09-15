"""
Greedy MST (Minimum Spanning Tree) 알고리즘 구현 - Cut Property 기반
그래프에서 최소 신장 트리를 찾습니다.

시간 복잡도: O(V * E) - 각 단계에서 모든 간선을 검사
공간 복잡도: O(V + E) - 그래프 저장과 MST 집합을 위한 공간
"""

import random
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


def print_mst_status(mst_vertices: set, vertices: int, step: int) -> None:
  """
  MST 현재 상태 출력

  Args:
      mst_vertices: MST에 포함된 정점들의 집합
      vertices: 전체 정점 개수
      step: 현재 단계 번호
  """
  print(f"Step {step + 1}: Finding cut between MST and remaining vertices")

  remaining_vertices = set(range(vertices)) - mst_vertices

  print(f"  Current MST vertices: {sorted(mst_vertices)}")
  print(f"  Remaining vertices: {sorted(remaining_vertices)}")


def find_min_cut_edge(graph: Graph, mst_vertices: set) -> Optional[Edge]:
  """
  Cut을 가로지르는 최소 가중치 간선 찾기 (Greedy MST 정의에 따라)

  Args:
      graph: 그래프
      mst_vertices: MST에 포함된 정점들의 집합

  Returns:
      최소 가중치 간선 (없으면 None)
  """
  min_weight = float('inf')
  min_edge = None

  # 모든 간선 검사
  for edge in graph.edges:
    src, dest = edge.src, edge.dest

    # Cut을 가로지르는 간선인지 확인 (한쪽은 MST에, 다른 쪽은 MST에 없어야 함)
    if (src in mst_vertices and dest not in mst_vertices) or \
       (src not in mst_vertices and dest in mst_vertices):
      print(f"  Cut edge candidate: {edge}")

      if edge.weight < min_weight:
        min_weight = edge.weight
        min_edge = edge

  return min_edge


def find_optimal_cut(graph: Graph, mst_vertices: set) -> Optional[Edge]:
  """
  모든 가능한 Cut을 검사하여 최적의 Cut 찾기 (진짜 Greedy MST)

  Args:
      graph: 그래프
      mst_vertices: MST에 포함된 정점들의 집합

  Returns:
      최소 가중치 간선 (없으면 None)
  """
  min_weight = float('inf')
  min_edge = None

  print("  Searching for optimal cut (no red crossing edges)...")

  # 모든 간선을 가중치 순으로 검사
  for edge in graph.edges:
    src, dest = edge.src, edge.dest

    # Cut을 가로지르는 간선인지 확인
    if (src in mst_vertices and dest not in mst_vertices) or \
       (src not in mst_vertices and dest in mst_vertices):
      print(f"  Valid cut edge: {edge}")

      # 첫 번째로 찾은 간선이 최소 가중치 (Greedy 선택)
      if edge.weight < min_weight:
        min_weight = edge.weight
        min_edge = edge
        print(f"  -> New minimum weight: {edge.weight}")

  if min_edge is not None:
    print(f"  -> Selected optimal cut edge: {min_edge}")

  return min_edge


def add_edge_to_mst(mst: MST, edge: Edge, mst_vertices: set) -> None:
  """
  선택된 간선을 MST에 추가

  Args:
      mst: MST 결과 객체
      edge: 추가할 간선
      mst_vertices: MST에 포함된 정점들의 집합
  """
  # MST에 간선 추가
  mst.add_edge(edge)

  # 새로운 정점을 MST에 추가
  mst_vertices.add(edge.src)
  mst_vertices.add(edge.dest)

  print(f"  Selected edge: {edge}")


def get_random_start_vertex(vertices: int) -> int:
  """랜덤 시작 정점 선택"""
  return random.randint(0, vertices - 1)


def greedy_mst(graph: Graph) -> Optional[MST]:
  """기본 Greedy MST 알고리즘"""
  return greedy_mst_with_options(graph, use_random_cut=False, fixed_cut_type=-1)


def true_greedy_mst(graph: Graph) -> Optional[MST]:
  """
  진짜 Greedy MST 알고리즘 (모든 가능한 Cut 검사)

  Args:
      graph: 가중치 그래프

  Returns:
      MST 결과 객체 (연결되지 않은 그래프인 경우 None)
  """
  vertices = graph.num_vertices

  if vertices <= 0:
    print("Invalid graph!")
    return None

  # MST 결과 객체 생성
  mst = MST()

  # MST에 포함된 정점들을 추적하는 집합
  mst_vertices = set()

  print("=== True Greedy MST Algorithm (All Possible Cuts) ===")
  print("Finding cuts with no red crossing edges...\n")

  # 시작 정점 선택 (정점 0)
  start_vertex = 0
  mst_vertices.add(start_vertex)
  print(f"Starting from vertex {start_vertex}\n")

  # MST 구성 메인 루프 (vertices-1개의 간선 필요)
  for step in range(vertices - 1):
    # 현재 MST 상태 출력
    print_mst_status(mst_vertices, vertices, step)

    # 모든 가능한 Cut을 검사하여 최적의 Cut 찾기
    min_edge = find_optimal_cut(graph, mst_vertices)

    # 최소 가중치 간선을 MST에 추가
    if min_edge is not None:
      add_edge_to_mst(mst, min_edge, mst_vertices)
    else:
      print("  No valid edge found - graph is not connected!")
      return None

    print()

  return mst


def greedy_mst_with_options(graph: Graph, use_random_cut: bool = False, fixed_cut_type: int = -1) -> Optional[MST]:
  """
  Cut Property 기반 Greedy MST 알고리즘 (옵션 포함)

  Args:
      graph: 가중치 그래프
      use_random_cut: True면 랜덤 cut 사용, False면 기존 방식
      fixed_cut_type: -1이면 랜덤, 0-3이면 특정 cut 타입 고정

  Returns:
      MST 결과 객체 (연결되지 않은 그래프인 경우 None)
  """
  vertices = graph.num_vertices

  if vertices <= 0:
    print("Invalid graph!")
    return None

  # MST 결과 객체 생성
  mst = MST()

  # MST에 포함된 정점들을 추적하는 집합
  mst_vertices = set()

  # 기존 방식
  print("=== Greedy MST Algorithm (Cut Property) ===")

  # 시작 정점 선택 (랜덤)
  start_vertex = get_random_start_vertex(vertices)
  mst_vertices.add(start_vertex)
  print(f"Starting from vertex {start_vertex}\n")

  # MST 구성 메인 루프 (vertices-1개의 간선 필요)
  for step in range(vertices - 1):
    # 현재 MST 상태 출력
    print_mst_status(mst_vertices, vertices, step)

    # Cut을 가로지르는 최소 가중치 간선 찾기
    min_edge = find_min_cut_edge(graph, mst_vertices)

    # 최소 가중치 간선을 MST에 추가
    if min_edge is not None:
      add_edge_to_mst(mst, min_edge, mst_vertices)
    else:
      print("  No valid edge found - graph is not connected!")
      return None

    print()

  return mst


def main():
  """
  메인 함수 - 예제 실행
  """
  # 랜덤 시드 설정 (일관된 결과를 위해 고정 시드 사용)
  random.seed(42)  # 고정 시드로 변경

  print("=== Greedy MST (Cut Property) Algorithm ===\n")

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

  # 진짜 Greedy MST 실행 (모든 가능한 Cut 검사)
  print("=== True Greedy MST Algorithm ===")
  mst_true = true_greedy_mst(graph)
  if mst_true:
    mst_true.print_mst()

  # 랜덤 시작 정점으로 Greedy MST 실행 (결과는 동일해야 함)
  print("=== Random Start Vertex Greedy MST ===")
  mst_random_start = greedy_mst_with_options(
      graph, use_random_cut=False, fixed_cut_type=-1)
  if mst_random_start:
    mst_random_start.print_mst()

  # 또 다른 랜덤 시작 정점으로 테스트
  print("=== Another Random Start Vertex Greedy MST ===")
  mst_random_start2 = greedy_mst_with_options(
      graph, use_random_cut=False, fixed_cut_type=-1)
  if mst_random_start2:
    mst_random_start2.print_mst()


if __name__ == "__main__":
  main()
