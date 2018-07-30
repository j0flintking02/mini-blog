import datetime
users = [{'user_id': 1, 'user_name': 'jonh', 'pword': 'word', 'user_type': 'admin', 'last_logged': ''},
         {'user_id': 2, 'user_name': 'david', 'pword': 'word2',
             'user_type': 'moderator', 'last_logged': ''},
         {'user_id': 3, 'user_name': 'jonh', 'pword': 'word', 'user_type': 'normal', 'last_logged': ''}]
comments = [{'entry_id': 1, 'user_id': 1,
             'content': 'test_content', 'time_stamp': ''}]



def make_comments(user_id,test_content):
    now = datetime.datetime.now()
    entry = {
            'entry_id':len(comments) + 1,
            'user_id': user_id,
            'test_content': test_content,
            'timestamp':now.strftime("%Y-%m-%d %H:%M")
    }
    comments.append(entry)
    return('Comment added')