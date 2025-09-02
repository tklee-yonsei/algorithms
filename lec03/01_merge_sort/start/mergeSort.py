# mergeSort.py
# TODO: 두 개의 정렬된 부분 배열을 합치는 함수를 구현하세요
def merge(arr, left, mid, right):
  """두 개의 정렬된 부분 배열을 합치는 함수"""
  # 여기에 코드를 작성하세요
  # 힌트:
  # 1. 임시 배열들 생성 (슬라이싱 사용)
  # 2. 인덱스 초기화
  # 3. 두 배열을 비교하며 작은 값부터 원본 배열에 복사
  # 4. 남은 요소들 모두 복사
  pass


# TODO: 병합 정렬 함수를 구현하세요
def merge_sort(arr, left=None, right=None):
  """병합 정렬 함수"""
  # 여기에 코드를 작성하세요
  # 힌트:
  # 1. left, right가 None인 경우 기본값 설정
  # 2. 베이스 케이스: left < right인지 확인
  # 3. 중간점 계산
  # 4. 왼쪽 부분 재귀 정렬
  # 5. 오른쪽 부분 재귀 정렬
  # 6. 정렬된 두 부분을 합치기
  pass


# 사용 예시
if __name__ == "__main__":
  arr = [64, 34, 25, 12, 22, 11, 90]

  print("정렬 전 배열:", arr)

  merge_sort(arr)

  print("정렬 후 배열:", arr)
