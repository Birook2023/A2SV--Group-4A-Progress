class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.is_word = True
        
    def search(self, word: str) -> bool:
        def dfs(node, word):
            if not word:
                return node.is_word

            char = word[0]
            if char == ".":
                for child in node.children.values():
                    if dfs(child, word[1:]):
                        return True
                return False

            if char not in node.children:
                return False
            
            return dfs(node.children[char], word[1:])
        
        return dfs(self.root, word)
