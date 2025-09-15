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
 * 우선순위 큐 원소 구조체 (f값-정점 쌍)
 */
typedef struct PriorityNode {
  int f_score;  // f(n) = g(n) + h(n)
  int vertex;   // 정점 번호
} PriorityNode;

/**
 * 간단한 우선순위 큐 구조체
 */
typedef struct PriorityQueue {
  PriorityNode* array;
  int size;
  int capacity;
} PriorityQueue;

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

// 우선순위 큐 생성
PriorityQueue* createPriorityQueue(int capacity) {
  PriorityQueue* pq = (PriorityQueue*)malloc(sizeof(PriorityQueue));
  pq->array = (PriorityNode*)malloc(capacity * sizeof(PriorityNode));
  pq->size = 0;
  pq->capacity = capacity;
  return pq;
}

// 우선순위 큐가 비어있는지 확인
bool isEmpty(PriorityQueue* pq) {
  return pq->size == 0;
}

// 우선순위 큐에 원소 삽입
void insertPQ(PriorityQueue* pq, int vertex, int f_score) {
  if (pq->size >= pq->capacity) {
    printf("Priority queue overflow!\n");
    return;
  }

  int i = pq->size++;
  pq->array[i].vertex = vertex;
  pq->array[i].f_score = f_score;

  // 삽입 정렬로 우선순위 유지 (간단한 구현)
  while (i > 0 && pq->array[i].f_score < pq->array[i - 1].f_score) {
    PriorityNode temp = pq->array[i];
    pq->array[i] = pq->array[i - 1];
    pq->array[i - 1] = temp;
    i--;
  }
}

// 최소값 추출
PriorityNode extractMin(PriorityQueue* pq) {
  if (isEmpty(pq)) {
    PriorityNode emptyNode = {INF, -1};
    return emptyNode;
  }

  PriorityNode min = pq->array[0];

  // 배열의 나머지 원소들을 앞으로 이동
  for (int i = 0; i < pq->size - 1; i++) {
    pq->array[i] = pq->array[i + 1];
  }
  pq->size--;

  return min;
}

// 특정 정점이 우선순위 큐에 있는지 확인
bool isInPQ(PriorityQueue* pq, int vertex) {
  for (int i = 0; i < pq->size; i++) {
    if (pq->array[i].vertex == vertex) {
      return true;
    }
  }
  return false;
}

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

  // A* 탐색 결과 구조체 생성
  AStarResult* result = (AStarResult*)malloc(sizeof(AStarResult));
  result->path = (int*)malloc(vertices * sizeof(int));
  result->pathLength = 0;
  result->totalCost = 0;

  // 초기화
  int* g_score = (int*)malloc(vertices * sizeof(int));    // 실제 거리
  int* f_score = (int*)malloc(vertices * sizeof(int));    // f(n) = g(n) + h(n)
  int* came_from = (int*)malloc(vertices * sizeof(int));  // 경로 추적
  bool* closed_set = (bool*)malloc(vertices * sizeof(bool));  // closed set

  // 우선순위 큐 생성 (open list)
  PriorityQueue* open_list = createPriorityQueue(vertices * vertices);

  // 배열 초기화
  for (int v = 0; v < vertices; v++) {
    g_score[v] = INF;
    f_score[v] = INF;
    came_from[v] = -1;
    closed_set[v] = false;
  }

  // 시작 정점 설정
  g_score[startVertex] = 0;
  f_score[startVertex] = heuristic(startVertex, goalVertex);
  insertPQ(open_list, startVertex, f_score[startVertex]);

  printf("=== A* Search Algorithm ===\n");
  printf("Starting A* search from %d to %d\n", startVertex, goalVertex);
  printf("Initial heuristic h(%d) = %d\n\n", startVertex,
         heuristic(startVertex, goalVertex));

  int step = 1;

  // A* 탐색 메인 루프
  while (!isEmpty(open_list)) {
    // f값이 가장 작은 정점 선택
    PriorityNode minNode = extractMin(open_list);
    int current = minNode.vertex;

    if (current == -1)
      break;

    // 이미 closed set에 있는 정점은 스킵
    if (closed_set[current]) {
      continue;
    }

    printf("Step %d: Exploring vertex %d with f=%d\n", step, current,
           f_score[current]);
    step++;

    // 목표에 도달했는지 확인
    if (current == goalVertex) {
      printf("Goal reached! Reconstructing path...\n");

      // 경로 재구성
      int path[MAX_VERTICES];
      int pathLength = 0;
      int node = current;

      while (node != -1) {
        path[pathLength++] = node;
        node = came_from[node];
      }

      // 경로를 올바른 순서로 복사
      for (int i = 0; i < pathLength; i++) {
        result->path[i] = path[pathLength - 1 - i];
      }
      result->pathLength = pathLength;
      result->totalCost = g_score[goalVertex];

      // 메모리 해제
      free(g_score);
      free(f_score);
      free(came_from);
      free(closed_set);
      free(open_list->array);
      free(open_list);

      return result;
    }

    // 현재 정점을 closed set에 추가
    closed_set[current] = true;

    // 인접한 정점들 탐색
    for (int neighbor = 0; neighbor < vertices; neighbor++) {
      int weight = graph->adjMatrix[current][neighbor];

      // 간선이 존재하고, closed set에 없는 경우
      if (weight != 0 && !closed_set[neighbor]) {
        int tentative_g_score = g_score[current] + weight;

        printf("  Checking neighbor %d with tentative g=%d\n", neighbor,
               tentative_g_score);

        // 더 나은 경로를 발견했거나 처음 방문하는 정점인 경우
        if (g_score[neighbor] == INF || tentative_g_score < g_score[neighbor]) {
          // 경로 정보 업데이트
          came_from[neighbor] = current;
          g_score[neighbor] = tentative_g_score;
          f_score[neighbor] =
              g_score[neighbor] + heuristic(neighbor, goalVertex);

          printf("    Updated: g(%d)=%d, h(%d)=%d, f(%d)=%d\n", neighbor,
                 g_score[neighbor], neighbor, heuristic(neighbor, goalVertex),
                 neighbor, f_score[neighbor]);

          // open list에 추가
          insertPQ(open_list, neighbor, f_score[neighbor]);
          printf("    Added to open list\n");
        }
      }
    }

    // 현재 open list 출력 (중복 제거된 상태로)
    printf("  Current open list: [");
    bool first = true;
    bool visited[MAX_VERTICES] = {false};
    for (int i = 0; i < open_list->size; i++) {
      int v = open_list->array[i].vertex;
      if (!closed_set[v] && !visited[v]) {
        if (!first)
          printf(", ");
        printf("(%d,f=%d)", v, open_list->array[i].f_score);
        first = false;
        visited[v] = true;
      }
    }
    printf("]\n\n");
  }

  // 경로를 찾지 못한 경우
  printf("No path found from %d to %d\n", startVertex, goalVertex);

  // 메모리 해제
  free(g_score);
  free(f_score);
  free(came_from);
  free(closed_set);
  free(open_list->array);
  free(open_list);
  free(result->path);
  free(result);

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
  addEdge(graph, 2, 5, 1);   // 2→5
  addEdge(graph, 2, 6, 11);  // 2→6
  addEdge(graph, 3, 6, 9);   // 3→6
  addEdge(graph, 4, 5, 4);   // 4→5
  addEdge(graph, 4, 6, 20);  // 4→6
  addEdge(graph, 5, 6, 13);  // 5→6
  addEdge(graph, 5, 7, 6);   // 5→7
  addEdge(graph, 7, 4, 5);   // 7→4
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
