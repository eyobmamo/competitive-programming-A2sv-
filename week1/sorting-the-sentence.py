class Solution:
    def sortSentence(self, s: str) -> str:
        new_s=s.split()
        new_s.sort(key=lambda x:x[-1])
        return " ".join(word[:-1] for word in new_s)    
       

        