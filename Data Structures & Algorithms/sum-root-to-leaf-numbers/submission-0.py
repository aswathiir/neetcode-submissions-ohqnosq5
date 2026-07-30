# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        cur = root
        num = 0
        power = [1]*10
        for i in range(1,10):
            power[i]*=power[i-1]*10
        while cur:
            if not cur.left:
                num = num*10+cur.val
                if not cur.right:
                    res+=num
                cur = cur.right
            else:
                prev = cur.left
                steps=1
                while prev.right and prev.right!=cur:
                    prev = prev.right
                    steps+=1
                if not prev.right:
                    prev.right = cur
                    num = num*10+cur.val
                    cur  = cur.left
                else:
                    prev.right = None
                    if not prev.left:
                        res+=num
                    num//=power[steps]
                    cur = cur.right
        return res