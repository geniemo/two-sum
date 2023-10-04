from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
	# YOUR ANSWER
	for i in range(len(nums)):
		if target - nums[i] in nums[i+1:]:
			return [i, nums.index(target - nums[i], i + 1)]
	return []