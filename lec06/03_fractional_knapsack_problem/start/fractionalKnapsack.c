// fractionalKnapsack.c
#include <stdio.h>
#include <stdlib.h>

// 물건을 나타내는 구조체
typedef struct {
  int weight;
  int value;
  double value_per_weight;  // 단위 무게당 가치
} Item;

// 선택된 물건을 나타내는 구조체
typedef struct {
  int weight;
  int value;
  double fraction;  // 선택 비율
} SelectedItem;

// TODO: 단위 무게당 가치로 내림차순 정렬을 위한 비교 함수를 작성하세요.
int compare_by_value_per_weight(const void *a, const void *b) {
  // TODO: 단위 무게당 가치 기준 내림차순 정렬 로직을 구현하세요
  return 0;
}

// TODO: 탐욕 알고리즘을 사용하여 분할 배낭 문제를 해결하는 함수를 작성하세요.
double fractional_knapsack(int capacity, Item items[], int n,
                           SelectedItem selected[]) {
  // TODO: 여기에 분할 배낭 알고리즘을 구현하세요
  // 1. 각 물건의 단위 무게당 가치를 계산
  // 2. 물건들을 단위 무게당 가치 기준으로 내림차순 정렬 (qsort 사용)
  // 3. 가치 밀도가 높은 물건부터 우선적으로 선택
  // 4. 배낭 용량이 부족하면 물건의 일부만 선택 (분할 가능)
  // 5. 총 가치를 반환
  return 0.0;
}

// 선택된 물건들 출력 함수
void print_selected_items(SelectedItem selected[], int count) {
  for (int i = 0; i < count; i++) {
    printf("무게 %d, 가치 %d, 선택 비율: %.2f\n", selected[i].weight,
           selected[i].value, selected[i].fraction);
  }
}

// 사용 예시
int main() {
  int capacity = 15;
  Item items[] = {{10, 60}, {20, 100}, {30, 120}};  // {무게, 가치}
  int n = 3;
  SelectedItem selected[100];  // 충분한 크기의 결과 배열

  double max_value = fractional_knapsack(capacity, items, n, selected);
  // TODO: 선택된 물건 개수를 올바르게 관리하세요
  int selected_count = 0;  // 실제 구현에서는 함수에서 반환하거나 별도로 관리

  printf("최대 가치: %.2f\n", max_value);
  print_selected_items(selected, selected_count);

  return 0;
}
