// shellSort.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int getShellGap(int n) {
  /*
   * Shell's original sequence: n/2, n/4, n/8, ...
   */
  return n / 2;
}

int getKnuthGap(int n) {
  /*
   * Knuth's sequence: 1, 4, 13, 40, 121, ...
   */
  int gap = 1;
  while (gap < n / 3) {
    gap = 3 * gap + 1;
  }
  return gap;
}

int getNextGap(int gap, const char* sequence_type) {
  /*
   * 다음 gap 값을 계산
   */
  if (strcmp(sequence_type, "knuth") == 0) {
    return gap / 3;
  } else {
    return gap / 2;  // shell's original (기본값)
  }
}

void insertion_sort_for_gap(int arr[], int n, int start, int gap) {
  /*
   * 특정 gap 그룹에 대해 삽입 정렬을 수행하는 함수
   * arr: 정렬할 배열
   * n: 배열 크기
   * start: 그룹의 시작 인덱스
   * gap: 간격
   */
  int i, j, temp;

  // 현재 gap 그룹의 요소들을 삽입 정렬
  for (i = start + gap; i < n; i += gap) {
    temp = arr[i];

    // gap만큼 떨어진 요소들과 비교하여 삽입
    for (j = i; j >= start + gap && arr[j - gap] > temp; j -= gap) {
      arr[j] = arr[j - gap];
    }
    arr[j] = temp;
  }
}

void shellSort(int arr[], int n, const char* sequence_type) {
  int gap, start;

  // 초기 gap 설정
  if (strcmp(sequence_type, "knuth") == 0) {
    gap = getKnuthGap(n);
  } else {
    gap = getShellGap(n);  // 기본값
  }

  // gap을 점진적으로 줄여나감
  while (gap > 0) {
    // 각 gap 그룹에 대해 삽입 정렬 수행
    for (start = 0; start < gap; start++) {
      insertion_sort_for_gap(arr, n, start, gap);
    }

    // 다음 gap 계산
    gap = getNextGap(gap, sequence_type);
  }
}

void printArray(int arr[], int n) {
  for (int i = 0; i < n; i++) {
    printf("%d ", arr[i]);
  }
  printf("\n");
}

int main() {
  int arr[] = {64, 34, 25, 12, 22, 11, 90};
  int n = sizeof(arr) / sizeof(arr[0]);

  printf("정렬 전 배열: ");
  printArray(arr, n);

  // Shell's original sequence 사용
  printf("\nShell's original sequence 사용:");
  int arr_copy[n];
  memcpy(arr_copy, arr, sizeof(arr));
  shellSort(arr_copy, n, "shell");
  printArray(arr_copy, n);

  // Knuth's sequence 사용
  printf("\nKnuth's sequence 사용:");
  memcpy(arr_copy, arr, sizeof(arr));
  shellSort(arr_copy, n, "knuth");
  printArray(arr_copy, n);

  return 0;
}
