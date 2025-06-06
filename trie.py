class Trie:
    def add(self, word):
        current_level = self.root
        for char in word:
            if char not in current_level:
                current_level[char] = {}
            current_level = current_level[char]
        current_level[self.end_symbol] = True
    
    def exists(self, word):
        current = self.root
        for char in word:
            if char not in current:
                return False
            current = current[char]
        if self.end_symbol in current:
            return True
        return False
                       

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"
