// msdRadixSort.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * MSD (Most Significant Digit) Radix Sort 구현 (C 언어)
 *
 * 시간 복잡도: O(d * (n + k)) (평균), O(n^2) (최악)
 * 공간 복잡도: O(n + k)
 *
 * d: 자릿수의 개수
 * n: 원소의 개수
 * k: 진법 (여기서는 10진법이므로 k=10)
 */

#define RADIX 10

// 함수 선언
void print_array(int arr[], int n);
void print_array_range(int arr[], int start, int end);

/**
 * 배열에서 최대값 찾기
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
 * MSD용 카운팅 정렬 함수 (특정 자릿수 기준)
 *
 * @param arr 정렬할 배열
 * @param start 정렬 범위 시작 인덱스
 * @param end 정렬 범위 끝 인덱스
 * @param exp 현재 자릿수
 * @param bucket_sizes 각 버킷의 크기를 저장할 배열
 */
void counting_sort_by_digit_msd(int arr[], int start, int end, int exp,
                                int bucket_sizes[]) {
  int n = end - start + 1;
  int output[n];
  int count[RADIX] = {0};

  // 현재 자릿수(exp)에 대한 각 자릿수의 빈도 계산
  for (int i = start; i <= end; i++) {
    int digit = (arr[i] / exp) % RADIX;
    count[digit]++;
  }

  // 버킷 크기 저장 (재귀 호출을 위해)
  for (int i = 0; i < RADIX; i++) {
    bucket_sizes[i] = count[i];
  }

  // 누적 카운트로 변경 (위치 정보 생성)
  for (int i = 1; i < RADIX; i++) {
    count[i] += count[i - 1];
  }

  // 뒤에서부터 처리하여 안정성 보장
  for (int i = end; i >= start; i--) {
    int digit = (arr[i] / exp) % RADIX;
    output[count[digit] - 1] = arr[i];
    count[digit]--;
  }

  // 결과를 원본 배열의 해당 구간으로 복사
  for (int i = 0; i < n; i++) {
    arr[start + i] = output[i];
  }
}

/**
 * MSD Radix Sort 재귀 함수
 *
 * @param arr 정렬할 배열
 * @param start 정렬 범위 시작 인덱스
 * @param end 정렬 범위 끝 인덱스
 * @param exp 현재 자릿수 (가장 높은 자릿수부터 시작)
 */
void msd_radix_sort_recursive(int arr[], int start, int end, int exp) {
  if (start >= end || exp <= 0)
    return;

  int bucket_sizes[RADIX];

  // 현재 자릿수에 대해 카운팅 정렬 수행
  counting_sort_by_digit_msd(arr, start, end, exp, bucket_sizes);

  // 중간 과정 출력 (디버깅용)
  printf("자릿수 %d 정렬 후 (%d~%d): ", exp, start, end);
  print_array_range(arr, start, end);

  // 각 버킷에 대해 재귀적으로 정렬
  int current_start = start;
  for (int i = 0; i < RADIX; i++) {
    if (bucket_sizes[i] > 1) {
      msd_radix_sort_recursive(
          arr, current_start, current_start + bucket_sizes[i] - 1, exp / RADIX);
    }
    current_start += bucket_sizes[i];
  }
}

/**
 * MSD Radix Sort 메인 함수
 *
 * @param arr 정렬할 배열
 * @param n 배열의 크기
 */
void msd_radix_sort(int arr[], int n) {
  if (n <= 1)
    return;

  // 최대값 찾기
  int max = get_max(arr, n);

  // 최대 자릿수의 exp 값 계산
  int exp = 1;
  while (max / exp >= RADIX) {
    exp *= RADIX;
  }

  msd_radix_sort_recursive(arr, 0, n - 1, exp);
}

/**
 * 배열 출력 함수
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
 * 배열 범위 출력 함수
 *
 * @param arr 출력할 배열
 * @param start 시작 인덱스
 * @param end 끝 인덱스
 */
void print_array_range(int arr[], int start, int end) {
  printf("[");
  for (int i = start; i <= end; i++) {
    printf("%d", arr[i]);
    if (i < end) {
      printf(", ");
    }
  }
  printf("]\n");
}

/**
 * 테스트 함수
 */
void test_msd_radix_sort() {
  printf("=== MSD Radix Sort 테스트 1 ===\n");
  int arr1[] = {170, 45, 75, 90, 2, 802, 24, 66};
  int n1 = sizeof(arr1) / sizeof(arr1[0]);

  printf("정렬 전: ");
  print_array(arr1, n1);

  msd_radix_sort(arr1, n1);

  printf("최종 정렬 후: ");
  print_array(arr1, n1);

  printf("\n=== MSD Radix Sort 테스트 2 ===\n");
  int arr2[] = {329, 457, 657, 839, 436, 720, 355};
  int n2 = sizeof(arr2) / sizeof(arr2[0]);

  printf("정렬 전: ");
  print_array(arr2, n2);

  msd_radix_sort(arr2, n2);

  printf("최종 정렬 후: ");
  print_array(arr2, n2);

  printf("\n=== 작은 숫자들 테스트 ===\n");
  int arr3[] = {9, 5, 1, 8, 3, 7, 2, 6, 4};
  int n3 = sizeof(arr3) / sizeof(arr3[0]);

  printf("정렬 전: ");
  print_array(arr3, n3);

  msd_radix_sort(arr3, n3);

  printf("최종 정렬 후: ");
  print_array(arr3, n3);

  printf("\n=== 큰 숫자들 테스트 ===\n");
  int arr4[] = {1234, 5678, 9012, 3456, 7890};
  int n4 = sizeof(arr4) / sizeof(arr4[0]);

  printf("정렬 전: ");
  print_array(arr4, n4);

  msd_radix_sort(arr4, n4);

  printf("최종 정렬 후: ");
  print_array(arr4, n4);

  printf("\n=== 중복값 포함 테스트 ===\n");
  int arr5[] = {123, 456, 123, 789, 456, 123};
  int n5 = sizeof(arr5) / sizeof(arr5[0]);

  printf("정렬 전: ");
  print_array(arr5, n5);

  msd_radix_sort(arr5, n5);

  printf("최종 정렬 후: ");
  print_array(arr5, n5);

  printf("\n=== 다양한 자릿수 테스트 ===\n");
  int arr6[] = {5, 50, 500, 5000, 55, 555};
  int n6 = sizeof(arr6) / sizeof(arr6[0]);

  printf("정렬 전: ");
  print_array(arr6, n6);

  msd_radix_sort(arr6, n6);

  printf("최종 정렬 후: ");
  print_array(arr6, n6);
}

// 메인 함수
int main() {
  test_msd_radix_sort();
  return 0;
}
