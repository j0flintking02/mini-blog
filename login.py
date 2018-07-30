
import subprocess as sp

def start():
    '''start menu for cmd and sp(subprocess) is call for subprocess'''
    tmp = sp.call('cls',shell=True)
    print('Please enter the option number you would like.')
    print('i.e. If I wanted to register, I would type 1')
    print('[1] Register')
    print('[2] User')
    print('[3] Moderator Controls')
    print('[4] Admin Controls')
    
    option = input('Option number: ') # Get user input
    if option == '1':
        register()
    elif option == '2':
        login()
    elif option == '3':
        moderator()
    elif option == '4':
        adminlogin()
    else:
        print('Option does not match the choices!')
        anykey = input('Press Enter to continue.')
        start()

def register():
    tmp = sp.call('cls',shell=True)
    our_list = [] # create empty list
    
    username =input('Enter Username: ')
    password = input('Enter password: ')
    
    our_list.append(username)
    our_list.append(password)
    login()

def login():
    '''Get login info from user'''
    tmp = sp.call('cls',shell=True)
    #nornmal user login
    _username = input('Username: ')
    _pass = input('Password: ')
   
    if _username == 'user':
        if _pass == 'user123':
            user()
        else:
            print("Username is incorrect!")
    else:
        print('Password is incorrect!')


def moderator():
    '''Moderator login'''
    _username = input('Moderator Username: ')
    _pass = input('Moderator Password: ')
   
    if _username == 'moderator':
        if _pass == 'moderator123':
            moderator()
        else:
            print("Username is incorrect!")
    else:
        print('Password is incorrect!')

def adminlogin():
    # Admin login
    _username = input('Admin Username: ')
    _pass = input('Admin Password: ')
   
    if _username == 'admin':
        if _pass == 'admin123':
            admincontrol()
        else:
            print("Username is incorrect!")
    else:
        print('Password is incorrect!')
    
            

def admincontrol():
    # Admin Control
    tmp = sp.call('cls',shell=True)
    print('Welcome to Admin Control!')    
    ai = input('Press enter to go back to the start screen.')
    if ai != 'Edit':
        start()
    else:
        start()

def user():
    # User Control
    tmp = sp.call('cls',shell=True)
    print('Welcome to User Control! Add comment')    
    ai = input('Press enter to go back to the start screen.')
    if ai != 'Edit':
        start()
    else:
        start()
        
start()