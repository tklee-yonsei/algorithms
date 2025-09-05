// fsa_simple.c - 시작 코드 (교육용 간단 버전)
#include <stdbool.h>
#include <stdio.h>

/**
 * 간단한 FSA 예시: a(b)*c 패턴 인식
 *
 * 상태 다이어그램:
 * S0 --'a'--> S1 --ε--> S2 --'b'--> S3 --'b'--> S2 (loop)
 *                       S2 --'c'--> S4 (accept)
 *                       S3 --'c'--> S4 (accept)
 */

// 상태 정의
typedef enum {
  S0 = 0,  // 시작 상태
  S1 = 1,  // 'a'를 읽은 상태
  S2 = 2,  // b* 시작 상태 (0개의 'b' 허용)
  S3 = 3,  // 'b'를 1개 이상 읽은 상태
  S4 = 4   // 'c'를 읽어서 패턴 매칭 완료 (Accept 상태)
} State;

/**
 * 간단한 FSA 수락 함수
 */
bool accept(const char* input) {
  // TODO: FSA 구현
  // 1. 시작 상태 S0에서 시작
  // 2. 입력 문자열의 각 문자에 대해:
  //    - 현재 상태와 입력 문자에 따라 다음 상태 결정
  //    - switch문이나 if문을 사용하여 상태 전이 규칙 구현
  //      * S0에서 'a' 입력 시 -> S1, 그리고 epsilon 전이로 S2
  //      * S2에서 'b' 입력 시 -> S3
  //      * S2에서 'c' 입력 시 -> S4
  //      * S3에서 'b' 입력 시 -> S2 (루프백)
  //      * S3에서 'c' 입력 시 -> S4
  //      * S4에서 어떤 입력이든 -> 거부 (더 이상 입력 불가)
  //    - 정의되지 않은 전이는 거부
  // 3. 최종 상태가 수락 상태(S4)인지 확인

  State currentState = S0;
  printf("시작 상태: S%d\n", currentState);

  // 여기에 구현하세요

  return false;
}

int main() {
  printf("=== 간단한 FSA 예시: a(b)*c 패턴 ===\n\n");

  // 테스트 케이스들
  const char* testCases[] = {"ac", "abc", "abbc", "abbbc", "ab", "bc", "aac"};
  int numTests = sizeof(testCases) / sizeof(testCases[0]);

  for (int i = 0; i < numTests; i++) {
    printf("테스트: '%s'\n", testCases[i]);
    bool result = accept(testCases[i]);
    printf("결과: %s\n\n", result ? "✓ 수락" : "✗ 거부");
  }

  return 0;
}
