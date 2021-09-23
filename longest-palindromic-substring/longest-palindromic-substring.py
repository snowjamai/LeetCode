class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_str = ""
        
        for i in range(len(s)):
            for j in range(i + 1,len(s) + 1):
                if j - i <= len(max_str):
                    continue
                tmp_str = s[i:j]
                r_str = tmp_str[::-1]
                if tmp_str == r_str and len(max_str) < len(tmp_str):
                    max_str = tmp_str
        if len(s) == 1:
            return s
        return max_str