# Biprodeep Roy - Class 2 - 26/1/2020

F=open("cs-class/student_marks.txt","r")

fileset=F.read()

values=fileset.split('\n')[1:-1]

#print(values)

D2_list=[]

for val in values:
    inn_val=val.split(' - ')
    out_val=[]
    for iv in inn_val:
        if(len(iv)>0):
            #print(iv)
            out_val.append(iv)
    D2_list.append(out_val)
    
#print(D2_list)

#Find out AVERAGE
for row in D2_list:
    sum=0
    cnt=0
    for col in row:
        try:
            sum+=int(col)
            cnt+=1
        except:
            continue
    avg=sum/cnt
    print(row[0]+"   Average Marks: "+ str(avg))

## Extract DOB For Q4
for row in D2_list:
    cnt=0
    for col in row:
        if(cnt==2):
            print(col)
        cnt+=1
