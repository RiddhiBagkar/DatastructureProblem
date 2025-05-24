class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        for i,char in enumerate(strs[0]):
            for words in strs[1:]:
                if i >= len(words) or words[i] != char:
                    return strs[0][:i]
            
        return strs[0]
    
lis=['flower','flower','flower']
s1=Solution()
print(s1.longestCommonPrefix(lis))