import sys


def shortest_path_memo(graph, start, end, steps, memo=None):
  if memo is None:
    memo = {}

  # 3단계를 모두 사용하고 목적지에 도달한 경우
  if steps == 3 and start == end:
    return 0

  # 3단계를 모두 사용했지만 목적지가 아닌 경우
  if steps == 3:
    return 1000000

  # 메모이제이션 체크 (노드와 단계를 함께 고려)
  memo_key = (start, steps)
  if memo_key in memo:
    print(f"💭 메모이제이션 {start}(단계 {steps}): {memo[memo_key]}")
    return memo[memo_key]

  print(f"💭 계산: 노드 {start}에서 {3 - steps}단계 남은 최단 경로 찾기")

  result = 1000000  # 충분히 큰 값이지만 오버플로우 방지

  # 모든 인접 노드 확인
  if start in graph:
    for next_node, weight in graph[start].items():
      cost = weight + shortest_path_memo(graph, next_node, end, steps + 1, memo)
      if cost < 1000000:  # 유효한 경로인 경우만
        result = min(result, cost)
        print(
            f"  → 노드 {start} → {next_node}: 가중치 {weight} + 최단경로 {cost - weight} = {cost}")

  memo[memo_key] = result
  print(f"└─ 노드 {start}(단계 {steps})의 최단 경로: {result}")
  return result


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

  print("=== 3단계 최단 경로 찾기 (메모이제이션) ===")
  print("시작 노드: 0, 목적지 노드: 3, 정확히 3단계로 이동\n")

  result = shortest_path_memo(graph, 0, 3, 0)

  if result == 1000000:
    print("\n결과: 3단계로 도달할 수 있는 경로가 존재하지 않습니다.")
  else:
    print(f"\n결과: 노드 0에서 노드 3까지 3단계로 이동하는 최단 거리 = {result}")
