
import hashlib
def hash_pwd(password):
    pwd=password.encode('utf-8')
    
    sha256_hash=hashlib.sha256()
    sha256_hash.update(pwd)
    
    sha512_hash=hashlib.sha512()
    sha512_hash.update(pwd)
    
    sha224_hash=hashlib.sha224()
    sha224_hash.update(pwd)
    
    sha384_hash=hashlib.sha384()
    sha384_hash.update(pwd)
    
    
    hash256=sha256_hash.hexdigest()
    hash512=sha512_hash.hexdigest()
    hash224=sha224_hash.hexdigest()
    hash384=sha384_hash.hexdigest()
    
    return hash256,hash512,hash224,hash384
    
            
 
#Main    
pwd=input("Enter a String : ")
hash256,hash512,hash224,hash384=hash_pwd(pwd)
print(f"SHA-256 hashed password : {hash256}\nSHA-512 hashed password : {hash512}")
print(f"SHA-224 hashed password : {hash224}\nSHA-384 hashed password : {hash384}")