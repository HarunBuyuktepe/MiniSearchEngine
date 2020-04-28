import argparse

def oku(path):
    print(path)

ap = argparse.ArgumentParser()
ap.add_argument('-path', '-p', required=True, help='Enter the file path')
arg_val = vars(ap.parse_args())

oku(path=arg_val['query'])