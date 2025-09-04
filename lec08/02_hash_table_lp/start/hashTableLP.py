# hashTableLP.py - Hash Table with Linear Probing (START CODE)

class HashItem:
  """해시 테이블 항목 클래스 - 완성됨"""

  def __init__(self, key=None, value=None):
    self.key = key
    self.value = value
    self.is_occupied = False  # 슬롯이 사용 중인지
    self.is_deleted = False   # lazy deletion을 위한 플래그


class HashTableLP:
  """Linear Probing 방식의 해시 테이블 클래스"""

  def __init__(self, size=7):
    """해시 테이블 초기화 - 완성됨"""
    self.size = size
    self.count = 0  # 사용된 항목 수
    self.table = [HashItem() for _ in range(size)]

  def _hash_function(self, key):
    """TODO: 해시 함수 구현 (간단한 modulo 연산)"""
    # 여기에 해시 함수를 구현하세요
    pass

  def get_load_factor(self):
    """로드 팩터 계산 - 완성됨"""
    return self.count / self.size

  def _resize(self, new_size):
    """해시 테이블 크기 조정 - 완성됨"""
    # 기존 데이터 백업
    old_table = self.table
    old_size = self.size

    # 새 테이블 초기화
    self.size = new_size
    self.count = 0
    self.table = [HashItem() for _ in range(new_size)]

    # 기존 데이터를 새 테이블에 재삽입
    for item in old_table:
      if item.is_occupied and not item.is_deleted:
        self.insert(item.key, item.value)

  def insert(self, key, value):
    """TODO: 키-값 쌍을 해시 테이블에 삽입"""
    # 여기에 삽입 로직을 구현하세요
    # 1. 로드 팩터가 0.7을 초과하면 크기를 2배로 증가
    # 2. 해시 함수로 인덱스 계산
    # 3. 선형 탐사로 빈 슬롯 찾기
    # 4. 기존 키가 있으면 업데이트, 없으면 새로 삽입
    pass

  def search(self, key):
    """TODO: 키에 해당하는 값을 검색"""
    # 여기에 검색 로직을 구현하세요
    # 1. 해시 함수로 인덱스 계산
    # 2. 선형 탐사로 키 찾기
    # 3. 찾으면 값 반환, 못 찾으면 None 반환
    pass

  def delete(self, key):
    """TODO: 키를 해시 테이블에서 삭제"""
    # 여기에 삭제 로직을 구현하세요
    # 1. 해시 함수로 인덱스 계산
    # 2. 선형 탐사로 키 찾기
    # 3. Lazy deletion: 삭제 표시만 함 (is_deleted = True)
    # 4. 성공하면 True, 실패하면 False 반환
    pass

  def print_table(self):
    """해시 테이블 내용을 출력 - 완성됨"""
    print(
        f"해시 테이블 내용 (크기: {self.size}, 사용된 항목: {self.count}, 로드 팩터: {self.get_load_factor():.2f}):")

    for i in range(self.size):
      print(f"슬롯 {i:2d}: ", end="")

      if not self.table[i].is_occupied:
        print("(비어있음)")
      elif self.table[i].is_deleted:
        print("(삭제됨)")
      else:
        print(f"[{self.table[i].key}:{self.table[i].value}]")

  def cleanup(self):
    """테이블 정리 (삭제된 항목들을 실제로 제거) - 완성됨"""
    self._resize(self.size)

  def get_statistics(self):
    """충돌 통계 계산 - 완성됨"""
    probes = 0
    max_probes = 0
    items_checked = 0

    for i in range(self.size):
      if self.table[i].is_occupied and not self.table[i].is_deleted:
        key = self.table[i].key
        expected_index = self._hash_function(key)
        actual_index = i

        if actual_index >= expected_index:
          probe_count = actual_index - expected_index
        else:
          probe_count = (self.size - expected_index) + actual_index

        probes += probe_count
        max_probes = max(max_probes, probe_count)
        items_checked += 1

    return {
        "총 항목 수": items_checked,
        "총 프로브 수": probes,
        "평균 프로브 수": probes / items_checked if items_checked > 0 else 0,
        "최대 프로브 수": max_probes,
        "로드 팩터": self.get_load_factor()
    }

  def print_statistics(self):
    """충돌 통계 출력 - 완성됨"""
    stats = self.get_statistics()
    print("\n=== 충돌 통계 ===")
    for key, value in stats.items():
      if isinstance(value, float):
        print(f"{key}: {value:.2f}")
      else:
        print(f"{key}: {value}")

  def get_all_items(self):
    """모든 키-값 쌍을 리스트로 반환 - 완성됨"""
    items = []
    for item in self.table:
      if item.is_occupied and not item.is_deleted:
        items.append((item.key, item.value))
    return items

  def is_empty(self):
    """해시 테이블이 비어있는지 확인 - 완성됨"""
    return self.count == 0

  def contains_key(self, key):
    """키가 존재하는지 확인 - 완성됨"""
    return self.search(key) is not None


# 테스트 코드 (완성됨)
if __name__ == "__main__":
  # 크기 7인 해시 테이블 생성
  hash_table = HashTableLP(7)

  print("=== 해시 테이블 (Linear Probing) 테스트 ===\n")

  # 데이터 삽입
  print("데이터 삽입: (10,100), (22,220), (31,310), (4,40), (15,150), (28,280), (17,170)")
  items_to_insert = [(10, 100), (22, 220), (31, 310), (4, 40),
                     (15, 150), (28, 280), (17, 170)]

  for key, value in items_to_insert:
    hash_table.insert(key, value)

  hash_table.print_table()
  hash_table.print_statistics()

  # 검색 테스트
  print("\n=== 검색 테스트 ===")
  result = hash_table.search(22)
  if result is not None:
    print(f"키 22 검색 결과: {result}")
  else:
    print("키 22를 찾을 수 없습니다.")

  result = hash_table.search(99)
  if result is not None:
    print(f"키 99 검색 결과: {result}")
  else:
    print("키 99를 찾을 수 없습니다.")

  # 업데이트 테스트
  print("\n=== 업데이트 테스트 ===")
  print("키 22의 값을 999로 업데이트")
  hash_table.insert(22, 999)
  hash_table.print_table()

  # 삭제 테스트
  print("\n=== 삭제 테스트 ===")
  print("키 22 삭제")
  if hash_table.delete(22):
    print("키 22 삭제 성공")
  else:
    print("키 22 삭제 실패")
  hash_table.print_table()

  print("\n키 99 삭제 시도")
  if hash_table.delete(99):
    print("키 99 삭제 성공")
  else:
    print("키 99 삭제 실패 (존재하지 않음)")

  # 더 많은 데이터 삽입 (자동 크기 조정 테스트)
  print("\n=== 자동 크기 조정 테스트 ===")
  print("더 많은 데이터 삽입 (자동 크기 조정 발생)")
  hash_table.insert(35, 350)
  hash_table.insert(42, 420)
  hash_table.insert(56, 560)

  hash_table.print_table()
  hash_table.print_statistics()

  # 테이블 정리 테스트
  print("\n=== 테이블 정리 테스트 ===")
  print("삭제된 항목들을 실제로 제거")
  hash_table.cleanup()
  hash_table.print_table()

  # 추가 기능 테스트
  print("\n=== 추가 기능 테스트 ===")
  print(f"테이블이 비어있는가? {hash_table.is_empty()}")
  print(f"키 35가 존재하는가? {hash_table.contains_key(35)}")
  print(f"키 99가 존재하는가? {hash_table.contains_key(99)}")
  print(f"모든 항목: {hash_table.get_all_items()}")
