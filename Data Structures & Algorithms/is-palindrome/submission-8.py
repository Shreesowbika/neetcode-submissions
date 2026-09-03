class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_low= "".join(char for char in s.lower() if char.isalnum())

        for i in range(0,len(s_low)//2):
            if s_low[i]!=s_low[len(s_low)-i-1]:
                return False
        return True


        