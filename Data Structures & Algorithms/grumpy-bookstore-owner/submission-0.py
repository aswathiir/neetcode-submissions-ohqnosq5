class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l=0
        window = max_wind=0
        satisfied = 0
        for r in range(len(customers)):
            if grumpy[r]:
                window+=customers[r]
            else:
                satisfied+=customers[r]
            if r-l+1>minutes:
                if grumpy[l]:
                    window-=customers[l]
                l+=1
            max_wind = max(window,max_wind)
        return satisfied + max_wind