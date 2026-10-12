class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenmap = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in seenmap:
                return [seenmap[diff],i]
            seenmap[num] = i