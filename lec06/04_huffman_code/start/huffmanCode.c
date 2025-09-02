// huffmanCode.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// TODO: 허프만 트리 노드 구조체를 정의하세요
typedef struct Node {
  char character;
  int frequency;
  struct Node* left;
  struct Node* right;
} Node;

// TODO: 우선순위 큐를 위한 최소 힙 구조체를 정의하세요
typedef struct MinHeap {
  int size;
  int capacity;
  Node** array;
} MinHeap;

// TODO: 새 노드 생성 함수를 구현하세요
Node* createNode(char character, int frequency) {
  // 새 노드를 할당하고 초기화
  return NULL;  // TODO: 실제 구현으로 교체
}

// TODO: 최소 힙 생성 함수를 구현하세요
MinHeap* createMinHeap(int capacity) {
  // 최소 힙을 생성하고 초기화
  return NULL;  // TODO: 실제 구현으로 교체
}

// TODO: 두 노드 교환 함수를 구현하세요
void swapNode(Node** a, Node** b) {
  // 두 노드의 포인터를 교환
}

// TODO: 최소 힙화 함수를 구현하세요
void minHeapify(MinHeap* minHeap, int index) {
  // 주어진 인덱스부터 힙 속성을 유지하도록 조정
}

// TODO: 최소값 추출 함수를 구현하세요
Node* extractMin(MinHeap* minHeap) {
  // 힙에서 최소값(루트)을 추출하고 힙 속성 유지
  return NULL;  // TODO: 실제 구현으로 교체
}

// TODO: 힙에 노드 삽입 함수를 구현하세요
void insertMinHeap(MinHeap* minHeap, Node* node) {
  // 새 노드를 힙에 삽입하고 힙 속성 유지
}

// TODO: 허프만 트리 구축 함수를 구현하세요
Node* buildHuffmanTree(char characters[], int frequencies[], int size) {
  // 1. 최소 힙 생성
  // 2. 각 문자에 대해 노드를 생성하여 힙에 삽입
  // 3. 허프만 트리 구성 (두 개씩 합치기)
  // 4. 루트 노드 반환
  return NULL;  // TODO: 실제 구현으로 교체
}

// TODO: 허프만 코드 생성 및 출력 함수를 구현하세요
void generateCodes(Node* root, char* code, int depth) {
  // 재귀적으로 트리를 순회하며 각 문자의 코드 생성
  // 왼쪽: '0', 오른쪽: '1'
  // 리프 노드에서 코드 출력
}

// TODO: 허프만 코딩 메인 함수를 구현하세요
void huffmanCoding(char characters[], int frequencies[], int size) {
  // 1. 허프만 트리 구축
  // 2. 허프만 코드 생성 및 출력
}

// 사용 예시
int main() {
  // 예제 데이터
  char characters[] = {'A', 'B', 'C', 'D'};
  int frequencies[] = {60, 25, 10, 5};
  int size = 4;

  printf("입력 데이터:\n");
  for (int i = 0; i < size; i++) {
    printf("문자: %c, 빈도: %d\n", characters[i], frequencies[i]);
  }
  printf("\n");

  // TODO: 허프만 코딩 수행
  // huffmanCoding(characters, frequencies, size);

  return 0;
}
