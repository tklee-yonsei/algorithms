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
  q->front = 0;
  q->rear = -1;
  q->size = 0;
}

// 큐가 비어있는지 확인
bool isEmpty(Queue* q) {
  return q->size == 0;
}

// 큐가 가득 찼는지 확인
bool isFull(Queue* q) {
  return q->size == MAX_VERTICES;
}

// 큐에 원소 추가 (enqueue)
void enqueue(Queue* q, int value) {
  if (isFull(q)) {
    printf("Queue is full!\n");
    return;
  }
  q->rear = (q->rear + 1) % MAX_VERTICES;
  q->data[q->rear] = value;
  q->size++;
}

// 큐에서 원소 제거 (dequeue)
int dequeue(Queue* q) {
  if (isEmpty(q)) {
    printf("Queue is empty!\n");
    return -1;
  }
  int value = q->data[q->front];
  q->front = (q->front + 1) % MAX_VERTICES;
  q->size--;
  return value;
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
  // src -> dest 간선 추가
  Node* newNode = (Node*)malloc(sizeof(Node));
  newNode->vertex = dest;
  newNode->next = graph->adjList[src];
  graph->adjList[src] = newNode;

  // dest -> src 간선 추가 (무방향 그래프)
  newNode = (Node*)malloc(sizeof(Node));
  newNode->vertex = src;
  newNode->next = graph->adjList[dest];
  graph->adjList[dest] = newNode;
}

/**
 * BFS 알고리즘 구현
 * @param graph: 탐색할 그래프
 * @param startVertex: 시작 정점
 */
void BFS(Graph* graph, int startVertex) {
  if (startVertex >= graph->numVertices || startVertex < 0) {
    printf("Invalid start vertex!\n");
    return;
  }

  // 방문 상태를 추적하는 배열
  bool* explored = (bool*)calloc(graph->numVertices, sizeof(bool));

  // 큐 초기화
  Queue q;
  initQueue(&q);

  // 시작 정점을 explored로 표시하고 큐에 추가
  explored[startVertex] = true;
  enqueue(&q, startVertex);

  printf("BFS Traversal starting from vertex %d: ", startVertex);

  // BFS 메인 루프
  while (!isEmpty(&q)) {
    // 큐에서 정점을 하나 꺼냄
    int currentVertex = dequeue(&q);
    printf("%d ", currentVertex);

    // 현재 정점의 모든 인접 정점을 확인
    Node* temp = graph->adjList[currentVertex];
    while (temp != NULL) {
      int adjVertex = temp->vertex;

      // 인접 정점이 아직 탐색되지 않았다면
      if (!explored[adjVertex]) {
        explored[adjVertex] = true;
        enqueue(&q, adjVertex);
      }

      temp = temp->next;
    }
  }

  printf("\n");
  free(explored);
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

// 그래프 메모리 해제
void freeGraph(Graph* graph) {
  for (int i = 0; i < graph->numVertices; i++) {
    Node* temp = graph->adjList[i];
    while (temp != NULL) {
      Node* toDelete = temp;
      temp = temp->next;
      free(toDelete);
    }
  }
  free(graph->adjList);
  free(graph);
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

  // 각 정점에서 시작하는 BFS 실행
  printf("BFS traversals:\n");
  for (int i = 0; i < graph->numVertices; i++) {
    BFS(graph, i);
  }

  printf("\n=== BFS with different graph ===\n");

  // 다른 그래프 예제
  Graph* graph2 = createGraph(5);
  addEdge(graph2, 0, 1);
  addEdge(graph2, 0, 4);
  addEdge(graph2, 1, 2);
  addEdge(graph2, 1, 3);
  addEdge(graph2, 1, 4);
  addEdge(graph2, 2, 3);
  addEdge(graph2, 3, 4);

  printGraph(graph2);
  BFS(graph2, 0);

  // 메모리 해제
  freeGraph(graph);
  freeGraph(graph2);

  return 0;
}
