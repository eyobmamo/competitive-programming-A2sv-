class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        
        x,y=start,destination
        def distances(x,y):
            forward_d=0
            total=sum(distance)
            for pos in range(x,y):
                forward_d +=distance[pos]
            if forward_d<(total-forward_d):
                return forward_d
            else:
                return total-forward_d
        if start<destination:
            return distances(x,y)
        else:
            return distances(y,x)       
        