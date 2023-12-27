import sys;
import os

tab = '    '

def mapper(filename):
    file = open(filename,'r')
    for line in file.readlines():
         words = line.rstrip(' ').split(' ')
         for word in words:
               if '\n' in word:
                    word = word.rstrip("\n")
               print(f'{word}{tab}{filename.split("/")[-1]}')
               
    

def main():
    path = sys.argv[1]
    files = os.listdir(path)
    
    for file in files:
         mapper('../input' + '/' + file)


main()

