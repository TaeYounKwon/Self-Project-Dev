#Get a command line parameter n
_numb=int(input("Please type the number of prime numbers: "))
_count=0

#Max numb to search the data
n=100000

#Statement to find and count the prime number
if _numb>0: 

    for i in range(n):
        isPrime=True

        if(i<2):
            isPrime=False
                
        if(i==2):
                isPrime=True
                
        if(i==3):
                isPrime=True

        #Find the numbers that are not prime number        
        for j in range(2,i):
            if(i%j)==0:
                isPrime=False
        
        #If Prime then print the value and _count ++
        if isPrime:
            print(i,end=' ')
            _count+=1
            
        #If _count is same as user prim
        #     
        if _count==_numb:
            break

#If wrong input then error message comes out         
else:
    print('Invalid Input Value! Please try again.')