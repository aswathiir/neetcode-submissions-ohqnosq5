"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldtocopy = collections.defaultdict(lambda: Node(0))
        oldtocopy[None] = None
        cur = head
        while cur:
            oldtocopy[cur].val = cur.val 
            oldtocopy[cur].next = oldtocopy[cur.next]
            oldtocopy[cur].random = oldtocopy[cur.random]
            cur = cur.next
        return oldtocopy[head]