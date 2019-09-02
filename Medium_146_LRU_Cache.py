class LRUCache:

    def __init__(self, capacity: int):
        self.capa = capacity
        self.dict = {}
    
    def put(self, key: int, value: int) -> None:
        
        if key in self.dict:
            del self.dict[key]
            self.dict[key]=value
            return None
        
        if len(self.dict) == self.capa:
            first_key = list(self.dict)[0]
            del self.dict[first_key]
            self.dict[key]=value
        else:
            self.dict[key]=value
            
    def get(self, key: int) -> int:
        if key in self.dict:
            val=self.dict[key]
            del self.dict[key]
            self.dict[key]=val
            return val
        return -1

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)