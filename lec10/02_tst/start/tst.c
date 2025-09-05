// tst.c - 시작 코드
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

/**
 * TST (Ternary Search Tree) 데이터 구조 구현 (C 언어) - 시작 코드
 *
 * 시간 복잡도:
 * - 평균 삽입: O(log n)
 * - 평균 검색: O(log n)
 * - 평균 삭제: O(log n)
 * - 최악의 경우: O(n) (불균형 트리)
 * 공간 복잡도: O(n) where n is the number of nodes
 */

// TST 노드 구조
typedef struct TSTNode {
    char data;              // 현재 노드의 문자
    bool hasValue;          // 값 존재 여부
    int value;              // 저장할 값
    struct TSTNode* left;   // 현재 문자보다 작은 문자
    struct TSTNode* middle; // 다음 문자로 이동
    struct TSTNode* right;  // 현재 문자보다 큰 문자
} TSTNode;

// 결과를 저장하기 위한 구조체
typedef struct WordValuePair {
    char word[100];
    int value;
} WordValuePair;

// 함수 선언
TSTNode* createTSTNode(char data);
TSTNode* insert(TSTNode* root, const char* word, int value, int index);
TSTNode* insertWord(TSTNode* root, const char* word, int value);
int search(TSTNode* root, const char* word, int index);
int searchWord(TSTNode* root, const char* word);
bool startsWith(TSTNode* root, const char* prefix, int index);
bool startsWithPrefix(TSTNode* root, const char* prefix);
void getAllWords(TSTNode* root, WordValuePair* results, int* count);
void getWordsWithPrefix(TSTNode* root, const char* prefix, WordValuePair* results, int* count);
TSTNode* deleteWord(TSTNode* root, const char* word);
void destroyTST(TSTNode* root);

/**
 * 새로운 TST 노드 생성 및 초기화
 *
 * @param data 노드에 저장할 문자
 * @return 새로 생성된 TSTNode 포인터
 */
TSTNode* createTSTNode(char data) {
    // TODO: 새로운 TSTNode 생성 및 초기화
    // 1. 메모리 할당
    // 2. data 설정
    // 3. hasValue를 false로, value를 0으로 초기화
    // 4. left, middle, right를 모두 NULL로 초기화
    return NULL;
}

/**
 * TST에 단어와 값을 삽입 (재귀적 구현)
 *
 * @param root 현재 노드
 * @param word 삽입할 단어
 * @param value 저장할 값
 * @param index 현재 문자 인덱스
 * @return 루트 노드 포인터
 */
TSTNode* insert(TSTNode* root, const char* word, int value, int index) {
    // TODO: TST에 재귀적으로 단어 삽입
    // 1. 단어 끝 확인
    // 2. 현재 문자 가져오기
    // 3. 루트가 NULL이면 새 노드 생성
    // 4. 문자 비교하여 left/middle/right로 이동
    // 5. 마지막 문자일 때 값 저장
    return NULL;
}

/**
 * TST에 단어와 값을 삽입하는 래퍼 함수
 *
 * @param root TST의 루트 노드
 * @param word 삽입할 단어
 * @param value 저장할 값
 * @return 루트 노드 포인터
 */
TSTNode* insertWord(TSTNode* root, const char* word, int value) {
    // TODO: 입력 검증 후 insert 함수 호출
    return NULL;
}

/**
 * TST에서 단어 검색 (재귀적 구현)
 *
 * @param root 현재 노드
 * @param word 검색할 단어
 * @param index 현재 문자 인덱스
 * @return 값이 있으면 해당 값, 없으면 -1
 */
int search(TSTNode* root, const char* word, int index) {
    // TODO: TST에서 재귀적으로 단어 검색
    // 1. NULL 체크 및 인덱스 범위 확인
    // 2. 현재 문자 가져오기
    // 3. 문자 비교하여 left/middle/right로 이동
    // 4. 마지막 문자일 때 값 반환
    return -1;
}

/**
 * TST에서 단어 검색하는 래퍼 함수
 *
 * @param root TST의 루트 노드
 * @param word 검색할 단어
 * @return 값이 있으면 해당 값, 없으면 -1
 */
int searchWord(TSTNode* root, const char* word) {
    // TODO: 입력 검증 후 search 함수 호출
    return -1;
}

/**
 * 주어진 prefix로 시작하는 단어들이 있는지 확인 (재귀적 구현)
 *
 * @param root 현재 노드
 * @param prefix 검색할 접두사
 * @param index 현재 문자 인덱스
 * @return 존재하면 true, 없으면 false
 */
bool startsWith(TSTNode* root, const char* prefix, int index) {
    // TODO: 접두사 존재 여부 확인
    // 1. NULL 체크
    // 2. prefix 끝까지 도달했으면 true
    // 3. 문자 비교하여 재귀 호출
    return false;
}

/**
 * 접두사 검색 래퍼 함수
 *
 * @param root TST의 루트 노드
 * @param prefix 검색할 접두사
 * @return 존재하면 true, 없으면 false
 */
bool startsWithPrefix(TSTNode* root, const char* prefix) {
    // TODO: 입력 검증 후 startsWith 함수 호출
    return false;
}

