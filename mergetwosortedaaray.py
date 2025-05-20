class Solution(object):
    
    def merge(self,nums1,m,nums2,n):
      i = m - 1
      j = n - 1
      k = m + n - 1

      while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

        # If anything is left in nums2
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

           
nums1=[1,2,3,0,0,0]
nums2=[2,5,6]
m=3
n=len(nums2)
s1=Solution()
s1.merge(nums1,m,nums2,n)
print(nums1)