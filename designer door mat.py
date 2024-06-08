
    
N,M=map(int,input('enter').split())
        
        

for i in range(1,N,2):
    pattern=('.|.'*i).center(M,'-')
    print(pattern)
welcome='WELCOME'.center(M,'-')
print(welcome)

for i in range(N-2,-1,-2):
    pattern=('.|.'*i).center(M,'-')
    print(pattern)    