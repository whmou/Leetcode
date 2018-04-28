class Solution(object):
    def helper(self, node):
        if node is None:
            return 0
        tmpLeft = self.helper(node.left)
        if tmpLeft == -1:
            return tmpLeft
        tmpRight = self.helper(node.right)
        if tmpRight == -1:
            return tmpRight
        if abs(tmpLeft - tmpRight) > 1:
            return -1
        return max(tmpLeft, tmpRight) + 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        return False if self.helper(root) == -1 else True
