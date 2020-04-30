# import  re
# def oku(path):
#     # Open the file in read mode
#     text = open(path, "r")
#
#     # Create an empty dictionary
#     d = dict()
#
#     # Loop through each line of the file
#     for line in text:
#         # Remove the leading spaces and newline character
#         line = line.strip()
#         line = re.sub("[,.]", "", line)
#
#         # Convert the characters in line to
#         # lowercase to avoid case mismatch
#         line = line.lower()
#
#         # Split the line into words
#         words = line.split(" ")
#
#         # Iterate over each word in line
#         for word in words:
#             # Check if the word is already in dictionary
#             if word in d:
#                 # Increment count of word by 1
#                 d[word] = d[word] + 1
#             else:
#                 # Add the word to dictionary with count 1
#                 d[word] = 1
#
#     words=[]
#     # Print the contents of dictionary
#     # print(d.keys())
#     for key in list(d.keys()):
#         # print(key, ":", d[key])
#         words.append(key)
#     # print(words)
#     return words
#
#
#
#
# import os
#
# file_list = []
# for file in os.listdir("./"):
#     if file.endswith(".txt"):
#         file_list.append(file)
#         print(os.path.join("./", file))
#
# print(file_list)
# t=oku(file_list[0])
# print(t)
#

list = [1, 2, 3, 1]
while 1 in list:
    list.remove(1) # [2, 3, 1]
print(list)
