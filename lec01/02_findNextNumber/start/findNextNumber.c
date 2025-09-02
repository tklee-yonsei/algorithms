// findNextNumber.c
#include <stdio.h>

// TODO: 내가 적어둔 수열에서 다음 수를 찾는 함수를 작성하세요.
// 내가 적어둔 수열에서 다음 수를 찾는 함수
int findNextNumber(int previousNumber, int mySequence[], int sequenceLength) {
  // 여기에 코드를 작성하세요
  return -1;
}

// 사용 예시
int main() {
  // 내가 미리 적어둔 수열
  int mySequence[] = {
      1,         2,         4,          8,        16,       32,       64,
      128,       256,       512,        1024,     2048,     4096,     8192,
      16384,     32768,     65536,      131072,   262144,   524288,   1048576,
      2097152,   4194304,   8388608,    16777216, 33554432, 67108864, 134217728,
      268435456, 536870912, 1073741824,
  };
  int sequenceLength = sizeof(mySequence) / sizeof(mySequence[0]);

  int prevNum = 8;
  int result = findNextNumber(prevNum, mySequence, sequenceLength);

  if (result != -1) {
    printf("앞 사람이 %d를 말했으니, 나는 %d를 말한다.\n", prevNum, result);
  } else {
    printf("내 수열에서 %d를 찾을 수 없습니다.\n", prevNum);
  }

  return 0;
}
