"""
Prim MST (Minimum Spanning Tree) 알고리즘 구현 - 우선순위 큐 기반
그래프에서 최소 신장 트리를 찾습니다.

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
    간선 추가 (무방향 가중치 그래프)

    Args:
        src: 시작 정점
        dest: 도착 정점
        weight: 간선의 가중치
    """
    # 무방향 그래프이므로 양방향 추가
    self.adj_list[src].append((dest, weight))
    self.adj_list[dest].append((src, weight))

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


def prim_mst(graph: Graph, start_vertex: int = 0) -> Optional[MST]:
  """
  Prim MST 알고리즘

  Args:
      graph: 가중치 그래프
      start_vertex: 시작 정점 (기본값: 0)

  Returns:
      MST 결과 객체 (연결되지 않은 그래프인 경우 None)
  """
  vertices = graph.num_vertices

  if vertices <= 0:
    print("Invalid graph!")
    return None

  # MST 결과 객체 생성
  mst = MST()

  # 초기화
  in_mst = [False] * vertices      # MST 포함 여부
  key = [float('inf')] * vertices  # 각 정점의 최소 가중치
  parent = [-1] * vertices         # MST에서의 부모 정점

  # 시작 정점 설정
  key[start_vertex] = 0

  # 우선순위 큐 초기화 (최소 힙)
  # (가중치, 정점) 튜플로 저장
  priority_queue = [(key[i], i) for i in range(vertices)]
  heapq.heapify(priority_queue)

  print("=== Prim MST Algorithm (Priority Queue) ===")
  print(f"Starting from vertex {start_vertex}")
  print("Processing vertices in order of minimum key values:\n")

  step = 1

  while priority_queue:
    # 방문하지 않은 정점 중 최소 키 값을 가진 정점 선택
    current_key, u = heapq.heappop(priority_queue)

    # 이미 MST에 포함된 정점이거나 더 좋은 경로가 이미 발견된 경우 스킵
    if in_mst[u] or current_key > key[u]:
      continue

    # 정점을 MST에 추가
    in_mst[u] = True

    if parent[u] != -1:
      edge = Edge(parent[u], u, key[u])
      mst.add_edge(edge)
      print(f"Step {step}: Added edge ({parent[u]}, {u}, {key[u]}) from heap")
      step += 1
    else:
      print(f"Step {step}: Starting vertex {u} (key = {key[u]})")
      step += 1

    # 인접한 정점들의 키 값 업데이트
    for neighbor, weight in graph.adj_list[u]:
      # MST에 포함되지 않았고, 더 작은 가중치를 가진 경우
      if not in_mst[neighbor] and weight < key[neighbor]:
        old_key = key[neighbor]
        key[neighbor] = weight
        parent[neighbor] = u

        # 새로운 키 값으로 우선순위 큐에 추가 (decreaseKey 효과)
        heapq.heappush(priority_queue, (weight, neighbor))

        print(
            f"  Updated key[{neighbor}] = {weight} (via {u}), was {old_key if old_key != float('inf') else 'INF'}")

    # 현재 MST에 포함된 정점들 출력
    mst_vertices = [i for i in range(vertices) if in_mst[i]]
    print(f"  Current MST vertices: {mst_vertices}")
    print()

    # MST 완성 확인
    if len(mst.edges) >= vertices - 1:
      break

  return mst


def main():
  """
  메인 함수 - 예제 실행
  """
  print("=== Prim MST Algorithm (Priority Queue) ===\n")

  # 그래프 생성 (8개 정점: 0-7)
  graph = Graph(8)

  # 간선 추가 (가중치 그래프) - Kruskal과 동일한 그래프
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

  # Prim MST 실행 (정점 0에서 시작)
  mst = prim_mst(graph, 0)
  if mst:
    mst.print_mst()


if __name__ == "__main__":
  main()
