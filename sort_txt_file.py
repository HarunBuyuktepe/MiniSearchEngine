# Python3 program to demonstrate auto-complete  
# feature using Trie data structure. 
# Note: This is a basic implementation of Trie 
# and not the most optimized one.
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

        # Forms a trie structure with the given set of strings 
        # if it does not exists already else it merges the key 
        # into it by extending the structure as required 
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

        # Searches the given key in trie for a full match 
        # and returns True on success else returns False. 
        node = self.root
        found = True

        for a in list(key):
            if not node.children.get(a):
                found = False
                break

            node = node.children[a]

        return node and node.last and found

    def suggestionsRec(self, node, word):

        # Method to recursively traverse the trie 
        # and return a whole word.  
        if node.last:
            self.word_list.append(word)

        for a, n in node.children.items():
            self.suggestionsRec(n, word + a)

    def printAutoSuggestions(self, key, trie_path):

        # Returns all the words in the trie whose common 
        # prefix is the given key thus listing out all  
        # the suggestions for autocomplete. 
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
        self.suggestionsRec(node, temp_word)
        print("Found words : ", self.word_list)
        for s in self.word_list:

            self.get_position(word=s,trie_path=trie_path)
            print()
        return 1

    def get_position(self,word,trie_path):
        print("Position of the \" ",word,"\" in the File ",trie_path)
        text = open(trie_path, "r")
        i = 1
        for line in text:
            line = re.sub("[,.]", "", line)
            line = line.lower()
            if word in line:
                print("Index of first character : ",line.index(word) ," Line of the word : ",i)
            i = i+1


def oku():
    # Open the file in read mode
    text = open("file1.txt", "r")

    # Create an empty dictionary
    d = dict()

    # Loop through each line of the file
    for line in text:
        # Remove the leading spaces and newline character
        line = line.strip()
        line = re.sub("[,.]", "", line)

        # Convert the characters in line to
        # lowercase to avoid case mismatch
        line = line.lower()

        # Split the line into words
        words = line.split(" ")

        # Iterate over each word in line
        for word in words:
            # Check if the word is already in dictionary
            if word in d:
                # Increment count of word by 1
                d[word] = d[word] + 1
            else:
                # Add the word to dictionary with count 1
                d[word] = 1

    words=[]
    # Print the contents of dictionary
    # print(d.keys())
    for key in list(d.keys()):
        # print(key, ":", d[key])
        words.append(key)
    # print(words)
    return words
#
#
# # Driver Code
# keys = oku()
# key = "adipiscingf"  # key for autocomplete suggestions.
#
# # creating trie object
# t = Trie()
#
# # creating the trie structure with the
# # given set of strings.
# t.formTrie(keys)
#
# # autocompleting the given key using
# # our trie structure.
# comp = t.printAutoSuggestions(key,trie_path)
#
# if comp == 0:
#     print("No string found with this prefix\n")


