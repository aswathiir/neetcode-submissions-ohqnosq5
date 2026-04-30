class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1set , num2set = set(nums1),set(nums2)
        res1,res2 = [],[]
        for num in num1set:
            if num not in num2set:
                res1.append(num)
        for num in num2set:
            if num not in num1set:
                res2.append(num)
        return [res1,res2]