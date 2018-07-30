# U = [{'user_id': 1, 'name': 'admin', 'pword': 'word', 'level': 'A,N,M'}]
# E = [{'entry_id': 1, 'user_id': 1, 'content': }]

def delete (users, user_id, comment_id, comments):
    for user in users:
        if user['user_id'] == user_id and user['type']== normal:
            for comment in comments:
                if comment['entry_id'] == 'comment_id':
                    comments.remove(comment)
                    return 'Comment has been removed'
        return 'User is not moderator or in existence'