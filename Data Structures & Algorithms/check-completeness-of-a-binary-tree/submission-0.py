# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        nullseen = False
        while q:
            node = q.popleft()
            if node:
                if nullseen:
                    return False
                q.append(node.left)
                q.append(node.right)
            else:
                nullseen = True
        return True