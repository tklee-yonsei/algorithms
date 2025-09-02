// random_program.c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/**
 * 간단한 랜덤 프로그램
 * 1. 고정 시드로 숫자 출력
 * 2. 다른 시드로 숫자 출력
 * 3. 시간 시드로 숫자 출력
 */

char *get_current_time_str() {
  static char time_str[20];
  time_t current_time = time(NULL);
  strftime(time_str, sizeof(time_str), "%Y-%m-%d %H:%M:%S",
           localtime(&current_time));
  return time_str;
}

void fixed_no_seed() {
  /* 고정 시드 없이 랜덤 숫자 생성 (매번 같은 숫자 출력) */
  time_t current_time = time(NULL);
  char *time_str = get_current_time_str();
  printf("1. 고정 시드 없이 (실행 시간 - %s):\n", time_str);
  for (int i = 0; i < 5; i++) {
    printf("%d\n", (rand() % 100) + 1);
  }
}

void fixed_seed_123() {
  /* 고정 시드 123으로 랜덤 숫자 생성 */
  char *time_str = get_current_time_str();
  printf("2. 다른 시드 (123) (실행 시간 - %s):\n", time_str);
  srand(123);
  for (int i = 0; i < 5; i++) {
    printf("%d\n", (rand() % 100) + 1);
  }
}

void time_seed() {
  /* 시간 기반 시드로 랜덤 숫자 생성 */
  char *time_str = get_current_time_str();
  printf("3. 시간 시드 (매번 다름) (실행 시간 - %s):\n", time_str);
  srand((unsigned int)time(NULL));
  for (int i = 0; i < 5; i++) {
    printf("%d\n", (rand() % 100) + 1);
  }
}

int main() {
  printf("=== C 랜덤 프로그램 ===\n");

  fixed_no_seed();
  printf("\n");

  fixed_seed_123();
  printf("\n");

  time_seed();
  return 0;
}