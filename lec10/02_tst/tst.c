// tst.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

/**
 * TST (Ternary Search Tree) 데이터 구조 구현 (C 언어)
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
void getAllWordsHelper(TSTNode* node, char* prefix, int prefixLen, WordValuePair* results, int* count);
void getAllWords(TSTNode* root, WordValuePair* results, int* count);
TSTNode* getNodeByPrefix(TSTNode* root, const char* prefix, int index);
void getWordsWithPrefix(TSTNode* root, const char* prefix, WordValuePair* results, int* count);
bool hasChildren(TSTNode* node);
TSTNode* deleteHelper(TSTNode* root, const char* word, int index);
TSTNode* deleteWord(TSTNode* root, const char* word);
void destroyTST(TSTNode* root);
void printTST(TSTNode* root, int depth);
void printMiddleChain(TSTNode* root, int isFirst);
void printTSTDetailed(TSTNode* root, char* prefix, int depth);
void inOrderTraversal(TSTNode* root, char* word, int wordLen, WordValuePair* results, int* count);
void getSortedWords(TSTNode* root, WordValuePair* results, int* count);

/**
 * 새로운 TST 노드 생성 및 초기화
 *
 * @param data 노드에 저장할 문자
 * @return 새로 생성된 TSTNode 포인터
 */
TSTNode* createTSTNode(char data) {
    TSTNode* node = (TSTNode*)malloc(sizeof(TSTNode));
    
    if (node) {
        node->data = data;
        node->hasValue = false;
        node->value = 0;
        node->left = NULL;
        node->middle = NULL;
        node->right = NULL;
    }
    
    return node;
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
    if (index >= (int)strlen(word)) {
        return root;
    }
    
    char currentChar = word[index];
    
    // 루트가 NULL이면 새 노드 생성
    if (root == NULL) {
        root = createTSTNode(currentChar);
        if (root == NULL) {
            return NULL;  // 메모리 할당 실패
        }
    }
    
    // 현재 문자와 노드의 문자 비교
    if (currentChar < root->data) {
        root->left = insert(root->left, word, value, index);
    } else if (currentChar > root->data) {
        root->right = insert(root->right, word, value, index);
    } else {  // currentChar == root->data
        if (index == (int)strlen(word) - 1) {
            // 단어의 마지막 문자에 도달
            root->hasValue = true;
            root->value = value;
        } else {
            // 다음 문자로 이동
            root->middle = insert(root->middle, word, value, index + 1);
        }
    }
    
    return root;
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
    if (word == NULL || strlen(word) == 0) {
        return root;
    }
    return insert(root, word, value, 0);
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
    if (root == NULL || index >= (int)strlen(word)) {
        return -1;
    }
    
    char currentChar = word[index];
    
    if (currentChar < root->data) {
        return search(root->left, word, index);
    } else if (currentChar > root->data) {
        return search(root->right, word, index);
    } else {  // currentChar == root->data
        if (index == (int)strlen(word) - 1) {
            // 단어의 마지막 문자에 도달
            return root->hasValue ? root->value : -1;
        } else {
            // 다음 문자로 이동
            return search(root->middle, word, index + 1);
        }
    }
}

/**
 * TST에서 단어 검색하는 래퍼 함수
 *
 * @param root TST의 루트 노드
 * @param word 검색할 단어
 * @return 값이 있으면 해당 값, 없으면 -1
 */
int searchWord(TSTNode* root, const char* word) {
    if (word == NULL || strlen(word) == 0) {
        return -1;
    }
    return search(root, word, 0);
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
    if (root == NULL) {
        return false;
    }
    
    if (index >= (int)strlen(prefix)) {
        return true;  // 모든 prefix 문자를 찾음
    }
    
    char currentChar = prefix[index];
    
    if (currentChar < root->data) {
        return startsWith(root->left, prefix, index);
    } else if (currentChar > root->data) {
        return startsWith(root->right, prefix, index);
    } else {  // currentChar == root->data
        if (index == (int)strlen(prefix) - 1) {
            // prefix의 마지막 문자에 도달
            return true;
        } else {
            // 다음 문자로 이동
            return startsWith(root->middle, prefix, index + 1);
        }
    }
}

/**
 * 접두사 검색 래퍼 함수
 *
 * @param root TST의 루트 노드
 * @param prefix 검색할 접두사
 * @return 존재하면 true, 없으면 false
 */
