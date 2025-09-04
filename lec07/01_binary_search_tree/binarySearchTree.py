# binarySearchTree.py

class TreeNode:
  """이진 탐색 트리 노드 클래스"""

  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


class BinarySearchTree:
  """이진 탐색 트리 클래스"""

  def __init__(self):
    self.root = None

  def insert(self, value):
    """값을 트리에 삽입"""
    self.root = self._insert_recursive(self.root, value)

  def _insert_recursive(self, node, value):
    """재귀적으로 값을 삽입하는 헬퍼 함수"""
    if node is None:
      return TreeNode(value)

    if value < node.data:
      node.left = self._insert_recursive(node.left, value)
    elif value > node.data:
      node.right = self._insert_recursive(node.right, value)

    return node

  def delete(self, value):
    """값을 트리에서 삭제"""
    self.root = self._delete_recursive(self.root, value)

  def _delete_recursive(self, node, value):
    """재귀적으로 값을 삭제하는 헬퍼 함수"""
    if node is None:
      return node

    if value < node.data:
      node.left = self._delete_recursive(node.left, value)
    elif value > node.data:
      node.right = self._delete_recursive(node.right, value)
    else:
      # 삭제할 노드 발견
      if node.left is None:
        return node.right
      elif node.right is None:
        return node.left

      # 자식이 둘 다 있는 경우
      temp = self._find_min(node.right)
      node.data = temp.data
      node.right = self._delete_recursive(node.right, temp.data)

    return node

  def _find_min(self, node):
    """최솟값을 가진 노드 찾기"""
    while node.left is not None:
      node = node.left
    return node

  def inorder_traversal(self):
    """중위 순회 (오름차순)"""
    result = []
    self._inorder_recursive(self.root, result)
    return result

  def _inorder_recursive(self, node, result):
    """중위 순회 재귀 헬퍼 함수"""
    if node is not None:
      self._inorder_recursive(node.left, result)
      result.append(node.data)
      self._inorder_recursive(node.right, result)

  def preorder_traversal(self):
    """전위 순회"""
    result = []
    self._preorder_recursive(self.root, result)
    return result

  def _preorder_recursive(self, node, result):
    """전위 순회 재귀 헬퍼 함수"""
    if node is not None:
      result.append(node.data)
      self._preorder_recursive(node.left, result)
      self._preorder_recursive(node.right, result)

  def postorder_traversal(self):
    """후위 순회"""
    result = []
    self._postorder_recursive(self.root, result)
    return result

  def _postorder_recursive(self, node, result):
    """후위 순회 재귀 헬퍼 함수"""
    if node is not None:
      self._postorder_recursive(node.left, result)
      self._postorder_recursive(node.right, result)
      result.append(node.data)

  def print_tree(self, prefix="", is_last=True):
    """트리를 시각적으로 출력"""
    if self.root is not None:
      self._print_tree_recursive(self.root, prefix, is_last)
    else:
      print("(빈 트리)")

  def _print_tree_recursive(self, node, prefix, is_last):
    """트리 출력 재귀 헬퍼 함수"""
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
    """트리의 모든 노드를 삭제"""
    self.root = None

  def copy(self):
    """트리를 복사하여 새로운 BinarySearchTree 객체 반환"""
    new_tree = BinarySearchTree()
    new_tree.root = self._copy_recursive(self.root)
    return new_tree

  def _copy_recursive(self, node):
    """트리 복사 재귀 헬퍼 함수"""
    if node is None:
      return None

    new_node = TreeNode(node.data)
    new_node.left = self._copy_recursive(node.left)
    new_node.right = self._copy_recursive(node.right)

    return new_node


# 사용 예시
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
