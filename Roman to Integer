# https://leetcode.com/problems/roman-to-integer

# Faster than 93.14% 
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        myDict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        sum = 0
        i=0
        while i < len(s):
            if(i == len(s)-1):
                sum = sum + myDict[s[i]]
                i=i+1 
            elif(myDict[s[i]] < myDict[s[i+1]] ):
                sum = sum + myDict[s[i+1]] - myDict[s[i]]
                i = i+2
            else:
                sum += myDict[s[i]]
                i = i+1
        return sum
