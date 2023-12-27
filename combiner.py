import sys
  
  
def combiner(): 
    oldKey = None
    total = 0
    for line in sys.stdin:
        if len(line.split("\t")) == 2:
            key,value = line.split("\t")
            if(oldKey == None):
                
                oldKey = key
                total = int(value)
            else:
                if(oldKey == key):
                   
                    total+= int(value)
                else:
                    print(f"{oldKey}\t{total}")
                    oldKey = key
                    total = int(value)


        else:
            continue


combiner()