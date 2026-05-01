class MyHashMap:

    def __init__(self):
        self.data=[]

    def put(self, key: int, value: int) -> None:
            f=0
            l=len(self.data)
            for i  in range(l):
                if self.data[i][0]==key:
                    self.data[i][1]=value 
                    f=1
            if f==0:
                self.data.append([key,value])

    def get(self, key: int) -> int:
            f=0

            l=len(self.data)
            for i in range(l):
                if self.data[i][0]==key:
                    return self.data[i][1]
                    f=1
            if f==0:
                return -1
        

    def remove(self, key: int) -> None:
            #l=len(self.data)
            for i in self.data:
                if i[0]==key:
                    self.data.remove(i)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)