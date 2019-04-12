# 3. longest substring without repeating characterse
# input : "abcabcbb"


    
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = []  # memory for storing characters
        l = 0   # the longest length ever
        for c in s:                       
            if c in m:
                l = max(l, len(m))
                m = m[m.index(c)+1:]
            m.append(c)
        return max(l, len(m))
