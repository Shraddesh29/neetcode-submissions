class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        IND = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in IND:
                return [IND[diff],i]
            IND[n] = i