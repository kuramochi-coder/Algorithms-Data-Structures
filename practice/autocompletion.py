class Node:
    def __init__(self, isWord, children):
        self.isWord = isWord
        self.children = children

class Solution:
    def build(self, words):
        trie = Node(False, {})

        for word in words:
            curr = trie
            for char in word:
                if char not in curr.children:
                    curr.children[char] = Node(False, {})
                curr = curr.children[char]
            curr.isWord = True
        self.trie = trie
    
    def autocomplete(self, word):
        curr = self.trie

        for char in word:
            if char not in curr.children:
                return []
            curr = curr.children[char]

        words = []
        # self.dfs(curr, word, words)
        self.dfsIterative(curr, word, words)
        return words

    def dfs(self, node, prefix, words):
        if node.isWord:
            words.append(prefix)

        for char in node.children:
            self.dfs(node.children[char], prefix+char, words)

    def dfsIterative(self, node, prefix, words):
        stack = [(node, prefix)]

        while stack:
            curr, prefix = stack.pop()

            if curr.isWord:
                words.append(prefix)
            
            for char in curr.children:
                stack.append((curr.children[char], prefix+char))

s = Solution()
s.build(['dog', 'dark', 'cat', 'door', 'dodge'])
print(s.autocomplete('do'))
# ['dog', 'door', 'dodge']