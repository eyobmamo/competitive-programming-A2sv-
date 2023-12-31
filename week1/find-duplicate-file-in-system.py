from typing import List

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        lst = []
        for i in range(len(paths)):
            l = paths[i] = paths[i].split()
            l = l[1:]
            for j in range(len(l)):
                l[j] = l[j][l[j].index('('):]
            lst.extend(l)

        new = []
        for contents in set(lst):
            if lst.count(contents) > 1:
                n = []
                for i in paths:
                    for j in i[1:]:
                        if contents in j:
                            j = j.replace(contents, '')
                            n.append(i[0] + '/' + j)
                new.append(n)

        return new
