import secrets
import string


print('''Greetings!
This is a password generator.
It can generate a password from 8 to 20 symbols.''')
number_of_symbols = int(input("Please enter number from 8 to 20 symbols for the password: "))
while number_of_symbols < 8 or number_of_symbols > 20:
    number_of_symbols = int(input("Please enter again number from 8 to 20 symbols for the password: "))
    if number_of_symbols < 8 or number_of_symbols > 20:
        print("The number can't be lesser than 8 or greater than 20")
    else:
        print(f"Generating a password for {number_of_symbols} symbols")


def generate_random(length):
    symbols = ("!@#$%^&*")
    alphabet = string.ascii_letters + string.digits + symbols
    while True:      
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)
            and any(c in symbols for c in password)):
            break
    return password
password = str(generate_random(number_of_symbols))
print('Your password: ' + password)
def write_output(path):
    if input('Do you want to save the name of the app, login and password? y/n: ') == 'y':
        app = input('Enter the app name password was created for: ')
        login = input('Enter your login: ')
        with open(path, 'a') as f:
            print('\n' + 'App: ' + app, file=f)
            print('Login: ' + login, file=f)
            print('Password: ' + password, file=f)
            f.write('--------------------')
        print(f'Your credentials were saved to {path}. Have a great day!')
    else:
        print('Have a great day!')
path = 'C:\\Users\\output.txt'
write_output(path)
