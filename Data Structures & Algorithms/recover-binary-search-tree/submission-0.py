# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        node1=node2=prev=None
        cur= root
        while cur:
            if not cur.left:
                if prev and prev.val>cur.val:
                    node2 = cur
                    if not node1:
                        node1= prev
                prev=cur
                cur = cur.right
            else:
                pred = cur.left
                while pred.right and pred.right!=cur:
                    pred = pred.right
                if not pred.right:
                    pred.right = cur
                    cur = cur.left
                else:
                    pred.right =None
                    if prev and prev.val>cur.val:
                        node2 = cur
                        if not node1:
                            node1 = prev
                    prev = cur
                    cur = cur.right
        node1.val,node2.val = node2.val,node1.val