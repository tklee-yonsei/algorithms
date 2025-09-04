// hashTableLP.c - Hash Table with Linear Probing
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

// 해시 테이블 항목 구조체
struct HashItem {
  int key;
  int value;
  bool is_occupied;  // 슬롯이 사용 중인지
  bool is_deleted;   // lazy deletion을 위한 플래그
};

// 해시 테이블 구조체
struct HashTable {
  int size;
  int count;  // 사용된 항목 수
  struct HashItem* table;
};

// 해시 함수 (간단한 modulo 연산)
int hashFunction(int key, int size) {
  return key % size;
}

// 해시 테이블 생성 함수
struct HashTable* createHashTable(int size) {
  struct HashTable* hashTable =
      (struct HashTable*)malloc(sizeof(struct HashTable));
  hashTable->size = size;
  hashTable->count = 0;
  hashTable->table = (struct HashItem*)malloc(size * sizeof(struct HashItem));

  // 모든 슬롯을 빈 상태로 초기화
  for (int i = 0; i < size; i++) {
    hashTable->table[i].is_occupied = false;
    hashTable->table[i].is_deleted = false;
  }

  return hashTable;
}

// 로드 팩터 계산 함수
double getLoadFactor(struct HashTable* hashTable) {
  return (double)hashTable->count / hashTable->size;
}

// 크기 조정 함수 선언 (상호 참조 때문에)
struct HashTable* resize(struct HashTable* oldTable, int newSize);

// 삽입 함수
void insert(struct HashTable** hashTable, int key, int value) {
  // 로드 팩터가 0.7을 초과하면 크기를 2배로 증가
  if (getLoadFactor(*hashTable) > 0.7) {
    struct HashTable* resized = resize(*hashTable, (*hashTable)->size * 2);
    free((*hashTable)->table);
    free(*hashTable);
    *hashTable = resized;
  }

  int index = hashFunction(key, (*hashTable)->size);
  int originalIndex = index;

  while (true) {
    if (!(*hashTable)->table[index].is_occupied ||
        (*hashTable)->table[index].is_deleted) {
      // 빈 슬롯 또는 삭제된 슬롯 발견
      if (!(*hashTable)->table[index].is_occupied) {
        (*hashTable)->count++;
      }

      (*hashTable)->table[index].key = key;
      (*hashTable)->table[index].value = value;
      (*hashTable)->table[index].is_occupied = true;
      (*hashTable)->table[index].is_deleted = false;
      return;
    } else if ((*hashTable)->table[index].key == key &&
               !(*hashTable)->table[index].is_deleted) {
      // 기존 키 업데이트
      (*hashTable)->table[index].value = value;
      return;
    }

    // 다음 슬롯으로 이동 (선형 탐사)
    index = (index + 1) % (*hashTable)->size;

    // 테이블이 가득 참 (이론적으로는 발생하지 않아야 함)
    if (index == originalIndex) {
      printf("해시 테이블이 가득 참\n");
      return;
    }
  }
}

// 검색 함수
int* search(struct HashTable* hashTable, int key) {
  int index = hashFunction(key, hashTable->size);
  int originalIndex = index;

  while (hashTable->table[index].is_occupied) {
    if (!hashTable->table[index].is_deleted &&
        hashTable->table[index].key == key) {
      return &(hashTable->table[index].value);
    }

    // 다음 슬롯으로 이동
    index = (index + 1) % hashTable->size;

    // 한 바퀴 돌았으면 종료
    if (index == originalIndex) {
      break;
    }
  }

  return NULL;  // 키를 찾지 못함
}

// 삭제 함수
bool deleteKey(struct HashTable* hashTable, int key) {
  int index = hashFunction(key, hashTable->size);
  int originalIndex = index;

  while (hashTable->table[index].is_occupied) {
    if (!hashTable->table[index].is_deleted &&
        hashTable->table[index].key == key) {
      // Lazy deletion: 삭제 표시만 함
      hashTable->table[index].is_deleted = true;
      hashTable->count--;
      return true;
    }

    // 다음 슬롯으로 이동
    index = (index + 1) % hashTable->size;

    // 한 바퀴 돌았으면 종료
    if (index == originalIndex) {
      break;
    }
  }

  return false;  // 키를 찾지 못함
}

