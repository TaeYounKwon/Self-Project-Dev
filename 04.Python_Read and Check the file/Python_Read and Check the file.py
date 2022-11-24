import math
import statistics
import os

# get the current working directory (cwd)
cwd = os.getcwd()  
files = os.listdir(cwd)  

#print the path and the files
print("Files in %r: %s" % (cwd, files))


#Get the data from the user file
data_origin = []
data_list   = []
fileName=input('Put the file Name: ')

with open(fileName,'r') as data:
    data_origin = data.readlines()

    #Seperate the input data by comma(,)
    data_list=[int(_numb)for _numb in data_origin[0].split(',')]

    #Calculate the user data
    min = min(data_list)
    max = max(data_list)    
    avg = sum(data_list)/len(data_list)
    std = statistics.stdev(data_list)

    #print out the original list and the calculated data     
    print(data_list)    
    print('Minimum: ',min,' Maximum: ',max, ' Average: ', avg, ' Standard Deviation: ', std)
