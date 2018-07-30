users = [
        {'user_id': 1, 'user_name': 'jonh', 'pword': 'word', 'user_type': 'admin','last_logged':''},
        {'user_id': 2, 'user_name': 'david', 'pword': 'word2', 'user_type': 'moderator','last_logged':''},
        {'user_id': 3, 'user_name': 'jonh', 'pword': 'word', 'user_type': 'normal','last_logged':''}
    ]
comments = [
        {'entry_id': 1, 'user_id': 1, 'content':'test content', 'time_stamp':''}
    ]
    
def register():
    """ Adds a new user the a list"""
next_id = len(users)
new_id=int(next_id+1)
user_name = input("Enter the user_name:")
user_password = input("Enter the password:")
user_type = input("type of user:")
new_entry = {
'user_id': new_id,
'user_name': user_name,
'pword': user_password,
'user_type': user_type}
users.append(new_entry)


    
if __name__ == '__main__':
    register()
