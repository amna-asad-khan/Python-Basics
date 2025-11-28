print("Hi. \nHow are you?")    #simple string structure
print()


#Special functions of string


s = "  Hello World 123  "  #there are 2 spaces at the beginning and ending of string


# 1. Case-related
print("Upper:", s.upper())
print("Lower:", s.lower())

print("Title:", s.title())
print("Capitalize:", s.capitalize())
print("Swapcase:", s.swapcase())
print()

# 2. Checking type/contents
print("Is Alpha:", s.isalpha())  #Checks if the string has only letters (a–z or A–Z)
print("Is Digit:", s.isdigit())  #Checks if the string has only digits (0–9)
print("Is Alnum:", s.isalnum())  #Checks if the string has only letters and numbers
print("Is Lower:", s.islower())
print("Is Upper:", s.isupper())
print("Is Space:", s.isspace())  #Checks if the string has only spaces or tabs
print()



# 3. Searching / Finding
print("Find 'World':", s.find("World"))
print("Index 'World':", s.index("World"))
print("Count 'l':", s.count("l"))  #tells hoe many time the selected letter appear's
print("Starts with 'Hello':", s.startswith("Hello"))
print("Ends with '123':", s.endswith("123"))
print()


# 4. Modifying / Formatting
print("Replace 'World' with 'Python':", s.replace("World", "Python"))
print("Strip:", s.strip()) #remove spaces from left and right
print("Lstrip:", s.lstrip()) 
print("Rstrip:", s.rstrip())
print("Split:", s.split()) #convert string into list
print("Join with '-':", "-".join(s.split())) #it join lists using -
print()


# 5. Encoding / Other
print("Format:", "{} is awesome!".format("Python"))
print("Center:", s.strip().center(22, "*"))
print("Ljust:", s.strip().ljust(20, "-"))
print("Rjust:", s.strip().rjust(20, "-"))
print("Zfill (10):", "123".zfill(10))



#string concatination
a = "Hi"
b = " thereHow are you?"
print(a+b)


#word replacenet in sentences
sentence = input('Enter the sentence: ')
print("Your sentence: ", sentence)

word1 = input('Enter the word that you want to replace from your entered sentance: ')
word2 = input('Enter the word that you want to place insted of above word: ')

new = sentence.replace(word1, word2)
print("Here is your updated sentence: ", new)

