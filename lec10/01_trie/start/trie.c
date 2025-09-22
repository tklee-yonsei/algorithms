// trie.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

/**
 * Trie (트라이) 데이터 구조 구현 (C 언어) - 시작 코드
 *
 * 시간 복잡도:
 * - 삽입: O(m) where m is the length of the word
 * - 검색: O(m) where m is the length of the word
 * - 삭제: O(m) where m is the length of the word
 * 공간 복잡도: O(ALPHABET_SIZE * N * M) where N is number of words, M is average length
 */

#define ALPHABET_SIZE 26

// 기본 구조 (정수 값 저장)
typedef struct TrieNode {
    struct TrieNode* children[26];  // a-z를 위한 배열
    bool hasValue;                  // 값이 저장되어 있는지 확인
    int value;                      // 실제 저장할 값 (빈도수, 점수 등)
} TrieNode;

// 결과를 저장하기 위한 구조체
typedef struct WordValuePair {
    char word[100];
    int value;
} WordValuePair;

// 함수 선언
TrieNode* createTrieNode();
bool insert(TrieNode* root, const char* word, int value);
int search(TrieNode* root, const char* word);
bool startsWith(TrieNode* root, const char* prefix);
bool deleteWord(TrieNode* root, const char* word);
void getAllWords(TrieNode* root, WordValuePair* results, int* count);
void getWordsWithPrefix(TrieNode* root, const char* prefix, WordValuePair* results, int* count);
void destroyTrie(TrieNode* root);
void printTrie(TrieNode* root, char* prefix, int depth);

/**
 * 새로운 Trie 노드 생성 및 초기화
 *
 * @return 새로 생성된 TrieNode 포인터
 */
TrieNode* createTrieNode() {
    // TODO: 새로운 TrieNode 생성 및 초기화
    // 1. 메모리 할당
    // 2. children 배열을 모두 NULL로 초기화
    // 3. hasValue를 false로, value를 0으로 초기화
    return NULL;
}

/**
 * Trie에 단어와 값을 삽입
 *
 * @param root Trie의 루트 노드
 * @param word 삽입할 단어
 * @param value 저장할 값
 * @return 성공하면 true, 실패하면 false
 */
bool insert(TrieNode* root, const char* word, int value) {
    // TODO: 단어와 값을 Trie에 삽입
    // 1. 입력 검증 (root, word가 NULL이 아닌지)
    // 2. 각 문자에 대해 경로 생성하며 이동
    // 3. 마지막 노드에서 값 저장
    return false;
}

/**
 * Trie에서 단어 검색
 *
 * @param root Trie의 루트 노드
 * @param word 검색할 단어
 * @return 값이 있으면 해당 값, 없으면 -1
 */
int search(TrieNode* root, const char* word) {
    // TODO: 단어 검색
    // 1. 입력 검증
    // 2. 각 문자에 대해 경로 따라가기
    // 3. 마지막 노드에서 값 확인
    return -1;
}

/**
 * 주어진 prefix로 시작하는 단어들이 있는지 확인
 *
 * @param root Trie의 루트 노드
 * @param prefix 검색할 접두사
 * @return 존재하면 true, 없으면 false
 */
bool startsWith(TrieNode* root, const char* prefix) {
    // TODO: 접두사 검색
    // 1. 입력 검증
    // 2. prefix의 각 문자에 대해 경로 확인
    // 3. 모든 문자에 대한 경로가 존재하면 true
    return false;
}

/**
 * Trie에서 단어 삭제
 *
 * @param root Trie의 루트 노드
 * @param word 삭제할 단어
 * @return 성공하면 true, 실패하면 false
 */
bool deleteWord(TrieNode* root, const char* word) {
    // TODO: 단어 삭제 (재귀적 구현 권장)
    // 1. 입력 검증
    // 2. 헬퍼 함수 호출
    return false;
}

/**
 * Trie의 모든 단어와 값을 반환
 *
 * @param root Trie의 루트 노드
 * @param results 결과를 저장할 배열
 * @param count 결과 개수를 저장할 변수
 */
