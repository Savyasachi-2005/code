if __name__ == '__main__':
    s=input('enter the string')
    position,charcter=input().split()
    
    string_list=list(s)
    string_list[int(position)]=charcter
    
    S_new=''.join(string_list)
    print(S_new)