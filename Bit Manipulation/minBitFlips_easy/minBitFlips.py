class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        set_bits = start ^ goal
        c=0
        while set_bits:
            set_bits = set_bits & (set_bits-1)
            c+=1
        return c