class Trie:
    def advanced_find_matches(self, document, variations):
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                ch = document[j]
                if ch in variations:
                    ch = variations[ch]
                if ch not in level:
                    break
                level = level[ch]
                if self.end_symbol in level:
                    matches.add(document[i : j + 1])
        return matches

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
    
    def longest_common_prefix(self):
        current = self.root
        prefix = ""
        while True:
            if self.end_symbol in current:
                break
            cur = list(current.keys())
            if len(cur) == 1:
                prefix += cur[0]
                current = current[cur[0]]
            else:
                break
        return prefix       

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"
