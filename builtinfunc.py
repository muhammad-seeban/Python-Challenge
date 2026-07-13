text = "hello"
number = 20

print("The type of variable is" ,type(text))
print("The type of variable is" ,type(number))

print("The length of variable is" ,len(text))
# print("The length of variable is" ,len(number)) #This would not work as integer datatype doesn't have a length


print(text.upper())
# print(number.upper()) This method would not work as upper() is a string method and number is an integer and same with lower

print(number.bit_length()) #This method would work as bit_length() is an integer method and number is an integer
# It Would not work with string as string doesn't have bit_length() method

