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

print('='*10)
def search(node,target):
    if not node:
        return f'{target} not found'
    if node.value == target:
        return f'{target} found'
    return search(node.left,target) or search(node.right,target)

print(search(A,11))
# Binary Search Trees (BSTs)

#       5
#    1    8
#  -1 3  7 9

A2 = TreeNode(5)
B2 = TreeNode(1)
C2 = TreeNode(8)
D2 = TreeNode(-1)
E2 = TreeNode(3)
F2 = TreeNode(7)
G2 = TreeNode(9)

A2.left, A2.right = B2, C2
B2.left, B2.right = D2, E2
C2.left, C2.right = F2, G2

print(A2)


def BST(node,target):
    if not node: 
        return f'{target} was not found'
    if node.value == target:
        return f'{target} was found '
    if target<node.value:
        return BST(node.left,target)
    else:
        BST(node.right,target)
print(BST(A2,1))