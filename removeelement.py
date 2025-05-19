class Solution(object):
    def removeElement(self, nums, val):
        k = 0  # Pointer for next position to keep
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

nums=[4,3,2,6,2,4,7]
val=2
s1=Solution()
print(s1.removeElement(nums,val))