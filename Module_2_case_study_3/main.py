import re

#LETTERS contains all the possible charecters of ref_id
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS = LETTERS+LETTERS.lower()
LETTERS = LETTERS+'0123456789'

#function to take input from command line 
def input_function():
  ref_id=input('Enter Reference ID : ')
  valid = validation_function(ref_id)
  if (valid == 0):
    print("Invalid Reference ID :")
    Error_Function()
  else:
    try:
      print("\n-----Encryption------\n")
      key = int(input("Enter the value for encryption key(integer value) : "))

      #encrypt ref_id
      ref_id = encrypt(key,ref_id)
      print("\nEncrypted ref_id : "+ref_id)

      #decrypt ref_id
      key2=input("Enter the key to decrypt : ")
      key2=int(key2)
      ref_id = decrypt(key2,ref_id)
      print("\nDecrypted ref_id : "+ref_id)

    except:
      print("There is an error while inputting key value!!")
      Error_Function()


    

#function to validate the inputted ref_id   
def validation_function(ref_id):
  if (len(ref_id)<=12):
    #here we are checking whether ref_id consist of special charecter or not
    string_check= re.compile('[@_!#$%^&*()<>?/\|}{~:]')  
    if (string_check.search(ref_id) == None):
      return 1
    else:
      return 0
      
  else:
    print("\n----Number of charecter must be lesser than or equal to 12----\n")
    Error_Function()

#function to handle the Error  
def Error_Function():
    print("\n\t----Try again----")
    input_function()

#function to encrypt data 
def encrypt(key,message):
    encrypted = ''
    for chars in message:
        if chars in LETTERS:
            num = LETTERS.find(chars)
            num = num + key
            encrypted +=  LETTERS[num]

    return encrypted

#function to encrypt data 
def decrypt(key,message):
    decrypted = ''
    for chars in message:
        if chars in LETTERS:
            num = LETTERS.find(chars)
            num -= key
            decrypted +=  LETTERS[num]

    return decrypted

#main   
input_function()