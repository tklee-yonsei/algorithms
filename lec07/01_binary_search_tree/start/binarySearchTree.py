# binarySearchTree.py (START CODE)

class TreeNode:
  """이진 탐색 트리 노드 클래스 - 완성됨"""

  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


class BinarySearchTree:
  """이진 탐색 트리 클래스"""

  def __init__(self):
    """초기화 - 완성됨"""
    self.root = None

  def insert(self, value):
    """TODO: 값을 트리에 삽입"""
    # 여기에 삽입 로직을 구현하세요
    # _insert_recursive 헬퍼 함수를 사용하세요
    pass

  def _insert_recursive(self, node, value):
    """TODO: 재귀적으로 값을 삽입하는 헬퍼 함수"""
    # 여기에 재귀적 삽입 로직을 구현하세요
    # 1. 노드가 None이면 새 노드 생성
    # 2. 값이 현재 노드보다 작으면 왼쪽 서브트리에 삽입
    # 3. 값이 현재 노드보다 크면 오른쪽 서브트리에 삽입
    # 4. 같은 값은 삽입하지 않음 (중복 방지)
    pass

  def delete(self, value):
    """TODO: 값을 트리에서 삭제"""
    # 여기에 삭제 로직을 구현하세요
    # _delete_recursive 헬퍼 함수를 사용하세요
    pass

  def _delete_recursive(self, node, value):
    """TODO: 재귀적으로 값을 삭제하는 헬퍼 함수"""
    # 여기에 재귀적 삭제 로직을 구현하세요
    # 1. 노드가 None이면 그대로 반환
    # 2. 값에 따라 왼쪽 또는 오른쪽 서브트리에서 재귀적으로 삭제
    # 3. 삭제할 노드를 찾으면:
    #    - 자식이 없는 경우: None 반환
    #    - 자식이 하나인 경우: 자식 반환
    #    - 자식이 둘인 경우: 오른쪽 서브트리의 최솟값으로 대체
    pass

  def _find_min(self, node):
    """최솟값을 가진 노드 찾기 - 완성됨"""
    while node.left is not None:
      node = node.left
    return node

  def inorder_traversal(self):
    """TODO: 중위 순회 (오름차순)"""
    # 여기에 중위 순회 로직을 구현하세요
    # _inorder_recursive 헬퍼 함수를 사용하세요
    pass

  def _inorder_recursive(self, node, result):
    """TODO: 중위 순회 재귀 헬퍼 함수"""
    # 여기에 중위 순회 로직을 구현하세요
    # 순서: 왼쪽 서브트리 → 현재 노드 → 오른쪽 서브트리
    pass

  def preorder_traversal(self):
    """TODO: 전위 순회"""
    # 여기에 전위 순회 로직을 구현하세요
    # _preorder_recursive 헬퍼 함수를 사용하세요
    pass

  def _preorder_recursive(self, node, result):
    """TODO: 전위 순회 재귀 헬퍼 함수"""
    # 여기에 전위 순회 로직을 구현하세요
    # 순서: 현재 노드 → 왼쪽 서브트리 → 오른쪽 서브트리
    pass

  def postorder_traversal(self):
    """TODO: 후위 순회"""
    # 여기에 후위 순회 로직을 구현하세요
    # _postorder_recursive 헬퍼 함수를 사용하세요
    pass

  def _postorder_recursive(self, node, result):
    """TODO: 후위 순회 재귀 헬퍼 함수"""
    # 여기에 후위 순회 로직을 구현하세요
    # 순서: 왼쪽 서브트리 → 오른쪽 서브트리 → 현재 노드
    pass

  def print_tree(self, prefix="", is_last=True):
    """트리를 시각적으로 출력 - 완성됨"""
    if self.root is not None:
      self._print_tree_recursive(self.root, prefix, is_last)
    else:
      print("(빈 트리)")

  def _print_tree_recursive(self, node, prefix, is_last):
    """트리 출력 재귀 헬퍼 함수 - 완성됨"""
    if node is not None:
      print(prefix, end="")

      if is_last:
        print("└── ", end="")
        new_prefix = prefix + "    "
      else:
        print("├── ", end="")
        new_prefix = prefix + "│   "

      print(node.data)

      if node.left is not None or node.right is not None:
        self._print_tree_recursive(node.left, new_prefix, node.right is None)
        self._print_tree_recursive(node.right, new_prefix, True)

  def clear(self):
    """트리의 모든 노드를 삭제 - 완성됨"""
    self.root = None

  def copy(self):
    """트리를 복사하여 새로운 BinarySearchTree 객체 반환 - 완성됨"""
    new_tree = BinarySearchTree()
    new_tree.root = self._copy_recursive(self.root)
    return new_tree

  def _copy_recursive(self, node):
    """트리 복사 재귀 헬퍼 함수 - 완성됨"""
    if node is None:
      return None

    new_node = TreeNode(node.data)
    new_node.left = self._copy_recursive(node.left)
    new_node.right = self._copy_recursive(node.right)

    return new_node

  def search(self, value):
    """값을 검색 - 완성됨"""
    return self._search_recursive(self.root, value)

  def _search_recursive(self, node, value):
    """재귀적 검색 헬퍼 함수 - 완성됨"""
    if node is None or node.data == value:
      return node

    if value < node.data:
      return self._search_recursive(node.left, value)
    else:
      return self._search_recursive(node.right, value)

  def get_height(self):
    """트리 높이 계산 - 완성됨"""
    return self._get_height_recursive(self.root)

  def _get_height_recursive(self, node):
    """트리 높이 계산 재귀 헬퍼 함수 - 완성됨"""
    if node is None:
      return -1

    left_height = self._get_height_recursive(node.left)
    right_height = self._get_height_recursive(node.right)

    return 1 + max(left_height, right_height)

  def count_nodes(self):
    """노드 개수 계산 - 완성됨"""
    return self._count_nodes_recursive(self.root)

  def _count_nodes_recursive(self, node):
    """노드 개수 계산 재귀 헬퍼 함수 - 완성됨"""
    if node is None:
      return 0

    return 1 + self._count_nodes_recursive(node.left) + self._count_nodes_recursive(node.right)


