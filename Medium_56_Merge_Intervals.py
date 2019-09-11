class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        #Case 1 : No input:
        if intervals==[]:
            return intervals
        
        head = intervals[0][0]
        tail = intervals[0][1]
        
        for x in intervals:
            #print(x,x[0],x[1],head,tail)
            if x[0] < head:
                head = x[0]
            if x[1] > tail:
                tail = x[1]                
  
        return [[head,tail]]