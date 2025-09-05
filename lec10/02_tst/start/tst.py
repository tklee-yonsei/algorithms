# tst.py - 시작 코드

class TSTNode:
    """
    TST (Ternary Search Tree) 노드 클래스
    
    TST 노드 구조:
    - data: 현재 노드의 문자
    - has_value: 값 존재 여부
    - value: 저장할 값
    - left: 현재 문자보다 작은 문자
    - middle: 다음 문자로 이동
    - right: 현재 문자보다 큰 문자
    """
    
    def __init__(self, data):
        # TODO: TSTNode 초기화
        # 1. data 설정
        # 2. has_value를 False로 초기화
        # 3. value를 0으로 초기화
        # 4. left, middle, right를 None으로 초기화
        pass


class TST:
    """
    TST (Ternary Search Tree) 데이터 구조 구현
    
    시간 복잡도:
    - 평균 삽입: O(log n)
    - 평균 검색: O(log n)
    - 평균 삭제: O(log n)
    - 최악의 경우: O(n) (불균형 트리)
    공간 복잡도: O(n) where n is the number of nodes
    """
    
    def __init__(self):
        """TST 초기화"""
        # TODO: 루트 노드를 None으로 초기화
        pass
    
    def insert(self, word, value):
        """
        TST에 단어와 값을 삽입
        
        Args:
            word (str): 삽입할 단어
            value (int): 저장할 값
            
        Returns:
            bool: 성공하면 True, 실패하면 False
        """
        # TODO: 단어와 값 삽입
        # 1. 입력 검증
        # 2. 헬퍼 함수 호출 (_insert)
        # 헬퍼 함수는 재귀적으로 구현
        return False
    
    def search(self, word):
        """
        TST에서 단어 검색
        
        Args:
            word (str): 검색할 단어
            
        Returns:
            int: 값이 있으면 해당 값, 없으면 -1
        """
        # TODO: 단어 검색
        # 1. 입력 검증
        # 2. 헬퍼 함수 호출 (_search)
        # 헬퍼 함수는 재귀적으로 구현
        return -1
    
    def starts_with(self, prefix):
        """
        주어진 prefix로 시작하는 단어들이 있는지 확인
        
        Args:
            prefix (str): 검색할 접두사
            
        Returns:
            bool: 존재하면 True, 없으면 False
        """
        # TODO: 접두사 검색
        # 1. 입력 검증
        # 2. 헬퍼 함수 호출 (_starts_with)
        return False
    
    def delete(self, word):
        """
        TST에서 단어 삭제
        
        Args:
            word (str): 삭제할 단어
            
        Returns:
            bool: 성공하면 True, 실패하면 False
        """
        # TODO: 단어 삭제
        # 헬퍼 함수 사용 권장 (재귀적 구현)
        return False
    
    def get_all_words(self):
        """
        TST의 모든 단어와 값을 반환
        
        Returns:
            list: (단어, 값) 튜플의 리스트
        """
        # TODO: 모든 단어 수집
        # 헬퍼 함수 사용 권장
        return []
    
    def get_words_with_prefix(self, prefix):
        """
        주어진 접두사로 시작하는 모든 단어와 값을 반환
        
        Args:
            prefix (str): 검색할 접두사
            
        Returns:
            list: (단어, 값) 튜플의 리스트
        """
        # TODO: 접두사로 시작하는 모든 단어 수집
        # 1. prefix에 해당하는 노드 찾기
        # 2. 해당 노드 이하의 모든 단어 수집
        return []
    
    def get_sorted_words(self):
        """
        사전순으로 정렬된 모든 단어를 반환
        
        Returns:
            list: (단어, 값) 튜플의 리스트 (사전순)
        """
        # TODO: 사전순 정렬된 단어 반환
        # 중위 순회 사용
        return []
    
    def print_tst(self):
        """TST 구조를 시각적으로 출력 (선택사항)"""
        # TODO: TST 구조 출력 (선택사항)
        pass
    
    def size(self):
        """
        TST에 저장된 단어의 개수 반환
        
        Returns:
            int: 저장된 단어의 개수
        """
        # TODO: 저장된 단어 개수 반환
        return 0
    
    def is_empty(self):
        """
        TST가 비어있는지 확인
        
        Returns:
            bool: 비어있으면 True, 아니면 False
        """
        # TODO: 비어있는지 확인
        return True


def test_tst():
    """테스트 함수"""
    print("=== TST (Ternary Search Tree) 테스트 ===\n")
    
    # TST 생성
    tst = TST()
    
    # 테스트 데이터 삽입
    print("=== 단어 삽입 테스트 ===")
    test_words = [
        ("apple", 10), ("app", 5), ("application", 20),
        ("apply", 8), ("banana", 15), ("band", 12), ("bandana", 18),
        ("cat", 25), ("car", 30), ("card", 35)
    ]
    
    for word, value in test_words:
        success = tst.insert(word, value)
        print(f"삽입: {word} (값: {value}) - {'성공' if success else '실패'}")
    print()
    
    # 검색 테스트
    print("=== 검색 테스트 ===")
    search_words = ["apple", "app", "application", "appl", "banana", "dog", "car"]
    
    for word in search_words:
        result = tst.search(word)
        if result != -1:
            print(f"검색: {word} -> 찾음, 값: {result}")
        else:
            print(f"검색: {word} -> 없음")
    print()
    
    # 접두사 검색 테스트
    print("=== 접두사 검색 테스트 ===")
    prefixes = ["app", "ban", "ca", "xyz"]
    
    for prefix in prefixes:
        exists = tst.starts_with(prefix)
        print(f"접두사: {prefix} -> {'존재함' if exists else '존재하지 않음'}")
        
        if exists:
            words = tst.get_words_with_prefix(prefix)
            word_strs = [f"{word}({value})" for word, value in words]
            print(f"  관련 단어들: {', '.join(word_strs)}")
    print()
    
    # 사전순 정렬된 단어 출력
    print("=== 사전순 정렬된 모든 단어 ===")
    sorted_words = tst.get_sorted_words()
    
    for word, value in sorted_words:
        print(f"{word}: {value}")
    print()
    
    # 삭제 테스트
    print("=== 삭제 테스트 ===")
    delete_words = ["app", "banana", "card"]
    
    for word in delete_words:
        print(f"삭제 전 검색: {word} -> {tst.search(word)}")
        tst.delete(word)
        print(f"삭제 후 검색: {word} -> {tst.search(word)}")
        print()
    
    # 삭제 후 남은 단어 출력
    print("=== 삭제 후 남은 모든 단어 ===")
    remaining_words = tst.get_all_words()
    
    for word, value in remaining_words:
        print(f"{word}: {value}")
    print()
    
    print(f"총 저장된 단어 수: {tst.size()}")
    print(f"TST가 비어있는가: {tst.is_empty()}")
    
    print("\n테스트 완료")


if __name__ == "__main__":
    test_tst()