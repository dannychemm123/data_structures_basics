class TreeNode:
    def __init__(self,value,left=None,right = None):
        self.value = value
        self.left = left
        self.right = right
    
    def __str__(self):
        return f'{self.value}'
    
A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F


def preorder(node):
    if not node:
        return
    print(node)
    preorder(node.left)
    preorder(node.right)
preorder(A)
print('='*10)
def in_order(node):
    if not node:
        return
    in_order(node.left)
    print(node)
    in_order(node.right)
in_order(A)
print('='*10)
def postorder(node):
    if not node:
        return 
    postorder(node.left)
    postorder(node.right)
    print(node)

postorder(A)
print('='*10)
# Using iterative method 
def iterative_binary_tree(node):
    stk = [node]
    while stk:
        node = stk.pop()
        if node.right:
            stk.append(node.right)
        if node.left:
            stk.append(node.left)
        print(node)
iterative_binary_tree(A)


def BFS(node):
    