class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        i = 1  # write pointer

        for j in range(1, len(nums)):
            if nums[j] != nums[j - 1]:
                nums[i] = nums[j]
                i += 1

        return i
nums=[1,1,2,3,3,4,4]
s1=Solution()
print(s1.removeDuplicates(nums))
