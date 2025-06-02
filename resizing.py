class HashMap:
    def insert(self, key, value):
        self.resize()
        index = self.key_to_index(key)
        self.hashmap[index] = (key, value)

    def resize(self):
        if len(self.hashmap) == 0:
            self.hashmap = [None]
            return
        if self.current_load() < 0.05:
            return
        temp = self.hashmap
        self.hashmap = [None] * (len(temp) * 10)
        for item in temp:
            if item is not None:
                index = self.key_to_index(item[0])
                self.hashmap[index] = (item[0], item[1])

    def current_load(self):
        if len(self.hashmap) == 0:
            return 1
        total = 0
        for i in self.hashmap:
            if i is not None:
                total += 1
        return total / len(self.hashmap)

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final
