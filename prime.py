while True:
    n=int(input('hey buddy enter the number\n'))
    if n == 1:
        print('exiting the loop')
        break
    
    count =0

    for i in range(1,n+1):
        if n % i == 0:
            count +=1
            
    if count == 2:
        print(n, 'is prime number')
    else :
        print(n,'is not prime number')    
        