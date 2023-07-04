from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def make_tree(tree, node, i, n):
    if n > i:
        if tree[i] is None:
            return None
        temp = TreeNode(tree[i])
        node = temp
        node.left = make_tree(tree, node.left, 2 * i + 1, n)
        node.right = make_tree(tree, node.right, 2 * i + 2, n)

    return node

def main():

    N = int(input())
    tree = [int(N) for N in input().split()]

    ans = []

    root = make_tree(tree, None, 0, len(tree))

    ans = []

    stack = deque([root])

    while stack:
        
        node = stack.pop()
        
        ans.append(node.val)
        
        if node.right:
            stack.append(node.right)
        
        if node.left:
            stack.append(node.left)
        print(ans)     

if __name__ == "__main__":
    main()