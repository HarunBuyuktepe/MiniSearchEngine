from pip._vendor.distlib.compat import raw_input
import os
path = ""

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
        print("Tries are constructed ...")

        # get key
        key = raw_input("Enter the path please : ")

        #search in tries




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


        file_list = []
        for file in os.listdir("./"):
            if file.endswith(".txt"):
                file_list.append(file)
                # print(os.path.join("./", file))
        print("Files in your work path is \n", file_list)

        selected_files = []
        while len(selected_files)<2:
            key = raw_input("Enter the file name please : ")
            selected_files = key.split(" ")
            print("selected files",selected_files)
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