class Solution(object):
    def searchInsert(self, nums, target):
        # Search for target
        for i in range(len(nums)):
            if nums[i] == target:
                return i

        # If not found, find the insert position
        insert_index = 0
        while insert_index < len(nums) and nums[insert_index] < target:
            insert_index += 1
        return insert_index
    
nums=[1,2,4,7,9]
target=5
s1=Solution()
print(s1.searchInsert(nums,target))