class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightmax =-1
        for i in range(len(arr) -1,-1,-1):
            newMax = max(rightmax,arr[i])
            arr[i]=rightmax
            rightmax = newMax
        return arr