class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # key: number, value: index

        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen.get(diff), i]
            seen[num] = i