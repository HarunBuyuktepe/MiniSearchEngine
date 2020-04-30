import re

class TrieNode():
    def __init__(self):
        # Initialising one node for trie
        self.children = {}
        self.last = False


class Trie():
    def __init__(self):

        # Initialising the trie structure. 
        self.root = TrieNode()
        self.word_list = []

    def formTrie(self, keys):
        for key in keys:
            self.insert(key)  # inserting one key to the trie.

    def insert(self, key):

        # Inserts a key into trie if it does not exist already. 
        # And if the key is a prefix of the trie node, just  
        # marks it as leaf node. 
        node = self.root

        for a in list(key):
            if not node.children.get(a):
                node.children[a] = TrieNode()

            node = node.children[a]

        node.last = True

    def search(self, key):
        node = self.root
        found = True

        for a in list(key):
            if not node.children.get(a):
                found = False
                break

            node = node.children[a]

        return node and node.last and found

    def getAll(self, node, word):
        if node.last:
            self.word_list.append(word)

        for a, n in node.children.items():
            self.getAll(n, word + a)

    def miniEngine(self, key, trie_path):

        node = self.root
        not_found = False
        temp_word = ''

        for a in list(key):
            if not node.children.get(a):
                not_found = True
                break

            temp_word += a
            node = node.children[a]

        if not_found:
            return 0

        print("Result in ", trie_path)
        self.getAll(node, temp_word)
        print("Found words : ", self.word_list)
        for s in self.word_list:

            self.get_position(word=s,trie_path=trie_path)
            print()
        return 1

    def get_position(self,word,trie_path):
        # Get the position of the word
        # from selected file location
        print("Position of the \" ",word,"\" in the File ",trie_path)
        text = open(trie_path, "r")
        i = 1
        for line in text:
            line = re.sub("[,.]", "", line)
            line = line.lower()
            if word in line:
                print("Index of first character : ",line.index(word) ," Line of the word : ",i)
            i = i+1
