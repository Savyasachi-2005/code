n= int(input('enter the    number of std'))

Student_marks={}

for _ in range(n):
    input_data =input('enter the name and scores').split()
    name=input_data[0]
    scores=list(map(float,input_data[1:]))
    Student_marks[name]=scores
querry_name=input()
if querry_name in Student_marks:
    scores=Student_marks[querry_name] 
    avg=sum(scores)/len(scores)
    print(f"{avg : .2f}")   