# 테스트 코드 (완성됨)
if __name__ == "__main__":
  bst = BinarySearchTree()

  # 노드 삽입
  print("노드 삽입: 50, 30, 70, 20, 40, 60, 80")
  values = [50, 30, 70, 20, 40, 60, 80]
  for value in values:
    bst.insert(value)

  print("중위 순회 (오름차순):", bst.inorder_traversal())
  print("전위 순회:", bst.preorder_traversal())
  print("후위 순회:", bst.postorder_traversal())

  # 트리 정보 출력
  print("\n=== 트리 정보 ===")
  print(f"트리 높이: {bst.get_height()}")
  print(f"노드 개수: {bst.count_nodes()}")

  # 검색 테스트
  print("\n=== 검색 테스트 ===")
  found = bst.search(40)
  if found is not None:
    print("값 40을 찾았습니다.")
  else:
    print("값 40을 찾지 못했습니다.")

  found = bst.search(99)
  if found is not None:
    print("값 99를 찾았습니다.")
  else:
    print("값 99를 찾지 못했습니다.")

  # 노드 삭제
  print("\n노드 20 삭제")
  bst.delete(20)
  print("중위 순회:", bst.inorder_traversal())

  print("\n노드 30 삭제")
  bst.delete(30)
  print("중위 순회:", bst.inorder_traversal())

  print("\n노드 50 삭제")
  bst.delete(50)
  print("중위 순회:", bst.inorder_traversal())

  print("\n=== 새로운 기능 테스트 ===")

  # 트리 시각적 출력
  print("\n트리 구조 출력:")
  bst.print_tree()

  # 트리 복사
  print("\n트리 복사 테스트")
  copied_tree = bst.copy()
  print("원본 트리 중위 순회:", bst.inorder_traversal())
  print("복사된 트리 중위 순회:", copied_tree.inorder_traversal())

  print("\n복사된 트리 구조:")
  copied_tree.print_tree()

  # 복사된 트리에 노드 추가 (원본과 독립적임을 확인)
  print("\n복사된 트리에 노드 25 추가")
  copied_tree.insert(25)
  print("원본 트리 중위 순회:", bst.inorder_traversal())
  print("복사된 트리 중위 순회:", copied_tree.inorder_traversal())

  # 트리 전체 삭제
  print("\n트리 전체 삭제")
  bst.clear()
  copied_tree.clear()

  print("삭제 후 원본 트리:")
  bst.print_tree()
  print("삭제 후 복사된 트리:")
  copied_tree.print_tree()
