print("Select function: ")
print()
print("1. to add")
print("2. to subtract")
print("3. to multiply")
print("4. to divide")


choice = int(input("Enter choice 1,2,3,4:  "))

a= int(input("Enter 1st number: "))
b= int(input("Enter 2nd number: "))

if choice ==1:
    print("The sum: ", a+b)
elif choice ==2:
    print("The difference: ", a-b)  
elif choice == 3:
    print("The product: ", a*b)
elif choice ==4:
    print("The quotient: ", a/b)
else:
    print("Error *-*")
    
    