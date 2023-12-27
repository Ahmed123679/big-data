import sys;
import os

def mapper(filename):
    file = open(filename,'r')
    for line in file.readlines():
         words = line.split(' ')
         for word in words:
               if '\n' in word:
                    word = word.rstrip("\n")
               print(f'{word}\t{filename.split("/")[-1]}')
               
    

def main():
    mapper(os.environ['map_input_file'])


main()

