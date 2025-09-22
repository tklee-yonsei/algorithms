#include <limits.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

#define MAX_N 10
#define INF 1000000  // 충분히 큰 값이지만 오버플로우 방지

int graph[MAX_N][MAX_N];
int dp[MAX_N];
int n;

/**
 * @brief 최소값 함수
 */
int min(int a, int b) {
  return a < b ? a : b;
}

/**
 * @brief 3단계 최단 경로 테이블레이션 함수
 */
int shortestPathTab(int start, int end) {
  // DP 테이블 초기화 [노드][단계]
  int dp_table[MAX_N][4];  // 최대 3단계 + 1

  // 모든 값을 INF로 초기화
  for (int i = 0; i < n; i++) {
    for (int step = 0; step <= 3; step++) {
      dp_table[i][step] = INF;
    }
  }

  dp_table[end][3] = 0;  // 목적지에서 3단계 완료시 거리는 0

  printf("=== 3단계 최단 경로 찾기 (테이블레이션) ===\n");
  printf("시작 노드: %d, 목적지 노드: %d, 정확히 3단계로 이동\n\n", start, end);

  // 역방향으로 단계별 계산
  for (int step = 2; step >= 0; step--) {
    printf("단계 %d 계산:\n", step + 1);
    bool updated = false;

    // 모든 노드에 대해
    for (int v = 0; v < n; v++) {
      if (dp_table[v][step + 1] == INF)
        continue;

      // v로 들어오는 모든 간선 확인
      for (int u = 0; u < n; u++) {
        if (graph[u][v] > 0) {  // 간선이 존재하는 경우
          int newDist = dp_table[v][step + 1] + graph[u][v];
          if (newDist < dp_table[u][step]) {
            printf("  노드 %d ← %d (간선 %d→%d): %d + %d = %d (이전: %d)\n", u,
                   v, u, v, dp_table[v][step + 1], graph[u][v], newDist,
                   dp_table[u][step]);
            dp_table[u][step] = newDist;
            updated = true;
          }
        }
      }
    }

    if (!updated) {
      printf("  더 이상 업데이트되지 않음.\n");
    }
    printf("\n");
  }

  return dp_table[start][0];
}

int main() {
  // 그래프 초기화 (이미지의 그래프 구조)
  n = 6;

  // 그래프 초기화
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

  int result = shortestPathTab(0, 3);

  if (result == INF) {
    printf("결과: 3단계로 도달할 수 있는 경로가 존재하지 않습니다.\n");
  } else {
    printf("결과: 노드 0에서 노드 3까지 3단계로 이동하는 최단 거리 = %d\n",
           result);
  }

  return 0;
}
