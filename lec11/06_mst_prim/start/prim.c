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

  // 인접 행렬 초기화
  for (int i = 0; i < vertices; i++) {
    for (int j = 0; j < vertices; j++) {
      graph->adjMatrix[i][j] = 0;
    }
  }

  return graph;
}

// 간선 추가 (무방향 가중치 그래프)
void addEdge(Graph* graph, int src, int dest, int weight) {
  if (graph->numEdges >= MAX_EDGES) {
    printf("Maximum number of edges exceeded!\n");
    return;
  }

  // 인접 행렬에 가중치 저장 (무방향 그래프)
  graph->adjMatrix[src][dest] = weight;
  graph->adjMatrix[dest][src] = weight;

  // 간선 리스트에도 저장 (출력용)
  graph->edges[graph->numEdges].src = src;
  graph->edges[graph->numEdges].dest = dest;
  graph->edges[graph->numEdges].weight = weight;
  graph->numEdges++;
}

/**
 * 방문하지 않은 정점 중 최소 키 값을 가진 정점을 찾는 함수
 * @param key: 각 정점의 키 값 배열
 * @param visited: 방문 여부 배열
 * @param vertices: 정점 개수
 * @return: 최소 키 값을 가진 정점의 인덱스
 */
int findMinKey(int* key, bool* visited, int vertices) {
  int min = INF;
  int minIndex = -1;

  for (int v = 0; v < vertices; v++) {
    if (!visited[v] && key[v] < min) {
      min = key[v];
      minIndex = v;
    }
  }

  return minIndex;
}

/**
 * Prim MST 알고리즘
 * @param graph: 가중치 그래프
 * @param startVertex: 시작 정점
 * @return: MST 결과
 */
MST* primMST(Graph* graph, int startVertex) {
  int vertices = graph->numVertices;

  if (vertices <= 0) {
    printf("Invalid graph!\n");
    return NULL;
  }

  // TODO: 이 함수를 완성하세요!
  //
  // 힌트 (우선순위 큐 기반):
  // 1. MST 결과 구조체 생성 (malloc으로 메모리 할당)
  // 2. key, parent, inMST 배열들을 할당하고 초기화
  //    - key[i]: 정점 i의 최소 가중치 (초기값: INF)
  //    - parent[i]: MST에서 정점 i의 부모 (초기값: -1)
  //    - inMST[i]: 정점 i가 MST에 포함되었는지 (초기값: false)
  // 3. 최소 힙(우선순위 큐) 생성 및 초기화
  //    - createMinHeap으로 힙 생성
  //    - 모든 정점을 힙에 추가 (시작 정점의 키는 0)
  // 4. 힙이 비지 않을 때까지 반복:
  //    - extractMin으로 최소 키 값을 가진 정점 추출
  //    - 해당 정점을 inMST로 표시
  //    - parent가 있으면 MST에 간선 추가
  //    - 인접한 정점들의 key 값 업데이트 (decreaseKey 사용)
  // 5. 사용한 메모리 해제
  // 6. MST 반환

  printf("=== Prim MST Algorithm (Priority Queue) ===\n");
  printf("Starting from vertex %d\n", startVertex);
  printf("Processing vertices in order of minimum key values:\n\n");

  // 여기에 코드를 작성하세요!

  return NULL;
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

/**
 * 메인 함수 - 예제 실행
 */
int main() {
  printf("=== Prim MST Algorithm (Priority Queue) ===\n\n");

  // 그래프 생성 (8개 정점: 0-7)
  Graph* graph = createGraph(8);

  // 간선 추가 (가중치 그래프) - Kruskal과 동일한 그래프
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

  // Prim MST 실행 (정점 0에서 시작)
  MST* mst = primMST(graph, 0);
  printMST(mst);

  return 0;
}
