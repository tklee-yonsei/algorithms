# hashTableSC.py - Hash Table with Separate Chaining

class HashNode:
  """해시 테이블 노드 클래스 (연결 리스트의 노드)"""

  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.next = None


class HashTableSC:
  """Separate Chaining 방식의 해시 테이블 클래스"""

  def __init__(self, size=7):
    """해시 테이블 초기화"""
    self.size = size
    self.table = [None] * size

  def _hash_function(self, key):
    """해시 함수 (간단한 modulo 연산)"""
    return key % self.size

  def insert(self, key, value):
    """키-값 쌍을 해시 테이블에 삽입"""
    index = self._hash_function(key)
    current = self.table[index]

    # 기존 키가 있는지 확인 (업데이트)
    while current is not None:
      if current.key == key:
        current.value = value
        return
      current = current.next

    # 새 노드를 리스트 앞에 삽입
    new_node = HashNode(key, value)
    new_node.next = self.table[index]
    self.table[index] = new_node

  def search(self, key):
    """키에 해당하는 값을 검색"""
    index = self._hash_function(key)
    current = self.table[index]

    while current is not None:
      if current.key == key:
        return current.value
      current = current.next

    return None  # 키를 찾지 못함

  def delete(self, key):
    """키를 해시 테이블에서 삭제"""
    index = self._hash_function(key)
    current = self.table[index]
    prev = None

    while current is not None:
      if current.key == key:
        if prev is None:
          # 첫 번째 노드 삭제
          self.table[index] = current.next
        else:
          # 중간 또는 마지막 노드 삭제
          prev.next = current.next
        return True  # 삭제 성공

      prev = current
      current = current.next

    return False  # 키를 찾지 못함

  def print_table(self):
    """해시 테이블 내용을 출력"""
    print("해시 테이블 내용:")

    for i in range(self.size):
      print(f"버킷 {i}: ", end="")
      current = self.table[i]

      if current is None:
        print("(비어있음)")
      else:
        chain = []
        while current is not None:
          chain.append(f"[{current.key}:{current.value}]")
          current = current.next
        print(" -> ".join(chain))

  def get_all_items(self):
    """모든 키-값 쌍을 리스트로 반환"""
    items = []
    for i in range(self.size):
      current = self.table[i]
      while current is not None:
        items.append((current.key, current.value))
        current = current.next
    return items

  def resize(self, new_size):
    """해시 테이블 크기 조정"""
    # 기존 모든 아이템을 저장
    old_items = self.get_all_items()

    # 새로운 크기로 테이블 초기화
    self.size = new_size
    self.table = [None] * new_size

    # 모든 아이템을 새 테이블에 재삽입
    for key, value in old_items:
      self.insert(key, value)

  def get_load_factor(self):
    """로드 팩터 계산"""
    item_count = len(self.get_all_items())
    return item_count / self.size

  def get_statistics(self):
    """해시 테이블 통계 정보 반환"""
    non_empty_buckets = 0
    max_chain_length = 0
    total_chain_length = 0

    for i in range(self.size):
      chain_length = 0
      current = self.table[i]

      if current is not None:
        non_empty_buckets += 1
        while current is not None:
          chain_length += 1
          current = current.next

      max_chain_length = max(max_chain_length, chain_length)
      total_chain_length += chain_length

    return {
        "총 버킷 수": self.size,
        "사용된 버킷 수": non_empty_buckets,
        "총 아이템 수": total_chain_length,
        "로드 팩터": self.get_load_factor(),
        "최대 체인 길이": max_chain_length,
        "평균 체인 길이": total_chain_length / self.size if self.size > 0 else 0
    }


# 사용 예시
if __name__ == "__main__":
  # 크기 7인 해시 테이블 생성
  hash_table = HashTableSC(7)

  print("=== 해시 테이블 (Separate Chaining) 테스트 ===\n")

  # 데이터 삽입
  print("데이터 삽입: (10,100), (22,220), (31,310), (4,40), (15,150), (28,280), (17,170)")
  items_to_insert = [(10, 100), (22, 220), (31, 310), (4, 40),
                     (15, 150), (28, 280), (17, 170)]

  for key, value in items_to_insert:
    hash_table.insert(key, value)

  hash_table.print_table()

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

  # 통계 정보
  print("\n=== 해시 테이블 통계 ===")
  stats = hash_table.get_statistics()
  for key, value in stats.items():
    if isinstance(value, float):
      print(f"{key}: {value:.2f}")
    else:
      print(f"{key}: {value}")

  # 크기 조정 테스트
  print("\n=== 크기 조정 테스트 ===")
  print("해시 테이블 크기를 7에서 13으로 조정")
  hash_table.resize(13)
  print("조정된 해시 테이블:")
  hash_table.print_table()

  print("\n조정 후 통계:")
  stats = hash_table.get_statistics()
  for key, value in stats.items():
    if isinstance(value, float):
      print(f"{key}: {value:.2f}")
    else:
      print(f"{key}: {value}")
