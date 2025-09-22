// regex.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>

/**
 * 정규식 매칭 알고리즘 구현 (C 언어)
 * 
 * 지원하는 메타 문자:
 * - '.' : 임의의 한 문자와 매칭
 * - '*' : 바로 앞 문자의 0개 이상 반복
 * - '^' : 문자열의 시작
 * - '$' : 문자열의 끝
 * 
 * 시간 복잡도: O(m * n) where m is pattern length, n is text length
 * 공간 복잡도: O(1) (재귀 스택 제외)
 */

// 통계 정보를 저장하는 구조체
typedef struct {
    bool result;
    int comparisons;
    int recursion_depth;
    double execution_time;
} MatchStats;

// 전역 변수 (통계용)
static int g_comparisons = 0;
static int g_max_recursion = 0;
static int g_current_recursion = 0;

// 함수 선언
bool match(char* pattern, char* text);
bool matchStar(char c, char* pattern, char* text);
bool matchHere(char* pattern, char* text);
bool matchAnywhere(char* pattern, char* text);
bool validatePattern(char* pattern);
int countMatches(char* pattern, char* text);
char* replaceFirst(char* pattern, char* text, char* replacement);
MatchStats matchWithStats(char* pattern, char* text);

/**
 * 기본 정규식 매칭 함수
 * 
 * @param pattern 정규식 패턴
 * @param text 검색할 텍스트
 * @return 매칭되면 true, 아니면 false
 */
bool match(char* pattern, char* text) {
    g_comparisons++;
    g_current_recursion++;
    if (g_current_recursion > g_max_recursion) {
        g_max_recursion = g_current_recursion;
    }
    
    // 베이스 케이스: 패턴이 끝나면 성공
    if (*pattern == '\0') {
        g_current_recursion--;
        return true;
    }
    
    // 다음 문자가 '*'인 경우 (x* 패턴)
    if (*(pattern + 1) == '*') {
        bool result = matchStar(*pattern, pattern + 2, text);
        g_current_recursion--;
        return result;
    }
    
    // 텍스트가 끝났는데 패턴이 남아있으면 실패
    if (*text == '\0') {
        g_current_recursion--;
        return false;
    }
    
    // 현재 문자가 일치하거나 '.'인 경우
    if (*pattern == *text || *pattern == '.') {
        bool result = match(pattern + 1, text + 1);
        g_current_recursion--;
        return result;
    }
    
    // 매칭 실패
    g_current_recursion--;
    return false;
}

/**
 * '*' 메타문자 처리 함수
 * 
 * @param c '*' 앞의 문자 (또는 '.')
 * @param pattern '*' 이후의 패턴
 * @param text 검색할 텍스트
 * @return 매칭되면 true, 아니면 false
 */
bool matchStar(char c, char* pattern, char* text) {
    g_current_recursion++;
    if (g_current_recursion > g_max_recursion) {
        g_max_recursion = g_current_recursion;
    }
    
    // 0개 매칭 시도 (c*를 빈 문자열로 매칭)
    if (match(pattern, text)) {
        g_current_recursion--;
        return true;
    }
    
    // 1개 이상 매칭 시도
    while (*text != '\0' && (*text == c || c == '.')) {
        text++;
        if (match(pattern, text)) {
            g_current_recursion--;
            return true;
        }
    }
    
    // 모든 경우 실패
    g_current_recursion--;
    return false;
}

/**
 * 텍스트의 시작 부분부터 매칭 시도
 * 
 * @param pattern 정규식 패턴
 * @param text 검색할 텍스트
 * @return 매칭되면 true, 아니면 false
 */
bool matchHere(char* pattern, char* text) {
    return match(pattern, text);
}

/**
 * 텍스트의 어느 위치에서든 패턴 매칭 시도
 * 
 * @param pattern 정규식 패턴
 * @param text 검색할 텍스트
 * @return 매칭되면 true, 아니면 false
 */
