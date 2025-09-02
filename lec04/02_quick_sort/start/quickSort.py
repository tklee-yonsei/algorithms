# quickSort.py
# TODO: 배열을 분할하는 함수를 구현하세요 (Hoare partition scheme)
def partition(arr, low, high):
  """배열을 분할하는 함수 (Hoare partition scheme)"""
  # 여기에 코드를 작성하세요
  # 힌트:
  # 1. 첫 번째 요소를 피벗으로 선택
  # 2. i를 low-1, j를 high+1로 초기화
  # 3. 무한 루프에서:
  #    - 왼쪽에서 피벗보다 큰 요소 찾기
  #    - 오른쪽에서 피벗보다 작은 요소 찾기
  #    - i >= j이면 j 반환
  #    - 그렇지 않으면 arr[i]와 arr[j] 교환
  return -1


# TODO: 퀵 정렬 함수를 구현하세요
def quick_sort(arr, low=None, high=None):
  """퀵 정렬 함수 (Hoare partition)"""
  # 여기에 코드를 작성하세요
  # 힌트:
  # 1. low, high가 None인 경우 기본값 설정
  # 2. 베이스 케이스: low < high인지 확인
  # 3. partition 함수로 배열 분할
  # 4. 왼쪽 부분 재귀 정렬
  # 5. 오른쪽 부분 재귀 정렬
  pass


# 사용 예시
if __name__ == "__main__":
  arr = [64, 34, 25, 12, 22, 11, 90]

  print("정렬 전 배열:", arr)

  quick_sort(arr)

  print("정렬 후 배열:", arr)
