# Decision Making Statements:
'''
Class 1: 19/01/2020 - Biprodeep Roy - Python Basics

if(<condition>):
    <description>
else:
    <description2>


SWITCH:

def switch(variable):
    try:
        if(<case 1>):
            <case-work-1>
        if(<case 2>):
            <case-work-2>
        if(<case 3>):
            <case-work-3>
        if(<case n>):
            <case-work-n>
    except:
       <default-case-work>
       
            
        
1- read grade file:
SS  E  M  S
30  25  30  30
35  35  40  40
28  38  42  28
8   7   6   8

IF average grade is < 40
grade=b

<30 = c
<20 = f


Looping Syntax in python:
set say S:

S=[1,2,3,4,5]
1
2
3
n(S)

Entry Controlled Loops:
for <variable> in <set>:
    print(<variable>)

while(<condition>):
    print(<variable>)
    variable+=1 (increment)

Exit Controlled Loop:

do:
    <work>
while(<condition>)


F=open(<path-filename>,<reading mode>) --> object
F --> File Object    
F.read()  ---> String (Content of the text file)
F.readlines() ---> List 



10 elements:

M1 M2 M3 M4 5 6 .. M10  



Object:
Identity
Characteristic 
Behaviour


'''

F=open("ngg.txt","r")

fileset=F.read()

values=fileset.split('\n')[1:-1]

print(values)

D2_list=[]

for val in values:
    inn_val=val.split(' ')
    out_val=[]
    for iv in inn_val:
        if(len(iv)>0):
            out_val.append(int(iv))
    D2_list.append(out_val)

row_index=1    
def switch(avg_row):
    try:
        
        if(avg_row>int(40)):
            print("Grade: A")
            return 
        
        if(avg_row<int(20)):
            print("Grade: F")
            return
        
        if(avg_row<int(30)):
            print("Grade: C")
            return
        
        if(avg_row<int(40)):
            print("Grade: B")
            return 
           
    except:
       print("Invalid Grade!")
              
for row in D2_list:
    avg_row=sum(row)/len(row)
    #print("row_index - "+row_index+" : "+str(avg_row))
    '''
    if(avg_row>int(40)):
        print("Grade: A")        
    
    elif(avg_row<int(20)):
        print("Grade: F")
    
    elif(avg_row<int(30)):
        print("Grade: C")
    
    elif(avg_row<int(40)):
        print("Grade: B")
    '''
    switch(avg_row)
        