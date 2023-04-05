SCRIPT 5
##WAS to create 2 udf input() to take input string and call strSymmetric() by passing inputted string.

#strSymmetric() check string is symmetric or not. A string is said to be symmetrical if both the halves of the string are the same.

#Example:

#Enter string : KhoKho

#String is Symmetrical.


def symme(n):
    half=(len(n)//2)
    a=n[:half]
    b=n[half:]
    if a==b:
        print("String is symmetric.")
    else:
        print("String is not symmetric.")

def inputstr():
     p=input("Enter a string:")
     symme(p)
     
inputstr()   