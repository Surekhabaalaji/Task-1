#simple calculator using function
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x//y

print(""" select operation
1.add 
2.sub
3.mul                 
4.div     
    """)
choice=int(input("enter your choice "))
x=int(input("enter first number "))
y=int(input("enter second number "))

if choice==1:
    print(add(x,y))
elif choice==2:
   print(sub(x,y))
elif choice==3:
    print(mul(x,y))
elif choice==4:
    print(div(x,y))
else:
    print("enter correct choice")