class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        v = [-1] * (n + 1)
        for num in nums:
            v[num] = num
        for i in range(len(v)):
            if v[i] == -1:
                return i

        return 0

nums=[3,0,1,4]
s1=Solution()
print(s1.missingNumber(nums))