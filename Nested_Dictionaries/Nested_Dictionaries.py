#1. Update Values in Dictionaries and Lists

x = [[5, 2, 3], [10, 8, 9]]

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]

sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

# solution:
x[1][0] = 15
print(x)

# change the value associated with the key 'last_name' to 'Bryant' for the first student
students[0]['last_name'] = 'Bryant'
print(students)

# change the value at index 0 to 'Andres' for the 'soccer' key
sports_directory['soccer'][0] = 'Andres'  
print(sports_directory)

# change the value associated with the key 'y' to 30 for the first element of the list
z[0]['y'] = 30 
print(z)

# 2. Iterate Through a List of Dictionaries

def iterateDictionary(students):

    students = [
        {'first_name':  'Michael', 'last_name': 'Jordan'},
        {'first_name': 'John', 'last_name': 'Rosales'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ]
    
    def iterateDictionary(some_list):
        for dictionary in some_list:  
            for key, value in dictionary.items():  
                print(key, '-', value)

students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

iterateDictionary(students)


# 3. Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for dictionary in some_list:  
        print(dictionary[key_name])


students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

iterateDictionary2('first_name', students)



# 4. Iterate Through a Dictionary with List Values
def printInfo(some_dict):
    for key, value in some_dict.items():
        print(f"{len(value)} {key.upper()}")
        for val in value:
            print(val)


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)
