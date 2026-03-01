class PoemHashtable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range (self.MAX)]


    def get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        
        return hash % self.MAX


    def __setitem__(self, key, value):
        hash = self.get_hash(key)
        found = False
        
        for idx, element in enumerate(self.arr[hash]):
            if len(element) and element[0] == key:
                self.arr[hash][idx] = (key, element[1]+value)
                found = True

        if not found:
            self.arr[hash].append((key, value))

    def __getitem__(self, key):
        hash = self.get_hash(key)
        
        for element in self.arr[hash]:
            if element[0] == str(key):
                return element[1]
            
    def __delitem__(self, key):
        hash = self.get_hash(key)

        for idx, element in enumerate(self.arr[hash]):
            if element[0] ==  key:
                del self.arr[hash][idx]
                return
    

data = PoemHashtable()

with open('poem.txt', 'r') as f:
    for line in f:
        words = line.strip().split(" ")
        for word in words:
            word = word.strip(",.;:!-— ").lower()
            data[word] = 1
    
for elements in data.arr:
    for element in elements:
        if element:
            print(f"'{element[0]}':{element[1]}")