/**
 * TST의 모든 단어와 값을 반환
 *
 * @param root TST의 루트 노드
 * @param results 결과를 저장할 배열
 * @param count 결과 개수를 저장할 변수
 */
void getAllWords(TSTNode* root, WordValuePair* results, int* count) {
    // TODO: 모든 단어 수집
    // 헬퍼 함수 사용 권장
    *count = 0;
}

/**
 * 주어진 접두사로 시작하는 모든 단어와 값을 반환
 *
 * @param root TST의 루트 노드
 * @param prefix 검색할 접두사
 * @param results 결과를 저장할 배열
 * @param count 결과 개수를 저장할 변수
 */
void getWordsWithPrefix(TSTNode* root, const char* prefix, WordValuePair* results, int* count) {
    // TODO: 접두사로 시작하는 모든 단어 수집
    // 1. prefix에 해당하는 노드 찾기
    // 2. 해당 노드 이하 모든 단어 수집
    *count = 0;
}

/**
 * TST에서 단어 삭제
 *
 * @param root TST의 루트 노드
 * @param word 삭제할 단어
 * @return 삭제 후 루트 노드 포인터
 */
TSTNode* deleteWord(TSTNode* root, const char* word) {
    // TODO: 단어 삭제 (재귀적 구현 권장)
    return root;
}

/**
 * TST의 모든 노드를 메모리에서 해제
 *
 * @param root 해제할 노드
 */
void destroyTST(TSTNode* root) {
    // TODO: 후위 순회로 모든 노드 해제
    // 1. NULL 체크
    // 2. 모든 자식 노드 먼저 해제 (left, middle, right)
    // 3. 현재 노드 해제
}

/**
 * 테스트 함수
 */
void testTST() {
    printf("=== TST (Ternary Search Tree) 테스트 ===\n\n");
    
    // TST 생성
    TSTNode* root = NULL;
    
    // 테스트 데이터 삽입
    printf("=== 단어 삽입 테스트 ===\n");
    struct {
        const char* word;
        int value;
    } testWords[] = {
        {"apple", 10}, {"app", 5}, {"application", 20},
        {"apply", 8}, {"banana", 15}, {"band", 12}, {"bandana", 18},
        {"cat", 25}, {"car", 30}, {"card", 35}
    };
    
    int numTestWords = sizeof(testWords) / sizeof(testWords[0]);
    
    for (int i = 0; i < numTestWords; i++) {
        root = insertWord(root, testWords[i].word, testWords[i].value);
        printf("삽입: %s (값: %d)\n", testWords[i].word, testWords[i].value);
    }
    printf("\n");
    
    // 검색 테스트
    printf("=== 검색 테스트 ===\n");
    const char* searchWords[] = {"apple", "app", "application", "appl", "banana", "dog", "car"};
    int numSearchWords = sizeof(searchWords) / sizeof(searchWords[0]);
    
    for (int i = 0; i < numSearchWords; i++) {
        int result = searchWord(root, searchWords[i]);
        if (result != -1) {
            printf("검색: %s -> 찾음, 값: %d\n", searchWords[i], result);
        } else {
            printf("검색: %s -> 없음\n", searchWords[i]);
        }
    }
    printf("\n");
    
    // 접두사 검색 테스트
    printf("=== 접두사 검색 테스트 ===\n");
    const char* prefixes[] = {"app", "ban", "ca", "xyz"};
    int numPrefixes = sizeof(prefixes) / sizeof(prefixes[0]);
    
    for (int i = 0; i < numPrefixes; i++) {
        bool exists = startsWithPrefix(root, prefixes[i]);
        printf("접두사: %s -> %s\n", prefixes[i], exists ? "존재함" : "존재하지 않음");
        
        if (exists) {
            WordValuePair results[100];
            int count = 0;
            getWordsWithPrefix(root, prefixes[i], results, &count);
            printf("  관련 단어들: ");
            for (int j = 0; j < count; j++) {
                printf("%s(%d)", results[j].word, results[j].value);
                if (j < count - 1) printf(", ");
            }
            printf("\n");
        }
    }
    printf("\n");
    
    // 삭제 테스트
    printf("=== 삭제 테스트 ===\n");
    const char* deleteWords[] = {"app", "banana", "card"};
    int numDeleteWords = sizeof(deleteWords) / sizeof(deleteWords[0]);
    
    for (int i = 0; i < numDeleteWords; i++) {
        printf("삭제 전 검색: %s -> %d\n", deleteWords[i], searchWord(root, deleteWords[i]));
        root = deleteWord(root, deleteWords[i]);
        printf("삭제 후 검색: %s -> %d\n", deleteWords[i], searchWord(root, deleteWords[i]));
        printf("\n");
    }
    
    // 전체 단어 출력
    printf("=== 남은 모든 단어 출력 ===\n");
    WordValuePair allResults[100];
    int allCount = 0;
    getAllWords(root, allResults, &allCount);
    
    for (int i = 0; i < allCount; i++) {
        printf("%s: %d\n", allResults[i].word, allResults[i].value);
    }
    printf("\n");
    
    // 메모리 해제
    destroyTST(root);
    
    printf("테스트 완료\n");
}

// 메인 함수
int main() {
    testTST();
    return 0;
}