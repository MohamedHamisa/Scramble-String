class Solution:
    def __init__(self):
        self.map = {}
    def isScramble(self, s1: str, s2: str):
        if (s1, s2) in self.map:
            return self.map[(s1, s2)]
        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            self.map[(s1, s2)] = False
            return False
        length = len(s1)
        if s1 == s2:
            self.map[(s1, s2)] = True
            return True
        for i in range(1, length):
            if self.isScramble(s1[i:], s2[i:]) and self.isScramble(s1[:i], s2[:i]):
                return True
            if self.isScramble(s1[:-i], s2[i:]) and self.isScramble(s1[-i:], s2[:i]):
                return True
        self.map[(s1, s2)] = False
        return False



