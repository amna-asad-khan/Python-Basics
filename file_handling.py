#reading from a file

file = open("C:\\Users\\abc\\Documents\\practice\\Codes\\raw.txt", "r")
for lines in file.readlines() :
   print(lines)
file.close()


#writing in the file

new_file = open("C:\\Users\\abc\\Documents\\practice\\Codes\\raw.txt", "w")
new_file.write('hi')
new_file.close()  
