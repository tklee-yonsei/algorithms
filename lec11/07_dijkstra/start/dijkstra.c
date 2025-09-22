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
 * 최단 경로 결과 구조체
 */
typedef struct {
  int* distances;
  int* parents;
  int numVertices;
} ShortestPath;

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
 * 방문하지 않은 정점 중 최소 거리를 가진 정점을 찾는 함수
 * @param distances: 각 정점의 거리 배열
 * @param visited: 방문 여부 배열
 * @param vertices: 정점 개수
 * @return: 최소 거리를 가진 정점의 인덱스
 */
int findMinDistance(int* distances, bool* visited, int vertices) {
  int min = INF;
  int minIndex = -1;

  for (int v = 0; v < vertices; v++) {
    if (!visited[v] && distances[v] < min) {
      min = distances[v];
      minIndex = v;
    }
  }

  return minIndex;
}

/**
 * Dijkstra 최단 경로 알고리즘
 * @param graph: 가중치 그래프
 * @param startVertex: 시작 정점
 * @return: 최단 경로 결과
 */
ShortestPath* dijkstra(Graph* graph, int startVertex) {
  int vertices = graph->numVertices;

  if (vertices <= 0) {
    printf("Invalid graph!\n");
    return NULL;
  }

  // TODO: 이 함수를 완성하세요!
  //
  // 힌트 (우선순위 큐 기반):
  // 1. 최단 경로 결과 구조체 생성 (malloc으로 메모리 할당)
  // 2. distances, parents, visited 배열들을 할당하고 초기화
  //    - distances[i]: 정점 i까지의 최단 거리 (초기값: INF)
  //    - parents[i]: 최단 경로에서 정점 i의 부모 (초기값: -1)
  //    - visited[i]: 정점 i가 방문되었는지 (초기값: false)
  // 3. 최소 힙(우선순위 큐) 생성 및 초기화
  //    - createMinHeap으로 힙 생성
  //    - 모든 정점을 힙에 추가 (시작 정점의 거리는 0)
  // 4. 힙이 비지 않을 때까지 반복:
  //    - extractMin으로 최소 거리를 가진 정점 추출
  //    - 해당 정점을 visited로 표시
  //    - 인접한 정점들의 distances 값 업데이트 (decreaseKey 사용)
  // 5. 사용한 메모리 해제
  // 6. 최단 경로 결과 반환

  printf("=== Dijkstra Shortest Path Algorithm (Priority Queue) ===\n");
  printf("Starting from vertex %d\n", startVertex);
  printf("Processing vertices in order of minimum distances:\n\n");

  // 여기에 코드를 작성하세요!

  return NULL;
}

// 최단 경로 결과 출력
void printShortestPaths(ShortestPath* result, int startVertex) {
  if (result == NULL) {
    printf("No shortest paths found!\n");
    return;
  }

  printf("=== Shortest Path Results ===\n");
  printf("Shortest distances from vertex %d:\n", startVertex);
  for (int i = 0; i < result->numVertices; i++) {
    if (result->distances[i] == INF) {
      printf("  Vertex %d: unreachable\n", i);
    } else {
      printf("  Vertex %d: %d\n", i, result->distances[i]);
    }
  }
  printf("\n");
}

// 경로 재구성 및 출력
void printPath(ShortestPath* result, int startVertex, int targetVertex) {
  if (result == NULL || result->distances[targetVertex] == INF) {
    printf("No path from vertex %d to vertex %d\n", startVertex, targetVertex);
    return;
  }

  printf("Shortest path from vertex %d to vertex %d:\n", startVertex,
         targetVertex);
  printf("Distance: %d\n", result->distances[targetVertex]);

  // 경로 재구성
  int path[MAX_VERTICES];
  int pathLength = 0;
  int current = targetVertex;

  while (current != -1) {
    path[pathLength++] = current;
    current = result->parents[current];
  }

  // 경로 출력
  printf("Path: ");
  for (int i = pathLength - 1; i >= 0; i--) {
    printf("%d", path[i]);
    if (i > 0)
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

// 최단 경로 메모리 해제
void freeShortestPath(ShortestPath* result) {
  if (result != NULL) {
    free(result->distances);
    free(result->parents);
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
  printf("=== Dijkstra Shortest Path Algorithm (Priority Queue) ===\n\n");

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

  // Dijkstra 최단 경로 실행 (정점 0에서 시작)
  ShortestPath* result = dijkstra(graph, 0);
  printShortestPaths(result, 0);

  // 특정 정점까지의 경로 출력
  printPath(result, 0, 6);
  printPath(result, 0, 3);
  printPath(result, 0, 7);

  // 메모리 해제
  freeShortestPath(result);
  freeGraph(graph);

  return 0;
}
