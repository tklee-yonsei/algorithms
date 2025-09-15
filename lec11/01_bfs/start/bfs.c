#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#define MAX_VERTICES 100

/**
 * 큐 구조체와 관련 함수들
 */
typedef struct {
  int data[MAX_VERTICES];
  int front;
  int rear;
  int size;
} Queue;

// 큐 초기화
void initQueue(Queue* q) {
  // TODO: 큐를 초기화하세요
}

// 큐가 비어있는지 확인
bool isEmpty(Queue* q) {
  // TODO: 큐가 비어있는지 확인하는 코드를 작성하세요
  return false;
}

// 큐에 원소 추가 (enqueue)
void enqueue(Queue* q, int value) {
  // TODO: 큐에 원소를 추가하는 코드를 작성하세요
}

// 큐에서 원소 제거 (dequeue)
int dequeue(Queue* q) {
  // TODO: 큐에서 원소를 제거하고 반환하는 코드를 작성하세요
  return -1;
}

/**
 * 그래프 구조체 (인접 리스트로 표현)
 */
typedef struct Node {
  int vertex;
  struct Node* next;
} Node;

typedef struct {
  int numVertices;
  Node** adjList;
} Graph;

// 그래프 생성
Graph* createGraph(int vertices) {
  Graph* graph = (Graph*)malloc(sizeof(Graph));
  graph->numVertices = vertices;
  graph->adjList = (Node**)malloc(vertices * sizeof(Node*));

  for (int i = 0; i < vertices; i++) {
    graph->adjList[i] = NULL;
  }

  return graph;
}

// 간선 추가 (무방향 그래프)
void addEdge(Graph* graph, int src, int dest) {
  // TODO: 무방향 그래프에 간선을 추가하는 코드를 작성하세요
  // src -> dest와 dest -> src 모두 추가해야 합니다
}

/**
 * BFS 알고리즘 구현
 * @param graph: 탐색할 그래프
 * @param startVertex: 시작 정점
 */
void BFS(Graph* graph, int startVertex) {
  // TODO: BFS 알고리즘을 구현하세요
  // 1. 방문 상태를 추적하는 배열 생성
  // 2. 큐 초기화
  // 3. 시작 정점을 explored로 표시하고 큐에 추가
  // 4. 큐가 비어있지 않은 동안 반복:
  //    - 큐에서 정점을 하나 꺼냄
  //    - 현재 정점의 모든 인접 정점을 확인
  //    - 아직 탐색되지 않은 인접 정점을 explored로 표시하고 큐에 추가

  printf("BFS Traversal starting from vertex %d: ", startVertex);
  // 구현 후 결과 출력
  printf("\n");
}

// 그래프 출력 (디버깅용)
void printGraph(Graph* graph) {
  printf("\nGraph representation (adjacency list):\n");
  for (int i = 0; i < graph->numVertices; i++) {
    printf("Vertex %d: ", i);
    Node* temp = graph->adjList[i];
    while (temp != NULL) {
      printf("%d -> ", temp->vertex);
      temp = temp->next;
    }
    printf("NULL\n");
  }
  printf("\n");
}

/**
 * 메인 함수 - 예제 실행
 */
int main() {
  printf("=== BFS (Breadth-First Search) Algorithm ===\n\n");

  // 그래프 생성 (7개 정점)
  Graph* graph = createGraph(7);

  // 간선 추가
  addEdge(graph, 0, 1);
  addEdge(graph, 0, 2);
  addEdge(graph, 1, 3);
  addEdge(graph, 1, 4);
  addEdge(graph, 2, 5);
  addEdge(graph, 2, 6);

  // 그래프 구조 출력
  printGraph(graph);

  // BFS 실행
  BFS(graph, 0);

  return 0;
}
