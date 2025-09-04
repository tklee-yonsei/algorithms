// lsdRadixSort.c - LSD Radix Sort (START CODE)
#include <stdio.h>
#include <stdlib.h>

/**
 * LSD (Least Significant Digit) Radix Sort 구현 (C 언어)
 *
 * 시간 복잡도: O(d * (n + k))
 * 공간 복잡도: O(n + k)
 *
 * d: 자릿수의 개수
 * n: 원소의 개수
 * k: 진법 (여기서는 10진법이므로 k=10)
 */

// 함수 선언
void print_array(int arr[], int n);

/**
 * 배열에서 최대값 찾기 (완성됨)
 *
 * @param arr 입력 배열
 * @param n 배열의 크기
 * @return 배열의 최대값
 */
int get_max(int arr[], int n) {
  int max = arr[0];
  for (int i = 1; i < n; i++) {
    if (arr[i] > max) {
      max = arr[i];
    }
  }
  return max;
}

/**
 * TODO: 특정 자릿수(exp)를 기준으로 counting sort 수행
 *
 * @param arr 정렬할 배열
 * @param n 배열의 크기
 * @param exp 현재 자릿수 (1, 10, 100, ...)
 */
void counting_sort_by_digit(int arr[], int n, int exp) {
  // TODO: Counting sort를 구현하세요
  // 힌트:
  // 1. output[n] 배열과 count[10] 배열 선언
  // 2. 각 자릿수의 빈도 계산: digit = (arr[i] / exp) % 10
  // 3. 누적 카운트로 변경 (위치 정보 생성)
  // 4. 뒤에서부터 처리하여 안정성 보장
  // 5. 결과를 원본 배열로 복사

  printf("  counting_sort_by_digit 구현 필요 (exp = %d)\n", exp);
}

/**
 * TODO: LSD Radix Sort 메인 함수
 *
 * @param arr 정렬할 배열
 * @param n 배열의 크기
 */
void lsd_radix_sort(int arr[], int n) {
  // TODO: LSD Radix Sort를 구현하세요
  // 힌트:
  // 1. get_max()를 사용해서 최대값 찾기
  // 2. exp = 1부터 시작해서 최고 자릿수까지 반복
  // 3. 각 자릿수에 대해 counting_sort_by_digit 호출
  // 4. 중간 과정 출력 (디버깅용)
  // 5. exp *= 10으로 다음 자릿수로 이동

  printf("lsd_radix_sort 구현 필요\n");
}

/**
 * 배열 출력 함수 (완성됨)
 *
 * @param arr 출력할 배열
 * @param n 배열의 크기
 */
void print_array(int arr[], int n) {
  printf("[");
  for (int i = 0; i < n; i++) {
    printf("%d", arr[i]);
    if (i < n - 1) {
      printf(", ");
    }
  }
  printf("]\n");
}

/**
 * 테스트 함수 (완성됨)
 */
void test_lsd_radix_sort() {
  printf("=== LSD Radix Sort 테스트 1 ===\n");
  int arr1[] = {170, 45, 75, 90, 2, 802, 24, 66};
  int n1 = sizeof(arr1) / sizeof(arr1[0]);

  printf("정렬 전: ");
  print_array(arr1, n1);

  lsd_radix_sort(arr1, n1);

  printf("최종 정렬 후: ");
  print_array(arr1, n1);

  printf("\n=== LSD Radix Sort 테스트 2 ===\n");
  int arr2[] = {329, 457, 657, 839, 436, 720, 355};
  int n2 = sizeof(arr2) / sizeof(arr2[0]);

  printf("정렬 전: ");
  print_array(arr2, n2);

  lsd_radix_sort(arr2, n2);

  printf("최종 정렬 후: ");
  print_array(arr2, n2);

  printf("\n=== 작은 숫자들 테스트 ===\n");
  int arr3[] = {9, 5, 1, 8, 3, 7, 2, 6, 4};
  int n3 = sizeof(arr3) / sizeof(arr3[0]);

  printf("정렬 전: ");
  print_array(arr3, n3);

  lsd_radix_sort(arr3, n3);

  printf("최종 정렬 후: ");
  print_array(arr3, n3);

  printf("\n=== 중복값 포함 테스트 ===\n");
  int arr4[] = {123, 456, 123, 789, 456, 123};
  int n4 = sizeof(arr4) / sizeof(arr4[0]);

  printf("정렬 전: ");
  print_array(arr4, n4);

  lsd_radix_sort(arr4, n4);

  printf("최종 정렬 후: ");
  print_array(arr4, n4);

  printf("\n=== 단일 자릿수 테스트 ===\n");
  int arr5[] = {4, 2, 7, 1, 9, 3};
  int n5 = sizeof(arr5) / sizeof(arr5[0]);

  printf("정렬 전: ");
  print_array(arr5, n5);

  lsd_radix_sort(arr5, n5);

  printf("최종 정렬 후: ");
  print_array(arr5, n5);
}

// 메인 함수 (완성됨)
int main() {
  test_lsd_radix_sort();
  return 0;
}