void getAllWords(TrieNode* root, WordValuePair* results, int* count) {
    // TODO: 모든 단어 수집
    // 헬퍼 함수 사용 권장
    *count = 0;
}

/**
 * 주어진 접두사로 시작하는 모든 단어와 값을 반환
 *
 * @param root Trie의 루트 노드
 * @param prefix 검색할 접두사
 * @param results 결과를 저장할 배열
 * @param count 결과 개수를 저장할 변수
 */
void getWordsWithPrefix(TrieNode* root, const char* prefix, WordValuePair* results, int* count) {
    // TODO: 접두사로 시작하는 모든 단어 수집
    // 1. prefix에 해당하는 노드로 이동
    // 2. 해당 노드 이하의 모든 단어 수집
    *count = 0;
}

/**
 * Trie의 모든 노드를 메모리에서 해제
 *
 * @param root 해제할 노드
 */
void destroyTrie(TrieNode* root) {
    // TODO: 메모리 해제 (재귀적 구현)
    // 1. NULL 체크
    // 2. 모든 자식 노드 먼저 해제
    // 3. 현재 노드 해제
}

/**
 * Trie 구조를 시각적으로 출력 (디버깅용)
 *
 * @param root 출력할 노드
 * @param prefix 현재까지의 접두사
 * @param depth 현재 깊이
 */
void printTrie(TrieNode* root, char* prefix, int depth) {
    // TODO: Trie 구조 출력 (선택사항)
}

/**
 * 테스트 함수
 */
void testTrie() {
    printf("=== Trie 데이터 구조 테스트 ===\n\n");
    
    // Trie 생성
    TrieNode* root = createTrieNode();
    if (root == NULL) {
        printf("Trie 생성 실패\n");
        return;
    }
    
    // 테스트 데이터 삽입
    printf("=== 단어 삽입 테스트 ===\n");
    struct {
        const char* word;
        int value;
    } testWords[] = {
        {"apple", 10}, {"app", 5}, {"application", 20},
        {"apply", 8}, {"banana", 15}, {"band", 12}, {"bandana", 18}
    };
    
    int numTestWords = sizeof(testWords) / sizeof(testWords[0]);
    
    for (int i = 0; i < numTestWords; i++) {
        bool success = insert(root, testWords[i].word, testWords[i].value);
        printf("삽입: %s (값: %d) - %s\n", 
               testWords[i].word, testWords[i].value, 
               success ? "성공" : "실패");
    }
    printf("\n");
    
    // 검색 테스트
    printf("=== 검색 테스트 ===\n");
    const char* searchWords[] = {"apple", "app", "application", "appl", "banana", "cat"};
    int numSearchWords = sizeof(searchWords) / sizeof(searchWords[0]);
    
    for (int i = 0; i < numSearchWords; i++) {
        int result = search(root, searchWords[i]);
        if (result != -1) {
            printf("검색: %s -> 찾음, 값: %d\n", searchWords[i], result);
        } else {
            printf("검색: %s -> 없음\n", searchWords[i]);
        }
    }
    printf("\n");
    
    // 접두사 검색 테스트
    printf("=== 접두사 검색 테스트 ===\n");
    const char* prefixes[] = {"app", "ban", "cat", "a"};
    int numPrefixes = sizeof(prefixes) / sizeof(prefixes[0]);
    
    for (int i = 0; i < numPrefixes; i++) {
        bool exists = startsWith(root, prefixes[i]);
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
    const char* deleteWords[] = {"app", "banana"};
    int numDeleteWords = sizeof(deleteWords) / sizeof(deleteWords[0]);
    
    for (int i = 0; i < numDeleteWords; i++) {
        printf("삭제 전 검색: %s -> %d\n", deleteWords[i], search(root, deleteWords[i]));
        deleteWord(root, deleteWords[i]);
        printf("삭제 후 검색: %s -> %d\n", deleteWords[i], search(root, deleteWords[i]));
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
    destroyTrie(root);
    
    printf("테스트 완료\n");
}

// 메인 함수
int main() {
    testTrie();
    return 0;
}