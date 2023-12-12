class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        dis_me=abs(target[0])+abs(target[1])
        for poi_g in ghosts:
            if abs(poi_g[0]-target[0]) + abs(poi_g[1]-target[1])<=dis_me:
                return False
        return True        
            
               

        