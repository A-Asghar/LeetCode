# https://leetcode.com/problems/grumpy-bookstore-owner/

class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        '''
        1. loop over customers to locate all satisfied customers when the grumpy for that index is 0.
        2. In the customer array, set the satisfied customers count to zero.
        3. use sliding window with window size of minutes and add the sum with not grumpy sum, if greater than totalSum then update it
        '''


        notGrumpySum = 0
        totalSum = 0
        n=len(grumpy)
        
        for i in range(n):
            if(grumpy[i] == 0):
                notGrumpySum+=customers[i]
                customers[i] = 0
        
        for i in range(n):
            if(i+minutes > n):
                break
            total = sum(customers[i:i+minutes]) + notGrumpySum
            if(total > totalSum):
                totalSum = total

        return totalSum
