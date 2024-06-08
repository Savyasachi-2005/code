s=input('enter the main string\t')

length=len(s)

sub_string={}

for i in range(length):
    for j in range(i,length):
        substring= ""
        for k in range(i,j+1):
            substring +=s[k]
            
        if substring in sub_string:
            sub_string[substring] += 1
        else :
            sub_string[substring] = 1
      
print('Substring count is ')

for substring,count in sub_string.items():
    print(f"'{substring}' : {count}")                    