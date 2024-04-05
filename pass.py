import itertools

def password_cracker():
    password = input("Enter the password to crack: ")
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' 
    password_length = len(password)
    print("Cracking password...")
    
    for length in range(1, password_length + 1):
        for guess in itertools.product(characters, repeat=length):
            current_guess = ''.join(guess)
            print(f"Trying: {current_guess}")
            if current_guess == password:
                return current_guess
            
cracked_password = password_cracker()
print(f'The cracked password is: {cracked_password}')
