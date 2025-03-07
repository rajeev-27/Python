class User:

    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user1 = User("001","Rajeev")
user2 = User("002", "Gupta")
user3 = User("003", "Anurag")

user1.follow(user3)
user1.follow(user2)
user2.follow(user3)

print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)
print(user3.followers)
print(user3.following)