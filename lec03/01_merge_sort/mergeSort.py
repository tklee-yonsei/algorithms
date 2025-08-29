# mergeSort.py
def merge(arr, left, mid, right):
  """두 개의 정렬된 부분 배열을 합치는 함수"""
  # 임시 배열 생성
  left_arr = arr[left:mid+1]
  right_arr = arr[mid+1:right+1]

  # 인덱스 초기화
  i = j = 0  # 임시 배열들의 인덱스
  k = left   # 원본 배열의 인덱스

  # 두 배열을 비교하며 작은 값부터 원본 배열에 복사
  while i < len(left_arr) and j < len(right_arr):
    if left_arr[i] <= right_arr[j]:
      arr[k] = left_arr[i]
      i += 1
    else:
      arr[k] = right_arr[j]
      j += 1
    k += 1

  # 남은 요소들 복사
  while i < len(left_arr):
    arr[k] = left_arr[i]
    i += 1
    k += 1

  while j < len(right_arr):
    arr[k] = right_arr[j]
    j += 1
    k += 1


def merge_sort(arr, left=None, right=None):
  """병합 정렬 함수"""
  if left is None:
    left = 0
  if right is None:
    right = len(arr) - 1

  if left < right:
    # 중간점 계산
    mid = (left + right) // 2

    # 왼쪽 부분 정렬
    merge_sort(arr, left, mid)

    # 오른쪽 부분 정렬
    merge_sort(arr, mid + 1, right)

    # 정렬된 두 부분을 합치기
    merge(arr, left, mid, right)


# 사용 예시
if __name__ == "__main__":
  arr = [64, 34, 25, 12, 22, 11, 90]

  print("정렬 전 배열:", arr)

  merge_sort(arr)

  print("정렬 후 배열:", arr)
