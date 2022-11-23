# https://leetcode.com/problems/valid-parentheses/description/

# Faster than 91.39% (https://leetcode.com/problems/valid-parentheses/submissions/840609552/)

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """  
        myList = []  

        for i in s:
            if(i == '(' or i == '[' or i =='{'):
                myList.append(i)
            if(i == ')'):
                try:
                    if(myList.pop() != '('):
                        return False
                except:
                    return False
            if(i == ']'):
                try:
                    if(myList.pop() != '['):
                        return False
                except:
                    return False
            if(i == '}'):
                try:
                    if(myList.pop() != '{'):
                        return False
                except:
                    return False                    
        if(len(myList) != 0):
            return False
        return True
