# https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution(object):
    def maxProduct(self, words):
        def sameChars(w1,w2):
            for i in w1:
                if(i in w2):
                    return False
            return True

        maxlen = 0
        n=len(words)
        for i in range(n):
            for j in range(i+1,n):
                x = len(words[i]) * len(words[j])
                if(x <= maxlen):
                    continue

                if(sameChars(words[i],words[j])):
                    maxlen = x


        return maxlen


