#include <limits.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#define MAX_HEAP_SIZE 100
#define ERROR_VALUE -1

/**
 * 최소 힙 구조체
 */
typedef struct {
  int* array;    // 힙 배열
  int size;      // 현재 크기
  int capacity;  // 최대 용량
} MinHeap;

/**
 * 힙 생성
 */
MinHeap* createHeap(int capacity) {
  MinHeap* heap = (MinHeap*)malloc(sizeof(MinHeap));
  heap->array = (int*)malloc(capacity * sizeof(int));
  heap->size = 0;
  heap->capacity = capacity;
  return heap;
}

/**
 * 부모 인덱스 계산
 */
int getParentIndex(int index) {
  return (index - 1) / 2;
}

/**
 * 왼쪽 자식 인덱스 계산
 */
int getLeftChildIndex(int index) {
  return 2 * index + 1;
}

/**
 * 오른쪽 자식 인덱스 계산
 */
int getRightChildIndex(int index) {
  return 2 * index + 2;
}

/**
 * 두 원소 교환
 */
void swap(MinHeap* heap, int index1, int index2) {
  int temp = heap->array[index1];
  heap->array[index1] = heap->array[index2];
  heap->array[index2] = temp;
}

/**
 * 상향 힙 정리 (Heapify Up)
 */
void heapifyUp(MinHeap* heap, int index) {
  // 루트에 도달하면 종료
  if (index == 0) {
    return;
  }

  int parentIndex = getParentIndex(index);

  printf("Comparing %d (index %d) with parent %d (index %d)\n",
         heap->array[index], index, heap->array[parentIndex], parentIndex);

  // 현재 노드가 부모보다 작으면 교환
  if (heap->array[index] < heap->array[parentIndex]) {
    printf("Swapping %d with %d\n", heap->array[index],
           heap->array[parentIndex]);
    swap(heap, index, parentIndex);

    // 재귀적으로 부모 방향으로 계속 정리
    heapifyUp(heap, parentIndex);
  }
}

/**
 * 원소 삽입
 */
bool insert(MinHeap* heap, int element) {
  // 1. 힙이 가득 찬 경우 확인
  if (heap->size >= heap->capacity) {
    printf("Heap is full!\n");
    return false;
  }

  // 2. 힙의 마지막에 새 원소 추가
  heap->array[heap->size] = element;
  int lastIndex = heap->size;
  heap->size++;

  printf("Inserted %d at index %d\n", element, lastIndex);

  // 3. 힙 속성 복구 (상향 이동)
  heapifyUp(heap, lastIndex);

  return true;
}

/**
 * 하향 힙 정리 (Heapify Down)
 */
void heapifyDown(MinHeap* heap, int index) {
  int minIndex = index;
  int leftChild = getLeftChildIndex(index);
  int rightChild = getRightChildIndex(index);

  // 왼쪽 자식과 비교
  if (leftChild < heap->size &&
      heap->array[leftChild] < heap->array[minIndex]) {
    minIndex = leftChild;
  }

  // 오른쪽 자식과 비교
  if (rightChild < heap->size &&
      heap->array[rightChild] < heap->array[minIndex]) {
    minIndex = rightChild;
  }

  // 최솟값이 현재 노드가 아니면 교환 후 재귀
  if (minIndex != index) {
    printf("Swapping %d (index %d) with %d (index %d)\n", heap->array[index],
           index, heap->array[minIndex], minIndex);
    swap(heap, index, minIndex);

    // 재귀적으로 자식 방향으로 계속 정리
    heapifyDown(heap, minIndex);
  }
}

/**
 * 최솟값 추출
 */
int extractMin(MinHeap* heap) {
  // 1. 빈 힙 확인
  if (heap->size == 0) {
    printf("Heap is empty!\n");
    return ERROR_VALUE;
  }

  // 2. 최솟값 저장 (루트)
  int minValue = heap->array[0];

  // 3. 마지막 원소를 루트로 이동
  heap->array[0] = heap->array[heap->size - 1];
  heap->size--;

  printf("Extracted min value: %d\n", minValue);

  // 4. 힙이 비어있지 않으면 힙 속성 복구 (하향 이동)
  if (heap->size > 0) {
    printf("Moving %d to root, heapifying down\n", heap->array[0]);
    heapifyDown(heap, 0);
  }

  return minValue;
}

/**
 * 최솟값 조회 (추출하지 않고)
 */
int peek(MinHeap* heap) {
  if (heap->size == 0) {
    printf("Heap is empty!\n");
    return ERROR_VALUE;
  }

  return heap->array[0];
}

/**
 * 힙이 비어있는지 확인
 */
bool isEmpty(MinHeap* heap) {
  return heap->size == 0;
}

/**
 * 힙 출력
 */
void printHeap(MinHeap* heap) {
  if (heap->size == 0) {
    printf("Heap is empty\n");
    return;
  }

  printf("Heap contents: [");
  for (int i = 0; i < heap->size; i++) {
    printf("%d", heap->array[i]);
    if (i < heap->size - 1) {
      printf(", ");
    }
  }
  printf("]\n");
  printf("Size: %d\n", heap->size);
}

/**
 * 트리 구조로 힙 출력 (시각화)
 */
void printTreeStructure(MinHeap* heap) {
  if (heap->size == 0) {
    printf("Heap is empty\n");
    return;
  }

  printf("\n=== Heap Tree Structure ===\n");
  int level = 0;
  int index = 0;

  while (index < heap->size) {
    int levelSize = 1 << level;  // 2^level

    // 들여쓰기로 레벨 표현
    for (int indent = 0; indent < (3 - level) && level < 3; indent++) {
      printf("  ");
    }

    printf("Level %d: ", level);

    for (int i = 0; i < levelSize && index + i < heap->size; i++) {
      printf("%d ", heap->array[index + i]);
    }
    printf("\n");

    index += levelSize;
    level++;
  }
}

/**
 * 힙 메모리 해제
 */
void freeHeap(MinHeap* heap) {
  if (heap != NULL) {
    free(heap->array);
    free(heap);
  }
}

/**
 * 메인 함수 - 힙 데모
 */
int main() {
  printf("=== Min Heap Demo ===\n");

  // 힙 생성
  MinHeap* heap = createHeap(10);

  // 원소들 삽입
  int elements[] = {4, 7, 2, 9, 1, 5, 8};
  int numElements = sizeof(elements) / sizeof(elements[0]);

  printf("\n--- Insertion Phase ---\n");
  for (int i = 0; i < numElements; i++) {
    printf("\nInserting: %d\n", elements[i]);
    insert(heap, elements[i]);
    printHeap(heap);
    printTreeStructure(heap);
  }

  printf("\n--- Extraction Phase ---\n");
  while (!isEmpty(heap)) {
    int min = extractMin(heap);
    printf("Extracted: %d\n", min);
    printHeap(heap);
    if (!isEmpty(heap)) {
      printTreeStructure(heap);
    }
    printf("\n");
  }

  // 메모리 해제
  freeHeap(heap);

  return 0;
}
