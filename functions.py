
print("1. Parameterized + Return Type")
def add(a, b):
    return a+b


x= int(input("Enter 1st number to add: "))
y=int(input("Enter 2nd number to sum: "))

result = add(x,y)
print("The sum is :  ", result)





print("2. Parameterized + Non-Return Type")
def sum(c, d):
    print("The sum is : ", c+d)
    
    
v= int(input("Enter 1st number to add: "))
w=int(input("Enter 2nd number to sum: "))

result = sum(v,w)




print("3. Non-Parameterized + Non-Return Type")

def summ():
    e= int(input("Enter 1st number to add: "))
    f=int(input("Enter 2nd number to sum: "))
    print("The sum is : ", e+f)
    
    
result = summ()






print("4. Non-Parameterized + Return Type")

def addd():
   g= int(input("Enter 1st number to add: "))
   h=int(input("Enter 2nd number to sum: "))
   print("The sum is : ", g+h)  
    
    
    
   
addd()