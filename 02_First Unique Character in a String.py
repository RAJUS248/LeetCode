class Solution(object):
    def firstUniqChar(self, s):

        freq = {}
        for chr in s:
            if chr in freq:
                freq[chr] += 1

            else:
                freq[chr] = 1

        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i
                
        
        return -1      





        
        
