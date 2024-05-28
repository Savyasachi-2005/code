import string
import random 

letter1=list(string.ascii_lowercase)
letter2=list(string.ascii_uppercase)
numbers=list(string.digits)
symbols=(list(string.punctuation))

letters=list(letter1+letter2)

n_letter=int(input('how many letters you want in your password'))
n_number=int(input('how many number you want in password'))
n_symbols=int(input('how many symbol you want in password'))

password=[]

for _ in range(n_letter):
    password.append(random.choice(letters))
    
for _ in range(n_number):
    password.append(random.choice(numbers))    
    
for _ in range(n_symbols):
    password.append(random.choice(symbols))    
    
random.shuffle(password)

new_password= ''.join(password)
print(f"the password is: {new_password}")    