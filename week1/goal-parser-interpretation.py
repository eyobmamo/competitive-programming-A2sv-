class Solution:
    def interpret(self, command: str) -> str:
        c=0
        encript=""
        while c<len(command):
            if command[c]=="G":
                c+=1
                encript += "G"
            elif command[c:c+2]=="()":
                c+=2
                encript += "o"
            elif command[c:c+4]=="(al)":
                c+=4
                encript += 'al'
            else:
                return ""    
        return encript                


        