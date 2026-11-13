"""Binary Tree - ANTEQUINA"""
from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree():
    #            A
    #          /   \
    #         N     T
    #        / \   / \
    #       E   Q U   I
    #      / \
    #     N   A
    a, n, t = Node("A"), Node("N"), Node("T")
    e, q, u, i = Node("E"), Node("Q"), Node("U"), Node("I")
    n2, a2 = Node("N"), Node("A")
    a.left, a.right = n, t
    n.left, n.right = e, q
    t.left, t.right = u, i
    e.left, e.right = n2, a2
    return a


def bfs(root):
    """Level-order: visit level by level, left to right (uses a queue)."""
    result, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


def dfs_preorder(node, result=None):
    """Preorder DFS: Root -> Left -> Right (uses recursion/stack)."""
    if result is None:
        result = []
    if node:
        result.append(node.value)
        dfs_preorder(node.left, result)
        dfs_preorder(node.right, result)
    return result


def count_nodes(node):
    return 0 if node is None else 1 + count_nodes(node.left) + count_nodes(node.right)


def run():
    root = build_tree()
    print("=== BINARY TREE - ANTEQUINA ===")
    print("Total nodes :", count_nodes(root))
    print("BFS         :", " -> ".join(bfs(root)))
    print("DFS Preorder:", " -> ".join(dfs_preorder(root)))
