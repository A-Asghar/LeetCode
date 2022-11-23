# https://leetcode.com/problems/longest-common-prefix/

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        s = ""
        same = True
        for i in range(len(strs[0])):
            for j in strs:
                try:
                    if(j[i] != strs[0][i]):
                        same = False
                        break
                except:
                    return s
            if(same):
                s= s+strs[0][i]
        return s