bool matchAnywhere(char* pattern, char* text) {
    // 빈 패턴은 항상 매칭
    if (*pattern == '\0') {
        return true;
    }
    
    // 패턴이 '^'로 시작하면 텍스트 시작에서만 매칭
    if (*pattern == '^') {
        return matchHere(pattern + 1, text);
    }
    
    // 패턴이 '$'로 끝나면 텍스트 끝에서만 매칭
    int patternLen = strlen(pattern);
    if (patternLen > 0 && pattern[patternLen - 1] == '$') {
        // '$'를 임시로 제거하고 매칭 후 전체 텍스트가 소비되었는지 확인
        char* tempPattern = malloc(patternLen);
        strncpy(tempPattern, pattern, patternLen - 1);
        tempPattern[patternLen - 1] = '\0';
        
        // 텍스트의 각 위치에서 시도하되, 끝까지 매칭되는지 확인
        for (int i = 0; i <= (int)strlen(text); i++) {
            if (match(tempPattern, text + i) && strlen(text + i) == strlen(tempPattern)) {
                free(tempPattern);
                return true;
            }
        }
        free(tempPattern);
        return false;
    }
    
    // 텍스트의 각 위치에서 매칭 시도
    do {
        if (matchHere(pattern, text)) {
            return true;
        }
    } while (*text++ != '\0');
    
    return false;
}

/**
 * 패턴의 문법 오류 검사
 * 
 * @param pattern 검사할 패턴
 * @return 유효하면 true, 아니면 false
 */
bool validatePattern(char* pattern) {
    if (pattern == NULL) {
        return false;
    }
    
    int len = strlen(pattern);
    for (int i = 0; i < len; i++) {
        if (pattern[i] == '*') {
            // '*'가 맨 앞에 올 수 없음
            if (i == 0) {
                return false;
            }
            // '**' 패턴은 유효하지 않음
            if (i > 0 && pattern[i-1] == '*') {
                return false;
            }
        }
    }
    
    return true;
}

/**
 * 텍스트에서 패턴이 매칭되는 횟수 계산
 * 
 * @param pattern 정규식 패턴
 * @param text 검색할 텍스트
 * @return 매칭 횟수
 */
int countMatches(char* pattern, char* text) {
    int count = 0;
    int textLen = strlen(text);
    
    for (int i = 0; i <= textLen; i++) {
        if (matchHere(pattern, text + i)) {
            count++;
        }
    }
    
    return count;
}

/**
 * 첫 번째 매칭되는 부분을 replacement로 교체
 * 
 * @param pattern 정규식 패턴
 * @param text 원본 텍스트
 * @param replacement 교체할 문자열
 * @return 새로운 문자열 (동적 할당됨)
 */
char* replaceFirst(char* pattern, char* text, char* replacement) {
    int textLen = strlen(text);
    int replLen = strlen(replacement);
    
    // 매칭되는 위치 찾기
    for (int i = 0; i <= textLen; i++) {
        for (int j = 1; j <= textLen - i; j++) {
            char* substr = malloc(j + 1);
            strncpy(substr, text + i, j);
            substr[j] = '\0';
            
            if (match(pattern, substr)) {
                // 교체된 문자열 생성
                char* result = malloc(textLen - j + replLen + 1);
                strncpy(result, text, i);
                strcpy(result + i, replacement);
                strcpy(result + i + replLen, text + i + j);
                
                free(substr);
                return result;
            }
            free(substr);
        }
    }
    
    // 매칭되지 않으면 원본 복사
    char* result = malloc(textLen + 1);
    strcpy(result, text);
    return result;
}

/**
 * 통계 정보와 함께 매칭 수행
 * 
 * @param pattern 정규식 패턴
 * @param text 검색할 텍스트
 * @return 매칭 결과와 통계 정보
 */
MatchStats matchWithStats(char* pattern, char* text) {
    MatchStats stats;
    
    // 통계 초기화
    g_comparisons = 0;
    g_max_recursion = 0;
    g_current_recursion = 0;
    
    clock_t start = clock();
    stats.result = matchAnywhere(pattern, text);
    clock_t end = clock();
    
    stats.comparisons = g_comparisons;
    stats.recursion_depth = g_max_recursion;
    stats.execution_time = ((double)(end - start)) / CLOCKS_PER_SEC * 1000; // ms
    
    return stats;
}

/**
 * 문자가 숫자인지 확인
 */
bool isDigit(char c) {
    return c >= '0' && c <= '9';
}

/**
 * 문자가 알파벳 소문자인지 확인
 */
bool isLowerAlpha(char c) {
    return c >= 'a' && c <= 'z';
}

/**
 * 문자가 알파벳 대문자인지 확인
 */
bool isUpperAlpha(char c) {
    return c >= 'A' && c <= 'Z';
}

/**
 * 테스트 케이스 실행
 */
