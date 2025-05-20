class Solution(object):
    def plusOne(self, digits):
        n = len(digits)
        
        # Start from the last digit
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
                
            else:
                digits[i] = 0
        
        # If all digits were 9, then add 1 at front
        digits.insert(0, 1)
        return digits
    
digits = [2, 2, 9]
s1 = Solution()
print(s1.plusOne(digits))