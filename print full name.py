def split_and_join(line):
    return '-'.join(line.split())
line=input('enter a sentence\t')
result=split_and_join(line)
print(result)