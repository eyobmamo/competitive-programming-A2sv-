class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        output=""
        for x in range(len(indices)):
            output+=s[indices.index(x)]
        return output 