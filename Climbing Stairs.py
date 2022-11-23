# https://leetcode.com/problems/climbing-stairs/description/

94.8% https://leetcode.com/problems/climbing-stairs/submissions/847403233/

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1,1]

        for i in range(2,n+1):
            dp.append(dp[i-1] + dp[i-2]) 
        return dp[-1]
