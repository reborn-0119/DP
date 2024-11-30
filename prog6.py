import itertools

def brute_force_attack(target_password, characters='abcdefghijklmnopqrstuvwxyz'):

    for password_length in range(1, len(target_password) + 1):
    
        for attempt in itertools.product(characters, repeat=password_length):
            
            attempt_password = ''.join(attempt)
            print(f"Trying: {attempt_password}")
        
            if attempt_password == target_password:
                return attempt_password


target_password = "abc"

found_password = brute_force_attack(target_password)

if found_password:
    print(f"Password found: {found_password}")
else:
    print("Password not found.")
    