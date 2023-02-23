for num in range(10,20):     
    for i in range(2,num):    
        if num%i == 0:         
            j=num/i
            print(num,i,j)  
    else:                  
        print(num, "is a prime number")
