#include <limits.h>
#include <stdio.h>
#include <string.h>

#define MAX_N 10
#define INF 1000000  // 충분히 큰 값이지만 오버플로우 방지

int graph[MAX_N][MAX_N];
int memo[MAX_N * 10];  // 노드 * 10 + 단계를 위한 충분한 크기
int n;

/**
 * @brief 최소값 함수
 */
int min(int a, int b) {
  return a < b ? a : b;
}

/**
 * @brief 3단계 최단 경로 메모이제이션 함수
 */
int shortestPathMemo(int node, int steps) {
  // 3단계를 모두 사용하고 목적지에 도달한 경우
  if (steps == 3 && node == 3) {
    return 0;
  }

  // 3단계를 모두 사용했지만 목적지가 아닌 경우
  if (steps == 3) {
    return INF;
  }

  // 메모이제이션 체크 (노드와 단계를 함께 고려)
  int memoKey = node * 10 + steps;
  if (memo[memoKey] != -1) {
    printf("💭 메모이제이션 %d(단계 %d): %d\n", node, steps, memo[memoKey]);
    return memo[memoKey];
  }

  printf("💭 계산: 노드 %d에서 %d단계 남은 최단 경로 찾기\n", node, 3 - steps);

  int result = INF;

  // 모든 인접 노드 확인
  for (int next = 0; next < n; next++) {
    if (graph[node][next] > 0) {  // 간선이 존재하는 경우
      int cost = graph[node][next] + shortestPathMemo(next, steps + 1);
      if (cost < INF) {  // 유효한 경로인 경우만
        result = min(result, cost);
        printf("  → 노드 %d → %d: 가중치 %d + 최단경로 %d = %d\n", node, next,
               graph[node][next], cost - graph[node][next], cost);
      }
    }
  }

  memo[memoKey] = result;
  printf("└─ 노드 %d(단계 %d)의 최단 경로: %d\n", node, steps, result);
  return result;
}

int main() {
  // 그래프 초기화 (이미지의 그래프 구조)
  n = 6;

  // 그래프 초기화 (INF로 채우기)
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      graph[i][j] = 0;
    }
  }

  // 간선 추가 (이미지의 그래프)
  graph[0][1] = 1;  // 0 → 1: 가중치 1
  graph[0][2] = 2;  // 0 → 2: 가중치 2
  graph[1][3] = 6;  // 1 → 3: 가중치 6
  graph[2][1] = 2;  // 2 → 1: 가중치 2
  graph[2][3] = 4;  // 2 → 3: 가중치 4
  graph[2][4] = 3;  // 2 → 4: 가중치 3
  graph[3][5] = 3;  // 3 → 5: 가중치 3
  graph[4][3] = 1;  // 4 → 3: 가중치 1
  graph[4][5] = 5;  // 4 → 5: 가중치 5

  // 메모이제이션 배열 초기화 (더 큰 배열 필요)
  memset(memo, -1, sizeof(memo));

  printf("=== 3단계 최단 경로 찾기 (메모이제이션) ===\n");
  printf("시작 노드: 0, 목적지 노드: 3, 정확히 3단계로 이동\n\n");

  int result = shortestPathMemo(0, 0);

  if (result == INF) {
    printf("\n결과: 3단계로 도달할 수 있는 경로가 존재하지 않습니다.\n");
  } else {
    printf("\n결과: 노드 0에서 노드 3까지 3단계로 이동하는 최단 거리 = %d\n",
           result);
  }

  return 0;
}
