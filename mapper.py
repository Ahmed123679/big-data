import sys;
import os

tab = '    '

def mapper(filename):
    file = open(filename,'r')   # delete this line when using hadoop
    for line in file.readlines():  # for line in sys.stdin
         words = line.strip().split(' ')
         for word in words:
               
               print(f'{word}{tab}{filename.split("/")[-1]}')
               
    

def main():
    
    path = sys.argv[1]
    files = os.listdir(path)
    
    for file in files:
         mapper('../input' + '/' + file)

      # main when using hadoop 
         # only has this line
         # mapper(os.environ['map_input_file'])


main()

