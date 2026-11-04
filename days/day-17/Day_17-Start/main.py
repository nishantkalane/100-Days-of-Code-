#creating a class

class Users:
    def __init__(self,user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following =0
    def follow(self,user):
        user.following +=1
        user.followers +=1


#creating object
user_1 = Users("001","Nish")

print(user_1.id, user_1.username)