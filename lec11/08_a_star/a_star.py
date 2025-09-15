"""
A* 최단 경로 알고리즘 구현 - 휴리스틱 기반 탐색
다익스트라 알고리즘에 휴리스틱 함수를 추가하여 목표 지향적 탐색을 수행합니다.

전제조건: 
- 모든 간선의 가중치는 0 이상
- 휴리스틱 함수는 admissible해야 함 (실제 거리를 과대평가하지 않음)

시간 복잡도: O(b^d) where b=branching factor, d=depth
공간 복잡도: O(b^d) - open과 closed list 저장
"""

import heapq
from typing import List, Tuple, Optional, Dict, Callable


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


class AStarResult:
  """A* 탐색 결과 클래스"""

  def __init__(self):
    self.path: List[int] = []
    self.total_cost: int = 0

  def print_result(self, start_vertex: int, goal_vertex: int) -> None:
    """A* 탐색 결과 출력"""
    if not self.path:
      print("No path found!")
      return

    print("=== A* Search Result ===")
    print(f"Shortest path from vertex {start_vertex} to vertex {goal_vertex}:")
    print(f"Total cost: {self.total_cost}")

    # 경로 출력
    print(f"Path: {' -> '.join(map(str, self.path))}")
    print()


def heuristic(vertex: int, goal: int) -> int:
  """
  휴리스틱 함수 - 이미지 데이터 사용

  Args:
      vertex: 현재 정점
      goal: 목표 정점

  Returns:
      휴리스틱 값 (추정 거리)
  """
  # 이미지에서 제공된 휴리스틱 값들
  h_values = [14, 10, 4, 2, 11, 6, 0, 8]
  return h_values[vertex]


def a_star(graph: Graph, start_vertex: int, goal_vertex: int) -> Optional[AStarResult]:
  """
  A* 최단 경로 알고리즘

  Args:
      graph: 가중치 그래프
      start_vertex: 시작 정점
      goal_vertex: 목표 정점

  Returns:
      A* 탐색 결과 객체 (경로를 찾지 못한 경우 None)
  """
  vertices = graph.num_vertices

  if vertices <= 0:
    print("Invalid graph!")
    return None

  # A* 탐색 결과 객체 생성
  result = AStarResult()

  # 초기화
  g_score: Dict[int, float] = {i: float('inf') for i in range(vertices)}  # 실제 거리
  f_score: Dict[int, float] = {i: float('inf')
                               for i in range(vertices)}  # f(n) = g(n) + h(n)
  came_from: Dict[int, int] = {}  # 경로 추적
  closed_set: set = set()  # closed set

  # 우선순위 큐 초기화 (open list)
  # (f_score, vertex) 튜플로 저장
  open_list = []

  # 시작 정점 설정
  g_score[start_vertex] = 0
  f_score[start_vertex] = heuristic(start_vertex, goal_vertex)
  heapq.heappush(open_list, (f_score[start_vertex], start_vertex))

  print("=== A* Search Algorithm ===")
  print(f"Starting A* search from {start_vertex} to {goal_vertex}")
  print(
      f"Initial heuristic h({start_vertex}) = {heuristic(start_vertex, goal_vertex)}\n")

  step = 1

  while open_list:
    # f값이 가장 작은 정점 선택
    current_f, current = heapq.heappop(open_list)

    # 이미 closed set에 있는 정점은 스킵
    if current in closed_set:
      continue

    print(f"Step {step}: Exploring vertex {current} with f={int(current_f)}")
    step += 1

    # 목표에 도달했는지 확인
    if current == goal_vertex:
      print("Goal reached! Reconstructing path...")

      # 경로 재구성
      path = []
      node = current

      while node is not None:
        path.append(node)
        node = came_from.get(node)

      # 경로를 올바른 순서로 뒤집기
      path.reverse()
      result.path = path
      result.total_cost = int(g_score[goal_vertex])

      return result

    # 현재 정점을 closed set에 추가
    closed_set.add(current)

    # 인접한 정점들 탐색
    for neighbor, weight in graph.adj_list[current]:
      # 이미 closed set에 있는 정점은 스킵
      if neighbor in closed_set:
        continue

      # 임시 g 점수 계산
      tentative_g_score = g_score[current] + weight

      print(f"  Checking neighbor {neighbor} with tentative g={int(tentative_g_score)}")

      # 더 나은 경로를 발견했거나 처음 방문하는 정점인 경우
      if g_score[neighbor] == float('inf') or tentative_g_score < g_score[neighbor]:
        # 경로 정보 업데이트
        came_from[neighbor] = current
        g_score[neighbor] = tentative_g_score
        f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal_vertex)

        print(f"    Updated: g({neighbor})={int(g_score[neighbor])}, "
              f"h({neighbor})={heuristic(neighbor, goal_vertex)}, "
              f"f({neighbor})={int(f_score[neighbor])}")

        # open list에 추가
        heapq.heappush(open_list, (f_score[neighbor], neighbor))
        print(f"    Added to open list")

    # 현재 open list 출력 (중복 제거된 상태로)
    open_vertices = set()
    open_list_items = []
    for f, v in open_list:
      if v not in closed_set and v not in open_vertices:
        open_list_items.append((v, int(f)))
        open_vertices.add(v)

    open_list_str = ", ".join([f"({v},f={f})" for v, f in sorted(open_list_items)])
    print(f"  Current open list: [{open_list_str}]")
    print()

  # 경로를 찾지 못한 경우
  print(f"No path found from {start_vertex} to {goal_vertex}")
  return None


def print_heuristics(vertices: int, goal_vertex: int) -> None:
  """휴리스틱 값 출력"""
  print(f"Heuristic values (h) from each vertex to goal {goal_vertex}:")
  for i in range(vertices):
    print(f"  h({i}) = {heuristic(i, goal_vertex)}")
  print()


def main():
  """
  메인 함수 - 예제 실행
  """
  print("=== A* Search Algorithm ===\n")

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

  # 휴리스틱 값 출력
  print_heuristics(8, 6)

  # A* 탐색 실행 (정점 0에서 시작, 정점 6이 목표)
  result = a_star(graph, 0, 6)
  if result:
    result.print_result(0, 6)


if __name__ == "__main__":
  main()
