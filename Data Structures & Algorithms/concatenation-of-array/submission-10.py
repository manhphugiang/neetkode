class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        k = len(nums)
        for i in range(0,k):
            nums.append(nums[i])            
        return nums