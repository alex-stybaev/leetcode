class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def setX(self, x):
        self.val = x

    def setLeft(self, l):
        self.left = l

    def setRight(self, r):
        self.right = r

class Solution(object):

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = 0
        if (root.left != None):
            result += self.sumOfLeftLeaves(root.left)

        if (root.right != None):
            result += self.sumOfLeftLeaves(root.right)

        if root.left == None and root.right == None:
            result += root.val

        return result


t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)

t1.setLeft(t2)
t1.setRight(t3)
t2.setLeft(t4)
t2.setRight(t5)

s= Solution()

print(s.sumOfLeftLeaves(t1))