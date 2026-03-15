class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range (self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key :
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        hash = self.get_hash(key)

        if self.arr[hash] is None:
            return 'No element found'

        if self.arr[hash][0] == key:
            return self.arr[hash][1]
        
        found = False
        itr = hash + 1
        while itr != hash:
            if itr >= self.MAX:
                itr = 0

            if self.arr[itr][0] == key:
                found = True
                return self.arr[itr][1]
        
            itr = itr + 1
        if not found:
            return 'No element found'

    
    def __setitem__(self, key, value):
        hash = self.get_hash(key)
        found = False
        
        if self.arr[hash] == key:
            self.arr[hash] = (key, value)
            found = True

        if not found:
            while hash != None:
                if hash >= self.MAX:
                    hash = 0
                
                if self.arr[hash] is None:
                    self.arr[hash] = (key, value)
                    return
                
                hash += 1
                
            

    def __delitem__(self, key):
        hash = self.get_hash(key)

        if self.arr[hash] is None:
            return 'There was no element at all!'
        
        if self.arr[hash][0] == key:
            self.arr[hash] = None
            return 'Deleted Successfully!'
        
        elif self.arr[hash][0] != key:
            itr = hash+1
            while itr != hash:
                if itr >= self.MAX:
                    itr = 0
                
                if self.arr[itr] is None:
                    pass

                elif self.arr[itr][0] == key:
                    self.arr[itr] = None
                    return 'Deleted Successfully!'
                
                itr += 1
            

if __name__ == '__main__':
    hm = HashTable()

    hm["One"] = 1
    hm["Two"] = 2
    hm["march 6"] = 108
    hm["march 17"] = 111


    print(hm['One'])
    print(hm['Two'])
    print(hm['hh'])
    print(hm.arr)

    print(hm["march 17"])
    print(hm.get_hash('march 17'))

    del hm['One']
    del hm['march 17']
    print(hm.arr)