class TrieNode(object):
    def __init__(self):
        self.children = {}

class Solution:
    def __init__(self):
        self.trie = TrieNode()
    
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=lambda x : (len(x),x))
        longest,res = 0,""
    
        for i in range(len(words)):
            length = self.make_and_search(words[i])        
            if length > longest:
                res = words[i]
            longest = max(length,longest)
        if not res:
            return ""
        return res

    def make_and_search(self,word):
        node = self.trie
        for i in range(len(word)):
            if len(word) != 1 and i != len(word)-1 and word[i] not in node.children:
                return -1
            elif word[i] not in node.children:
                node.children[word[i]] = TrieNode()
            node = node.children[word[i]]
        return len(word)
