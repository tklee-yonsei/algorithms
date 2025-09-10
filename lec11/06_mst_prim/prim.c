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
 * 힙 원소 구조체 (키-정점 쌍)
 */
typedef struct HeapNode {
  int key;     // 키 값 (가중치)
  int vertex;  // 정점 번호
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

  if (left < heap->size && heap->array[left].key < heap->array[smallest].key) {
    smallest = left;
  }

  if (right < heap->size &&
      heap->array[right].key < heap->array[smallest].key) {
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
 * 키 값 감소 (decreaseKey)
 */
void decreaseKey(MinHeap* heap, int vertex, int key) {
  int i = heap->pos[vertex];
  heap->array[i].key = key;

  // 상향 정리
  while (i && heap->array[i].key < heap->array[(i - 1) / 2].key) {
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
 * 배열에서 방문한 정점들을 출력하는 함수
 */
void printVisitedVertices(bool* visited, int vertices) {
  printf("  Current MST vertices: [");
  bool first = true;
  for (int i = 0; i < vertices; i++) {
    if (visited[i]) {
      if (!first)
        printf(", ");
      printf("%d", i);
      first = false;
    }
  }
  printf("]\n");
}

/**
 * Prim MST 알고리즘 - 우선순위 큐 기반
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

  // MST 결과 구조체 생성
  MST* mst = (MST*)malloc(sizeof(MST));
  mst->edges = (Edge*)malloc((vertices - 1) * sizeof(Edge));
  mst->numEdges = 0;
  mst->totalWeight = 0;

  // 초기화
  int* key = (int*)malloc(vertices * sizeof(int));  // 각 정점의 최소 가중치
  int* parent = (int*)malloc(vertices * sizeof(int));  // MST에서의 부모 정점
  bool* inMST = (bool*)malloc(vertices * sizeof(bool));  // MST 포함 여부

  // 최소 힙 생성
  MinHeap* heap = createMinHeap(vertices);

  // 배열 초기화
  for (int v = 0; v < vertices; v++) {
    parent[v] = -1;
    key[v] = INF;
    inMST[v] = false;
    heap->array[v].key = key[v];
    heap->array[v].vertex = v;
    heap->pos[v] = v;
  }

  // 시작 정점 설정
  key[startVertex] = 0;
  heap->array[startVertex].key = 0;
  heap->size = vertices;

  printf("=== Prim MST Algorithm (Priority Queue) ===\n");
  printf("Starting from vertex %d\n", startVertex);
  printf("Processing vertices in order of minimum key values:\n\n");

  int step = 1;

  // MST 구성
  while (!isEmpty(heap)) {
    // 최소 키 값을 가진 정점 추출
    HeapNode minNode = extractMin(heap);
    int u = minNode.vertex;

    if (u == -1)
      break;  // 더 이상 연결된 정점이 없음

    // 정점을 MST에 추가
    inMST[u] = true;

    if (parent[u] != -1) {
      // MST에 간선 추가
      mst->edges[mst->numEdges].src = parent[u];
      mst->edges[mst->numEdges].dest = u;
      mst->edges[mst->numEdges].weight = key[u];
      mst->numEdges++;
      mst->totalWeight += key[u];

      printf("Step %d: Added edge (%d, %d, %d) from heap\n", step, parent[u], u,
             key[u]);
    } else {
      printf("Step %d: Starting vertex %d (key = %d)\n", step, u, key[u]);
    }
    step++;

    // 인접한 정점들의 키 값 업데이트
    for (int v = 0; v < vertices; v++) {
      int weight = graph->adjMatrix[u][v];

      // 간선이 존재하고, MST에 포함되지 않았고, 더 작은 가중치를 가진 경우
      if (weight != 0 && !inMST[v] && isInMinHeap(heap, v) && weight < key[v]) {
        int oldKey = (key[v] == INF) ? -1 : key[v];
        key[v] = weight;
        parent[v] = u;

        // 힙에서 키 값 감소
        decreaseKey(heap, v, weight);

        printf("  Updated key[%d] = %d (via %d), was %s\n", v, weight, u,
               (oldKey == -1) ? "INF" : "");
        if (oldKey != -1) {
          printf("%d", oldKey);
        }
        printf("\n");
      }
    }

    // 현재 MST에 포함된 정점들 출력
    printf("  Current MST vertices: [");
    bool first = true;
    for (int i = 0; i < vertices; i++) {
      if (inMST[i]) {
        if (!first)
          printf(", ");
        printf("%d", i);
        first = false;
      }
    }
    printf("]\n\n");
  }

  // 메모리 해제
  free(key);
  free(parent);
  free(inMST);
  free(heap->array);
  free(heap->pos);
  free(heap);

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

  // 메모리 해제
  freeMST(mst);
  freeGraph(graph);

  return 0;
}
