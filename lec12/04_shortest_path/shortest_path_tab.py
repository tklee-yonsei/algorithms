import sys


def shortest_path_tab(graph, start, end):
  n = len(graph)
  # DP 테이블 초기화 [노드][단계]
  dp_table = [[1000000 for _ in range(4)] for _ in range(n)]

  dp_table[end][3] = 0  # 목적지에서 3단계 완료시 거리는 0

  print("=== 3단계 최단 경로 찾기 (테이블레이션) ===")
  print(f"시작 노드: {start}, 목적지 노드: {end}, 정확히 3단계로 이동\n")

  # 역방향으로 단계별 계산
  for step in range(2, -1, -1):
    print(f"단계 {step + 1} 계산:")
    updated = False

    # 모든 노드에 대해
    for v in range(n):
      if dp_table[v][step + 1] == 1000000:
        continue

      # v로 들어오는 모든 간선 확인
      for u in range(n):
        if u in graph and v in graph[u]:
          weight = graph[u][v]
          new_dist = dp_table[v][step + 1] + weight
          if new_dist < dp_table[u][step]:
            print(
                f"  노드 {u} ← {v}: {dp_table[v][step + 1]} + {weight} = {new_dist} (이전: {dp_table[u][step]})")
            dp_table[u][step] = new_dist
            updated = True

    if not updated:
      print("  더 이상 업데이트되지 않음.")
    print()

  return dp_table[start][0]


if __name__ == "__main__":
  # 그래프 초기화 (이미지의 그래프 구조)
  graph = {
      0: {1: 1, 2: 2},    # 0 → 1: 가중치 1, 0 → 2: 가중치 2
      1: {3: 6},          # 1 → 3: 가중치 6
      2: {1: 2, 3: 4, 4: 3},  # 2 → 1: 가중치 2, 2 → 3: 가중치 4, 2 → 4: 가중치 3
      3: {5: 3},          # 3 → 5: 가중치 3
      4: {3: 1, 5: 5},    # 4 → 3: 가중치 1, 4 → 5: 가중치 5
      5: {}               # 5는 끝 노드
  }

  result = shortest_path_tab(graph, 0, 3)

  if result == 1000000:
    print("결과: 3단계로 도달할 수 있는 경로가 존재하지 않습니다.")
  else:
    print(f"결과: 노드 0에서 노드 3까지 3단계로 이동하는 최단 거리 = {result}")
