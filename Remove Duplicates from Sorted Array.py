# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

# Faster than 77.25% https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/846216814/
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        try:
            for i in range(len(nums)-1):
                while(nums[i] == nums[i+1]):
                    nums.pop(i)
        except:
            return
        
