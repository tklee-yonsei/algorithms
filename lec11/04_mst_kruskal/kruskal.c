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
 * 그래프 구조체 (간선 리스트로 표현)
 */
typedef struct {
  int numVertices;
  int numEdges;
  Edge edges[MAX_EDGES];
} Graph;

/**
 * MST 결과 구조체
 */
typedef struct {
  Edge* edges;
  int numEdges;
  int totalWeight;
} MST;

/**
 * 연결 성분을 추적하기 위한 배열
 * component[i] = 정점 i가 속한 연결 성분의 번호
 */

// 그래프 생성
Graph* createGraph(int vertices) {
  Graph* graph = (Graph*)malloc(sizeof(Graph));
  graph->numVertices = vertices;
  graph->numEdges = 0;
  return graph;
}

// 간선 추가 (무방향 가중치 그래프)
void addEdge(Graph* graph, int src, int dest, int weight) {
  if (graph->numEdges >= MAX_EDGES) {
    printf("Maximum number of edges exceeded!\n");
    return;
  }

  // 무방향 그래프이므로 한 번만 추가 (중복 방지)
  graph->edges[graph->numEdges].src = src;
  graph->edges[graph->numEdges].dest = dest;
  graph->edges[graph->numEdges].weight = weight;
  graph->numEdges++;
}

/**
 * 연결 성분 배열 초기화
 * @param component: 연결 성분 배열
 * @param vertices: 정점 개수
 */
void initializeComponents(int* component, int vertices) {
  // 각 정점을 자기 자신만의 연결 성분으로 초기화
  for (int i = 0; i < vertices; i++) {
    component[i] = i;
  }
}

/**
 * 두 정점이 같은 연결 성분에 속하는지 확인
 * @param component: 연결 성분 배열
 * @param u: 첫 번째 정점
 * @param v: 두 번째 정점
 * @return: 같은 연결 성분이면 true, 아니면 false
 */
bool isConnected(int* component, int u, int v) {
  return component[u] == component[v];
}

/**
 * 두 연결 성분을 합치기 (간선 추가 시)
 * @param component: 연결 성분 배열
 * @param vertices: 정점 개수
 * @param u: 첫 번째 정점
 * @param v: 두 번째 정점
 */
void mergeComponents(int* component, int vertices, int u, int v) {
  int oldComponent = component[v];
  int newComponent = component[u];

  // v의 연결 성분에 속한 모든 정점을 u의 연결 성분으로 변경
  for (int i = 0; i < vertices; i++) {
    if (component[i] == oldComponent) {
      component[i] = newComponent;
    }
  }
}

/**
 * 간선 비교 함수 (가중치 오름차순 정렬용)
 */
int compareEdges(const void* a, const void* b) {
  Edge* edgeA = (Edge*)a;
  Edge* edgeB = (Edge*)b;
  return edgeA->weight - edgeB->weight;
}

/**
 * 정렬된 간선들 출력
 */
void printSortedEdges(Edge* edges, int numEdges) {
  printf("=== Sorted Edges by Weight ===\n");
  for (int i = 0; i < numEdges; i++) {
    printf("  Edge %d: (%d, %d, %d)\n", i, edges[i].src, edges[i].dest,
           edges[i].weight);
  }
  printf("\n");
}

/**
 * Kruskal MST 알고리즘
 * @param graph: 가중치 그래프
 * @return: MST 결과
 */
