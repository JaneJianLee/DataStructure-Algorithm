class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        digit=[]
        letter=[]
        
        for x in logs:
            if x.split()[1].isdigit():
                digit.append(x)
            else:
                letter.append(x)
        letter.sort(key= lambda x : x.split()[0])
        letter.sort(key= lambda x : x.split()[1:])
        return letter+digit