bool startsWithPrefix(TSTNode* root, const char* prefix) {
    if (prefix == NULL || strlen(prefix) == 0) {
        return true;
    }
    return startsWith(root, prefix, 0);
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
void getAllWordsHelper(TSTNode* node, char* prefix, int prefixLen, WordValuePair* results, int* count) {
    if (node == NULL) {
        return;
    }
    
    // 왼쪽 서브트리 탐색 (현재 문자보다 작은 문자들)
    getAllWordsHelper(node->left, prefix, prefixLen, results, count);
    
    // 현재 노드 처리
    prefix[prefixLen] = node->data;
    prefix[prefixLen + 1] = '\0';
    
    // 현재 노드에 값이 저장되어 있다면 결과에 추가
    if (node->hasValue) {
        strcpy(results[*count].word, prefix);
        results[*count].value = node->value;
        (*count)++;
    }
    
    // 가운데 서브트리 탐색 (다음 문자들)
    getAllWordsHelper(node->middle, prefix, prefixLen + 1, results, count);
    
    // 백트래킹
    prefix[prefixLen] = '\0';
    
    // 오른쪽 서브트리 탐색 (현재 문자보다 큰 문자들)
    getAllWordsHelper(node->right, prefix, prefixLen, results, count);
}

/**
 * TST의 모든 단어와 값을 반환
 *
 * @param root TST의 루트 노드
 * @param results 결과를 저장할 배열
 * @param count 결과 개수를 저장할 변수
 */
void getAllWords(TSTNode* root, WordValuePair* results, int* count) {
    *count = 0;
    
    if (root != NULL) {
        char prefix[100] = "";
        getAllWordsHelper(root, prefix, 0, results, count);
    }
}

/**
 * prefix에 해당하는 노드를 찾아 반환 (재귀적 구현)
 *
 * @param root 현재 노드
 * @param prefix 찾을 접두사
 * @param index 현재 문자 인덱스
 * @return 해당 노드 포인터 또는 NULL
 */
TSTNode* getNodeByPrefix(TSTNode* root, const char* prefix, int index) {
    if (root == NULL) {
        return NULL;
    }
    
    if (index >= (int)strlen(prefix)) {
        return root;
    }
    
    char currentChar = prefix[index];
    
    if (currentChar < root->data) {
        return getNodeByPrefix(root->left, prefix, index);
    } else if (currentChar > root->data) {
        return getNodeByPrefix(root->right, prefix, index);
    } else {  // currentChar == root->data
        if (index == (int)strlen(prefix) - 1) {
            // prefix의 마지막 문자에 도달
            return root;
        } else {
            // 다음 문자로 이동
            return getNodeByPrefix(root->middle, prefix, index + 1);
        }
    }
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
    *count = 0;
    
    if (root == NULL || prefix == NULL) {
        return;
    }
    
    // prefix에 해당하는 노드를 찾음
    TSTNode* prefixNode = getNodeByPrefix(root, prefix, 0);
    
    if (prefixNode == NULL) {
        return;  // 접두사가 존재하지 않음
    }
    
    char fullPrefix[100];
    strcpy(fullPrefix, prefix);
    int prefixLen = strlen(prefix);
    
    // 해당 노드에 값이 있다면 추가 (prefix 자체가 완전한 단어인 경우)
    if (prefixNode->hasValue) {
        strcpy(results[*count].word, prefix);
        results[*count].value = prefixNode->value;
        (*count)++;
    }
    
    // 해당 노드의 middle 서브트리에서 모든 단어 수집
    getAllWordsHelper(prefixNode->middle, fullPrefix, prefixLen, results, count);
}

/**
 * 노드가 자식을 가지고 있는지 확인
 *
 * @param node 확인할 노드
 * @return 자식이 있으면 true, 없으면 false
 */
bool hasChildren(TSTNode* node) {
    if (node == NULL) {
        return false;
    }
    
    return node->left != NULL || node->middle != NULL || node->right != NULL;
}

/**
 * 삭제 헬퍼 함수 (재귀적 구현)
 *
 * @param root 현재 노드
 * @param word 삭제할 단어
 * @param index 현재 문자 인덱스
 * @return 삭제 후 현재 노드의 포인터 (NULL이면 노드 삭제됨)
 */
TSTNode* deleteHelper(TSTNode* root, const char* word, int index) {
    if (root == NULL || index >= (int)strlen(word)) {
        return root;
    }
    
    char currentChar = word[index];
    
    if (currentChar < root->data) {
        root->left = deleteHelper(root->left, word, index);
    } else if (currentChar > root->data) {
        root->right = deleteHelper(root->right, word, index);
    } else {  // currentChar == root->data
        if (index == (int)strlen(word) - 1) {
            // 단어의 마지막 문자에 도달
            root->hasValue = false;
            root->value = 0;
            
            // 자식이 없다면 노드 삭제
            if (!hasChildren(root)) {
                free(root);
                return NULL;
            }
        } else {
            // 다음 문자로 이동하여 삭제
            root->middle = deleteHelper(root->middle, word, index + 1);
            
            // 현재 노드에 값도 없고 자식도 없다면 삭제
            if (!root->hasValue && !hasChildren(root)) {
                free(root);
                return NULL;
            }
        }
    }
    
    return root;
}

/**
 * TST에서 단어 삭제하는 래퍼 함수
 *
 * @param root TST의 루트 노드
 * @param word 삭제할 단어
 * @return 삭제 후 루트 노드 포인터
 */
TSTNode* deleteWord(TSTNode* root, const char* word) {
    if (word == NULL || strlen(word) == 0) {
        return root;
    }
    return deleteHelper(root, word, 0);
}

/**
 * TST의 모든 노드를 메모리에서 해제
 *
 * @param root 해제할 노드
 */
void destroyTST(TSTNode* root) {
    if (root == NULL) {
        return;
    }
    
    // 후위 순회로 모든 자식 노드를 먼저 해제
    destroyTST(root->left);
    destroyTST(root->middle);
    destroyTST(root->right);
    
    // 현재 노드 해제
    free(root);
}

/**
 * TST 구조를 시각적으로 출력 (디버깅용)
 *
 * @param root 출력할 노드
 * @param depth 현재 깊이
 */
void printTST(TSTNode* root, int depth) {
    if (root == NULL) {
        return;
    }
    
    // 오른쪽 서브트리 먼저 출력
    printTST(root->right, depth + 1);
    
    // 들여쓰기 및 현재 노드 출력
    for (int i = 0; i < depth; i++) {
        printf("    ");
    }
    
    printf("%c", root->data);
    if (root->hasValue) {
        printf(" [값: %d]", root->value);
    }
    
    // middle 링크가 있으면 표시
    if (root->middle != NULL) {
        printf(" -> ");
        printMiddleChain(root->middle, 0);
    }
    printf("\n");
    
    // 왼쪽 서브트리 출력
    printTST(root->left, depth + 1);
}

/**
 * Middle 체인을 가로로 출력하는 헬퍼 함수
 *
 * @param root 현재 노드
 * @param isFirst 첫 번째 노드인지 여부
 */
void printMiddleChain(TSTNode* root, int isFirst) {
    if (root == NULL) {
        return;
    }
    
    if (!isFirst) {
        printf("-");
    }
    printf("%c", root->data);
    if (root->hasValue) {
        printf("[%d]", root->value);
    }
    
    if (root->middle != NULL) {
        printMiddleChain(root->middle, 0);
    }
}

/**
 * TST를 더 자세히 출력하는 함수
 *
 * @param root 출력할 노드
 * @param prefix 현재까지의 접두사
 * @param depth 현재 깊이
 */
void printTSTDetailed(TSTNode* root, char* prefix, int depth) {
    if (root == NULL) {
        return;
    }
    
    // 들여쓰기
    for (int i = 0; i < depth; i++) {
        printf("  ");
    }
    
    // 현재 노드 정보 출력
    printf("'%c'", root->data);
    if (root->hasValue) {
        printf(" [단어완성: %s, 값: %d]", prefix, root->value);
    }
    printf("\n");
    
    // 현재 문자를 prefix에 추가
    int prefixLen = strlen(prefix);
    prefix[prefixLen] = root->data;
    prefix[prefixLen + 1] = '\0';
    
    // left 서브트리
    if (root->left != NULL) {
        for (int i = 0; i < depth + 1; i++) printf("  ");
        printf("L:\n");
        // left는 같은 depth의 다른 문자이므로 prefix에서 마지막 문자 제거
        prefix[prefixLen] = '\0';
        printTSTDetailed(root->left, prefix, depth + 2);
        prefix[prefixLen] = root->data;
        prefix[prefixLen + 1] = '\0';
    }
    
    // middle 서브트리
    if (root->middle != NULL) {
        for (int i = 0; i < depth + 1; i++) printf("  ");
        printf("M:\n");
        printTSTDetailed(root->middle, prefix, depth + 2);
    }
    
    // right 서브트리
    if (root->right != NULL) {
        for (int i = 0; i < depth + 1; i++) printf("  ");
        printf("R:\n");
        // right는 같은 depth의 다른 문자이므로 prefix에서 마지막 문자 제거
        prefix[prefixLen] = '\0';
        printTSTDetailed(root->right, prefix, depth + 2);
        prefix[prefixLen] = root->data;
        prefix[prefixLen + 1] = '\0';
    }
    
    // 백트래킹
    prefix[prefixLen] = '\0';
}

/**
 * 중위 순회로 단어들을 사전순으로 수집
 *
 * @param root 현재 노드
 * @param word 현재까지 구성된 단어
 * @param wordLen 단어 길이
 * @param results 결과를 저장할 배열
 * @param count 결과 개수
 */
void inOrderTraversal(TSTNode* root, char* word, int wordLen, WordValuePair* results, int* count) {
    if (root == NULL) {
        return;
    }
    
    // 왼쪽 서브트리 먼저
    inOrderTraversal(root->left, word, wordLen, results, count);
    
    // 현재 노드 처리
    word[wordLen] = root->data;
    word[wordLen + 1] = '\0';
    
    // 값이 있다면 결과에 추가
    if (root->hasValue) {
        strcpy(results[*count].word, word);
        results[*count].value = root->value;
        (*count)++;
    }
    
    // 가운데 서브트리 (다음 문자들)
    inOrderTraversal(root->middle, word, wordLen + 1, results, count);
    
    // 백트래킹
    word[wordLen] = '\0';
    
    // 오른쪽 서브트리
    inOrderTraversal(root->right, word, wordLen, results, count);
}

/**
 * 사전순으로 정렬된 모든 단어를 반환
 *
 * @param root TST의 루트 노드
 * @param results 결과를 저장할 배열
 * @param count 결과 개수를 저장할 변수
 */
void getSortedWords(TSTNode* root, WordValuePair* results, int* count) {
    *count = 0;
    
    if (root != NULL) {
        char word[100] = "";
        inOrderTraversal(root, word, 0, results, count);
    }
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
    
    // TST 구조 출력
    printf("=== TST 구조 출력 (간단) ===\n");
    printTST(root, 0);
    printf("\n");
    
    // TST 상세 구조 출력
    printf("=== TST 상세 구조 출력 ===\n");
    char detailPrefix[100] = "";
    printTSTDetailed(root, detailPrefix, 0);
    printf("\n");
    
    // 사전순 정렬된 단어 출력
    printf("=== 사전순 정렬된 모든 단어 ===\n");
    WordValuePair sortedResults[100];
    int sortedCount = 0;
    getSortedWords(root, sortedResults, &sortedCount);
    
    for (int i = 0; i < sortedCount; i++) {
        printf("%s: %d\n", sortedResults[i].word, sortedResults[i].value);
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
    
    // 삭제 후 남은 단어 출력
    printf("=== 삭제 후 남은 모든 단어 ===\n");
    WordValuePair remainingResults[100];
    int remainingCount = 0;
    getAllWords(root, remainingResults, &remainingCount);
    
    for (int i = 0; i < remainingCount; i++) {
        printf("%s: %d\n", remainingResults[i].word, remainingResults[i].value);
    }
    printf("\n");
    
    // 대량 데이터 테스트
    printf("=== 대량 데이터 테스트 ===\n");
    const char* largeTestWords[] = {
        "the", "and", "for", "are", "but", "not", "you", "all",
        "can", "had", "her", "was", "one", "our", "out", "day",
        "get", "has", "him", "his", "how", "its", "may", "new",
        "now", "old", "see", "two", "way", "who", "boy", "did"
    };
    
    TSTNode* testRoot = NULL;
    int numLargeWords = sizeof(largeTestWords) / sizeof(largeTestWords[0]);
    
    for (int i = 0; i < numLargeWords; i++) {
        testRoot = insertWord(testRoot, largeTestWords[i], i + 100);
    }
    
    printf("대량 삽입 완료: %d개 단어\n", numLargeWords);
    
    // 접두사별 검색 성능 테스트
    const char* testPrefixes[] = {"t", "a", "c", "w"};
    int numTestPrefixes = sizeof(testPrefixes) / sizeof(testPrefixes[0]);
    
    for (int i = 0; i < numTestPrefixes; i++) {
        WordValuePair prefixResults[100];
        int prefixCount = 0;
        getWordsWithPrefix(testRoot, testPrefixes[i], prefixResults, &prefixCount);
        printf("접두사 '%s'로 시작하는 단어 수: %d\n", testPrefixes[i], prefixCount);
    }
    
    // 메모리 해제
    destroyTST(root);
    destroyTST(testRoot);
    
    printf("\n테스트 완료\n");
}

// 메인 함수
int main() {
    testTST();
    return 0;
}