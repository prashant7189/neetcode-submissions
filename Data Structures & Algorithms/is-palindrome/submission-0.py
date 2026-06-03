class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_condensed = ""
        for i in range (len(s)):
            if s[i].isalnum():
                s_condensed += s[i].lower()
        
        return s_condensed == s_condensed[::-1]

        