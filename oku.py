from pip._vendor.distlib.compat import raw_input
import os
import sort_txt_file as trie_lib
import re
path = ""

file_list = []
for file in os.listdir("./"):
    if file.endswith(".txt"):
        file_list.append(file)
        # print(os.path.join("./", file))

def get_words(path):
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
                  '\n0.Exit\n')
    x = int(x)
    if x == 1:
        print("path")
        if path == "":
            get_path = raw_input("Enter the path please : ")
            for i in path:
                if i =='\"' or i=='\'':
                    print("Please do not use quotes")
                    starter(path)
            path = get_path


        print("Tries are constructing ...")
        # contruct tries
        tries = []

        for i in range(len(file_list)):
            trie = trie_lib.Trie()
            keys = get_words(file_list[i])
            trie.formTrie(keys)
            tries.append(trie)
        print("Tries are constructed ...")

        # get key
        key = raw_input("Enter the key please : ")
        #search in tries
        print()
        for i in range(len(tries)):
            print("Result in ",file_list[i])
            tries[i].printAutoSuggestions(key)





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

        # get selected file


        print("Files in your work path is \n", file_list)
        selected_files = []
        while len(selected_files)<2:
            key = raw_input("Enter the file name please : ")
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

        #trieleri oluştur oratkları arat








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






# arg_list = []
# arg_list=sys.argv
# # python oku.py -c [path]
# if len(arg_list)>2:
#     print(arg_list[1])
#     if str(arg_list[1] ) == "-c":
#         print(arg_list[1])
#     elif arg_list[1] == "-k":
#         print(arg_list[1])
# else:
#     print("You are missing or incorrectly dialed")