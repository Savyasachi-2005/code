import textwrap

def wrap(string, maxWidth) :
    return textwrap.fill(string,maxWidth)

string,maxWidth=input('Enter the values\t'),int(input('enter the gap u want\t'))
ans=wrap(string,maxWidth)
print(ans)