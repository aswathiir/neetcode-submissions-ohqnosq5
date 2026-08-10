# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cursum = 0
        cur = root
        while cur:
            if cur.right:
                prev = cur.right
                while prev.left and prev.left!=cur:
                    prev = prev.left
                if not prev.left:
                    prev.left = cur
                    cur = cur.right
                else:
                    prev.left = None
                    cursum+=cur.val 
                    cur.val = cursum 
                    cur = cur.left
            else:
                cursum+=cur.val 
                cur.val = cursum 
                cur = cur.left
        return root