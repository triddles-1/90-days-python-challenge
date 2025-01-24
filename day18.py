import hashlib

#print(hashlib.algorithms_available)

known_hash ="839c1d07d1c9a2b89d40d2b1c5c90477831dc698f927066f6fb06a9d71c8f6477"
def hash_password(password):
# Hash the password using SHA-256
    return hashlib.sha256(password.encode('utf-8')).hexdigest()
user_input = input("Enter your password:")
user_hash = hash_password(user_input)
#Compare the hashed user input to the known hash
if user_hash == known_hash:   print("Password match!Access granted.")


import hashlib
import sys

def hash_password(password):    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def verify_password():
    # Prompt for the known hash and user input in one go
        data = input("Enter the known hash and your password (separated by a space):").split() 
        if len(data)!=2:
         print("Error: Please provide both the known hash and your password separated by a space.")
        sys.exit(1)
        known_hash, password = data
        user_hash = hash_password(password)
        if user_hash == known_hash:
         print("Password match! Access granted.")
        else:
         print("Password mismatch. Access denied.")  

#if__name__== '__main__':   verify_password()



