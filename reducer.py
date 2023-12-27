import pandas as pd
import numpy as np
import sys
all_words = set()
all_files = set()
files = []
input = sys.stdin.readlines()
def reduce():

    for line in input:
        if len(line.split("\t")) == 2:
            word,filename = line.split("\t")
            all_words.add(word) # gathering all words
            all_files.add(filename[:-1]) # gathering all file names
        else:
            continue

    # creating a hash table 
    global files
    files = list(all_files)
    files.sort()

    hashTable = pd.DataFrame(np.zeros((len(all_words),len(all_files)),dtype='int16'),
                             index = list(all_words),columns = files)
    
    # print(hashTable)

    # update counts of the words in hash table
    for line in input:
        if len(line.split("\t")) == 2:
            word,filename = line.split("\t")
            hashTable.loc[word,filename[:-1]] += 1
        else:
            continue
    # print(hashTable)

    # files that contain that word
    print("============== word found in [files]===============\n")
    for word in all_words:
        matched_files = []
        for file in files:
            if(hashTable.loc[word,file] != 0):
                matched_files.append(file)
            else:
                continue
        print(word,matched_files)
    # words in aech file
    print("============== file contains [words]===============\n")
    for file in files:
        words = []
        for word in all_words:
            if(hashTable.loc[word,file] != 0):
                words.append(word)
            else:
                continue
        print(file,words)  
    
    # word and word
    print("============== word AND word in [files]===============\n")
    for firstword in all_words:
        for secondword in all_words:
            matched_files = []
            if(firstword == secondword):
                continue
            else:
                 for file in files:
                     if(hashTable.loc[firstword,file] != 0 and hashTable.loc[secondword,file] != 0):
                            matched_files.append(file)
                     else:
                            continue
                 
                 print(f'{firstword} and {secondword} found in\t{", ".join(matched_files)}') if len(matched_files) != 0 else print('',end='')
    
    # word OR word
    print("============== word OR word in [files]===============\n")
    for firstword in all_words:
        for secondword in all_words:
            matched_files = []
            if(firstword == secondword):
                continue
            else:
                 for file in files:
                     if(hashTable.loc[firstword,file] != 0 or hashTable.loc[secondword,file] != 0):
                            matched_files.append(file)
                     else:
                            continue
                 print(f'{firstword} or {secondword} found in \t{", ".join(matched_files)}') if len(files) != 0 else print('',end='')
  

    

reduce()