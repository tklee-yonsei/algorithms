// binarySearchTree.c (START CODE)
#include <stdio.h>
#include <stdlib.h>

// 이진 탐색 트리 노드 구조체
struct TreeNode {
  int data;
  struct TreeNode* left;
  struct TreeNode* right;
};

// 새 노드 생성 함수 (완성됨)
struct TreeNode* createNode(int value) {
  struct TreeNode* newNode = (struct TreeNode*)malloc(sizeof(struct TreeNode));
  newNode->data = value;
  newNode->left = NULL;
  newNode->right = NULL;
  return newNode;
}

// TODO: 삽입 함수 구현
struct TreeNode* insert(struct TreeNode* root, int value) {
  // 여기에 삽입 로직을 구현하세요
  // 1. 루트가 NULL이면 새 노드 생성
  // 2. 값이 현재 노드보다 작으면 왼쪽 서브트리에 삽입
  // 3. 값이 현재 노드보다 크면 오른쪽 서브트리에 삽입
  // 4. 같은 값은 삽입하지 않음 (중복 방지)
  return NULL;  // 임시 반환값
}

// 최솟값 찾기 함수 (완성됨)
struct TreeNode* findMin(struct TreeNode* node) {
  while (node->left != NULL) {
    node = node->left;
  }
  return node;
}

// TODO: 삭제 함수 구현
struct TreeNode* deleteNode(struct TreeNode* root, int value) {
  // 여기에 삭제 로직을 구현하세요
  // 1. 루트가 NULL이면 그대로 반환
  // 2. 값에 따라 왼쪽 또는 오른쪽 서브트리에서 재귀적으로 삭제
  // 3. 삭제할 노드를 찾으면:
  //    - 자식이 없는 경우: 그냥 삭제
  //    - 자식이 하나인 경우: 자식으로 대체
  //    - 자식이 둘인 경우: 오른쪽 서브트리의 최솟값으로 대체
  return NULL;  // 임시 반환값
}

// TODO: 중위 순회 함수 구현 (Inorder Traversal)
void inorderTraversal(struct TreeNode* root) {
  // 여기에 중위 순회 로직을 구현하세요
  // 순서: 왼쪽 서브트리 → 현재 노드 → 오른쪽 서브트리
  // 결과: 오름차순으로 정렬된 값들이 출력됨
}

// TODO: 전위 순회 함수 구현 (Preorder Traversal)
void preorderTraversal(struct TreeNode* root) {
  // 여기에 전위 순회 로직을 구현하세요
  // 순서: 현재 노드 → 왼쪽 서브트리 → 오른쪽 서브트리
}

// TODO: 후위 순회 함수 구현 (Postorder Traversal)
void postorderTraversal(struct TreeNode* root) {
  // 여기에 후위 순회 로직을 구현하세요
  // 순서: 왼쪽 서브트리 → 오른쪽 서브트리 → 현재 노드
}

// 트리 시각적 출력 함수 (완성됨)
void printTree(struct TreeNode* root, char* prefix, int isLast) {
  if (root != NULL) {
    printf("%s", prefix);

    if (isLast) {
      printf("└── ");
    } else {
      printf("├── ");
    }

    printf("%d\n", root->data);

    char newPrefix[256];
    sprintf(newPrefix, "%s%s", prefix, isLast ? "    " : "│   ");

    if (root->left != NULL || root->right != NULL) {
      printTree(root->left, newPrefix, root->right == NULL);
      printTree(root->right, newPrefix, 1);
    }
  }
}

// 트리 전체 삭제 함수 (완성됨)
struct TreeNode* clearTree(struct TreeNode* root) {
  if (root != NULL) {
    clearTree(root->left);
    clearTree(root->right);
    free(root);
  }
  return NULL;
}

// 트리 복사 함수 (완성됨)
struct TreeNode* copyTree(struct TreeNode* root) {
  if (root == NULL) {
    return NULL;
  }

  struct TreeNode* newNode = createNode(root->data);
  newNode->left = copyTree(root->left);
  newNode->right = copyTree(root->right);

  return newNode;
}

