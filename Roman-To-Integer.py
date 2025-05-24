class Solution(object):
    def romanToInt(self, s):
        roman={'I':1 ,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        SOL=0
        for i in range(len(s)-1):
            if roman[s[i]] >= roman[s[i+1]] :
               SOL += roman[s[i]]
            else:

                SOL -= roman[s[i]]
        SOL += roman[s[-1]]         
        return SOL

s=input("ENTER ROMAN LETTER::").upper()
s11=Solution()
print(s11.romanToInt(s))