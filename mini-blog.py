import datetime

user = [{"usrnm":"user1", "passwd":"pass1", "us_id":1, "us_type":"admin"}]
E = [{e_id:1, message:"bla", time:'timestamp', author:1, parent:None}]

def edit_comment(user, comment, new_data):
	if current_user["us_type"] == "admin":
		comment["message"] = new_data
		date = datetime.datetime.now()
		timestamp = date.strftime("%Y-%m-%d %H:%M")
		comment["timestamp"] = timestamp
		message = "Comment updated"
	else:
		message = "You are not authorized to edit this comment"
	return message

def main:
	comment = "this is the new new_data"
	current_user = user[0]
	E[0].edit_comment(current_user, E[0], comment)


if __name__ == "__main__":
	main()
