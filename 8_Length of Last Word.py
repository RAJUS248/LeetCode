class Solution(object):
    def lengthOfLastWord(self, s):

        i = len(s) - 1

        lenth = 0

        while i >= 0 and s[i] == " ":
            i -= 1

        while i >= 0 and s[i] != " ": 
            lenth += 1
            i -= 1

        return lenth

"""
        words = s.split()

        return len(words[-1])

"""
        
