# trie.py - 시작 코드

class TrieNode:
    """
    Trie 노드 클래스
    
    기본 구조 (정수 값 저장)
    - children: a-z를 위한 딕셔너리
    - has_value: 값이 저장되어 있는지 확인
    - value: 실제 저장할 값 (빈도수, 점수 등)
    """
    
    def __init__(self):
        # TODO: TrieNode 초기화
        # 1. children 딕셔너리 생성
        # 2. has_value를 False로 초기화
        # 3. value를 0으로 초기화
        pass


class Trie:
    """
    Trie (트라이) 데이터 구조 구현
    
    시간 복잡도:
    - 삽입: O(m) where m is the length of the word
    - 검색: O(m) where m is the length of the word  
    - 삭제: O(m) where m is the length of the word
    공간 복잡도: O(ALPHABET_SIZE * N * M) where N is number of words, M is average length
    """
    
    def __init__(self):
        """Trie 초기화"""
        # TODO: 루트 노드 생성
        pass
    
    def insert(self, word, value):
        """
        Trie에 단어와 값을 삽입
        
        Args:
            word (str): 삽입할 단어 (소문자 a-z만 허용)
            value (int): 저장할 값
            
        Returns:
            bool: 성공하면 True, 실패하면 False
        """
        # TODO: 단어와 값 삽입
        # 1. 입력 검증 (단어가 유효한지)
        # 2. 각 문자에 대해 경로 생성하며 이동
        # 3. 마지막 노드에서 값 저장
        return False
    
    def search(self, word):
        """
        Trie에서 단어 검색
        
        Args:
            word (str): 검색할 단어
            
        Returns:
            int: 값이 있으면 해당 값, 없으면 -1
        """
        # TODO: 단어 검색
        # 1. 입력 검증
        # 2. 각 문자에 대해 경로 따라가기
        # 3. 마지막 노드에서 값 확인
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
        # 2. prefix의 각 문자에 대해 경로 확인
        return False
    
    def delete(self, word):
        """
        Trie에서 단어 삭제
        
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
        Trie의 모든 단어와 값을 반환
        
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
        # 1. prefix에 해당하는 노드로 이동
        # 2. 해당 노드 이하의 모든 단어 수집
        return []
    
    def print_trie(self, node=None, prefix="", depth=0):
        """
        Trie 구조를 시각적으로 출력 (디버깅용) - 선택사항
        
        Args:
            node (TrieNode): 출력할 노드 (None이면 루트부터)
            prefix (str): 현재까지의 접두사
            depth (int): 현재 깊이
        """
        # TODO: Trie 구조 출력 (선택사항)
        pass
    
    def size(self):
        """
        Trie에 저장된 단어의 개수 반환
        
        Returns:
            int: 저장된 단어의 개수
        """
        # TODO: 저장된 단어 개수 반환
        return 0
    
    def is_empty(self):
        """
        Trie가 비어있는지 확인
        
        Returns:
            bool: 비어있으면 True, 아니면 False
        """
        # TODO: 비어있는지 확인
        return True


def test_trie():
    """테스트 함수"""
    print("=== Trie 데이터 구조 테스트 ===\n")
    
    # Trie 생성
    trie = Trie()
    
    # 테스트 데이터 삽입
    print("=== 단어 삽입 테스트 ===")
    test_words = [
        ("apple", 10), ("app", 5), ("application", 20),
        ("apply", 8), ("banana", 15), ("band", 12), ("bandana", 18)
    ]
    
    for word, value in test_words:
        success = trie.insert(word, value)
        print(f"삽입: {word} (값: {value}) - {'성공' if success else '실패'}")
    print()
    
    # 검색 테스트
    print("=== 검색 테스트 ===")
    search_words = ["apple", "app", "application", "appl", "banana", "cat"]
    
    for word in search_words:
        result = trie.search(word)
        if result != -1:
            print(f"검색: {word} -> 찾음, 값: {result}")
        else:
            print(f"검색: {word} -> 없음")
    print()
    
    # 접두사 검색 테스트
    print("=== 접두사 검색 테스트 ===")
    prefixes = ["app", "ban", "cat", "a"]
    
    for prefix in prefixes:
        exists = trie.starts_with(prefix)
        print(f"접두사: {prefix} -> {'존재함' if exists else '존재하지 않음'}")
        
        if exists:
            words = trie.get_words_with_prefix(prefix)
            word_strs = [f"{word}({value})" for word, value in words]
            print(f"  관련 단어들: {', '.join(word_strs)}")
    print()
    
    # 삭제 테스트
    print("=== 삭제 테스트 ===")
    delete_words = ["app", "banana"]
    
    for word in delete_words:
        print(f"삭제 전 검색: {word} -> {trie.search(word)}")
        trie.delete(word)
        print(f"삭제 후 검색: {word} -> {trie.search(word)}")
        print()
    
    # 전체 단어 출력
    print("=== 남은 모든 단어 출력 ===")
    all_words = trie.get_all_words()
    
    for word, value in all_words:
        print(f"{word}: {value}")
    print()
    
    print(f"총 저장된 단어 수: {trie.size()}")
    print(f"Trie가 비어있는가: {trie.is_empty()}")
    
    print("\n테스트 완료")


if __name__ == "__main__":
    test_trie()