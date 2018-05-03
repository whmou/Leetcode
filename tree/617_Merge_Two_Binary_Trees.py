# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None and t2 is None:
            return
        if t1 is None:
            return t2
        if t2 is None:
            return t1

        t = TreeNode(t1.val + t2.val)
        t.left = self.mergeTrees(t1.left, t2.left)
        t.right = self.mergeTrees(t1.right, t2.right)

        return t


t1_1 = TreeNode(1)
t1_2 = TreeNode(3)
t1_3 = TreeNode(2)
t1_4 = TreeNode(5)
t1_1.left = t1_2
t1_1.right = t1_3
t1_2.left = t1_4

t2_1 = TreeNode(2)
t2_2 = TreeNode(1)
t2_3 = TreeNode(3)
t2_4 = TreeNode(4)
t2_5 = TreeNode(7)
t2_1.left = t2_2
t2_1.right = t2_3
t2_2.right = t2_4
t2_3.right = t2_5


s = Solution()
t3 = s.mergeTrees(t1_1, t2_1)
print t3.val
print t3.left.val
print t3.right.val
