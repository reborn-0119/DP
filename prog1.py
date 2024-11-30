
def encrypt(text,shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)  
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)  
    return result

    
    
def decrypt(text,shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)  
        else:
            result += chr((ord(char) - shift - 97) % 26 + 97) 
    return result
    

#menu    
print("1.Encryption \n2.Decryption")
ch=int(input("Enter ur choice : "))
if ch==1:
    textE=input("Enter text to encrypt : ")
    shiftE=int(input("Enter shift value : "))
    en_text=encrypt(textE,shiftE)
    print(f"Encrypted text : {en_text}")
    
elif ch==2:
    textD=input("Enter text: ")
    shiftD=int(input("Enter shift value : "))
    de_text=decrypt(textD,shiftD)
    print(f"Decrypted text : {de_text}")
    
else:
    print("Invalid choice \nRe-run the code")
    