// huffmanCode.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 허프만 트리 노드 구조체
typedef struct Node {
  char character;
  int frequency;
  struct Node* left;
  struct Node* right;
} Node;

// 우선순위 큐를 위한 최소 힙 구조체
typedef struct MinHeap {
  int size;
  int capacity;
  Node** array;
} MinHeap;

// 새 노드 생성 함수
Node* createNode(char character, int frequency) {
  Node* node = (Node*)malloc(sizeof(Node));
  node->character = character;
  node->frequency = frequency;
  node->left = NULL;
  node->right = NULL;
  return node;
}

// 최소 힙 생성 함수
MinHeap* createMinHeap(int capacity) {
  MinHeap* minHeap = (MinHeap*)malloc(sizeof(MinHeap));
  minHeap->size = 0;
  minHeap->capacity = capacity;
  minHeap->array = (Node**)malloc(capacity * sizeof(Node*));
  return minHeap;
}

// 두 노드 교환 함수
void swapNode(Node** a, Node** b) {
  Node* temp = *a;
  *a = *b;
  *b = temp;
}

// 최소 힙화 함수
void minHeapify(MinHeap* minHeap, int index) {
  int smallest = index;
  int left = 2 * index + 1;
  int right = 2 * index + 2;

  if (left < minHeap->size &&
      minHeap->array[left]->frequency < minHeap->array[smallest]->frequency)
    smallest = left;

  if (right < minHeap->size &&
      minHeap->array[right]->frequency < minHeap->array[smallest]->frequency)
    smallest = right;

  if (smallest != index) {
    swapNode(&minHeap->array[smallest], &minHeap->array[index]);
    minHeapify(minHeap, smallest);
  }
}

// 최소값 추출 함수
Node* extractMin(MinHeap* minHeap) {
  Node* temp = minHeap->array[0];
  minHeap->array[0] = minHeap->array[minHeap->size - 1];
  --minHeap->size;
  minHeapify(minHeap, 0);
  return temp;
}

// 힙에 노드 삽입 함수
void insertMinHeap(MinHeap* minHeap, Node* node) {
  ++minHeap->size;
  int i = minHeap->size - 1;

  while (i && node->frequency < minHeap->array[(i - 1) / 2]->frequency) {
    minHeap->array[i] = minHeap->array[(i - 1) / 2];
    i = (i - 1) / 2;
  }

  minHeap->array[i] = node;
}

// 허프만 트리 구축 함수
Node* buildHuffmanTree(char characters[], int frequencies[], int size) {
  Node *left, *right, *top;

  // 1. 최소 힙 생성
  MinHeap* minHeap = createMinHeap(size);

  // 2. 각 문자에 대해 노드를 생성하여 힙에 삽입
  for (int i = 0; i < size; ++i) {
    insertMinHeap(minHeap, createNode(characters[i], frequencies[i]));
  }

  // 3. 허프만 트리 구성
  while (minHeap->size != 1) {
    // 빈도가 가장 작은 두 노드 추출
    left = extractMin(minHeap);
    right = extractMin(minHeap);

    // 새 내부 노드 생성 (문자는 '$', 빈도는 두 노드의 합)
    top = createNode('$', left->frequency + right->frequency);
    top->left = left;
    top->right = right;

    // 새 노드를 힙에 삽입
    insertMinHeap(minHeap, top);
  }

  // 루트 노드 반환
  return extractMin(minHeap);
}

// 허프만 코드 생성 및 출력 함수
void generateCodes(Node* root, char* code, int depth) {
  if (root != NULL) {
    // 리프 노드인 경우 (문자 노드)
    if (root->left == NULL && root->right == NULL) {
      printf("문자: %c, 빈도: %d, 코드: ", root->character, root->frequency);
      for (int i = 0; i < depth; i++) {
        printf("%c", code[i]);
      }
      printf("\n");
      return;
    }

    // 왼쪽으로 갈 때는 '1'
    if (root->left) {
      code[depth] = '1';
      generateCodes(root->left, code, depth + 1);
    }

    // 오른쪽으로 갈 때는 '0'
    if (root->right) {
      code[depth] = '0';
      generateCodes(root->right, code, depth + 1);
    }
  }
}

// 허프만 코딩 메인 함수
void huffmanCoding(char characters[], int frequencies[], int size) {
  // 1. 허프만 트리 구축
  Node* root = buildHuffmanTree(characters, frequencies, size);

  // 2. 허프만 코드 생성 및 출력
  char code[100];
  printf("=== 허프만 코딩 결과 ===\n");
  generateCodes(root, code, 0);
}

// 트리 출력 함수 (디버깅용)
void printTree(Node* root, int depth) {
  if (root != NULL) {
    for (int i = 0; i < depth; i++) {
      printf("  ");
    }
    if (root->character == '$') {
      printf("내부노드 (빈도: %d)\n", root->frequency);
    } else {
      printf("리프노드: %c (빈도: %d)\n", root->character, root->frequency);
    }
    printTree(root->left, depth + 1);
    printTree(root->right, depth + 1);
  }
}

// 압축률 계산 함수
void calculateCompressionRatio(char characters[], int frequencies[], int size) {
  // 원본 크기 계산 (각 문자당 8비트 가정)
  int originalSize = 0;
  for (int i = 0; i < size; i++) {
    originalSize += frequencies[i] * 8;
  }

  // 허프만 코드 크기 계산을 위한 함수 (간단화된 버전)
  printf("\n=== 압축률 분석 ===\n");
  printf("원본 크기 (8비트 고정 길이): %d 비트\n", originalSize);
  printf("예상 허프만 코드 크기는 트리 구조에 따라 계산됩니다.\n");
}

// 사용 예시
int main() {
  // 예제 데이터 (문제에서 제시된 빈도표)
  char characters[] = {'A', 'B', 'C', 'D'};
  int frequencies[] = {60, 25, 10, 5};
  int size = 4;

  printf("입력 데이터:\n");
  for (int i = 0; i < size; i++) {
    printf("문자: %c, 빈도: %d\n", characters[i], frequencies[i]);
  }
  printf("\n");

  // 허프만 코딩 수행
  huffmanCoding(characters, frequencies, size);

  // 압축률 분석
  calculateCompressionRatio(characters, frequencies, size);

  // 추가 테스트 케이스
  printf("\n--- 추가 테스트 케이스 ---\n");

  char characters2[] = {'a', 'b', 'c', 'd', 'e', 'f'};
  int frequencies2[] = {5, 9, 12, 13, 16, 45};
  int size2 = 6;

  printf("테스트 케이스 2:\n");
  huffmanCoding(characters2, frequencies2, size2);

  return 0;
}
