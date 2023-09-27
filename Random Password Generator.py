import random
import string

def generate_password(length=12, use_digits=True, use_special_chars=True):
   
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    
    return password


password = generate_password()
print("Random Password:", password)
