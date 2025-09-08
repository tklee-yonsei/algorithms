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
 * MST 현재 상태 출력
 * @param inMST: MST에 포함된 정점들을 나타내는 boolean 배열
 * @param vertices: 전체 정점 개수
 * @param step: 현재 단계 번호
 */
void printMSTStatus(bool* inMST, int vertices, int step) {
  printf("Step %d: Finding cut between MST and remaining vertices\n", step + 1);

  printf("  Current MST vertices: {");
  for (int i = 0; i < vertices; i++) {
    if (inMST[i]) {
      printf("%d ", i);
    }
  }
  printf("}\n");

  printf("  Remaining vertices: {");
  for (int i = 0; i < vertices; i++) {
    if (!inMST[i]) {
      printf("%d ", i);
    }
  }
  printf("}\n");
}

/**
 * Cut을 가로지르는 최소 가중치 간선 찾기
 * @param graph: 그래프
 * @param inMST: MST에 포함된 정점들을 나타내는 boolean 배열
 * @return: 최소 가중치 간선의 인덱스 (없으면 -1)
 */
int findMinCutEdge(Graph* graph, bool* inMST) {
  int minWeight = INF;
  int minEdgeIndex = -1;

  // 모든 간선 검사
  for (int i = 0; i < graph->numEdges; i++) {
    int src = graph->edges[i].src;
    int dest = graph->edges[i].dest;
    int weight = graph->edges[i].weight;

    // Cut을 가로지르는 간선인지 확인 (한쪽은 MST에, 다른 쪽은 MST에 없어야 함)
    if ((inMST[src] && !inMST[dest]) || (!inMST[src] && inMST[dest])) {
      printf("  Cut edge candidate: (%d, %d, %d)\n", src, dest, weight);

      if (weight < minWeight) {
        minWeight = weight;
        minEdgeIndex = i;
      }
    }
  }

  return minEdgeIndex;
}

/**
 * 선택된 간선을 MST에 추가
 * @param mst: MST 결과 객체
 * @param graph: 그래프
 * @param edgeIndex: 추가할 간선의 인덱스
 * @param inMST: MST에 포함된 정점들을 나타내는 boolean 배열
 */
void addEdgeToMST(MST* mst, Graph* graph, int edgeIndex, bool* inMST) {
  Edge selectedEdge = graph->edges[edgeIndex];

  // MST에 간선 추가
  mst->edges[mst->numEdges] = selectedEdge;
  mst->numEdges++;
  mst->totalWeight += selectedEdge.weight;

  // 새로운 정점을 MST에 추가
  if (!inMST[selectedEdge.src]) {
    inMST[selectedEdge.src] = true;
  }
  if (!inMST[selectedEdge.dest]) {
    inMST[selectedEdge.dest] = true;
  }

  printf("  Selected edge: (%d, %d, %d)\n", selectedEdge.src, selectedEdge.dest,
         selectedEdge.weight);
}

/**
 * Cut Property 기반 Greedy MST 알고리즘
 * @param graph: 가중치 그래프
 * @return: MST 결과
 */
MST* greedyMST(Graph* graph) {
  int vertices = graph->numVertices;

  if (vertices <= 0) {
    printf("Invalid graph!\n");
    return NULL;
  }

  // MST 결과 구조체 생성
  MST* mst = (MST*)malloc(sizeof(MST));
  mst->edges = (Edge*)malloc((vertices - 1) * sizeof(Edge));
  mst->numEdges = 0;
  mst->totalWeight = 0;

  // MST에 포함된 정점들을 추적하는 배열
  bool* inMST = (bool*)malloc(vertices * sizeof(bool));
  for (int i = 0; i < vertices; i++) {
    inMST[i] = false;
  }

  // 시작 정점 선택 (정점 0)
  int startVertex = 0;
  inMST[startVertex] = true;

  printf("=== Greedy MST Algorithm (Cut Property) ===\n");
  printf("Starting from vertex %d\n\n", startVertex);

  // MST 구성 메인 루프 (vertices-1개의 간선 필요)
  for (int step = 0; step < vertices - 1; step++) {
    // 현재 MST 상태 출력
    printMSTStatus(inMST, vertices, step);

    // Cut을 가로지르는 최소 가중치 간선 찾기
    int minEdgeIndex = findMinCutEdge(graph, inMST);

    // 최소 가중치 간선을 MST에 추가
    if (minEdgeIndex != -1) {
      addEdgeToMST(mst, graph, minEdgeIndex, inMST);
    } else {
      printf("  No valid edge found - graph is not connected!\n");
      break;
    }
    printf("\n");
  }

  free(inMST);
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
  printf("=== Greedy MST (Cut Property) Algorithm ===\n\n");

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

  // Greedy MST 실행
  MST* mst = greedyMST(graph);
  printMST(mst);

  // 동일한 그래프로 다시 한 번 테스트
  printf("=== Same Graph - Second Run ===\n");
  Graph* graph2 = createGraph(8);

  // 동일한 간선들을 다시 추가
  addEdge(graph2, 0, 7, 16);
  addEdge(graph2, 2, 3, 17);
  addEdge(graph2, 1, 7, 19);
  addEdge(graph2, 0, 2, 26);
  addEdge(graph2, 5, 7, 28);
  addEdge(graph2, 1, 3, 29);
  addEdge(graph2, 1, 5, 32);
  addEdge(graph2, 2, 7, 34);
  addEdge(graph2, 4, 5, 35);
  addEdge(graph2, 1, 2, 36);
  addEdge(graph2, 4, 7, 37);
  addEdge(graph2, 0, 4, 38);
  addEdge(graph2, 6, 2, 40);
  addEdge(graph2, 3, 6, 52);
  addEdge(graph2, 6, 0, 58);
  addEdge(graph2, 6, 4, 93);

  printGraph(graph2);
  MST* mst2 = greedyMST(graph2);
  printMST(mst2);

  // 메모리 해제
  freeMST(mst);
  freeMST(mst2);
  freeGraph(graph);
  freeGraph(graph2);

  return 0;
}