MST* kruskalMST(Graph* graph) {
  int vertices = graph->numVertices;
  int numEdges = graph->numEdges;

  if (vertices <= 0 || numEdges <= 0) {
    printf("Invalid graph!\n");
    return NULL;
  }

  // MST 결과 구조체 생성
  MST* mst = (MST*)malloc(sizeof(MST));
  mst->edges = (Edge*)malloc((vertices - 1) * sizeof(Edge));
  mst->numEdges = 0;
  mst->totalWeight = 0;

  // 간선들을 가중치 오름차순으로 정렬
  Edge* sortedEdges = (Edge*)malloc(numEdges * sizeof(Edge));
  for (int i = 0; i < numEdges; i++) {
    sortedEdges[i] = graph->edges[i];
  }
  qsort(sortedEdges, numEdges, sizeof(Edge), compareEdges);

  // 정렬된 간선들 출력
  printSortedEdges(sortedEdges, numEdges);

  // 연결 성분 배열 초기화
  int* component = (int*)malloc(vertices * sizeof(int));
  initializeComponents(component, vertices);

  printf("=== Kruskal MST Algorithm ===\n");
  printf("Processing edges in order of increasing weight:\n\n");

  // 정렬된 간선들을 순서대로 검사
  for (int i = 0; i < numEdges && mst->numEdges < vertices - 1; i++) {
    Edge currentEdge = sortedEdges[i];
    int src = currentEdge.src;
    int dest = currentEdge.dest;
    int weight = currentEdge.weight;

    printf("Step %d: Considering edge (%d, %d, %d)\n", mst->numEdges + 1, src,
           dest, weight);

    // 사이클 검사: 두 정점이 다른 연결 성분에 속하는지 확인
    if (!isConnected(component, src, dest)) {
      // 사이클이 생기지 않으므로 MST에 간선 추가
      mst->edges[mst->numEdges] = currentEdge;
      mst->numEdges++;
      mst->totalWeight += weight;

      // 두 연결 성분을 합침
      mergeComponents(component, vertices, src, dest);

      printf("  ✓ Added to MST (no cycle created)\n");
    } else {
      printf("  ✗ Rejected (would create cycle)\n");
    }
    printf("\n");
  }

  // 메모리 해제
  free(sortedEdges);
  free(component);

  return mst;
}

// MST 결과 출력
void printMST(MST* mst) {
  if (mst == NULL || mst->numEdges == 0) {
    printf("No MST found!\n");
    return;
  }

  printf("=== MST Result ===\n");
  printf("MST Edges:\n");
  for (int i = 0; i < mst->numEdges; i++) {
    printf("  %d - %d : %d\n", mst->edges[i].src, mst->edges[i].dest,
           mst->edges[i].weight);
  }
  printf("Total Weight: %d\n\n", mst->totalWeight);
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

// MST 메모리 해제
void freeMST(MST* mst) {
  if (mst != NULL) {
    free(mst->edges);
    free(mst);
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
  printf("=== Kruskal MST Algorithm ===\n\n");

  // 그래프 생성 (8개 정점: 0-7)
  Graph* graph = createGraph(8);

  // 간선 추가 (가중치 그래프) - 이미지의 그래프 기준
  // 정점: 0, 1, 2, 3, 4, 5, 6, 7
  addEdge(graph, 0, 7, 16);  // 0.16 * 100
  addEdge(graph, 2, 3, 17);  // 0.17 * 100
  addEdge(graph, 1, 7, 19);  // 0.19 * 100
  addEdge(graph, 0, 2, 26);  // 0.26 * 100
  addEdge(graph, 5, 7, 28);  // 0.28 * 100
  addEdge(graph, 1, 3, 29);  // 0.29 * 100
  addEdge(graph, 1, 5, 32);  // 0.32 * 100
  addEdge(graph, 2, 7, 34);  // 0.34 * 100
  addEdge(graph, 4, 5, 35);  // 0.35 * 100
  addEdge(graph, 1, 2, 36);  // 0.36 * 100
  addEdge(graph, 4, 7, 37);  // 0.37 * 100
  addEdge(graph, 0, 4, 38);  // 0.38 * 100
  addEdge(graph, 6, 2, 40);  // 0.40 * 100
  addEdge(graph, 3, 6, 52);  // 0.52 * 100
  addEdge(graph, 6, 0, 58);  // 0.58 * 100
  addEdge(graph, 6, 4, 93);  // 0.93 * 100

  // 그래프 구조 출력
  printGraph(graph);

  // Kruskal MST 실행
  MST* mst = kruskalMST(graph);
  printMST(mst);

  // 메모리 해제
  freeMST(mst);
  freeGraph(graph);

  return 0;
}
