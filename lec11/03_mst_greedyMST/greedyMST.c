#include <limits.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

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

// 함수 선언
MST* greedyMSTWithOptions(Graph* graph, bool useRandomCut, int fixedCutType);
MST* trueGreedyMST(Graph* graph);

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
 * Cut을 가로지르는 최소 가중치 간선 찾기 (Greedy MST 정의에 따라)
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
 * 모든 가능한 Cut을 검사하여 최적의 Cut 찾기 (진짜 Greedy MST)
 * @param graph: 그래프
 * @param inMST: MST에 포함된 정점들을 나타내는 boolean 배열
 * @return: 최소 가중치 간선의 인덱스 (없으면 -1)
 */
int findOptimalCut(Graph* graph, bool* inMST) {
  int minWeight = INF;
  int minEdgeIndex = -1;

  printf("  Searching for optimal cut (no red crossing edges)...\n");

  // 모든 간선을 가중치 순으로 정렬하여 검사
  // (실제로는 모든 간선을 검사하되, 가중치가 작은 것부터)
  for (int i = 0; i < graph->numEdges; i++) {
    int src = graph->edges[i].src;
    int dest = graph->edges[i].dest;
    int weight = graph->edges[i].weight;

    // Cut을 가로지르는 간선인지 확인
    if ((inMST[src] && !inMST[dest]) || (!inMST[src] && inMST[dest])) {
      printf("  Valid cut edge: (%d, %d, %d)\n", src, dest, weight);

      // 첫 번째로 찾은 간선이 최소 가중치 (Greedy 선택)
      if (weight < minWeight) {
        minWeight = weight;
        minEdgeIndex = i;
        printf("  -> New minimum weight: %d\n", weight);
      }
    }
  }

  if (minEdgeIndex != -1) {
    printf("  -> Selected optimal cut edge: (%d, %d, %d)\n",
           graph->edges[minEdgeIndex].src, graph->edges[minEdgeIndex].dest,
           graph->edges[minEdgeIndex].weight);
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
 * 랜덤 시작 정점 선택
 */
int getRandomStartVertex(int vertices) {
  return rand() % vertices;
}

/**
 * 이미지와 같은 수직/수평 cut을 시뮬레이션하는 정점 그룹 생성
 * @param vertices: 전체 정점 개수
 * @param cutType: 0=수직cut, 1=수평cut, 2=대각선cut, 3=랜덤
 * @param leftGroup: 왼쪽/위쪽 그룹에 포함될 정점들 (출력)
 * @param leftCount: 왼쪽/위쪽 그룹 정점 개수 (출력)
 */
void createRandomCut(int vertices, int cutType, int* leftGroup,
                     int* leftCount) {
  // 이미지의 정점 위치를 가정 (8개 정점의 2D 좌표)
  // 0:(1,3), 1:(3,0), 2:(3,2), 3:(4,0), 4:(0,3), 5:(2,1), 6:(5,3), 7:(2,2)
  int coords[8][2] = {{1, 3}, {3, 0}, {3, 2}, {4, 0},
                      {0, 3}, {2, 1}, {5, 3}, {2, 2}};

  *leftCount = 0;

  if (cutType == 0) {
    // 수직 cut (x < 2.5)
    printf("  Using vertical cut (x < 2.5)\n");
    for (int i = 0; i < vertices; i++) {
      if (coords[i][0] < 3) {  // x좌표가 3보다 작으면 왼쪽 그룹
        leftGroup[(*leftCount)++] = i;
      }
    }
  } else if (cutType == 1) {
    // 수평 cut (y < 1.5)
    printf("  Using horizontal cut (y < 1.5)\n");
    for (int i = 0; i < vertices; i++) {
      if (coords[i][1] < 2) {  // y좌표가 2보다 작으면 아래쪽 그룹
        leftGroup[(*leftCount)++] = i;
      }
    }
  } else if (cutType == 2) {
    // 대각선 cut
    printf("  Using diagonal cut (x + y < 4)\n");
    for (int i = 0; i < vertices; i++) {
      if (coords[i][0] + coords[i][1] < 4) {
        leftGroup[(*leftCount)++] = i;
      }
    }
  } else {
    // 랜덤 그룹 (절반 정도)
    printf("  Using random grouping\n");
    int targetSize = vertices / 2 + (rand() % 2);
    for (int i = 0; i < vertices; i++) {
      if (*leftCount < targetSize &&
          (rand() % (vertices - i) < targetSize - *leftCount)) {
        leftGroup[(*leftCount)++] = i;
      }
    }
  }
}

/**
 * Cut Property 기반 Greedy MST 알고리즘 (랜덤 cut 포함)
 * @param graph: 가중치 그래프
 * @param useRandomCut: true면 랜덤 cut 사용, false면 기존 방식
 * @return: MST 결과
 */
MST* greedyMST(Graph* graph) {
  return greedyMSTWithOptions(graph, true, -1);  // 랜덤 cut 타입
}

/**
 * 진짜 Greedy MST 알고리즘 (모든 가능한 Cut 검사)
 * @param graph: 가중치 그래프
 * @return: MST 결과
 */
MST* trueGreedyMST(Graph* graph) {
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

  printf("=== True Greedy MST Algorithm (All Possible Cuts) ===\n");
  printf("Finding cuts with no red crossing edges...\n\n");

  // 시작 정점 선택 (정점 0)
  int startVertex = 0;
  inMST[startVertex] = true;
  printf("Starting from vertex %d\n\n", startVertex);

  // MST 구성 메인 루프 (vertices-1개의 간선 필요)
  for (int step = 0; step < vertices - 1; step++) {
    // 현재 MST 상태 출력
    printMSTStatus(inMST, vertices, step);

    // 모든 가능한 Cut을 검사하여 최적의 Cut 찾기
    int minEdgeIndex = findOptimalCut(graph, inMST);

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

/**
 * Cut Property 기반 Greedy MST 알고리즘 (옵션 포함)
 * @param graph: 가중치 그래프
 * @param useRandomCut: true면 랜덤 cut 사용, false면 기존 방식
 * @param fixedCutType: -1이면 랜덤, 0-3이면 특정 cut 타입 고정
 * @return: MST 결과
 */
MST* greedyMSTWithOptions(Graph* graph, bool useRandomCut, int fixedCutType) {
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

  if (useRandomCut) {
    printf("=== Greedy MST Algorithm (Cut Property with Random Cuts) ===\n");

    // 랜덤 cut 방식: 첫 번째 단계에서 그래프를 두 그룹으로 나누기
    int cutType = (fixedCutType == -1) ? (rand() % 4)
                                       : fixedCutType;  // 고정 또는 랜덤 선택
    int leftGroup[MAX_VERTICES];
    int leftCount;

    createRandomCut(vertices, cutType, leftGroup, &leftCount);

    // 첫 번째 그룹의 모든 정점을 MST에 추가
    printf("Initial group vertices: {");
    for (int i = 0; i < leftCount; i++) {
      inMST[leftGroup[i]] = true;
      printf("%d ", leftGroup[i]);
    }
    printf("}\n\n");

    // 나머지는 기존 방식으로 진행
    for (int step = 0; step < vertices - leftCount; step++) {
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
  } else {
    // 기존 방식
    printf("=== Greedy MST Algorithm (Cut Property) ===\n");

    // 시작 정점 선택 (랜덤 또는 0)
    int startVertex = getRandomStartVertex(vertices);
    inMST[startVertex] = true;
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
  // 랜덤 시드 초기화 (일관된 결과를 위해 고정 시드 사용)
  srand(42);  // 고정 시드로 변경

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

  // 진짜 Greedy MST 실행 (모든 가능한 Cut 검사)
  printf("=== True Greedy MST Algorithm ===\n");
  MST* mst_true = trueGreedyMST(graph);
  printMST(mst_true);

  // 랜덤 시작 정점으로 Greedy MST 실행 (결과는 동일해야 함)
  printf("=== Random Start Vertex Greedy MST ===\n");
  MST* mst_random_start = greedyMSTWithOptions(graph, false, -1);
  printMST(mst_random_start);

  // 또 다른 랜덤 시작 정점으로 테스트
  printf("=== Another Random Start Vertex Greedy MST ===\n");
  MST* mst_random_start2 = greedyMSTWithOptions(graph, false, -1);
  printMST(mst_random_start2);

  // 메모리 해제
  freeMST(mst_true);
  freeMST(mst_random_start);
  freeMST(mst_random_start2);
  freeGraph(graph);

  return 0;
}
