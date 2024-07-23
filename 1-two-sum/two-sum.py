class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp_map = {}

        for i in range(len(nums)):
            target2 = target - nums[i]
            if target2 in tmp_map:
                return [tmp_map[target2], i]

            tmp_map[nums[i]] = i