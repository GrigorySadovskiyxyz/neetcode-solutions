class Solution(object):
    def isAnagram(self, s, t):
        s = sorted(s)
        t = sorted(t)
        if len(s) != len(t):
            return False
        for count, value in enumerate(s):
            if value == t[count]:
                continue
            else:
                return False
        return True
