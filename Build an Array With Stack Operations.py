class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        # continue while len(stack) != len(target)
        # make a res array
        # make a pointer to first elem in target once n == pointer add

        res = []
        i = 0

        for curr in range(1, n+1):
            if curr == target[i]:
                res.append("Push")
                i += 1
            else:
                res.append("Push")
                res.append("Pop")
            if i == len(target): return res
