import itertools

def brute_force_attack(target_password, characters='abcdefghijklmnopqrstuvwxyz'):
    # Try passwords of increasing length
    for password_length in range(1, len(target_password) + 1):
        # Generate all possible combinations for the current password length
        for attempt in itertools.product(characters, repeat=password_length):
            # Join characters to form a string for the current attempt
            attempt_password = ''.join(attempt)
            print(f"Trying: {attempt_password}")
            # Check if the attempt matches the target password
            if attempt_password == target_password:
                return attempt_password

# Example target password
target_password = "abc"

# Perform brute-force attack
found_password = brute_force_attack(target_password)

if found_password:
    print(f"Password found: {found_password}")
else:
    print("Password not found.")
    