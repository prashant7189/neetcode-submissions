class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_list = {}
        dict_list[target - nums[0]] = 0
        for index in range (1, len(nums)):
            if nums[index] in dict_list.keys():
                return [dict_list.get(nums[index]), index]
            dict_list[target-nums[index]] = index



        