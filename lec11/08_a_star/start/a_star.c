#include <limits.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#define MAX_VERTICES 100
#define MAX_EDGES 1000
#define INF INT_MAX

/**
 * 간선 구조체
 */
typedef struct Edge {
  int src, dest, weight;
} Edge;

/**
 * 그래프 구조체 (인접 행렬로 표현)
 */
typedef struct {
  int numVertices;
  int adjMatrix[MAX_VERTICES][MAX_VERTICES];
  Edge edges[MAX_EDGES];
  int numEdges;
} Graph;

/**
 * A* 탐색 결과 구조체
 */
typedef struct {
  int* path;
  int pathLength;
  int totalCost;
} AStarResult;

// 그래프 생성
Graph* createGraph(int vertices) {
  Graph* graph = (Graph*)malloc(sizeof(Graph));
  graph->numVertices = vertices;
  graph->numEdges = 0;

  // 인접 행렬 초기화
  for (int i = 0; i < vertices; i++) {
    for (int j = 0; j < vertices; j++) {
      graph->adjMatrix[i][j] = 0;
    }
  }

  return graph;
}

// 간선 추가 (방향 가중치 그래프)
void addEdge(Graph* graph, int src, int dest, int weight) {
  if (graph->numEdges >= MAX_EDGES) {
    printf("Maximum number of edges exceeded!\n");
    return;
  }

  // 인접 행렬에 가중치 저장 (방향 그래프)
  graph->adjMatrix[src][dest] = weight;

  // 간선 리스트에도 저장 (출력용)
  graph->edges[graph->numEdges].src = src;
  graph->edges[graph->numEdges].dest = dest;
  graph->edges[graph->numEdges].weight = weight;
  graph->numEdges++;
}

/**
 * 휴리스틱 함수 - 이미지 데이터 사용
 */
int heuristic(int vertex, int goal) {
  // TODO: 이미지에서 제공된 휴리스틱 값들을 배열로 정의하세요
  // 이미지에서 제공된 휴리스틱 값들
  int h_values[] = {14, 10, 4, 2, 11, 6, 0, 8};
  return h_values[vertex];
}

/**
 * A* 최단 경로 알고리즘
 * @param graph: 가중치 그래프
 * @param startVertex: 시작 정점
 * @param goalVertex: 목표 정점
 * @return: A* 탐색 결과
 */
AStarResult* aStar(Graph* graph, int startVertex, int goalVertex) {
  int vertices = graph->numVertices;

  if (vertices <= 0) {
    printf("Invalid graph!\n");
    return NULL;
  }

  // TODO: 이 함수를 완성하세요!
  //
  // pseudo 코드를 참고하여 A* 알고리즘을 구현하세요:
  // 1. A* 탐색 결과 구조체 생성 (malloc으로 메모리 할당)
  // 2. g_score, f_score, came_from, closed_set 배열들을 할당하고 초기화
  //    - g_score[i]: 시작점에서 정점 i까지의 실제 거리 (초기값: INF)
  //    - f_score[i]: f(n) = g(n) + h(n) (초기값: INF)
  //    - came_from[i]: 경로 추적용 부모 정점 (초기값: -1)
  //    - closed_set[i]: closed set에 포함되었는지 (초기값: false)
  // 3. 우선순위 큐(open list) 초기화
  //    - 시작 정점의 g_score를 0으로, f_score를 h(startVertex)로 설정
  //    - 시작 정점을 우선순위 큐에 추가
  // 4. 우선순위 큐가 비지 않을 때까지 반복:
  //    - f값이 가장 작은 정점을 선택 (extractMin)
  //    - 이미 closed set에 있는 정점은 스킵
  //    - 목표 정점에 도달했으면 경로 재구성 후 반환
  //    - 현재 정점을 closed_set에 추가
  //    - 인접한 정점들의 g_score, f_score 업데이트
  //    - 더 나은 경로를 발견했거나 처음 방문하는 정점인 경우 open list에 추가
  // 5. 사용한 메모리 해제
  // 6. A* 탐색 결과 반환

  printf("=== A* Search Algorithm ===\n");
  printf("Starting A* search from %d to %d\n", startVertex, goalVertex);
  printf("Initial heuristic h(%d) = %d\n\n", startVertex,
         heuristic(startVertex, goalVertex));

  // 여기에 코드를 작성하세요!
  // pseudo 코드의 A_STAR_SEARCH 알고리즘을 참고하세요

  return NULL;
}

