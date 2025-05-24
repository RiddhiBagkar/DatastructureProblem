class Solution(object):
    def areOccurrencesEqual(self, s):
        occur_count={}
        for i in range(len(s)):
            if s[i] not in occur_count:
                occur_count[s[i]]=1
            
            else:
                occur_count[s[i]]+=1
        
        all_values_same=len(set(occur_count.values())) ==1 

        return all_values_same


strr="abcab"
s1=Solution()
print(s1.areOccurrencesEqual(strr))