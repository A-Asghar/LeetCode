# https://leetcode.com/problems/find-closest-number-to-zero

# Faster than 96.7% (https://leetcode.com/submissions/detail/795514978/)
class Solution(object):
    def findClosestNumber(self, nums):

        minimum = float('inf')
        k = float('-inf')

        for i in nums:
            if( abs(i)<abs(minimum) ):
                minimum = i
                k=i
            elif(abs(i)==abs(minimum) & i > minimum):
                    k = i

        return k if k>=0 else minimum
        
        
# Faster than 87.26%
class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minimum = float('inf')
        l = []

        for i in nums:
            if( abs(i)<abs(minimum) ):
                minimum = i
            elif(abs(i)==abs(minimum)):
                if(len(l)>0):
                    if(l[0]!=abs(i)):
                        del l[:]
                l.append(i)
                l.append(minimum)
                     
        return minimum if len(l) == 0 else max(l)
        
                
        
