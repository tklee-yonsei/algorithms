// O1_constant.c
#include <stdbool.h>
#include <stdio.h>

// O(1) - 상수 시간복잡도
// 입력 크기와 관계없이 항상 일정한 시간이 걸림

int get_first_element(int arr[], int size) {
  // 배열의 첫 번째 요소 반환 - O(1)
  if (size > 0) {
    return arr[0];
  }
  return -1;  // 빈 배열인 경우
}

int add_numbers(int a, int b) {
  // 두 숫자 더하기 - O(1)
  return a + b;
}

bool check_if_even(int n) {
  // 짝수인지 확인 - O(1)
  return n % 2 == 0;
}

int main() {
  int numbers[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  int size = sizeof(numbers) / sizeof(numbers[0]);

  printf("O(1) 예시들:\n");
  printf("첫 번째 요소: %d\n", get_first_element(numbers, size));
  printf("5 + 3 = %d\n", add_numbers(5, 3));
  printf("7은 짝수인가? %s\n", check_if_even(7) ? "예" : "아니오");
  printf("8은 짝수인가? %s\n", check_if_even(8) ? "예" : "아니오");

  return 0;
}
