import random
import string

def random_password():
    length = random.randint(8, 15)
    password = ''
    for k in range(length):
        password += random.choice(string.ascii_letters + string.digits)
    return password

for _ in range(3):
    print(random_password())