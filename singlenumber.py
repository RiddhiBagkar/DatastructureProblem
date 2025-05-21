class Solution(object):
    def singleNumber(self, nums):
       number=0
       for num in nums:
        number ^= num
       return number
    

nums=[4,1,2,1,2]    
s1=Solution()
print(s1.singleNumber(nums))