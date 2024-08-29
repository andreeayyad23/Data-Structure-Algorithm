num1 = 11
num2 = num1

print(id(num1))
print(num1)
print(id(num2))
print(num2)

num2 = 22
print(id(num1))
print(num1)
print(id(num2))
print(num2)

dict1 = {
    'value' : 11
}

dict3 = {
    'value' : 22
}

dict1 = dict3
dict2 = dict3

print(dict1)
print(id(dict1))
print(dict2)
print(id(dict2))