// 해시 테이블 출력 함수
void printHashTable(struct HashTable* hashTable) {
  printf("해시 테이블 내용 (크기: %d, 사용된 항목: %d, 로드 팩터: %.2f):\n",
         hashTable->size, hashTable->count, getLoadFactor(hashTable));

  for (int i = 0; i < hashTable->size; i++) {
    printf("슬롯 %2d: ", i);

    if (!hashTable->table[i].is_occupied) {
      printf("(비어있음)");
    } else if (hashTable->table[i].is_deleted) {
      printf("(삭제됨)");
    } else {
      printf("[%d:%d]", hashTable->table[i].key, hashTable->table[i].value);
    }
    printf("\n");
  }
}

// 크기 조정 함수
struct HashTable* resize(struct HashTable* oldTable, int newSize) {
  struct HashTable* newTable = createHashTable(newSize);

  // 기존 모든 요소를 새 테이블에 재삽입
  for (int i = 0; i < oldTable->size; i++) {
    if (oldTable->table[i].is_occupied && !oldTable->table[i].is_deleted) {
      insert(&newTable, oldTable->table[i].key, oldTable->table[i].value);
    }
  }

  return newTable;
}

// 테이블 정리 함수 (삭제된 항목들을 실제로 제거)
void cleanup(struct HashTable** hashTable) {
  struct HashTable* newTable = resize(*hashTable, (*hashTable)->size);
  free((*hashTable)->table);
  free(*hashTable);
  *hashTable = newTable;
}

// 해시 테이블 메모리 해제 함수
void freeHashTable(struct HashTable* hashTable) {
  free(hashTable->table);
  free(hashTable);
}

// 충돌 통계 계산 함수
void printStatistics(struct HashTable* hashTable) {
  int probes = 0;
  int maxProbes = 0;
  int itemsChecked = 0;

  for (int i = 0; i < hashTable->size; i++) {
    if (hashTable->table[i].is_occupied && !hashTable->table[i].is_deleted) {
      int key = hashTable->table[i].key;
      int expectedIndex = hashFunction(key, hashTable->size);
      int actualIndex = i;

      int probeCount = 0;
      if (actualIndex >= expectedIndex) {
        probeCount = actualIndex - expectedIndex;
      } else {
        probeCount = (hashTable->size - expectedIndex) + actualIndex;
      }

      probes += probeCount;
      maxProbes = (probeCount > maxProbes) ? probeCount : maxProbes;
      itemsChecked++;
    }
  }

  printf("\n=== 충돌 통계 ===\n");
  printf("총 항목 수: %d\n", itemsChecked);
  printf("총 프로브 수: %d\n", probes);
  printf("평균 프로브 수: %.2f\n",
         itemsChecked > 0 ? (double)probes / itemsChecked : 0);
  printf("최대 프로브 수: %d\n", maxProbes);
}

// 사용 예시
int main() {
  // 크기 7인 해시 테이블 생성
  struct HashTable* hashTable = createHashTable(7);

  printf("=== 해시 테이블 (Linear Probing) 테스트 ===\n\n");

  // 데이터 삽입
  printf(
      "데이터 삽입: (10,100), (22,220), (31,310), (4,40), (15,150), (28,280), "
      "(17,170)\n");
  insert(&hashTable, 10, 100);
  insert(&hashTable, 22, 220);
  insert(&hashTable, 31, 310);
  insert(&hashTable, 4, 40);
  insert(&hashTable, 15, 150);
  insert(&hashTable, 28, 280);
  insert(&hashTable, 17, 170);

  printHashTable(hashTable);
  printStatistics(hashTable);

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
  insert(&hashTable, 22, 999);
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

  // 더 많은 데이터 삽입 (자동 크기 조정 테스트)
  printf("\n=== 자동 크기 조정 테스트 ===\n");
  printf("더 많은 데이터 삽입 (자동 크기 조정 발생)\n");
  insert(&hashTable, 35, 350);
  insert(&hashTable, 42, 420);
  insert(&hashTable, 56, 560);

  printHashTable(hashTable);
  printStatistics(hashTable);

  // 테이블 정리 테스트
  printf("\n=== 테이블 정리 테스트 ===\n");
  printf("삭제된 항목들을 실제로 제거\n");
  cleanup(&hashTable);
  printHashTable(hashTable);

  // 메모리 해제
  freeHashTable(hashTable);

  return 0;
}
