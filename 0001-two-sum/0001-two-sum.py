class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for index, num in enumerate(nums):
            exclude_self = nums[:index] + nums[index+1:]
            if target - num in exclude_self: result.append(index)

        return result