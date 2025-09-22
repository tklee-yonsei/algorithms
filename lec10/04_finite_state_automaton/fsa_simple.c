// fsa_simple.c - 교육용 간단 버전
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
  State currentState = S0;

  printf("시작 상태: S%d\n", currentState);

  for (int i = 0; input[i] != '\0'; i++) {
    char ch = input[i];
    State nextState = currentState;

    // 상태 전이 규칙
    switch (currentState) {
      case S0:
        if (ch == 'a') {
          nextState = S1;
          printf("'%c' 입력 -> S%d\n", ch, nextState);
          // S1에서 epsilon 전이로 S2로 자동 이동
          currentState = S2;
          printf("ε 전이 -> S%d\n", currentState);
          continue;  // 다음 루프로 이동
        } else {
          return false;  // 거부
        }
        break;

      case S2:  // b* 시작 상태
        if (ch == 'b') {
          nextState = S3;
        } else if (ch == 'c') {
          nextState = S4;
        } else {
          return false;  // 거부
        }
        break;

      case S3:  // 'b'를 1개 이상 읽은 상태
        if (ch == 'b') {
          nextState = S2;  // S2로 돌아가서 루프
        } else if (ch == 'c') {
          nextState = S4;
        } else {
          return false;  // 거부
        }
        break;

      case S4:         // 수락 상태
        return false;  // 수락 후에는 더 이상 입력 불가

      default:
        return false;  // 정의되지 않은 상태
    }

    printf("'%c' 입력 -> S%d\n", ch, nextState);
    currentState = nextState;
  }

  // 최종 상태가 수락 상태(S4)인지 확인
  bool result = (currentState == S4);
  printf("최종 상태: S%d -> %s\n", currentState, result ? "수락" : "거부");
  return result;
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