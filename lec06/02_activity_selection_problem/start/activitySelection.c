// activitySelection.c
#include <stdio.h>
#include <stdlib.h>

// 활동을 나타내는 구조체
typedef struct {
  int start;
  int end;
} Activity;

// TODO: 끝나는 시간으로 오름차순 정렬을 위한 비교 함수를 작성하세요.
int compare_by_end_time(const void *a, const void *b) {
  // TODO: 끝나는 시간 기준 오름차순 정렬 로직을 구현하세요
  return 0;
}

// TODO: 탐욕 알고리즘을 사용하여 활동 선택 문제를 해결하는 함수를 작성하세요.
int activity_selection(Activity activities[], int n, Activity selected[]) {
  // TODO: 여기에 활동 선택 알고리즘을 구현하세요
  // 1. 활동들을 끝나는 시간 기준으로 오름차순 정렬 (qsort 사용)
  // 2. 첫 번째 활동을 선택
  // 3. 나머지 활동들 중에서 이전에 선택한 활동과 겹치지 않는 활동들을 순서대로
  // 선택
  // 4. 선택된 활동들의 개수를 반환
  return 0;
}

// 활동 배열 출력 함수
void print_activities(Activity activities[], int count) {
  printf("[");
  for (int i = 0; i < count; i++) {
    printf("(%d, %d)", activities[i].start, activities[i].end);
    if (i < count - 1)
      printf(", ");
  }
  printf("]");
}

// 사용 예시
int main() {
  Activity activities[] = {{1, 3}, {2, 5}, {4, 6}, {6, 7}, {5, 8}, {8, 9}};
  int n = 6;
  Activity selected[100];  // 충분한 크기의 결과 배열

  int count = activity_selection(activities, n, selected);

  printf("선택된 활동들: ");
  print_activities(selected, count);
  printf("\n선택된 활동 개수: %d\n", count);

  return 0;
}
