# A-Z 65 - 90
#a-z 97 - 122
orig_message = input("Enter the Message: ")
shift = int(input("Enter the shift number : "))
secret= ""
decrypt= ""
for chars in orig_message:

     if chars.isalpha():
         char_code = ord(chars)+shift
         if chars.isupper():
             if char_code > ord('Z'):
                 char_code -= 26
             if char_code < ord('A'):
                 char_code +=26

         else:
             if char_code > ord('z'):
                 char_code -= 26
             if char_code < ord('a'):
                 char_code += 26

         secret += chr(char_code)

     else:
         secret += chars
print ("Encrypted Message is : ", secret)

shift = -shift
for chars in secret:

     if chars.isalpha():
         char_code = ord(chars)+shift
         if chars.isupper():
             if char_code > ord('Z'):
                 char_code -= 26
             if char_code < ord('A'):
                 char_code +=26

         else:
             if char_code > ord('z'):
                 char_code -= 26
             if char_code < ord('a'):
                 char_code += 26

         decrypt += chr(char_code)

     else:
         decrypt+= chars


print("Decrypted Message is : ", decrypt )


