def count_substring(string,Sub_string):
    count=0
    for i in range(len(string)-len(Sub_string)+1):
        if string[i:i+len(Sub_string)] == Sub_string :
            count+=1
    return count

if __name__ == '__main__':
    string=input('enter main string\t').strip()
    Sub_string=input('enter sub string\t').strip()
    count=count_substring(string,Sub_string)
    print(count)       