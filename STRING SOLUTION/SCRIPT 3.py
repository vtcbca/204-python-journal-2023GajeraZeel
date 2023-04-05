SCRIPT 3
#Write a script to create a list with 5 string and count total number of string with even number of length with string using UDF


def evenstring(x):
    z=[]
    count=0
    for i in x:
        if(len(i)%2==0):
            z.append(i)
            count=count+1
    if(count>0):
        print(f'Even string is {count} and string :{z}')
    else:
        print( "even string is not available.")

x=[]
for i in range(5):
    z1=input(f"Enter string:{i+1}:")
    x.append(z1)    
evenstring(x)    