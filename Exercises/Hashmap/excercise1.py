"""
nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
What was the average temperature in first week of Jan
What was the maximum temperature in first 10 days of Jan
Figure out data structure that is best for this problem
"""

"""I am using Hash table for my practice...
Note: Dictonary is the python specific implementation of hashmap/hashtable
"""

class Hashtable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range (self.MAX)]
    
    def get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.MAX

    def __setitem__(self, key, value):
        hash = self.get_hash(key)
        found = False

        for index, element in enumerate(self.arr[hash]):
            if len(element) == 2 and element[0] == key:
                self.arr[hash][index] = (key, value)
                found = True

        if not found:
            self.arr[hash].append((key, value))

    def __getitem__(self, key):
        hash = self.get_hash(key)
        for element in self.arr[hash]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        hash = self.get_hash(key)
        for index, element in enumerate(self.arr[hash]):
            if element[0] == key:
                del self.arr[hash][index]
                return
    

data = Hashtable()
with open('nyc_weather.csv', 'r') as f:
    for line in f:
        tokens = line.split(',')
        # print(tokens)
        data [tokens[0]] = float(tokens[1])


day = 1
average_temp = 0
max_temp = 0
while day != 11:
    if day<8:
        average_temp += data[f'Jan {day}']
    
    if data[f'Jan {day}'] > max_temp:
        max_temp = data[f'Jan {day}']

    day +=1
average_temp /= 7

print(f'Average temperature in the first week of the Jan month is: {average_temp}')

print(f'Max temp is {max_temp}')

print(f'The temp on Jan 9 is:  {data['Jan 9']}')
print(f'The temp on Jan 4 is:  {data['Jan 4']}')