#I assume it's concept as oposite of if-else (in if-else when the condition gets true then it apply working but here if the conditions gets false then it apply the working
# )

try:
    num = int(input("Enter number: "))
    result = 10/num
    print("Result: ", result)
except ValueError:
    print("It's not an integer")    
 