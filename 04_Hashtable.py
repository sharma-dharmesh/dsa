class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range (self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key :
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        hash = self.get_hash(key)
        for element in self.arr[hash]:
            if element[0] == key:
                return element[1]
    
    def __setitem__(self, key, value):
        hash = self.get_hash(key)
        found = False

        for idx, element in enumerate(self.arr[hash]):
            if len(element) == 2 and element == key:
                self.arr[hash][idx] = (key, value)
                found = True

        if not found:
            self.arr[hash].append((key, value))

    def __delitem__(self, key):
        hash = self.get_hash(key)
        for idx, element in enumerate(self.arr[hash]):
            if element[0] == key:
                del self.arr[hash][idx]


hm = HashTable()
hm["One"] = 1
hm["Two"] = 2
hm["march 6"] = 108
hm["march 17"] = 111


print(hm['One'])
print(hm['Two'])
print(hm.arr)

print(hm["march 17"])

del hm['One']
del hm['march 17']
print(hm.arr)