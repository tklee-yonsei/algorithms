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
 * 힙 원소 구조체 (거리-정점 쌍)
 */
typedef struct HeapNode {
  int distance;  // 거리 값
  int vertex;    // 정점 번호
} HeapNode;

/**
 * 최소 힙 구조체 (우선순위 큐)
 */
typedef struct MinHeap {
  HeapNode* array;
  int size;
  int capacity;
  int* pos;  // 각 정점의 힙에서의 위치 (업데이트용)
} MinHeap;

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
 * 힙 생성
 */
MinHeap* createMinHeap(int capacity) {
  MinHeap* heap = (MinHeap*)malloc(sizeof(MinHeap));
  heap->array = (HeapNode*)malloc(capacity * sizeof(HeapNode));
  heap->size = 0;
  heap->capacity = capacity;
  heap->pos = (int*)malloc(capacity * sizeof(int));
  return heap;
}

/**
 * 두 힙 노드 교환
 */
void swapHeapNode(HeapNode* a, HeapNode* b) {
  HeapNode temp = *a;
  *a = *b;
  *b = temp;
}

/**
 * 최소 힙 속성 유지 (하향 정리)
 */
void minHeapify(MinHeap* heap, int idx) {
  int smallest = idx;
  int left = 2 * idx + 1;
  int right = 2 * idx + 2;

  if (left < heap->size &&
      heap->array[left].distance < heap->array[smallest].distance) {
    smallest = left;
  }

  if (right < heap->size &&
      heap->array[right].distance < heap->array[smallest].distance) {
    smallest = right;
  }

  if (smallest != idx) {
    // 위치 배열 업데이트
    heap->pos[heap->array[smallest].vertex] = idx;
    heap->pos[heap->array[idx].vertex] = smallest;

    swapHeapNode(&heap->array[smallest], &heap->array[idx]);
    minHeapify(heap, smallest);
  }
}

/**
 * 힙이 비어있는지 확인
 */
bool isEmpty(MinHeap* heap) {
  return heap->size == 0;
}

/**
 * 최소값 추출
 */
HeapNode extractMin(MinHeap* heap) {
  if (isEmpty(heap)) {
    HeapNode emptyNode = {INF, -1};
    return emptyNode;
  }

  HeapNode root = heap->array[0];
  HeapNode lastNode = heap->array[heap->size - 1];
  heap->array[0] = lastNode;

  heap->pos[lastNode.vertex] = 0;
  heap->pos[root.vertex] = heap->size - 1;

  heap->size--;
  minHeapify(heap, 0);

  return root;
}

/**
 * 거리 값 감소 (decreaseKey)
 */
void decreaseKey(MinHeap* heap, int vertex, int distance) {
  int i = heap->pos[vertex];
  heap->array[i].distance = distance;

  // 상향 정리
  while (i && heap->array[i].distance < heap->array[(i - 1) / 2].distance) {
    heap->pos[heap->array[i].vertex] = (i - 1) / 2;
    heap->pos[heap->array[(i - 1) / 2].vertex] = i;

    swapHeapNode(&heap->array[i], &heap->array[(i - 1) / 2]);
    i = (i - 1) / 2;
  }
}

/**
 * 정점이 힙에 있는지 확인
 */
bool isInMinHeap(MinHeap* heap, int vertex) {
  return heap->pos[vertex] < heap->size;
}

/**
 * Dijkstra 최단 경로 알고리즘 - 우선순위 큐 기반
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

  // 최단 경로 결과 구조체 생성
  ShortestPath* result = (ShortestPath*)malloc(sizeof(ShortestPath));
  result->distances = (int*)malloc(vertices * sizeof(int));
  result->parents = (int*)malloc(vertices * sizeof(int));
  result->numVertices = vertices;

  // 초기화
  bool* visited = (bool*)malloc(vertices * sizeof(bool));

  // 최소 힙 생성
  MinHeap* heap = createMinHeap(vertices);

  // 배열 초기화
  for (int v = 0; v < vertices; v++) {
    result->parents[v] = -1;
    result->distances[v] = INF;
    visited[v] = false;
    heap->array[v].distance = result->distances[v];
    heap->array[v].vertex = v;
    heap->pos[v] = v;
  }

  // 시작 정점 설정
  result->distances[startVertex] = 0;
  heap->array[startVertex].distance = 0;
  heap->size = vertices;

  printf("=== Dijkstra Shortest Path Algorithm (Priority Queue) ===\n");
  printf("Starting from vertex %d\n", startVertex);
  printf("Processing vertices in order of minimum distances:\n\n");

  int step = 1;

  // 최단 경로 탐색
  while (!isEmpty(heap)) {
    // 최소 거리를 가진 정점 추출
    HeapNode minNode = extractMin(heap);
    int u = minNode.vertex;

    if (u == -1)
      break;  // 더 이상 연결된 정점이 없음

    // 이미 방문한 정점이면 스킵
    if (visited[u])
      continue;

    // 정점을 방문 처리
    visited[u] = true;

    printf("Step %d: Visit vertex %d with distance %d\n", step, u,
           result->distances[u]);
    step++;

    // 인접한 정점들의 거리 업데이트 (Relaxation)
    for (int v = 0; v < vertices; v++) {
      int weight = graph->adjMatrix[u][v];

      // 간선이 존재하고, 방문하지 않았고, 더 짧은 경로를 발견한 경우
      if (weight != 0 && !visited[v] && isInMinHeap(heap, v)) {
        int tentativeDistance = result->distances[u] + weight;

        if (tentativeDistance < result->distances[v]) {
          int oldDistance =
              (result->distances[v] == INF) ? -1 : result->distances[v];
          result->distances[v] = tentativeDistance;
          result->parents[v] = u;

          // 힙에서 거리 값 감소
          decreaseKey(heap, v, tentativeDistance);

          printf("  Updated dist[%d] = %d (via %d), was %s", v,
                 tentativeDistance, u, (oldDistance == -1) ? "INF" : "");
          if (oldDistance != -1) {
            printf("%d", oldDistance);
          }
          printf("\n");
        }
      }
    }

    // 현재 거리 배열 출력
    printf("  Current distances: [");
    bool first = true;
    for (int i = 0; i < vertices; i++) {
      if (!first)
        printf(", ");
      if (result->distances[i] == INF) {
        printf("INF");
      } else {
        printf("%d", result->distances[i]);
      }
      first = false;
    }
    printf("]\n\n");
  }

  // 메모리 해제
  free(visited);
  free(heap->array);
  free(heap->pos);
  free(heap);

  return result;
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
