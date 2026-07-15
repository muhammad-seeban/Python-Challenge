age = 15
print(type(age)) # This will print <class 'int'> as age is an integer   
print(len(str(age))) # This will print 2 as the length of the string representation of age is 2
print (type(age)) # This will print <class 'int'> as age is still an integer
age = str(age) # This will convert age to a string
print(type(age)) # This will print <class 'str'> as age is now a string
print(int(len(age))) # This will print 2 as the length of the string representation of age is 2

# age = age + 5 # This will raise a TypeError because age is now a string and cannot be added to an integer

