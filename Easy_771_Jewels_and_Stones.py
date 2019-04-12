#771. Jewels and Stones


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        num=0
        for cha in J:
            num+=S.count(cha)
        return num