void runTests() {
    printf("=== 정규식 매칭 알고리즘 테스트 ===\n\n");
    
    // 기본 테스트 케이스들
    struct {
        char* pattern;
        char* text;
        bool expected;
        char* description;
    } testCases[] = {
        {"abc", "abc", true, "정확한 매칭"},
        {"a.c", "abc", true, "'.' 메타문자"},
        {"a.c", "adc", true, "'.' 메타문자 (다른 문자)"},
        {"a.c", "ac", false, "'.'는 반드시 한 문자 매칭"},
        {"a*", "", true, "'*' 0개 매칭"},
        {"a*", "a", true, "'*' 1개 매칭"},
        {"a*", "aaa", true, "'*' 여러 개 매칭"},
        {"a*b", "aaab", true, "'*' + 다른 문자"},
        {".*", "anything", true, "'.*'는 모든 문자열 매칭"},
        {"ca*t", "ct", true, "'a*' 0개 매칭"},
        {"ca*t", "cat", true, "'a*' 1개 매칭"},
        {"ca*t", "caaaat", true, "'a*' 여러 개 매칭"},
        {"ab*c", "ac", true, "b* 0개 매칭"},
        {"ab*c", "abc", true, "b* 1개 매칭"},
        {"ab*c", "abbbbc", true, "b* 여러 개 매칭"}
    };
    
    printf("=== 기본 매칭 테스트 ===\n");
    int testCount = sizeof(testCases) / sizeof(testCases[0]);
    int passCount = 0;
    
    for (int i = 0; i < testCount; i++) {
        bool result = matchAnywhere(testCases[i].pattern, testCases[i].text);
        bool passed = (result == testCases[i].expected);
        char* status = passed ? "PASS" : "FAIL";
        
        printf("패턴: '%-8s', 텍스트: '%-10s' -> %-5s (%s) [%s]\n", 
               testCases[i].pattern, testCases[i].text, 
               result ? "true" : "false", status, testCases[i].description);
        
        if (passed) passCount++;
    }
    
    printf("\n테스트 결과: %d/%d 통과\n\n", passCount, testCount);
    
    // 실제 사용 예시들
    printf("=== 실제 사용 예시 ===\n");
    
    // 간단한 이메일 패턴
    char* emails[] = {"user@example.com", "test@test", "invalid-email", "a@b.c"};
    char* emailPattern = ".*@.*\\..*";  // 단순화된 이메일 패턴
    
    printf("이메일 검증 (패턴: %s):\n", emailPattern);
    for (int i = 0; i < 4; i++) {
        bool isValid = matchAnywhere(emailPattern, emails[i]);
        printf("  %-20s -> %s\n", emails[i], isValid ? "유효" : "무효");
    }
    printf("\n");
    
    // 문자열 치환 예시
    printf("=== 문자열 치환 예시 ===\n");
    char* originalText = "Hello world";
    char* pattern = "world";
    char* replacement = "universe";
    
    char* replaced = replaceFirst(pattern, originalText, replacement);
    printf("원본: %s\n", originalText);
    printf("치환 후: %s\n", replaced);
    printf("\n");
    free(replaced);
    
    // 성능 테스트
    printf("=== 성능 테스트 ===\n");
    char longText[1001];
    for (int i = 0; i < 1000; i++) {
        longText[i] = 'a';
    }
    longText[1000] = 'b';
    longText[1001] = '\0';
    
    char* complexPattern = "a*b";
    
    MatchStats stats = matchWithStats(complexPattern, longText);
    printf("패턴: %s\n", complexPattern);
    printf("텍스트 길이: %d\n", 1001);
    printf("결과: %s\n", stats.result ? "매칭됨" : "매칭되지 않음");
    printf("실행 시간: %.3f ms\n", stats.execution_time);
    printf("비교 횟수: %d\n", stats.comparisons);
    printf("최대 재귀 깊이: %d\n", stats.recursion_depth);
    printf("\n");
    
    // 에러 케이스 테스트
    printf("=== 패턴 검증 테스트 ===\n");
    char* testPatterns[] = {"*abc", "a**", "", "abc", "a*b*c"};
    int patternCount = sizeof(testPatterns) / sizeof(testPatterns[0]);
    
    for (int i = 0; i < patternCount; i++) {
        bool isValid = validatePattern(testPatterns[i]);
        printf("패턴: '%-5s' -> %s\n", testPatterns[i], 
               isValid ? "유효" : "무효");
    }
    printf("\n");
    
    // 매칭 횟수 테스트
    printf("=== 매칭 횟수 테스트 ===\n");
    char* countText = "abcabcabc";
    char* countPattern = "abc";
    int matchCount = countMatches(countPattern, countText);
    printf("텍스트: %s\n", countText);
    printf("패턴: %s\n", countPattern);
    printf("매칭 횟수: %d\n", matchCount);
    printf("\n");
    
    printf("테스트 완료\n");
}

// 메인 함수
int main() {
    runTests();
    return 0;
}