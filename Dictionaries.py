# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30

#**My Code**
x = [[5,2,3], [10,8,9]]
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Rondaldo', 'Rooney']
}
z = [{'x': 10, 'y':20}]

x[1][0] = 15
print(x)

students[0]['last_name'] = 'Bryant'
print(students)

sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

z[0]['y'] = 30
print(z)


# Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary 
# in the list and prints each key and the associated value. For example, given the following list:

# students = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
# iterateDictionary(students) 

# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)

# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


# #**MyCode 


def iterateDictionary(some_list):
    for x in range(0,len(some_list)):
        for key, val in some_list[x].items():
            print(f' {key} - {val}')

students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
iterateDictionary(students)


# Create a function iterateDictionary2(key_name, some_list) that, given a 
# list of dictionaries and a key name, the function prints the value stored in 
# that key for each dictionary. For example, iterateDictionary2('first_name', students) 
# should output:
# Michael
# John
# mark
# KB

#then print last names

**My cocde
def iterateDictionary2(key_name, some_list):
    for x in range(0,len(some_list)):
        for key, val in some_list[x].items():
            if key == key_name:
                print(val)
            

        
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
(iterateDictionary2('first_name', students))
(iterateDictionary2('last_name', students))



# Create a function printInfo(some_dict) that given a dictionary whose values are all lists,
#  prints the name of each key along with the size of its list, and then prints the associated 
#  values within each key's list. For example:


def printInfo(some_dict):
    for key, val in some_dict.items():
        print(f" {len(val)}, {key}, ")
        for x in range(0, len(val)):
            print(val[x])       
    
dojo = {
    'locations': ['San Jose', 'Seatle', 'Dalles', 'Chicago', 'Tulsa', 'DC'],
    'instructers': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


printInfo(dojo)