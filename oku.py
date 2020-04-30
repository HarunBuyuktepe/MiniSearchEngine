from pip._vendor.distlib.compat import raw_input
import os
import trie as trie_lib
import re
path = ""
file_list = []

def getFiles(path):
    file_list.clear()
    for file in os.listdir(path):
        if file.endswith(".txt"):
            file_list.append(file)
            # print(os.path.join("./", file))

def getWords(path):
    # Open the file in read mode
    text = open(path, "r")

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

def starter(path):
    x = raw_input('Enter your choice '
                  '\n1.Search key in file which existed at selected path \n2.Common word(s) in selected files'
                  '\n3.Change the path '
                  '\n0.Exit\n')
    x = int(x)
    if x == 1:
        if path == "":
            get_path = raw_input("Enter the path please : ")
            for i in path:
                if i =='\"' or i=='\'':
                    print("Please do not use quotes")
                    starter(path)
            path = get_path
        getFiles(path)

        print("Tries are constructing ...")
        # contruct tries
        tries = []
        for i in range(len(file_list)):
            trie = trie_lib.Trie()
            keys = getWords(file_list[i])
            trie.formTrie(keys)
            tries.append(trie)
        print("Tries are constructed ...")

        # get key
        key = raw_input("Enter the key please : ")
        key = key.lower()
        #search in tries
        print()
        for i in range(len(tries)):
            tries[i].miniEngine(key,path+file_list[i])

        starter(path)
    elif x == 2:
        print("common")
        if path == "":
            get_path = raw_input("Enter the path please : ")
            for i in path:
                if i == '\"' or i == '\'':
                    print("Please do not use quotes")
                    starter(path)
            path = get_path
        getFiles(path)
        # get selected file
        print("Files in your work path is \n", file_list)
        selected_files = []
        while len(selected_files)<2:
            key = raw_input("\nWrite name of the files, to compare all just write ALL\nEnter the file name please : ")
            if key == "ALL":
                selected_files = file_list
                break
            selected_files = key.split(" ")
            for i in range(len(selected_files)):
                if ".txt" not in selected_files[i]:
                    selected_files[i] = selected_files[i] + ".txt"
            if len(selected_files)<2:
                print("Please enter more than 1 txt file")
                print("Files in your work path is \n", file_list)
            for i in selected_files:
                if i not in file_list:
                    print("Please select current files or change your path")
                    print("Files in your work path is \n", file_list)

        # trieleri oluştur ortakları arat
        tries = []
        for i in range(len(selected_files)):
            trie = trie_lib.Trie()
            keys = getWords(selected_files[i])
            trie.formTrie(keys)
            tries.append(trie)
        print("Tries are constructed ...")

        # search in tries
        print()
        common_words = []
        keys = getWords(selected_files[1])
        for key in keys:
            if tries[0].search(key):
                common_words.append(key)
        if len(selected_files)>2:
            for i in range(2,len(selected_files)):
                for key in common_words:
                    if not tries[i].search(key):
                        # print(common_words)
                        while key in common_words:
                            common_words.remove(key)

        print("Common word of selected files \n",common_words)
        starter(path)

    elif x == 3:
        print("path")
        get_path = raw_input("Enter the path please : ")
        for i in path:
            if i == '\"' or i == '\'':
                print("Please do not use quotes")
                starter(path)
        path = get_path
        starter(path)
    elif x == 0:
        return
    else:
        print("You are missing or incorrectly dialed")
        starter(path)

if __name__ == "__main__":
    starter(path)

