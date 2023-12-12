class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ball_move=[]
        length=len(boxes)
        for i in range(length):
            box_opr=0
            for j in range(length):
                if boxes[j]=="1":
                    box_opr+=abs(i-j)
            ball_move.append(box_opr)
        return ball_move            


        