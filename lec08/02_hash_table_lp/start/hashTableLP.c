// hashTableLP.c - Hash Table with Linear Probing (START CODE)
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

// TODO: 해시 함수 구현 (간단한 modulo 연산)
int hashFunction(int key, int size) {
  // 여기에 해시 함수를 구현하세요
  return 0;  // 임시 반환값
}

// TODO: 해시 테이블 생성 함수 구현
struct HashTable* createHashTable(int size) {
  // 여기에 해시 테이블 생성 코드를 구현하세요
  // 1. 해시테이블 메모리 할당
  // 2. 크기와 카운트 설정
  // 3. 테이블 배열 메모리 할당
  // 4. 모든 슬롯을 빈 상태로 초기화 (is_occupied = false, is_deleted = false)
  return NULL;  // 임시 반환값
}

// 로드 팩터 계산 함수 (완성됨)
double getLoadFactor(struct HashTable* hashTable) {
  return (double)hashTable->count / hashTable->size;
}

// 크기 조정 함수 선언 (상호 참조 때문에)
struct HashTable* resize(struct HashTable* oldTable, int newSize);

// TODO: 삽입 함수 구현
void insert(struct HashTable** hashTable, int key, int value) {
  // 여기에 삽입 로직을 구현하세요
  // 1. 로드 팩터가 0.7을 초과하면 크기를 2배로 증가
  // 2. 해시 함수로 인덱스 계산
  // 3. 선형 탐사로 빈 슬롯 찾기
  // 4. 기존 키가 있으면 업데이트, 없으면 새로 삽입
}

// TODO: 검색 함수 구현
int* search(struct HashTable* hashTable, int key) {
  // 여기에 검색 로직을 구현하세요
  // 1. 해시 함수로 인덱스 계산
  // 2. 선형 탐사로 키 찾기
  // 3. 찾으면 값의 주소 반환, 못 찾으면 NULL 반환
  return NULL;  // 임시 반환값
}

// TODO: 삭제 함수 구현
bool deleteKey(struct HashTable* hashTable, int key) {
  // 여기에 삭제 로직을 구현하세요
  // 1. 해시 함수로 인덱스 계산
  // 2. 선형 탐사로 키 찾기
  // 3. Lazy deletion: 삭제 표시만 함 (is_deleted = true)
  // 4. 성공하면 true, 실패하면 false 반환
  return false;  // 임시 반환값
}

// 해시 테이블 출력 함수 (완성됨)
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

// 크기 조정 함수 (완성됨)
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

// 테이블 정리 함수 (완성됨)
void cleanup(struct HashTable** hashTable) {
  struct HashTable* newTable = resize(*hashTable, (*hashTable)->size);
  free((*hashTable)->table);
  free(*hashTable);
  *hashTable = newTable;
}

// 해시 테이블 메모리 해제 함수 (완성됨)
void freeHashTable(struct HashTable* hashTable) {
  free(hashTable->table);
  free(hashTable);
}

// 충돌 통계 계산 함수 (완성됨)
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

// 테스트 코드 (완성됨)
int main() {
  // 크기 7인 해시 테이블 생성
  struct HashTable* hashTable = createHashTable(7);

  if (hashTable == NULL) {
    printf("해시 테이블 생성 실패\n");
    return 1;
  }

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
