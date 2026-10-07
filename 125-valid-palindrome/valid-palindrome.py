class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=len(s)
        s_="".join(c for c in s if c.isalnum())
        s_=s_.lower()
        return s_[:]==s_[::-1]
