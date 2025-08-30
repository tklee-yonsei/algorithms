// countingSort.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * 카운팅 정렬 구현 (C 언어)
 *
 * 시간 복잡도: O(n + k)
 * 공간 복잡도: O(k)
 *
 * n: 원소의 개수
 * k: 값의 범위 (max - min + 1)
 */

// 함수 선언
void print_array(int arr[], int n);

// 배열의 최대값 찾기
int find_max(int arr[], int n) {
  int max = arr[0];
  for (int i = 1; i < n; i++) {
    if (arr[i] > max) {
      max = arr[i];
    }
  }
  return max;
}

// 배열의 최소값 찾기
int find_min(int arr[], int n) {
  int min = arr[0];
  for (int i = 1; i < n; i++) {
    if (arr[i] < min) {
      min = arr[i];
    }
  }
  return min;
}

/**
 * 카운팅 정렬 함수
 *
 * @param arr 정렬할 배열
 * @param n 배열의 크기
 * @param result 정렬된 결과를 저장할 배열
 */
void counting_sort(int arr[], int n, int result[]) {
  if (n <= 0)
    return;

  // 1. 최대값과 최소값 찾기
  int min_val = find_min(arr, n);
  int max_val = find_max(arr, n);

  // 값의 범위 계산
  int range = max_val - min_val + 1;
  int offset = -min_val;  // 음수 처리를 위한 오프셋

  // 2. 카운팅 배열 동적 할당 및 초기화
  int *count = (int *)calloc(range, sizeof(int));
  if (count == NULL) {
    printf("메모리 할당 실패!\n");
    exit(1);
  }

  // 3. 각 원소의 개수 세기
  for (int i = 0; i < n; i++) {
    count[arr[i] + offset]++;
  }

  // 4. 카운팅 배열을 누적합으로 변환
  for (int i = 1; i < range; i++) {
    count[i] += count[i - 1];
  }

  // 5. 원본 배열을 뒤에서부터 순회하며 결과 배열에 배치
  for (int i = n - 1; i >= 0; i--) {
    int value = arr[i];
    int position = count[value + offset] - 1;
    result[position] = value;
    count[value + offset]--;
  }

  // 메모리 해제
  free(count);
}

/**
 * 단계별 출력을 포함한 카운팅 정렬
 *
 * @param arr 정렬할 배열
 * @param n 배열의 크기
 * @param result 정렬된 결과를 저장할 배열
 */
void counting_sort_with_steps(int arr[], int n, int result[]) {
  if (n <= 0)
    return;

  printf("입력 배열: ");
  print_array(arr, n);

  // 1. 최대값과 최소값 찾기
  int min_val = find_min(arr, n);
  int max_val = find_max(arr, n);
  int range = max_val - min_val + 1;
  int offset = -min_val;

  printf("값의 범위: %d ~ %d (크기: %d)\n", min_val, max_val, range);

  // 2. 카운팅 배열 동적 할당 및 초기화
  int *count = (int *)calloc(range, sizeof(int));
  if (count == NULL) {
    printf("메모리 할당 실패!\n");
    exit(1);
  }

  // 3. 각 원소의 개수 세기
  for (int i = 0; i < n; i++) {
    count[arr[i] + offset]++;
  }

  printf("카운팅 배열 (개수): ");
  print_array(count, range);

  // 4. 카운팅 배열을 누적합으로 변환
  for (int i = 1; i < range; i++) {
    count[i] += count[i - 1];
  }

  printf("카운팅 배열 (누적): ");
  print_array(count, range);

  printf("\n배치 과정:\n");

  // 5. 원본 배열을 뒤에서부터 순회하며 결과 배열에 배치
  for (int i = n - 1; i >= 0; i--) {
    int value = arr[i];
    int position = count[value + offset] - 1;
    result[position] = value;
    count[value + offset]--;

    printf("  %d을(를) 위치 %d에 배치\n", value, position);
  }

  printf("\n최종 결과: ");
  print_array(result, n);

  // 메모리 해제
  free(count);
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
 * 테스트 함수
 */
void test_counting_sort() {
  printf("=== 기본 카운팅 정렬 테스트 ===\n");
  int arr1[] = {4, 2, 2, 8, 3, 3, 1};
  int n1 = sizeof(arr1) / sizeof(arr1[0]);
  int result1[n1];

  printf("정렬 전: ");
  print_array(arr1, n1);

  counting_sort(arr1, n1, result1);

  printf("정렬 후: ");
  print_array(result1, n1);

  printf("\n=== 단계별 카운팅 정렬 ===\n");
  int arr2[] = {1, 4, 1, 2, 7, 5, 2};
  int n2 = sizeof(arr2) / sizeof(arr2[0]);
  int result2[n2];

  counting_sort_with_steps(arr2, n2, result2);

  printf("\n=== 기본 정렬 테스트 2 ===\n");
  int arr3[] = {3, 1, 4, 1, 5, 9, 2, 6};
  int n3 = sizeof(arr3) / sizeof(arr3[0]);
  int result3[n3];

  printf("정렬 전: ");
  print_array(arr3, n3);

  counting_sort(arr3, n3, result3);

  printf("정렬 후: ");
  print_array(result3, n3);

  printf("\n=== 음수 포함 테스트 ===\n");
  int arr4[] = {-2, 1, -1, 3, 0, 2};
  int n4 = sizeof(arr4) / sizeof(arr4[0]);
  int result4[n4];

  printf("정렬 전: ");
  print_array(arr4, n4);

  counting_sort(arr4, n4, result4);

  printf("정렬 후: ");
  print_array(result4, n4);

  printf("\n=== 중복값 많은 경우 ===\n");
  int arr5[] = {3, 1, 1, 3, 2, 2, 3, 1};
  int n5 = sizeof(arr5) / sizeof(arr5[0]);
  int result5[n5];

  printf("정렬 전: ");
  print_array(arr5, n5);

  counting_sort(arr5, n5, result5);

  printf("정렬 후: ");
  print_array(result5, n5);
}

// 메인 함수
int main() {
  test_counting_sort();
  return 0;
}
