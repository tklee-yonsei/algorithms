// hashTableSC.c - Hash Table with Separate Chaining (START CODE)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 해시 테이블 노드 구조체 (연결 리스트의 노드)
struct HashNode {
  int key;
  int value;
  struct HashNode* next;
};

// 해시 테이블 구조체
struct HashTable {
  int size;
  struct HashNode** table;
};

// TODO: 해시 함수 구현 (간단한 modulo 연산)
int hashFunction(int key, int size) {
  // 여기에 해시 함수를 구현하세요
  return 0;  // 임시 반환값
}

// 새 노드 생성 함수 (완성됨)
struct HashNode* createNode(int key, int value) {
  struct HashNode* newNode = (struct HashNode*)malloc(sizeof(struct HashNode));
  newNode->key = key;
  newNode->value = value;
  newNode->next = NULL;
  return newNode;
}

// TODO: 해시 테이블 생성 함수 구현
struct HashTable* createHashTable(int size) {
  // 여기에 해시 테이블 생성 코드를 구현하세요
  // 1. 해시테이블 메모리 할당
  // 2. 크기 설정
  // 3. 테이블 배열 메모리 할당
  // 4. 모든 버킷을 NULL로 초기화
  return NULL;  // 임시 반환값
}

// TODO: 삽입 함수 구현
void insert(struct HashTable* hashTable, int key, int value) {
  // 여기에 삽입 로직을 구현하세요
  // 1. 해시 함수로 인덱스 계산
  // 2. 기존 키가 있는지 확인 (업데이트)
  // 3. 새 노드를 리스트 앞에 삽입
}

// TODO: 검색 함수 구현
int* search(struct HashTable* hashTable, int key) {
  // 여기에 검색 로직을 구현하세요
  // 1. 해시 함수로 인덱스 계산
  // 2. 연결 리스트를 순회하며 키 찾기
  // 3. 찾으면 값의 주소 반환, 못 찾으면 NULL 반환
  return NULL;  // 임시 반환값
}

// TODO: 삭제 함수 구현
int deleteKey(struct HashTable* hashTable, int key) {
  // 여기에 삭제 로직을 구현하세요
  // 1. 해시 함수로 인덱스 계산
  // 2. 연결 리스트를 순회하며 키 찾기
  // 3. 노드 삭제 (첫 번째, 중간, 마지막 노드 케이스 고려)
  // 4. 성공하면 1, 실패하면 0 반환
  return 0;  // 임시 반환값
}

// 해시 테이블 출력 함수 (완성됨)
void printHashTable(struct HashTable* hashTable) {
  printf("해시 테이블 내용:\n");

  for (int i = 0; i < hashTable->size; i++) {
    printf("버킷 %d: ", i);
    struct HashNode* current = hashTable->table[i];

    if (current == NULL) {
      printf("(비어있음)");
    } else {
      while (current != NULL) {
        printf("[%d:%d]", current->key, current->value);
        if (current->next != NULL) {
          printf(" -> ");
        }
        current = current->next;
      }
    }
    printf("\n");
  }
}

// 해시 테이블 메모리 해제 함수 (완성됨)
void freeHashTable(struct HashTable* hashTable) {
  for (int i = 0; i < hashTable->size; i++) {
    struct HashNode* current = hashTable->table[i];
    while (current != NULL) {
      struct HashNode* temp = current;
      current = current->next;
      free(temp);
    }
  }

  free(hashTable->table);
  free(hashTable);
}

// 해시 테이블 크기 조정 함수 (완성됨)
struct HashTable* resize(struct HashTable* oldTable, int newSize) {
  struct HashTable* newTable = createHashTable(newSize);

  // 기존 모든 요소를 새 테이블에 재삽입
  for (int i = 0; i < oldTable->size; i++) {
    struct HashNode* current = oldTable->table[i];
    while (current != NULL) {
      insert(newTable, current->key, current->value);
      current = current->next;
    }
  }

  return newTable;
}

// 테스트 코드 (완성됨)
int main() {
  // 크기 7인 해시 테이블 생성
  struct HashTable* hashTable = createHashTable(7);

  if (hashTable == NULL) {
    printf("해시 테이블 생성 실패\n");
    return 1;
  }

  printf("=== 해시 테이블 (Separate Chaining) 테스트 ===\n\n");

  // 데이터 삽입
  printf(
      "데이터 삽입: (10,100), (22,220), (31,310), (4,40), (15,150), (28,280), "
      "(17,170)\n");
  insert(hashTable, 10, 100);
  insert(hashTable, 22, 220);
  insert(hashTable, 31, 310);
  insert(hashTable, 4, 40);
  insert(hashTable, 15, 150);
  insert(hashTable, 28, 280);
  insert(hashTable, 17, 170);

  printHashTable(hashTable);

  // 검색 테스트
  printf("\n=== 검색 테스트 ===\n");
  int* result = search(hashTable, 22);
  if (result != NULL) {
    printf("키 22 검색 결과: %d\n", *result);
  } else {
    printf("키 22를 찾을 수 없습니다.\n");
  }

  result = search(hashTable, 99);
  if (result != NULL) {
    printf("키 99 검색 결과: %d\n", *result);
  } else {
    printf("키 99를 찾을 수 없습니다.\n");
  }

  // 업데이트 테스트
  printf("\n=== 업데이트 테스트 ===\n");
  printf("키 22의 값을 999로 업데이트\n");
  insert(hashTable, 22, 999);
  printHashTable(hashTable);

  // 삭제 테스트
  printf("\n=== 삭제 테스트 ===\n");
  printf("키 22 삭제\n");
  if (deleteKey(hashTable, 22)) {
    printf("키 22 삭제 성공\n");
  } else {
    printf("키 22 삭제 실패\n");
  }
  printHashTable(hashTable);

  printf("\n키 99 삭제 시도\n");
  if (deleteKey(hashTable, 99)) {
    printf("키 99 삭제 성공\n");
  } else {
    printf("키 99 삭제 실패 (존재하지 않음)\n");
  }

  // 크기 조정 테스트
  printf("\n=== 크기 조정 테스트 ===\n");
  printf("해시 테이블 크기를 7에서 13으로 조정\n");
  struct HashTable* resizedTable = resize(hashTable, 13);
  printf("조정된 해시 테이블:\n");
  printHashTable(resizedTable);

  // 메모리 해제
  freeHashTable(hashTable);
  freeHashTable(resizedTable);

  return 0;
}
