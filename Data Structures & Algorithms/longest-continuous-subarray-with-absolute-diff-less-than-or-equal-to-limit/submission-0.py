class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minheap = []
        maxheap = []
        j,res=0,0
        for i,v in enumerate(nums):
            heapq.heappush(maxheap,(-v,i))
            heapq.heappush(minheap,(v,i))
            while -maxheap[0][0] - minheap[0][0]>limit:
                j+=1
                while maxheap and maxheap[0][1]<j:
                    heapq.heappop(maxheap)
                while minheap and minheap[0][1]<j:
                    heapq.heappop(minheap)
            res = max(res,i-j+1)
        return res