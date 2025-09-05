# tst.py

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
        self.data = data
        self.has_value = False
        self.value = 0
        self.left = None
        self.middle = None
        self.right = None


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
        self.root = None
    
    def _insert(self, node, word, value, index):
        """
        TST에 단어와 값을 삽입 (재귀적 구현)
        
        Args:
            node (TSTNode): 현재 노드
            word (str): 삽입할 단어
            value (int): 저장할 값
            index (int): 현재 문자 인덱스
            
        Returns:
            TSTNode: 루트 노드
        """
        if index >= len(word):
            return node
        
        current_char = word[index]
        
        # 노드가 None이면 새 노드 생성
        if node is None:
            node = TSTNode(current_char)
        
        # 현재 문자와 노드의 문자 비교
        if current_char < node.data:
            node.left = self._insert(node.left, word, value, index)
        elif current_char > node.data:
            node.right = self._insert(node.right, word, value, index)
        else:  # current_char == node.data
            if index == len(word) - 1:
                # 단어의 마지막 문자에 도달
                node.has_value = True
                node.value = value
            else:
                # 다음 문자로 이동
                node.middle = self._insert(node.middle, word, value, index + 1)
        
        return node
    
    def insert(self, word, value):
        """
        TST에 단어와 값을 삽입
        
        Args:
            word (str): 삽입할 단어
            value (int): 저장할 값
            
        Returns:
            bool: 성공하면 True, 실패하면 False
        """
        if not word:
            return False
        
        self.root = self._insert(self.root, word, value, 0)
        return True
    
    def _search(self, node, word, index):
        """
        TST에서 단어 검색 (재귀적 구현)
        
        Args:
            node (TSTNode): 현재 노드
            word (str): 검색할 단어
            index (int): 현재 문자 인덱스
            
        Returns:
            int: 값이 있으면 해당 값, 없으면 -1
        """
        if node is None or index >= len(word):
            return -1
        
        current_char = word[index]
        
        if current_char < node.data:
            return self._search(node.left, word, index)
        elif current_char > node.data:
            return self._search(node.right, word, index)
        else:  # current_char == node.data
            if index == len(word) - 1:
                # 단어의 마지막 문자에 도달
                return node.value if node.has_value else -1
            else:
                # 다음 문자로 이동
                return self._search(node.middle, word, index + 1)
    
    def search(self, word):
        """
        TST에서 단어 검색
        
        Args:
            word (str): 검색할 단어
            
        Returns:
            int: 값이 있으면 해당 값, 없으면 -1
        """
        if not word:
            return -1
        
        return self._search(self.root, word, 0)
    
    def _starts_with(self, node, prefix, index):
        """
        주어진 prefix로 시작하는 단어들이 있는지 확인 (재귀적 구현)
        
        Args:
            node (TSTNode): 현재 노드
            prefix (str): 검색할 접두사
            index (int): 현재 문자 인덱스
            
        Returns:
            bool: 존재하면 True, 없으면 False
        """
        if node is None:
            return False
        
        if index >= len(prefix):
            return True  # 모든 prefix 문자를 찾음
        
        current_char = prefix[index]
        
        if current_char < node.data:
            return self._starts_with(node.left, prefix, index)
        elif current_char > node.data:
            return self._starts_with(node.right, prefix, index)
        else:  # current_char == node.data
            if index == len(prefix) - 1:
                # prefix의 마지막 문자에 도달
                return True
            else:
                # 다음 문자로 이동
                return self._starts_with(node.middle, prefix, index + 1)
    
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
        
        return self._starts_with(self.root, prefix, 0)
    
    def _get_all_words_helper(self, node, prefix, results):
        """
        주어진 노드 이하의 모든 단어를 수집하는 헬퍼 함수
        
        Args:
            node (TSTNode): 현재 노드
            prefix (str): 현재까지의 접두사
            results (list): 결과를 저장할 리스트
        """
        if node is None:
            return
        
        # 왼쪽 서브트리 탐색 (현재 문자보다 작은 문자들)
        self._get_all_words_helper(node.left, prefix, results)
        
        # 현재 노드 처리
        current_word = prefix + node.data
        
        # 현재 노드에 값이 저장되어 있다면 결과에 추가
        if node.has_value:
            results.append((current_word, node.value))
        
        # 가운데 서브트리 탐색 (다음 문자들)
        self._get_all_words_helper(node.middle, current_word, results)
        
        # 오른쪽 서브트리 탐색 (현재 문자보다 큰 문자들)
        self._get_all_words_helper(node.right, prefix, results)
    
    def get_all_words(self):
        """
        TST의 모든 단어와 값을 반환
        
        Returns:
            list: (단어, 값) 튜플의 리스트
        """
        results = []
        
        if self.root is not None:
            self._get_all_words_helper(self.root, "", results)
        
        return results
    
    def _get_node_by_prefix(self, node, prefix, index):
        """
        prefix에 해당하는 노드를 찾아 반환 (재귀적 구현)
        
        Args:
            node (TSTNode): 현재 노드
            prefix (str): 찾을 접두사
            index (int): 현재 문자 인덱스
            
        Returns:
            TSTNode: 해당 노드 또는 None
        """
        if node is None:
            return None
        
        if index >= len(prefix):
            return node
        
        current_char = prefix[index]
        
        if current_char < node.data:
            return self._get_node_by_prefix(node.left, prefix, index)
        elif current_char > node.data:
            return self._get_node_by_prefix(node.right, prefix, index)
        else:  # current_char == node.data
            if index == len(prefix) - 1:
                # prefix의 마지막 문자에 도달
                return node
            else:
                # 다음 문자로 이동
                return self._get_node_by_prefix(node.middle, prefix, index + 1)
    
    def get_words_with_prefix(self, prefix):
        """
        주어진 접두사로 시작하는 모든 단어와 값을 반환
        
        Args:
            prefix (str): 검색할 접두사
            
        Returns:
            list: (단어, 값) 튜플의 리스트
        """
        results = []
        
        if not prefix:
            return self.get_all_words()
        
        # prefix에 해당하는 노드를 찾음
        prefix_node = self._get_node_by_prefix(self.root, prefix, 0)
        
        if prefix_node is None:
            return results  # 접두사가 존재하지 않음
        
        # 해당 노드에 값이 있다면 추가 (prefix 자체가 완전한 단어인 경우)
        if prefix_node.has_value:
            results.append((prefix, prefix_node.value))
        
        # 해당 노드의 middle 서브트리에서 모든 단어 수집
        self._get_all_words_helper(prefix_node.middle, prefix, results)
        
        return results
    
    def _has_children(self, node):
        """
        노드가 자식을 가지고 있는지 확인
        
        Args:
            node (TSTNode): 확인할 노드
            
        Returns:
            bool: 자식이 있으면 True, 없으면 False
        """
        if node is None:
            return False
        
        return node.left is not None or node.middle is not None or node.right is not None
    
    def _delete_helper(self, node, word, index):
        """
        삭제 헬퍼 함수 (재귀적 구현)
        
        Args:
            node (TSTNode): 현재 노드
            word (str): 삭제할 단어
            index (int): 현재 문자 인덱스
            
        Returns:
            TSTNode: 삭제 후 현재 노드 (None이면 노드 삭제됨)
        """
        if node is None or index >= len(word):
            return node
        
        current_char = word[index]
        
        if current_char < node.data:
            node.left = self._delete_helper(node.left, word, index)
        elif current_char > node.data:
            node.right = self._delete_helper(node.right, word, index)
        else:  # current_char == node.data
            if index == len(word) - 1:
                # 단어의 마지막 문자에 도달
                node.has_value = False
                node.value = 0
                
                # 자식이 없다면 노드 삭제
                if not self._has_children(node):
                    return None
            else:
                # 다음 문자로 이동하여 삭제
                node.middle = self._delete_helper(node.middle, word, index + 1)
                
                # 현재 노드에 값도 없고 자식도 없다면 삭제
                if not node.has_value and not self._has_children(node):
                    return None
        
        return node
    
    def delete(self, word):
        """
        TST에서 단어 삭제
        
        Args:
            word (str): 삭제할 단어
            
        Returns:
            bool: 성공하면 True, 실패하면 False
        """
        if not word:
            return False
        
        self.root = self._delete_helper(self.root, word, 0)
        return True
    
    def _print_tst(self, node, depth=0):
        """
        TST 구조를 시각적으로 출력 (디버깅용)
        
        Args:
            node (TSTNode): 출력할 노드
            depth (int): 현재 깊이
        """
        if node is None:
            return
        
        # 오른쪽 서브트리 먼저 출력
        self._print_tst(node.right, depth + 1)
        
        # 들여쓰기 및 현재 노드 출력
        indent = "    " * depth
        value_str = f" [값: {node.value}]" if node.has_value else ""
        middle_str = ""
        
        # middle 링크가 있으면 체인 표시
        if node.middle is not None:
            middle_str = " -> " + self._get_middle_chain(node.middle)
        
        print(f"{indent}{node.data}{value_str}{middle_str}")
        
        # 왼쪽 서브트리 출력
        self._print_tst(node.left, depth + 1)
    
    def _get_middle_chain(self, node):
        """Middle 체인을 문자열로 반환"""
        if node is None:
            return ""
        
        chain = node.data
        if node.has_value:
            chain += f"[{node.value}]"
        
        if node.middle is not None:
            chain += "-" + self._get_middle_chain(node.middle)
        
        return chain
    
    def print_tst(self):
        """TST 구조를 시각적으로 출력"""
        print("=== TST 구조 (간단) ===")
        if self.root is None:
            print("(빈 트리)")
        else:
            self._print_tst(self.root)
        print()
    
    def _print_tst_detailed(self, node, prefix="", depth=0):
        """
        TST 상세 구조 출력
        
        Args:
            node (TSTNode): 현재 노드
            prefix (str): 현재까지의 접두사
            depth (int): 현재 깊이
        """
        if node is None:
            return
        
        # 들여쓰기
        indent = "  " * depth
        
        # 현재 노드 정보 출력
        value_info = f" [단어완성: {prefix + node.data}, 값: {node.value}]" if node.has_value else ""
        print(f"{indent}'{node.data}'{value_info}")
        
        # 현재 문자를 prefix에 추가
        new_prefix = prefix + node.data
        
        # left 서브트리
        if node.left is not None:
            print(f"{indent}  L:")
            self._print_tst_detailed(node.left, prefix, depth + 2)
        
        # middle 서브트리
        if node.middle is not None:
            print(f"{indent}  M:")
            self._print_tst_detailed(node.middle, new_prefix, depth + 2)
        
        # right 서브트리
        if node.right is not None:
            print(f"{indent}  R:")
            self._print_tst_detailed(node.right, prefix, depth + 2)
    
    def print_tst_detailed(self):
        """TST 상세 구조를 시각적으로 출력"""
        print("=== TST 상세 구조 ===")
        if self.root is None:
            print("(빈 트리)")
        else:
            self._print_tst_detailed(self.root)
        print()
    
    def _in_order_traversal(self, node, word, results):
        """
        중위 순회로 단어들을 사전순으로 수집
        
        Args:
            node (TSTNode): 현재 노드
            word (str): 현재까지 구성된 단어
            results (list): 결과를 저장할 리스트
        """
        if node is None:
            return
        
        # 왼쪽 서브트리 먼저
        self._in_order_traversal(node.left, word, results)
        
        # 현재 노드 처리
        current_word = word + node.data
        
        # 값이 있다면 결과에 추가
        if node.has_value:
            results.append((current_word, node.value))
        
        # 가운데 서브트리 (다음 문자들)
        self._in_order_traversal(node.middle, current_word, results)
        
        # 오른쪽 서브트리
        self._in_order_traversal(node.right, word, results)
    
    def get_sorted_words(self):
        """
        사전순으로 정렬된 모든 단어를 반환
        
        Returns:
            list: (단어, 값) 튜플의 리스트 (사전순)
        """
        results = []
        
        if self.root is not None:
            self._in_order_traversal(self.root, "", results)
        
        return results
    
    def size(self):
        """
        TST에 저장된 단어의 개수 반환
        
        Returns:
            int: 저장된 단어의 개수
        """
        return len(self.get_all_words())
    
    def is_empty(self):
        """
        TST가 비어있는지 확인
        
        Returns:
            bool: 비어있으면 True, 아니면 False
        """
        return self.root is None


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
    
    # TST 구조 출력
    tst.print_tst()
    
    # TST 상세 구조 출력
    tst.print_tst_detailed()
    
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
    
    # 대량 데이터 테스트
    print("=== 대량 데이터 테스트 ===")
    large_test_words = [
        "the", "and", "for", "are", "but", "not", "you", "all",
        "can", "had", "her", "was", "one", "our", "out", "day",
        "get", "has", "him", "his", "how", "its", "may", "new",
        "now", "old", "see", "two", "way", "who", "boy", "did"
    ]
    
    test_tst = TST()
    for i, word in enumerate(large_test_words):
        test_tst.insert(word, i + 100)
    
    print(f"대량 삽입 완료: {len(large_test_words)}개 단어")
    
    # 접두사별 검색 성능 테스트
    test_prefixes = ["t", "a", "c", "w"]
    for prefix in test_prefixes:
        prefix_words = test_tst.get_words_with_prefix(prefix)
        print(f"접두사 '{prefix}'로 시작하는 단어 수: {len(prefix_words)}")
    
    print(f"\n총 저장된 단어 수: {tst.size()}")
    print(f"TST가 비어있는가: {tst.is_empty()}")
    
    print("\n테스트 완료")


