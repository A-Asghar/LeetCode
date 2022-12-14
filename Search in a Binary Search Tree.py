# https://leetcode.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        output = TreeNode()
        def traverse(node):
            if node:
                if val < node.val:
                    traverse(node.left)
                else:
                    traverse(node.right)
                if(node.val == val):
                    output.val = node.val
                    output.right = node.right
                    output.left = node.left
        traverse(root)
        return None if output.val == 0 else output
