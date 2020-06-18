print('Call the function password, to start! ')
print('You can only enter your pin 5 times, else out of limit. ')
def password():
    password = 'owolabi'
    pin = ''
    pin_count = 0
    pin_limit = 5
    out_of_pin_limit = False
    while pin != password and not out_of_pin_limit :
         if pin_count < pin_limit :
             pin = input('Enter the password pin : ')
             pin_count += 1
         else:
             out_of_pin_limit = 'True'
    if out_of_pin_limit :
         print('Wrong password, out of limit')
    else:
         print('Password correct, Welcome !')
