#!/usr/bin/python

import unittest
from collections import deque # A double-ended queue

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

class SortBinaryTree:
    def tree_by_levels(self, node):
        if node == None:
            return []

        a_list, queue = [], deque([node])
        while queue:
            n = queue.popleft()
            a_list.append(n.value)
            if n.left is not None:
                queue.append(n.left)
            if n.right is not None:
                queue.append(n.right)
        return a_list

class ValidTree(unittest.TestCase):

    def test_empty_node(self):
        vtclass = SortBinaryTree()
        self.assertEquals(vtclass.tree_by_levels(None), [])

    def test_sort_a_binary_tree(self):
        vtcls = SortBinaryTree()
        self.assertEquals(vtcls.tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)  ), [1,2,3,4,5,6])

if __name__ == "__main__":
    unittest.main()
