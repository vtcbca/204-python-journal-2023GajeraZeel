SCRIPT 1
#Write a script to enter any word and check it is palindrom or not.

p=input("Enter any String :")
q=p[::-1]
if(p==q):
    print("String is Palindrome.")
else:
    print("String is Not Palindrome.")