def demo_auto_complete():
    """자동완성 기능 데모"""
    print("\n" + "="*50)
    print("=== TST를 활용한 자동완성 기능 데모 ===")
    
    # 프로그래밍 관련 단어 사전 구축
    tst = TST()
    programming_words = [
        ("python", 100), ("programming", 95), ("program", 90),
        ("class", 85), ("function", 80), ("variable", 75),
        ("algorithm", 70), ("data", 65), ("structure", 60),
        ("tree", 55), ("array", 50), ("list", 45),
        ("dictionary", 40), ("string", 35), ("integer", 30)
    ]
    
    for word, frequency in programming_words:
        tst.insert(word, frequency)
    
    # 자동완성 시뮬레이션
    user_inputs = ["pro", "cl", "ar", "st"]
    
    for user_input in user_inputs:
        suggestions = tst.get_words_with_prefix(user_input)
        # 빈도수로 정렬
        suggestions.sort(key=lambda x: x[1], reverse=True)
        
        print(f"\n'{user_input}' 입력 시 추천 단어:")
        for word, freq in suggestions[:5]:  # 상위 5개만
            print(f"  {word} (빈도: {freq})")


def performance_comparison():
    """성능 비교 데모"""
    print("\n" + "="*50)
    print("=== TST vs 일반 리스트 성능 비교 데모 ===")
    
    # 테스트 데이터 생성
    words = ["apple", "application", "apply", "apartment", "appreciate", 
             "approach", "appropriate", "approve", "approximate", "april"]
    
    # TST 구축
    tst = TST()
    for i, word in enumerate(words):
        tst.insert(word, i)
    
    # 일반 리스트
    word_list = [(word, i) for i, word in enumerate(words)]
    
    prefix = "app"
    
    print(f"'{prefix}' 접두사 검색 결과:")
    
    # TST 결과
    tst_results = tst.get_words_with_prefix(prefix)
    print(f"TST 결과: {[word for word, _ in tst_results]}")
    
    # 리스트 결과 (단순 검색)
    list_results = [(word, val) for word, val in word_list if word.startswith(prefix)]
    print(f"리스트 결과: {[word for word, _ in list_results]}")
    
    print(f"\n성능 특성:")
    print(f"TST: O(log n) 평균 시간, 메모리 효율적")
    print(f"리스트: O(n) 시간, 단순 구조")


if __name__ == "__main__":
    test_tst()
    demo_auto_complete()
    performance_comparison()