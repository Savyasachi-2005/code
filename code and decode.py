while True:    
    import string
    import random
    alpha=list(string.ascii_letters)+list(string.digits)+list(string.punctuation)
    cd=list(input("Enter the name Buddy..! that you want to convert into code.\n"))
    cd1=[]
    cd2=[]
    

    if len(cd)<=4 :
        cd.reverse()
        final_code=''.join(cd)
        print(f"so your modified code is : {final_code}") 
    
    
    elif (len(cd)>4):  
        cd[0],cd[-2]=cd[-2],cd[0]
        cd[2],cd[-1]=cd[-1],cd[2]
        cd[3],cd[-3]=cd[-3],cd[3]
        a=''.join(cd)

        for i in range(5):
            ad=random.choice(alpha)
            cd1.append(ad)
            prefix=''.join(cd1)
    
        for _ in range(5):
            ab=random.choice(alpha)
            cd2.append(ab)
            suffix=''.join(cd2)
      
        b=prefix+a+suffix
        final_code=''.join(b)
        print(f"so your modified code is :  {final_code}")       

    take=input("do you want to decode\n")
    if take.lower() == 'Yes'.lower():
        #dc=input('Enter the name Buddy..! that you want to Decode.\n')

        if len(final_code)<=4:
            final = list(final_code)
            final.reverse()
            f_ans=''.join(final)
            print(f"Hey Buddy, the decoded message from the code is: {f_ans}")
        elif len(final_code)>4:    
            dcd=list(final_code)
            r=dcd[5:-1]
            g=r[0:-4]
            g[0],g[-2]=g[-2],g[0]
            g[2],g[-1]=g[-1],g[2]
            g[3],g[-3]=g[-3],g[3]
            decoded_ans=''.join(g)
            print(f"Hey Buddy, the decoded message from the code is: {decoded_ans}")

    elif take.lower() == 'No'.lower():
        print("ok Buddy......!")        

   