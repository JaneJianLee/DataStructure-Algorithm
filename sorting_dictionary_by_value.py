class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        result_dic = dict()
        
        for i in range(len(points)):
            value = (points[i][0])**2 + (points[i][1])**2
            result_dic[tuple(points[i])] = value
        
        print("result dic:",result_dic)
        sorted_dic = sorted(result_dic.items(), key = lambda kv:kv[1])
        result=list(map(lambda x:list(x[0]), sorted_dic))
        print("last output:",result)
        return result[0:K]