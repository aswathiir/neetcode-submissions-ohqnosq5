class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res , prefix = 0,0
        count = [0]*k
        count[0] = 1
        for num in nums:
            prefix = (prefix+num+k)%k
            res+=count[prefix]
            count[prefix]+=1
        return res