// A* 탐색 결과 출력
void printAStarResult(AStarResult* result, int startVertex, int goalVertex) {
  if (result == NULL) {
    printf("No path found!\n");
    return;
  }

  printf("=== A* Search Result ===\n");
  printf("Shortest path from vertex %d to vertex %d:\n", startVertex,
         goalVertex);
  printf("Total cost: %d\n", result->totalCost);

  // 경로 출력
  printf("Path: ");
  for (int i = 0; i < result->pathLength; i++) {
    printf("%d", result->path[i]);
    if (i < result->pathLength - 1)
      printf(" -> ");
  }
  printf("\n\n");
}

// 그래프 출력 (디버깅용)
void printGraph(Graph* graph) {
  printf("Graph representation (edge list):\n");
  printf("Vertices: %d, Edges: %d\n", graph->numVertices, graph->numEdges);
  for (int i = 0; i < graph->numEdges; i++) {
    printf("  Edge %d: (%d, %d, %d)\n", i, graph->edges[i].src,
           graph->edges[i].dest, graph->edges[i].weight);
  }
  printf("\n");
}

// 휴리스틱 값 출력
void printHeuristics(int vertices, int goalVertex) {
  printf("Heuristic values (h) from each vertex to goal %d:\n", goalVertex);
  for (int i = 0; i < vertices; i++) {
    printf("  h(%d) = %d\n", i, heuristic(i, goalVertex));
  }
  printf("\n");
}

// A* 탐색 결과 메모리 해제
void freeAStarResult(AStarResult* result) {
  if (result != NULL) {
    free(result->path);
    free(result);
  }
}

// 그래프 메모리 해제
void freeGraph(Graph* graph) {
  if (graph != NULL) {
    free(graph);
  }
}

/**
 * 메인 함수 - 예제 실행
 */
int main() {
  printf("=== A* Search Algorithm ===\n\n");

  // 그래프 생성 (8개 정점: 0-7)
  Graph* graph = createGraph(8);

  // 간선 추가 (방향 가중치 그래프) - 이미지 데이터 사용
  // 정점: 0, 1, 2, 3, 4, 5, 6, 7
  addEdge(graph, 0, 1, 5);   // 0→1
  addEdge(graph, 0, 4, 9);   // 0→4
  addEdge(graph, 0, 7, 8);   // 0→7
  addEdge(graph, 1, 2, 12);  // 1→2
  addEdge(graph, 1, 3, 15);  // 1→3
  addEdge(graph, 1, 7, 4);   // 1→7
  addEdge(graph, 2, 3, 3);   // 2→3
  addEdge(graph, 2, 6, 11);  // 2→6
  addEdge(graph, 3, 6, 9);   // 3→6
  addEdge(graph, 4, 5, 4);   // 4→5
  addEdge(graph, 4, 6, 20);  // 4→6
  addEdge(graph, 4, 7, 5);   // 4→7
  addEdge(graph, 5, 2, 1);   // 5→2
  addEdge(graph, 5, 6, 13);  // 5→6
  addEdge(graph, 7, 5, 6);   // 7→5
  addEdge(graph, 7, 2, 7);   // 7→2

  // 그래프 구조 출력
  printGraph(graph);

  // 휴리스틱 값 출력
  printHeuristics(8, 6);

  // A* 탐색 실행 (정점 0에서 시작, 정점 6이 목표)
  AStarResult* result = aStar(graph, 0, 6);
  printAStarResult(result, 0, 6);

  // 메모리 해제
  freeAStarResult(result);
  freeGraph(graph);

  return 0;
}
