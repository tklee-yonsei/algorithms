# trie.py

class TrieNode:
    """
    Trie 노드 클래스
    
    기본 구조 (정수 값 저장)
    - children: a-z를 위한 딕셔너리
    - has_value: 값이 저장되어 있는지 확인
    - value: 실제 저장할 값 (빈도수, 점수 등)
    """
    
    def __init__(self):
        self.children = {}  # 문자 -> TrieNode 매핑
        self.has_value = False
        self.value = 0


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
        self.root = TrieNode()
    
    def insert(self, word, value):
        """
        Trie에 단어와 값을 삽입
        
        Args:
            word (str): 삽입할 단어 (소문자 a-z만 허용)
            value (int): 저장할 값
            
        Returns:
            bool: 성공하면 True, 실패하면 False
        """
        if not word or not word.isalpha() or not word.islower():
            return False
        
        current = self.root
        
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        
        # 단어의 끝에서 값 저장
        current.has_value = True
        current.value = value
        
        return True
    
    def search(self, word):
        """
        Trie에서 단어 검색
        
        Args:
            word (str): 검색할 단어
            
        Returns:
            int: 값이 있으면 해당 값, 없으면 -1
        """
        if not word:
            return -1
        
        current = self.root
        
        for char in word:
            if char not in current.children:
                return -1  # 경로가 존재하지 않음
            current = current.children[char]
        
        if current.has_value:
            return current.value
        else:
            return -1  # 단어는 존재하지만 값이 저장되지 않음
    
    def starts_with(self, prefix):
        """
        주어진 prefix로 시작하는 단어들이 있는지 확인
        
        Args:
            prefix (str): 검색할 접두사
            
        Returns:
            bool: 존재하면 True, 없으면 False
        """
        if not prefix:
            return True
        
        current = self.root
        
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        
        return True  # 접두사 경로가 존재함
    
    def _has_children(self, node):
        """
        노드가 자식을 가지고 있는지 확인
        
        Args:
            node (TrieNode): 확인할 노드
            
        Returns:
            bool: 자식이 있으면 True, 없으면 False
        """
        return len(node.children) > 0
    
    def _delete_helper(self, node, word, index):
        """
        삭제 헬퍼 함수 (재귀적 구현)
        
        Args:
            node (TrieNode): 현재 노드
            word (str): 삭제할 단어
            index (int): 현재 문자 인덱스
            
        Returns:
            bool: 현재 노드를 삭제해야 하면 True, 아니면 False
        """
        if not node:
            return False
        
        # 단어의 끝에 도달한 경우
        if index == len(word):
            # 값이 저장되어 있지 않다면 삭제할 것이 없음
            if not node.has_value:
                return False
            
            # 값을 제거
            node.has_value = False
            node.value = 0
            
            # 자식이 없다면 이 노드는 삭제 가능
            return not self._has_children(node)
        
        char = word[index]
        if char not in node.children:
            return False
        
        should_delete_child = self._delete_helper(node.children[char], word, index + 1)
        
        if should_delete_child:
            # 자식 노드 삭제
            del node.children[char]
            
            # 현재 노드도 삭제 가능한지 확인
            # (값이 없고 다른 자식도 없다면 삭제 가능)
            return not node.has_value and not self._has_children(node)
        
        return False
    
    def delete(self, word):
        """
        Trie에서 단어 삭제
        
        Args:
            word (str): 삭제할 단어
            
        Returns:
            bool: 성공하면 True, 실패하면 False
        """
        if not word:
            return False
        
        self._delete_helper(self.root, word, 0)
        return True
    
    def _get_all_words_helper(self, node, prefix, results):
        """
        주어진 노드 이하의 모든 단어를 수집하는 헬퍼 함수
        
        Args:
            node (TrieNode): 현재 노드
            prefix (str): 현재까지의 접두사
            results (list): 결과를 저장할 리스트
        """
        if not node:
            return
        
        # 현재 노드에 값이 저장되어 있다면 결과에 추가
        if node.has_value:
            results.append((prefix, node.value))
        
        # 모든 자식 노드에 대해 재귀 호출
        for char, child_node in sorted(node.children.items()):
            new_prefix = prefix + char
            self._get_all_words_helper(child_node, new_prefix, results)
    
    def get_all_words(self):
        """
        Trie의 모든 단어와 값을 반환
        
        Returns:
            list: (단어, 값) 튜플의 리스트
        """
        results = []
        self._get_all_words_helper(self.root, "", results)
        return results
    
    def get_words_with_prefix(self, prefix):
        """
        주어진 접두사로 시작하는 모든 단어와 값을 반환
        
        Args:
            prefix (str): 검색할 접두사
            
        Returns:
            list: (단어, 값) 튜플의 리스트
        """
        if not prefix:
            return self.get_all_words()
        
        results = []
        
        # prefix에 해당하는 노드로 이동
        current = self.root
        
        for char in prefix:
            if char not in current.children:
                return results  # 접두사가 존재하지 않음
            current = current.children[char]
        
        # 해당 노드 이하의 모든 단어 수집
        self._get_all_words_helper(current, prefix, results)
        
        return results
    
    def print_trie(self, node=None, prefix="", depth=0):
        """
        Trie 구조를 시각적으로 출력 (디버깅용)
        
        Args:
            node (TrieNode): 출력할 노드 (None이면 루트부터)
            prefix (str): 현재까지의 접두사
            depth (int): 현재 깊이
        """
        if node is None:
            node = self.root
        
        # 들여쓰기 출력
        indent = "  " * depth
        
        if depth > 0:
            print(f"{indent}{prefix[-1]}:", end="")
        else:
            print(f"{indent}ROOT:", end="")
        
        if node.has_value:
            print(f" [값: {node.value}]")
        else:
            print()
        
        # 모든 자식에 대해 재귀 출력 (정렬된 순서로)
        for char in sorted(node.children.keys()):
            new_prefix = prefix + char
            self.print_trie(node.children[char], new_prefix, depth + 1)
    
    def size(self):
        """
        Trie에 저장된 단어의 개수 반환
        
        Returns:
            int: 저장된 단어의 개수
        """
        return len(self.get_all_words())
    
    def is_empty(self):
        """
        Trie가 비어있는지 확인
        
        Returns:
            bool: 비어있으면 True, 아니면 False
        """
        return self.size() == 0


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
    
    # Trie 구조 출력
    print("=== Trie 구조 출력 ===")
    trie.print_trie()
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
    
    # 추가 테스트 케이스들
    print("=== 특별한 경우들 테스트 ===")
    
    # 새로운 Trie로 특별한 케이스 테스트
    test_trie_special = Trie()
    
    # 완전히 같은 문자들로 구성된 단어
    test_trie_special.insert("aaaa", 100)
    test_trie_special.insert("aaa", 50)
    print(f"'aaaa' 검색: {test_trie_special.search('aaaa')}")
    print(f"'aaa' 검색: {test_trie_special.search('aaa')}")
    print(f"'aa' 검색: {test_trie_special.search('aa')}")
    
    # 한 단어가 다른 단어의 접두사인 경우
    test_trie_special.insert("abc", 10)
    test_trie_special.insert("abcdef", 20)
    prefix_words = test_trie_special.get_words_with_prefix("abc")
    print(f"'abc'로 시작하는 단어들: {prefix_words}")
    print()
    
    # 성능 및 다양한 패턴 테스트
    print("=== 다양한 패턴에서의 Trie 테스트 ===")
    test_strings_data = [
        ("hello", 1), ("world", 2), ("python", 3),
        ("programming", 4), ("algorithm", 5), ("data", 6),
        ("structure", 7), ("tree", 8), ("graph", 9), ("hash", 10)
    ]
    
    pattern_trie = Trie()
    for word, value in test_strings_data:
        pattern_trie.insert(word, value)
    
    print(f"총 저장된 단어 수: {pattern_trie.size()}")
    print(f"Trie가 비어있는가: {pattern_trie.is_empty()}")
    
    # 다양한 접두사로 검색
    test_prefixes = ["pr", "al", "da", "xyz"]
    for prefix in test_prefixes:
        words = pattern_trie.get_words_with_prefix(prefix)
        if words:
            word_strs = [f"{word}({value})" for word, value in words]
            print(f"'{prefix}'로 시작하는 단어들: {', '.join(word_strs)}")
        else:
            print(f"'{prefix}'로 시작하는 단어 없음")
    print()
    
    print("=== 잘못된 입력 테스트 ===")
    error_trie = Trie()
    
    # 잘못된 입력들
    invalid_inputs = ["", "ABC", "abc123", "한글", None]
    
    for invalid_input in invalid_inputs:
        try:
            if invalid_input is None:
                continue
            result = error_trie.insert(invalid_input, 1)
            print(f"'{invalid_input}' 삽입 결과: {result}")
        except Exception as e:
            print(f"'{invalid_input}' 삽입 시 오류: {e}")
    
    print("\n테스트 완료")


# 사용 예시 및 추가 유틸리티 함수들
def demo_autocomplete():
    """자동완성 기능 데모"""
    print("=== 자동완성 기능 데모 ===")
    
    # 단어 사전 구축
    dictionary = Trie()
    words_with_freq = [
        ("cat", 100), ("car", 80), ("card", 60), ("care", 40),
        ("careful", 20), ("carry", 90), ("case", 70), ("cash", 50),
        ("dog", 120), ("door", 85), ("down", 95), ("during", 30)
    ]
    
    for word, freq in words_with_freq:
        dictionary.insert(word, freq)
    
    # 자동완성 시뮬레이션
    user_inputs = ["ca", "car", "do"]
    
    for user_input in user_inputs:
        suggestions = dictionary.get_words_with_prefix(user_input)
        # 빈도수로 정렬
        suggestions.sort(key=lambda x: x[1], reverse=True)
        
        print(f"'{user_input}' 입력 시 추천 단어:")
        for word, freq in suggestions[:5]:  # 상위 5개만
            print(f"  {word} (빈도: {freq})")
        print()


if __name__ == "__main__":
    test_trie()
    print("\n" + "="*50 + "\n")
    demo_autocomplete()