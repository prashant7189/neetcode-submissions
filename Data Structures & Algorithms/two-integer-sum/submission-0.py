class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_list = {}
        dict_list[target-nums[0]] = 0

        for i in range(1, len(nums)):
            if nums[i] in dict_list.keys():
                return [dict_list.get(nums[i]), i]
            dict_list[target-nums[i]] = i


        