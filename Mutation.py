def mutate_string(string,position,character):
    string_list=list(string)
    string_list[int(position)]=character
    return ''.join(string_list)

if __name__ == '__main__':
    s=input('enter the original word')
    i,c=input('enter the postion and character to change').split()
    s_new=mutate_string(s,int(i),c)
    print(s_new)