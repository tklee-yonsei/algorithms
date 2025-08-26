// multiplyByTwo.c
#include <stdio.h>

// 앞 사람의 수에 2를 곱해서 답변하는 함수
int multiplyByTwo(int previousNumber) {
  int myAnswer = previousNumber * 2;
  return myAnswer;
}

// 사용 예시
int main() {
  int prevNum = 5;
  int result = multiplyByTwo(prevNum);
  printf("앞 사람이 %d를 말했으니, 나는 %d를 말한다.\n", prevNum, result);
  return 0;
}