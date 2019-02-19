Input_String = input("Enter a string : ")
Input_String = Input_String.upper()

IS_list = Input_String.split()
print (IS_list)
acr= ''

for char in IS_list:
    acr += char[0].upper()

print(acr)
