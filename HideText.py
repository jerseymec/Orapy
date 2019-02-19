# Encrypt string to code.. Upper/Lower/Space
Message = input("Enter the Mixedcase string : ")

hide = ""
message = ""

for chars in Message:
    print("Character is : ", chars, str(ord(chars) - 23))
    # if (ord(chars) - 23 < 10) :
    #     hide += "0" + str(ord(chars) - 23)
    #     continue
   # converted = format(str(ord(chars) - 23), '02')

    converted = str(ord(chars) - 23).zfill(2)
    #converted = converted.zfill(2)
    #print (type(converted ))
    hide = hide + converted

print("The Secrete message : ", hide)

for i in range(0, len(hide)-1, 2):
    print(" Converted Character is : ", int(hide[i:i+2]) + 23)
    message += chr(int(hide[i:i+2]) + 23)

print("The Orginal Message is : ", message)
Meldo