// trie.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

/**
 * Trie (트라이) 데이터 구조 구현 (C 언어)
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
bool hasChildren(TrieNode* node);
void getAllWordsHelper(TrieNode* node, char* prefix, int prefixLen, WordValuePair* results, int* count);
bool deleteHelper(TrieNode* root, const char* word, int index, int wordLen);

/**
 * 새로운 Trie 노드 생성 및 초기화
 *
 * @return 새로 생성된 TrieNode 포인터
 */
TrieNode* createTrieNode() {
    TrieNode* node = (TrieNode*)malloc(sizeof(TrieNode));
    
    if (node) {
        for (int i = 0; i < ALPHABET_SIZE; i++) {
            node->children[i] = NULL;
        }
        node->hasValue = false;
        node->value = 0;
    }
    
    return node;
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
    if (root == NULL || word == NULL) {
        return false;
    }
    
    TrieNode* current = root;
    int wordLen = strlen(word);
    
    for (int i = 0; i < wordLen; i++) {
        int index = word[i] - 'a';  // 문자를 인덱스로 변환 (a=0, b=1, ...)
        
        if (index < 0 || index >= ALPHABET_SIZE) {
            return false;  // 유효하지 않은 문자
        }
        
        if (current->children[index] == NULL) {
            current->children[index] = createTrieNode();
            if (current->children[index] == NULL) {
                return false;  // 메모리 할당 실패
            }
        }
        
        current = current->children[index];
    }
    
    // 단어의 끝에서 값 저장
    current->hasValue = true;
    current->value = value;
    
    return true;
}

/**
 * Trie에서 단어 검색
 *
 * @param root Trie의 루트 노드
 * @param word 검색할 단어
 * @return 값이 있으면 해당 값, 없으면 -1
 */
int search(TrieNode* root, const char* word) {
    if (root == NULL || word == NULL) {
        return -1;
    }
    
    TrieNode* current = root;
    int wordLen = strlen(word);
    
    for (int i = 0; i < wordLen; i++) {
        int index = word[i] - 'a';
        
        if (index < 0 || index >= ALPHABET_SIZE || current->children[index] == NULL) {
            return -1;  // 경로가 존재하지 않음
        }
        
        current = current->children[index];
    }
    
    if (current->hasValue) {
        return current->value;
    } else {
        return -1;  // 단어는 존재하지만 값이 저장되지 않음
    }
}

/**
 * 주어진 prefix로 시작하는 단어들이 있는지 확인
 *
 * @param root Trie의 루트 노드
 * @param prefix 검색할 접두사
 * @return 존재하면 true, 없으면 false
 */
bool startsWith(TrieNode* root, const char* prefix) {
    if (root == NULL || prefix == NULL) {
        return false;
    }
    
    TrieNode* current = root;
    int prefixLen = strlen(prefix);
    
    for (int i = 0; i < prefixLen; i++) {
        int index = prefix[i] - 'a';
        
        if (index < 0 || index >= ALPHABET_SIZE || current->children[index] == NULL) {
            return false;
        }
        
        current = current->children[index];
    }
    
    return true;  // 접두사 경로가 존재함
}

/**
 * 노드가 자식을 가지고 있는지 확인
 *
 * @param node 확인할 노드
 * @return 자식이 있으면 true, 없으면 false
 */
bool hasChildren(TrieNode* node) {
    if (node == NULL) {
        return false;
    }
    
    for (int i = 0; i < ALPHABET_SIZE; i++) {
        if (node->children[i] != NULL) {
            return true;
        }
    }
    
    return false;
}

/**
 * 삭제 헬퍼 함수 (재귀적 구현)
 *
 * @param root 현재 노드
 * @param word 삭제할 단어
 * @param index 현재 문자 인덱스
 * @param wordLen 단어 길이
 * @return 현재 노드를 삭제해야 하면 true, 아니면 false
 */
bool deleteHelper(TrieNode* root, const char* word, int index, int wordLen) {
    if (root == NULL) {
        return false;
    }
    
    // 단어의 끝에 도달한 경우
    if (index == wordLen) {
        // 값이 저장되어 있지 않다면 삭제할 것이 없음
        if (!root->hasValue) {
            return false;
        }
        
        // 값을 제거
        root->hasValue = false;
        root->value = 0;
        
        // 자식이 없다면 이 노드는 삭제 가능
        return !hasChildren(root);
    }
    
    int charIndex = word[index] - 'a';
    if (charIndex < 0 || charIndex >= ALPHABET_SIZE) {
        return false;
    }
    
    bool shouldDeleteChild = deleteHelper(root->children[charIndex], word, index + 1, wordLen);
    
    if (shouldDeleteChild) {
        // 자식 노드 삭제
        free(root->children[charIndex]);
        root->children[charIndex] = NULL;
        
        // 현재 노드도 삭제 가능한지 확인
        // (값이 없고 다른 자식도 없다면 삭제 가능)
        return !root->hasValue && !hasChildren(root);
    }
    
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
    if (root == NULL || word == NULL) {
        return false;
    }
    
    int wordLen = strlen(word);
    deleteHelper(root, word, 0, wordLen);
    
    return true;
}

