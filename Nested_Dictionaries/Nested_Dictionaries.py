# Update Values in Dictionaries and Lists
# 1. Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

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

# 2. Iterate Through a List of Dictionaries

def iterateDictionary(students)

    students = [
        {'first_name':  'Michael', 'last_name': 'Jordan'},
        {'first_name': 'John', 'last_name': 'Rosales'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ]
    iterateDictionary(students)
    # should output: (it's okay if each key-value pair ends up on 2 separate lines;
    # bonus to get them to appear exactly as below!)
    first_name - Michael, last_name - Jordan
    first_name - John, last_name - Rosales
    first_name - Mark, last_name - Guillen
    first_name - KB, last_name - Tonel


# 3. def iterateDictionary2(key_name, some_list)
# For example, iterateDictionary2('first_name', students) should output: 
# Michael
# John
# Mark
# KB
# And iterateDictionary2('last_name', students) should output:
# Jordan
# Rosales
# Guillen
# Tonel

# 4. Iterate Through a Dictionary with List Values

def printInfo(some_dict)
    dojo = {
        'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
        'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
    
    printInfo(dojo)
    # output:
    7 LOCATIONS
    San Jose
    Seattle
    Dallas
    Chicago
    Tulsa
    DC
    Burbank

    8 INSTRUCTORS
    Michael
    Amy
    Eduardo
    Josh
    Graham
    Patrick
    Minh
    Devon

}
