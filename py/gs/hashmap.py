class hashmap():
    # assume k is all string
    def __init__(self,size=256):
        self.arr = [[] for i in range(0,size)]
        self.size = size
        pass
    
    def put(self, k, v):
        index = self.hash(k) % self.size
        bucket = self.arr[index]
        existIndex = -1
        for i in range(0, len(bucket)):
            if bucket[i][0] == k:
                existIndex = i
        if existIndex > -1:
            bucket[existIndex] = (k, v)
            print("bucket after updating value:"+str(bucket))
        else:
            bucket.append((k,v))
            print("bucket after putting new value:"+str(bucket))
        return index
    
    def get(self, k):
        index = self.hash(k) % self.size
        bucket = self.arr[index]
        for e in bucket:
            if e[0]==k:
                return e[1]
        print("the key doesn't exist!")
        return None

    def hash(self, k):
        h = 7
        for i in range(0, len(k)):
            h = h * 31 + ord(k[i])
        return h
    
    def resize(self, n=2):
        pass
    
test = hashmap()
test.put("vincent", 24)
test.put("yilia", 24)
test.put("maqiu", 1)
print(test.get("vincent"))
print(test.get("maqiu"))
test.put("vincent", 25)
print(test.get("vincent"))