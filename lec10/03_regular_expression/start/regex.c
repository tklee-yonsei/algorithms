// regex.c - 시작 코드
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>

/**
 * 정규식 매칭 알고리즘 구현 (C 언어) - 시작 코드
 * 
 * 지원하는 메타 문자:
 * - '.' : 임의의 한 문자와 매칭
 * - '*' : 바로 앞 문자의 0개 이상 반복
 * - '^' : 문자열의 시작 (선택사항)
 * - '$' : 문자열의 끝 (선택사항)
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

// 함수 선언
bool match(char* pattern, char* text);
bool matchStar(char c, char* pattern, char* text);
bool matchAnywhere(char* pattern, char* text);
bool validatePattern(char* pattern);

/**
 * 기본 정규식 매칭 함수
 * 
 * @param pattern 정규식 패턴
 * @param text 검색할 텍스트
 * @return 매칭되면 true, 아니면 false
 */
bool match(char* pattern, char* text) {
    // TODO: 기본 정규식 매칭 구현
    // 1. 베이스 케이스: 패턴이 끝나면 성공
    // 2. 다음 문자가 '*'인 경우 (x* 패턴) -> matchStar 호출
    // 3. 텍스트가 끝났는데 패턴이 남아있으면 실패
    // 4. 현재 문자가 일치하거나 '.'인 경우 -> 재귀 호출
    // 5. 매칭 실패
    
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
    // TODO: '*' 메타문자 처리
    // 1. 0개 매칭 시도 (c*를 빈 문자열로 매칭)
    // 2. 1개 이상 매칭 시도 (반복)
    //    - 현재 텍스트 문자가 c와 일치하거나 c가 '.'인 경우
    //    - 텍스트를 한 문자씩 진행하면서 재귀 호출
    
    return false;
}

/**
 * 텍스트의 어느 위치에서든 패턴 매칭 시도
 * 
 * @param pattern 정규식 패턴
 * @param text 검색할 텍스트
 * @return 매칭되면 true, 아니면 false
 */
bool matchAnywhere(char* pattern, char* text) {
    // TODO: 텍스트의 어느 위치에서든 매칭 시도
    // 1. 빈 패턴은 항상 매칭
    // 2. '^'로 시작하는 패턴은 텍스트 시작에서만 매칭 (선택사항)
    // 3. '$'로 끝나는 패턴은 텍스트 끝에서만 매칭 (선택사항)
    // 4. 텍스트의 각 위치에서 match 함수 호출
    
    return false;
}

/**
 * 패턴의 문법 오류 검사
 * 
 * @param pattern 검사할 패턴
 * @return 유효하면 true, 아니면 false
 */
bool validatePattern(char* pattern) {
    // TODO: 패턴 유효성 검사
    // 1. NULL 체크
    // 2. '*'가 맨 앞에 오면 안됨
    // 3. '**' 패턴은 유효하지 않음
    
    return true;
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
        {"ca*t", "caaaat", true, "'a*' 여러 개 매칭"}
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
    
    // 패턴 검증 테스트
    printf("=== 패턴 검증 테스트 ===\n");
    char* testPatterns[] = {"*abc", "a**", "", "abc", "a*b*c"};
    int patternCount = sizeof(testPatterns) / sizeof(testPatterns[0]);
    
    for (int i = 0; i < patternCount; i++) {
        bool isValid = validatePattern(testPatterns[i]);
        printf("패턴: '%-5s' -> %s\n", testPatterns[i], 
               isValid ? "유효" : "무효");
    }
    printf("\n");
    
    printf("테스트 완료\n");
}

// 메인 함수
int main() {
    runTests();
    return 0;
}