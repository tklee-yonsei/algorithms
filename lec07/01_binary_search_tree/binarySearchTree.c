// binarySearchTree.c
#include <stdio.h>
#include <stdlib.h>

// 이진 탐색 트리 노드 구조체
struct TreeNode {
  int data;
  struct TreeNode* left;
  struct TreeNode* right;
};

// 새 노드 생성 함수
struct TreeNode* createNode(int value) {
  struct TreeNode* newNode = (struct TreeNode*)malloc(sizeof(struct TreeNode));
  newNode->data = value;
  newNode->left = NULL;
  newNode->right = NULL;
  return newNode;
}

// 삽입 함수
struct TreeNode* insert(struct TreeNode* root, int value) {
  if (root == NULL) {
    return createNode(value);
  }

  if (value < root->data) {
    root->left = insert(root->left, value);
  } else if (value > root->data) {
    root->right = insert(root->right, value);
  }

  return root;
}

// 최솟값 찾기 함수
struct TreeNode* findMin(struct TreeNode* node) {
  while (node->left != NULL) {
    node = node->left;
  }
  return node;
}

// 삭제 함수
struct TreeNode* deleteNode(struct TreeNode* root, int value) {
  if (root == NULL) {
    return root;
  }

  if (value < root->data) {
    root->left = deleteNode(root->left, value);
  } else if (value > root->data) {
    root->right = deleteNode(root->right, value);
  } else {
    // 삭제할 노드 발견
    if (root->left == NULL) {
      struct TreeNode* temp = root->right;
      free(root);
      return temp;
    } else if (root->right == NULL) {
      struct TreeNode* temp = root->left;
      free(root);
      return temp;
    }

    // 자식이 둘 다 있는 경우
    struct TreeNode* temp = findMin(root->right);
    root->data = temp->data;
    root->right = deleteNode(root->right, temp->data);
  }

  return root;
}

// 중위 순회 함수 (Inorder Traversal)
void inorderTraversal(struct TreeNode* root) {
  if (root != NULL) {
    inorderTraversal(root->left);
    printf("%d ", root->data);
    inorderTraversal(root->right);
  }
}

// 전위 순회 함수 (Preorder Traversal)
void preorderTraversal(struct TreeNode* root) {
  if (root != NULL) {
    printf("%d ", root->data);
    preorderTraversal(root->left);
    preorderTraversal(root->right);
  }
}

// 후위 순회 함수 (Postorder Traversal)
void postorderTraversal(struct TreeNode* root) {
  if (root != NULL) {
    postorderTraversal(root->left);
    postorderTraversal(root->right);
    printf("%d ", root->data);
  }
}

// 트리 시각적 출력 함수
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

// 트리 전체 삭제 함수 (루트를 NULL로 설정)
struct TreeNode* clearTree(struct TreeNode* root) {
  if (root != NULL) {
    clearTree(root->left);
    clearTree(root->right);
    free(root);
  }
  return NULL;
}

// 트리 복사 함수
struct TreeNode* copyTree(struct TreeNode* root) {
  if (root == NULL) {
    return NULL;
  }

  struct TreeNode* newNode = createNode(root->data);
  newNode->left = copyTree(root->left);
  newNode->right = copyTree(root->right);

  return newNode;
}

// 트리 메모리 해제 함수 (기존 함수 유지)
void freeTree(struct TreeNode* root) {
  if (root != NULL) {
    freeTree(root->left);
    freeTree(root->right);
    free(root);
  }
}

// 사용 예시
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
