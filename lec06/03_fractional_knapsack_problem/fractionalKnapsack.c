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

// 단위 무게당 가치로 내림차순 정렬을 위한 비교 함수
int compare_by_value_per_weight(const void *a, const void *b) {
  Item *itemA = (Item *)a;
  Item *itemB = (Item *)b;

  if (itemB->value_per_weight > itemA->value_per_weight)
    return 1;
  if (itemB->value_per_weight < itemA->value_per_weight)
    return -1;
  return 0;
}

// 탐욕 알고리즘을 사용하여 분할 배낭 문제를 해결하는 함수
double fractional_knapsack(int capacity, Item items[], int n,
                           SelectedItem selected[]) {
  // 단위 무게당 가치 계산
  for (int i = 0; i < n; i++) {
    items[i].value_per_weight = (double)items[i].value / items[i].weight;
  }

  // 단위 무게당 가치로 내림차순 정렬
  qsort(items, n, sizeof(Item), compare_by_value_per_weight);

  double total_value = 0;
  int selected_count = 0;

  for (int i = 0; i < n; i++) {
    if (capacity >= items[i].weight) {
      // 물건 전체를 가져갈 수 있는 경우
      selected[selected_count].weight = items[i].weight;
      selected[selected_count].value = items[i].value;
      selected[selected_count].fraction = 1.0;

      total_value += items[i].value;
      capacity -= items[i].weight;
      selected_count++;
    } else {
      // 물건의 일부만 가져갈 수 있는 경우
      double fraction = (double)capacity / items[i].weight;

      selected[selected_count].weight = items[i].weight;
      selected[selected_count].value = items[i].value;
      selected[selected_count].fraction = fraction;

      total_value += items[i].value * fraction;
      selected_count++;
      break;
    }
  }

  // 실제 선택된 물건 개수를 마지막 요소에 저장 (편의상)
  // 실제로는 별도의 매개변수나 전역변수로 관리하는 것이 좋음
  selected[n].weight = selected_count;  // 편의상 개수 저장

  return total_value;
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
  int selected_count = selected[n].weight;  // 편의상 저장된 개수

  printf("최대 가치: %.2f\n", max_value);
  print_selected_items(selected, selected_count);

  // 추가 테스트 케이스
  printf("\n--- 추가 테스트 케이스 ---\n");

  // 테스트 케이스 1
  printf("\n테스트 1: 용량 50\n");
  Item test1[] = {{10, 60}, {20, 100}, {30, 120}};
  SelectedItem selected1[100];
  double max_value1 = fractional_knapsack(50, test1, 3, selected1);
  int count1 = selected1[3].weight;
  printf("최대 가치: %.2f\n", max_value1);
  print_selected_items(selected1, count1);

  // 테스트 케이스 2
  printf("\n테스트 2: 용량 25\n");
  Item test2[] = {{15, 20}, {10, 30}, {5, 40}};
  SelectedItem selected2[100];
  double max_value2 = fractional_knapsack(25, test2, 3, selected2);
  int count2 = selected2[3].weight;
  printf("최대 가치: %.2f\n", max_value2);
  print_selected_items(selected2, count2);

  // 테스트 케이스 3
  printf("\n테스트 3: 용량 7\n");
  Item test3[] = {{2, 1}, {3, 4}, {5, 7}, {1, 1}};
  SelectedItem selected3[100];
  double max_value3 = fractional_knapsack(7, test3, 4, selected3);
  int count3 = selected3[4].weight;
  printf("최대 가치: %.2f\n", max_value3);
  print_selected_items(selected3, count3);

  return 0;
}
