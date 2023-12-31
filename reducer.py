import pandas as pd
import numpy as np
import sys
all_words = set()
all_files = set()
files = []
searchWords = []
input = sys.stdin.readlines()
tab = '    '
def reduce():

    for line in input:
        if len(line.split(tab)) == 2:
            word,filename = line.split(tab)
            all_words.add(word) # gathering all words
            all_files.add(filename.strip()) # gathering all file names
        else:
            continue

    # creating a hash table 
    global files
    files = list(all_files)
    files.sort()
    global searchWords
    searchWords = list(all_words)
    searchWords.sort()

    hashTable = pd.DataFrame(np.zeros((len(all_words),len(all_files)),dtype='int16'),
                             index = searchWords,columns = files)
    
    # print(hashTable)

    # update counts of the words in hash table
    for line in input:
        if len(line.split(tab)) == 2:
            word,filename = line.split(tab)
            hashTable.loc[word,filename.strip()] += 1
        else:
            continue
    # print(hashTable)

    # files that contain that word
    print("============== word found in [files]===============\n")
    for word in searchWords:
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
        for word in searchWords:
            if(hashTable.loc[word,file] != 0):
                words.append(word)
            else:
                continue
        print(file,words)  
    
    # word and word
    print("============== word AND word in [files]===============\n")
    for firstword in searchWords:
        for secondword in searchWords:
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
    for firstword in searchWords:
        for secondword in searchWords:
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