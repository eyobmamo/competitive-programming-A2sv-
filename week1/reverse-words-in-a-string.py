class Solution:
    def reverseWords(self, s: str) -> str:
        words=([word for word in reversed(s.split()) if word ])

        return " ".join(words)


        