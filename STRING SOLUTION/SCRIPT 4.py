SCRIPT 4
##Write a menu driven list which perform following operation

#1. Create list of string till user choise.
#2. Print string with even character in length.
#3. Replace odd character of string with index no.
#4. Enter start and end value and extract character from the list of string.

p=[]
q="y"
while q=="y" or q=="Y":

  print("\n1.Add iteams in list.")
  print("\n2.print string with even character in length.")
  print("\n3.Replace odd character of string with index no.")
  print("\n4.enter start and end value and extraxt character from the string\n")
  c=int(input("Enter your choice."))

  
  if c== 1:
          x="y"
          while x=="y" or x=="Y":
            i=input("Enter your string:")
            p.append(i)
            x=input("Add string (y/Y):")
               
  elif c==2:
         s=[]
         count=0
         for i in a:
            if(len(i)%2==0):
              s.append(i)
              count+=1
         if count>0:    
            print("Even character is {s}")  
         else:  
            print(" No even charcater .")
 
   
  elif c==4:
          p=int(input("Enter start index:"))
          q=int(input("Enter end index:"))
          res=" ".join([sub for sub in a ])[p:q]
          print(f"Your string is {res}")

  else:
       print("Enter a valid choice!")

  q=input("Do you want to continue:(y/Y):")        
  
  