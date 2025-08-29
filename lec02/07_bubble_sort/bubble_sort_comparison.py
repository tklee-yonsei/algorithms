# bubble_sort_comparison.py
# 기본 버블 정렬 vs 최적화된 버블 정렬 비교

def bubble_sort_basic(arr):
  """기본 버블 정렬 - 끝까지 모든 패스 수행"""
  n = len(arr)
  comparisons = 0
  swaps = 0
  passes = 0

  print(f"=== 기본 버블 정렬 시작 ===")
  print(f"초기 배열: {arr}")

  for i in range(n):
    passes += 1
    print(f"\n--- 패스 {passes} ---")

    for j in range(0, n - i - 1):
      comparisons += 1
      print(f"비교: arr[{j}]({arr[j]}) vs arr[{j+1}]({arr[j+1]})", end="")

      if arr[j] > arr[j + 1]:
        # 큰 요소를 뒤로 보내기 (swap)
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        swaps += 1
        print(f" → 교환! {arr}")
      else:
        print(f" → 교환 없음")

    print(f"패스 {passes} 완료: {arr}")

  print(f"\n=== 기본 버블 정렬 완료 ===")
  print(f"총 패스: {passes}, 비교: {comparisons}, 교환: {swaps}")
  return comparisons, swaps, passes


def bubble_sort_optimized(arr):
  """최적화된 버블 정렬 - 조기 종료"""
  n = len(arr)
  comparisons = 0
  swaps = 0
  passes = 0

  print(f"\n=== 최적화된 버블 정렬 시작 ===")
  print(f"초기 배열: {arr}")

  for i in range(n):
    passes += 1
    swapped = False
    print(f"\n--- 패스 {passes} ---")

    for j in range(0, n - i - 1):
      comparisons += 1
      print(f"비교: arr[{j}]({arr[j]}) vs arr[{j+1}]({arr[j+1]})", end="")

      if arr[j] > arr[j + 1]:
        # 큰 요소를 뒤로 보내기 (swap)
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        swaps += 1
        swapped = True
        print(f" → 교환! {arr}")
      else:
        print(f" → 교환 없음")

    print(f"패스 {passes} 완료: {arr}")

    # 한 번의 패스에서 swap이 없었다면 이미 정렬됨
    if not swapped:
      print(f"🎉 조기 종료! 패스 {passes}에서 교환이 없어서 정렬 완료")
      break

  print(f"\n=== 최적화된 버블 정렬 완료 ===")
  print(f"총 패스: {passes}, 비교: {comparisons}, 교환: {swaps}")
  return comparisons, swaps, passes


def compare_algorithms():
  """두 알고리즘 비교"""
  print("버블 정렬 알고리즘 비교")
  print("=" * 60)

  # 테스트 케이스들
  test_cases = [
      ([1, 2, 3, 4, 5], "이미 정렬됨"),
      ([2, 1, 3, 4, 5], "거의 정렬됨 (1개만 틀림)"),
      ([5, 4, 3, 2, 1], "완전 역순"),
      ([3, 1, 4, 2], "무작위")
  ]

  for test_data, description in test_cases:
    print(f"\n{'='*80}")
    print(f"테스트 케이스: {description}")
    print(f"데이터: {test_data}")
    print(f"{'='*80}")

    # 기본 버블 정렬
    basic_arr = test_data.copy()
    basic_comp, basic_swaps, basic_passes = bubble_sort_basic(basic_arr)

    # 최적화된 버블 정렬
    opt_arr = test_data.copy()
    opt_comp, opt_swaps, opt_passes = bubble_sort_optimized(opt_arr)

    # 결과 비교
    print(f"\n📊 성능 비교:")
    print(f"{'항목':<15} {'기본':<10} {'최적화':<10} {'개선율'}")
    print(f"{'-'*45}")
    print(f"{'패스 수':<15} {basic_passes:<10} {opt_passes:<10} {((basic_passes-opt_passes)/basic_passes*100):.1f}%")
    print(f"{'비교 횟수':<15} {basic_comp:<10} {opt_comp:<10} {((basic_comp-opt_comp)/basic_comp*100):.1f}%")
    print(f"{'교환 횟수':<15} {basic_swaps:<10} {opt_swaps:<10} {'동일' if basic_swaps == opt_swaps else f'{((basic_swaps-opt_swaps)/basic_swaps*100):.1f}%'}")

    # 결과 검증
    assert basic_arr == opt_arr == sorted(test_data), "정렬 결과가 다릅니다!"
    print(f"✅ 정렬 결과: {basic_arr}")


if __name__ == "__main__":
  compare_algorithms()
