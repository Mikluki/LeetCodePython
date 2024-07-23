class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp = {}
        for i, num in enumerate(nums):
            for key, val in tmp.items():
                if val + num == target:
                    return [key, i]
            else:
                tmp[i] = num