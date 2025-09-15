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
 * @param heap: 힙 포인터
 * @param index: 정리를 시작할 인덱스
 */
void heapifyUp(MinHeap* heap, int index) {
  // TODO: 이 함수를 완성하세요!
  //
  // 힌트:
  // 1. 루트(index == 0)에 도달하면 종료
  // 2. 부모 인덱스 계산: getParentIndex(index)
  // 3. 현재 노드가 부모보다 작으면:
  //    - swap으로 교환
  //    - 재귀적으로 heapifyUp(heap, parentIndex) 호출
  // 4. 과정을 printf로 출력하여 디버깅
}

/**
 * 원소 삽입
 * @param heap: 힙 포인터
 * @param element: 삽입할 원소
 * @return: 성공 여부
 */
bool insert(MinHeap* heap, int element) {
  // TODO: 이 함수를 완성하세요!
  //
  // 힌트:
  // 1. 힙이 가득 찼는지 확인 (heap->size >= heap->capacity)
  // 2. 새 원소를 배열 끝에 추가
  // 3. size 증가
  // 4. heapifyUp으로 힙 속성 복구
  // 5. 성공 시 true 반환

  printf("=== Insert Function - TODO ===\n");
  return false;
}

/**
 * 하향 힙 정리 (Heapify Down)
 * @param heap: 힙 포인터
 * @param index: 정리를 시작할 인덱스
 */
void heapifyDown(MinHeap* heap, int index) {
  // TODO: 이 함수를 완성하세요!
  //
  // 힌트:
  // 1. 현재 인덱스를 최소값으로 초기화
  // 2. 왼쪽/오른쪽 자식 인덱스 계산
  // 3. 자식들과 비교하여 가장 작은 값의 인덱스 찾기
  // 4. 최소값이 현재 노드가 아니면:
  //    - swap으로 교환
  //    - 재귀적으로 heapifyDown 호출
}

/**
 * 최솟값 추출
 * @param heap: 힙 포인터
 * @return: 최솟값 (실패 시 ERROR_VALUE)
 */
int extractMin(MinHeap* heap) {
  // TODO: 이 함수를 완성하세요!
  //
  // 힌트:
  // 1. 빈 힙 확인 (heap->size == 0)
  // 2. 최솟값(루트) 저장
  // 3. 마지막 원소를 루트로 이동
  // 4. size 감소
  // 5. heapifyDown으로 힙 속성 복구
  // 6. 최솟값 반환

  printf("=== ExtractMin Function - TODO ===\n");
  return ERROR_VALUE;
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
  printf("=== Min Heap Demo (TODO Implementation) ===\n");

  // 힙 생성
  MinHeap* heap = createHeap(10);

  // 원소들 삽입
  int elements[] = {4, 7, 2, 9, 1, 5, 8};
  int numElements = sizeof(elements) / sizeof(elements[0]);

  printf("\n--- Insertion Phase ---\n");
  for (int i = 0; i < numElements; i++) {
    printf("\nInserting: %d\n", elements[i]);
    if (insert(heap, elements[i])) {
      printHeap(heap);
    }
  }

  printf("\n--- Extraction Phase ---\n");
  while (!isEmpty(heap)) {
    int min = extractMin(heap);
    if (min != ERROR_VALUE) {
      printf("Extracted: %d\n", min);
      printHeap(heap);
    }
    printf("\n");
  }

  // 메모리 해제
  freeHeap(heap);

  return 0;
}
