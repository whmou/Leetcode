# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def __init__(self):
        self.level_cnt = {}
        self.level_sum = {}

    def helper(self, node, level):
        if level not in self.level_cnt:
            self.level_cnt[level] = 1
            self.level_sum[level] = node.val
        else:
            self.level_cnt[level] += 1
            self.level_sum[level] += node.val
        if node.left is not None:
            self.helper(node.left, level + 1)
        if node.right is not None:
            self.helper(node.right, level + 1)

    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        self.helper(root, 0)
        l = []
        for i in range(len(self.level_cnt)):
            l.append(float(self.level_sum[i]) / float(self.level_cnt[i]))
        return l
