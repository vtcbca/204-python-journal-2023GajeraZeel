SCRIPT 2
#write a script to enter any sentence and print those word which is palindrome also print total number of palindrome word.
def paliwordcount(p):
    q=p.split(" ")
    r=0
    x=[]
    for i in q:
        if (i==i[::-1]):
            r=r+1
            x.append(i)
    if r>0:
        print(" Palindrome Word In Sentence Is {r} And Palindrome Words Are:{x}.")              
    else:
        print(" No Palindrome Word in Sentence!!!")    
p=input("enter a sentece:")
paliwordcount(p)
