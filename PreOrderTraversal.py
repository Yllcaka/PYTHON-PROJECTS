# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> "List[int]":
        returner = []
        for i in root:
            if type(i) != int:
                continue
            returner.append(i)
        return returner
tree = TreeNode(3)
solution = Solution()
# print(tree.__dir__)
exec("print(solution.preorderTraversal([1,'2',2,None,3]))")