// 트리 메모리 해제 함수 (완성됨)
void freeTree(struct TreeNode* root) {
  if (root != NULL) {
    freeTree(root->left);
    freeTree(root->right);
    free(root);
  }
}

// 검색 함수 (추가 - 완성됨)
struct TreeNode* search(struct TreeNode* root, int value) {
  if (root == NULL || root->data == value) {
    return root;
  }

  if (value < root->data) {
    return search(root->left, value);
  } else {
    return search(root->right, value);
  }
}

// 트리 높이 계산 함수 (추가 - 완성됨)
int getHeight(struct TreeNode* root) {
  if (root == NULL) {
    return -1;
  }

  int leftHeight = getHeight(root->left);
  int rightHeight = getHeight(root->right);

  return 1 + (leftHeight > rightHeight ? leftHeight : rightHeight);
}

// 노드 개수 계산 함수 (추가 - 완성됨)
int countNodes(struct TreeNode* root) {
  if (root == NULL) {
    return 0;
  }

  return 1 + countNodes(root->left) + countNodes(root->right);
}

// 테스트 코드 (완성됨)
int main() {
  struct TreeNode* root = NULL;

  // 노드 삽입
  printf("노드 삽입: 50, 30, 70, 20, 40, 60, 80\n");
  root = insert(root, 50);
  root = insert(root, 30);
  root = insert(root, 70);
  root = insert(root, 20);
  root = insert(root, 40);
  root = insert(root, 60);
  root = insert(root, 80);

  printf("중위 순회 (오름차순): ");
  inorderTraversal(root);
  printf("\n");

  printf("전위 순회: ");
  preorderTraversal(root);
  printf("\n");

  printf("후위 순회: ");
  postorderTraversal(root);
  printf("\n");

  // 트리 정보 출력
  printf("\n=== 트리 정보 ===\n");
  printf("트리 높이: %d\n", getHeight(root));
  printf("노드 개수: %d\n", countNodes(root));

  // 검색 테스트
  printf("\n=== 검색 테스트 ===\n");
  struct TreeNode* found = search(root, 40);
  if (found != NULL) {
    printf("값 40을 찾았습니다.\n");
  } else {
    printf("값 40을 찾지 못했습니다.\n");
  }

  found = search(root, 99);
  if (found != NULL) {
    printf("값 99를 찾았습니다.\n");
  } else {
    printf("값 99를 찾지 못했습니다.\n");
  }

  // 노드 삭제
  printf("\n노드 20 삭제\n");
  root = deleteNode(root, 20);
  printf("중위 순회: ");
  inorderTraversal(root);
  printf("\n");

  printf("\n노드 30 삭제\n");
  root = deleteNode(root, 30);
  printf("중위 순회: ");
  inorderTraversal(root);
  printf("\n");

  printf("\n노드 50 삭제\n");
  root = deleteNode(root, 50);
  printf("중위 순회: ");
  inorderTraversal(root);
  printf("\n");

  printf("\n=== 새로운 기능 테스트 ===\n");

  // 트리 시각적 출력
  printf("\n트리 구조 출력:\n");
  printTree(root, "", 1);

  // 트리 복사
  printf("\n트리 복사 테스트\n");
  struct TreeNode* copiedTree = copyTree(root);
  printf("원본 트리 중위 순회: ");
  inorderTraversal(root);
  printf("\n");
  printf("복사된 트리 중위 순회: ");
  inorderTraversal(copiedTree);
  printf("\n");

  printf("\n복사된 트리 구조:\n");
  printTree(copiedTree, "", 1);

  // 복사된 트리에 노드 추가 (원본과 독립적임을 확인)
  printf("\n복사된 트리에 노드 25 추가\n");
  copiedTree = insert(copiedTree, 25);
  printf("원본 트리 중위 순회: ");
  inorderTraversal(root);
  printf("\n");
  printf("복사된 트리 중위 순회: ");
  inorderTraversal(copiedTree);
  printf("\n");

  // 트리 전체 삭제
  printf("\n트리 전체 삭제\n");
  root = clearTree(root);
  copiedTree = clearTree(copiedTree);

  printf("삭제 후 원본 트리 중위 순회: ");
  inorderTraversal(root);
  printf("(빈 트리)\n");

  return 0;
}
