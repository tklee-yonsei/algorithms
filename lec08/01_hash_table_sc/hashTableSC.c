// hashTableSC.c - Hash Table with Separate Chaining
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

// 해시 함수 (간단한 modulo 연산)
int hashFunction(int key, int size) {
  return key % size;
}

// 새 노드 생성 함수
struct HashNode* createNode(int key, int value) {
  struct HashNode* newNode = (struct HashNode*)malloc(sizeof(struct HashNode));
  newNode->key = key;
  newNode->value = value;
  newNode->next = NULL;
  return newNode;
}

// 해시 테이블 생성 함수
struct HashTable* createHashTable(int size) {
  struct HashTable* hashTable =
      (struct HashTable*)malloc(sizeof(struct HashTable));
  hashTable->size = size;
  hashTable->table = (struct HashNode**)malloc(size * sizeof(struct HashNode*));

  // 모든 버킷을 NULL로 초기화
  for (int i = 0; i < size; i++) {
    hashTable->table[i] = NULL;
  }

  return hashTable;
}

// 삽입 함수
void insert(struct HashTable* hashTable, int key, int value) {
  int index = hashFunction(key, hashTable->size);
  struct HashNode* current = hashTable->table[index];

  // 기존 키가 있는지 확인 (업데이트)
  while (current != NULL) {
    if (current->key == key) {
      current->value = value;
      return;
    }
    current = current->next;
  }

  // 새 노드를 리스트 앞에 삽입
  struct HashNode* newNode = createNode(key, value);
  newNode->next = hashTable->table[index];
  hashTable->table[index] = newNode;
}

// 검색 함수
int* search(struct HashTable* hashTable, int key) {
  int index = hashFunction(key, hashTable->size);
  struct HashNode* current = hashTable->table[index];

  while (current != NULL) {
    if (current->key == key) {
      return &(current->value);
    }
    current = current->next;
  }

  return NULL;  // 키를 찾지 못함
}

// 삭제 함수
int deleteKey(struct HashTable* hashTable, int key) {
  int index = hashFunction(key, hashTable->size);
  struct HashNode* current = hashTable->table[index];
  struct HashNode* prev = NULL;

  while (current != NULL) {
    if (current->key == key) {
      if (prev == NULL) {
        // 첫 번째 노드 삭제
        hashTable->table[index] = current->next;
      } else {
        // 중간 또는 마지막 노드 삭제
        prev->next = current->next;
      }

      free(current);
      return 1;  // 삭제 성공
    }

    prev = current;
    current = current->next;
  }

  return 0;  // 키를 찾지 못함
}

// 해시 테이블 출력 함수
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

// 해시 테이블 메모리 해제 함수
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

// 해시 테이블 크기 조정 함수
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

// 사용 예시
int main() {
  // 크기 7인 해시 테이블 생성
  struct HashTable* hashTable = createHashTable(7);

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
