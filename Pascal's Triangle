# https://leetcode.com/problems/pascals-triangle/description/

# 88.30% https://leetcode.com/problems/pascals-triangle/submissions/848048349/

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1],[1,1]]
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return res
        else:
            for i in range(2,numRows):
                l = []
                for j in range(i+1):
                    if(j==0 or j==i):
                        l.append(1)
                    else:
                        l.append(res[i-1][j-1] + res[i-1][j])
                res.append(l)
        return res
