#List can be define by two ways

countries = ['UK', 'Pakistan', 'Turkey', 'Indonesia'] #using square bracket
print(countries)

cities = list(('London', 'Istanbul', 'Lahore', 'Jkarta')) #using list constructor
print(cities)



#List methods
countries.append('Japan')
print(countries)

countries.extend(['China', 'Korea'])
print(countries)

countries.insert(1, 'Iran')
print(countries)

countries.remove('UK')
print(countries)

countries.pop()
print(countries)

countries.sort()
print(countries)

countries.reverse()
print(countries)


#2D lis

print()
print("2D list")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matrix:")
for row in matrix:
    print(row)
