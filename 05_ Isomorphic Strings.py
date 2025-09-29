class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        s1 = {}
        s2 = {}

        for ch1,ch2 in zip(s,t):
            if ch1 in s1 and s1[ch1] != ch2:
                return False

            if ch2 in s2 and s2[ch2] != ch1:
                return False

            s1[ch1] = ch2
            s2[ch2] = ch1

        return True
        
