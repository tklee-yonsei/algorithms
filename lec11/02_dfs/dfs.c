#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#define MAX_VERTICES 100

/**
 * 스택 구조체와 관련 함수들
 */
typedef struct {
  int data[MAX_VERTICES];
  int top;
} Stack;

// 스택 초기화
void initStack(Stack* s) {
  s->top = -1;
}

// 스택이 비어있는지 확인
bool isStackEmpty(Stack* s) {
  return s->top == -1;
}

// 스택이 가득 찼는지 확인
bool isStackFull(Stack* s) {
  return s->top == MAX_VERTICES - 1;
}

// 스택에 원소 추가 (push)
void push(Stack* s, int value) {
  if (isStackFull(s)) {
    printf("Stack is full!\n");
    return;
  }
  s->data[++s->top] = value;
}

// 스택 상태 출력 (디버깅용)
void printStack(Stack* s) {
  printf("[");
  for (int i = 0; i <= s->top; i++) {
    printf("%d", s->data[i]);
    if (i < s->top)
      printf(", ");
  }
  printf("]");
}

// 스택에서 원소 제거 (pop)
int pop(Stack* s) {
  if (isStackEmpty(s)) {
    printf("Stack is empty!\n");
    return -1;
  }
  return s->data[s->top--];
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
 * DFS 알고리즘 구현 (반복적)
 * @param graph: 탐색할 그래프
 * @param startVertex: 시작 정점
 */
void DFS_Iterative(Graph* graph, int startVertex) {
  if (startVertex >= graph->numVertices || startVertex < 0) {
    printf("Invalid start vertex!\n");
    return;
  }

  // 방문 상태를 추적하는 배열
  bool* explored = (bool*)calloc(graph->numVertices, sizeof(bool));

  // 스택 초기화
  Stack s;
  initStack(&s);

  // 시작 정점을 스택에 추가
  push(&s, startVertex);
  printf("Initial stack: ");
  printStack(&s);
  printf("\n");

  printf("DFS Iterative Traversal starting from vertex %d:\n", startVertex);

  // DFS 메인 루프
  while (!isStackEmpty(&s)) {
    printf("  Stack before pop: ");
    printStack(&s);

    // 스택에서 정점을 하나 꺼냄
    int currentVertex = pop(&s);
    printf(" -> Pop %d -> Stack after pop: ", currentVertex);
    printStack(&s);
    printf("\n");

    // 아직 탐색되지 않은 정점이라면
    if (!explored[currentVertex]) {
      explored[currentVertex] = true;
      printf("  Visit: %d\n", currentVertex);

      // 현재 정점의 모든 인접 정점을 스택에 추가 (역순으로)
      // 일관된 순서를 위해 배열에 저장 후 역순으로 push
      int neighbors[MAX_VERTICES];
      int neighborCount = 0;

      Node* temp = graph->adjList[currentVertex];
      while (temp != NULL) {
        neighbors[neighborCount++] = temp->vertex;
        temp = temp->next;
      }

      // 역순으로 스택에 추가
      for (int i = neighborCount - 1; i >= 0; i--) {
        if (!explored[neighbors[i]]) {
          push(&s, neighbors[i]);
          printf("  Push %d -> Stack: ", neighbors[i]);
          printStack(&s);
          printf("\n");
        }
      }
    } else {
      printf("  %d already visited, skip\n", currentVertex);
    }
    printf("\n");
  }

  printf("\n");
  free(explored);
}

/**
 * DFS 알고리즘 구현 (재귀적) - 보조 함수
 */
void DFS_Visit(Graph* graph, int vertex, bool* explored) {
  // 현재 정점을 방문 처리
  explored[vertex] = true;
  printf("%d ", vertex);

  // 현재 정점의 모든 인접 정점에 대해 재귀 호출
  Node* temp = graph->adjList[vertex];
  while (temp != NULL) {
    int adjVertex = temp->vertex;
    if (!explored[adjVertex]) {
      DFS_Visit(graph, adjVertex, explored);
    }
    temp = temp->next;
  }
}

/**
 * DFS 알고리즘 구현 (재귀적)
 * @param graph: 탐색할 그래프
 * @param startVertex: 시작 정점
 */
void DFS_Recursive(Graph* graph, int startVertex) {
  if (startVertex >= graph->numVertices || startVertex < 0) {
    printf("Invalid start vertex!\n");
    return;
  }

  // 방문 상태를 추적하는 배열
  bool* explored = (bool*)calloc(graph->numVertices, sizeof(bool));

  printf("DFS Recursive Traversal starting from vertex %d: ", startVertex);

  // 재귀 DFS 시작
  DFS_Visit(graph, startVertex, explored);

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
  printf("=== DFS (Depth-First Search) Algorithm ===\n\n");

  // 그래프 생성 (7개 정점)
  Graph* graph = createGraph(7);

  // 간선 추가
  //   addEdge(graph, 0, 1);
  //   addEdge(graph, 0, 2);
  //   addEdge(graph, 1, 3);
  //   addEdge(graph, 1, 4);
  //   addEdge(graph, 2, 5);
  //   addEdge(graph, 2, 6);

  addEdge(graph, 0, 1);
  addEdge(graph, 0, 2);
  addEdge(graph, 0, 5);
  addEdge(graph, 0, 6);
  addEdge(graph, 3, 4);
  addEdge(graph, 3, 5);
  addEdge(graph, 4, 5);
  addEdge(graph, 4, 6);

  // 그래프 구조 출력
  printGraph(graph);

  // DFS 실행 (한 개 예제만)
  printf("=== DFS Recursive ===\n");
  DFS_Recursive(graph, 0);

  printf("\n=== DFS Iterative (with stack visualization) ===\n");
  DFS_Iterative(graph, 0);

  printf("\n=== DFS with different graph ===\n");

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
  DFS_Recursive(graph2, 0);
  DFS_Iterative(graph2, 0);

  // 메모리 해제
  freeGraph(graph);
  freeGraph(graph2);

  return 0;
}
