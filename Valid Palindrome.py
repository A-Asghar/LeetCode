# https://leetcode.com/problems/valid-palindrome/description/
# 93.77% https://leetcode.com/problems/valid-palindrome/submissions/883631507/

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join([c for c in s if c.isalnum()]).lower()
        return s == s[::-1]
