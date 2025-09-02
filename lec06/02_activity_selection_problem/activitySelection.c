// activitySelection.c
#include <stdio.h>
#include <stdlib.h>

// 활동을 나타내는 구조체
typedef struct {
  int start;
  int end;
} Activity;

// 끝나는 시간으로 오름차순 정렬을 위한 비교 함수
int compare_by_end_time(const void *a, const void *b) {
  Activity *actA = (Activity *)a;
  Activity *actB = (Activity *)b;
  return actA->end - actB->end;
}

// 탐욕 알고리즘을 사용하여 활동 선택 문제를 해결하는 함수
int activity_selection(Activity activities[], int n, Activity selected[]) {
  // 끝나는 시간으로 정렬
  qsort(activities, n, sizeof(Activity), compare_by_end_time);

  // 첫 번째 활동 선택
  selected[0] = activities[0];
  int selected_count = 1;
  int last_end_time = activities[0].end;

  for (int i = 1; i < n; i++) {
    if (activities[i].start >= last_end_time) {  // 겹치지 않으면
      selected[selected_count] = activities[i];
      selected_count++;
      last_end_time = activities[i].end;
    }
  }

  return selected_count;
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

  // 추가 테스트 케이스
  printf("\n--- 추가 테스트 케이스 ---\n");

  // 테스트 케이스 1
  Activity test1[] = {{1, 4},  {3, 5},  {0, 6},  {5, 7},  {3, 9},  {5, 9},
                      {6, 10}, {8, 11}, {8, 12}, {2, 14}, {12, 16}};
  Activity selected1[100];
  int count1 = activity_selection(test1, 11, selected1);
  printf("테스트 1 선택된 활동: ");
  print_activities(selected1, count1);
  printf(", 개수: %d\n", count1);

  // 테스트 케이스 2
  Activity test2[] = {{0, 1}, {1, 2}, {2, 3}, {3, 4}, {4, 5}};
  Activity selected2[100];
  int count2 = activity_selection(test2, 5, selected2);
  printf("테스트 2 선택된 활동: ");
  print_activities(selected2, count2);
  printf(", 개수: %d\n", count2);

  // 테스트 케이스 3
  Activity test3[] = {{0, 5}, {1, 2}, {3, 4}};
  Activity selected3[100];
  int count3 = activity_selection(test3, 3, selected3);
  printf("테스트 3 선택된 활동: ");
  print_activities(selected3, count3);
  printf(", 개수: %d\n", count3);

  return 0;
}