/**
 * 주어진 노드 이하의 모든 단어를 수집하는 헬퍼 함수
 *
 * @param node 현재 노드
 * @param prefix 현재까지의 접두사
 * @param prefixLen 접두사 길이
 * @param results 결과를 저장할 배열
 * @param count 현재 결과 개수 (참조로 전달)
 */
void getAllWordsHelper(TrieNode* node, char* prefix, int prefixLen, WordValuePair* results, int* count) {
    if (node == NULL) {
        return;
    }
    
    // 현재 노드에 값이 저장되어 있다면 결과에 추가
    if (node->hasValue) {
        strcpy(results[*count].word, prefix);
        results[*count].value = node->value;
        (*count)++;
    }
    
    // 모든 자식 노드에 대해 재귀 호출
    for (int i = 0; i < ALPHABET_SIZE; i++) {
        if (node->children[i] != NULL) {
            char ch = 'a' + i;
            prefix[prefixLen] = ch;
            prefix[prefixLen + 1] = '\0';
            getAllWordsHelper(node->children[i], prefix, prefixLen + 1, results, count);
            prefix[prefixLen] = '\0';  // 백트래킹
        }
    }
}

/**
 * Trie의 모든 단어와 값을 반환
 *
 * @param root Trie의 루트 노드
 * @param results 결과를 저장할 배열
 * @param count 결과 개수를 저장할 변수
 */
void getAllWords(TrieNode* root, WordValuePair* results, int* count) {
    *count = 0;
    
    if (root != NULL) {
        char prefix[100] = "";
        getAllWordsHelper(root, prefix, 0, results, count);
    }
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
    *count = 0;
    
    if (root == NULL || prefix == NULL) {
        return;
    }
    
    // prefix에 해당하는 노드로 이동
    TrieNode* current = root;
    int prefixLen = strlen(prefix);
    
    for (int i = 0; i < prefixLen; i++) {
        int index = prefix[i] - 'a';
        
        if (index < 0 || index >= ALPHABET_SIZE || current->children[index] == NULL) {
            return;  // 접두사가 존재하지 않음
        }
        
        current = current->children[index];
    }
    
    // 해당 노드 이하의 모든 단어 수집
    char fullPrefix[100];
    strcpy(fullPrefix, prefix);
    getAllWordsHelper(current, fullPrefix, prefixLen, results, count);
}

/**
 * Trie의 모든 노드를 메모리에서 해제
 *
 * @param root 해제할 노드
 */
void destroyTrie(TrieNode* root) {
    if (root == NULL) {
        return;
    }
    
    // 모든 자식 노드를 먼저 해제
    for (int i = 0; i < ALPHABET_SIZE; i++) {
        if (root->children[i] != NULL) {
            destroyTrie(root->children[i]);
        }
    }
    
    // 현재 노드 해제
    free(root);
}

/**
 * Trie 구조를 시각적으로 출력 (디버깅용)
 *
 * @param root 출력할 노드
 * @param prefix 현재까지의 접두사
 * @param depth 현재 깊이
 */
void printTrie(TrieNode* root, char* prefix, int depth) {
    if (root == NULL) {
        return;
    }
    
    // 들여쓰기 출력
    for (int i = 0; i < depth; i++) {
        printf("  ");
    }
    
    if (depth > 0) {
        printf("%c:", prefix[depth - 1]);
    } else {
        printf("ROOT:");
    }
    
    if (root->hasValue) {
        printf(" [값: %d]", root->value);
    }
    
    printf("\n");
    
    // 모든 자식에 대해 재귀 출력
    for (int i = 0; i < ALPHABET_SIZE; i++) {
        if (root->children[i] != NULL) {
            char ch = 'a' + i;
            prefix[depth] = ch;
            prefix[depth + 1] = '\0';
            printTrie(root->children[i], prefix, depth + 1);
            prefix[depth] = '\0';  // 백트래킹
        }
    }
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
    
    // Trie 구조 출력
    printf("=== Trie 구조 출력 ===\n");
    char prefix[100] = "";
    printTrie(root, prefix, 0);
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