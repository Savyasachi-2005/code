n=int(input('number of elements\t'))

int_list=list(map(int,input().split()))
t=tuple(int_list)
print(hash((t,)))