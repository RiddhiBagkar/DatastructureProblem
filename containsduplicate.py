class Solution(object):
    def containsDuplicate(self, nums):
        number=set()
        for num in nums:
            if num in number:
                return True
            number.add(num)
        return False

nums=[1,2,4,5]
s1=Solution()
print(s1.containsDuplicate(nums))