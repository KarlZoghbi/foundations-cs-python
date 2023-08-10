class SocialMediaPlatform:
    def __init__(self):
        self.users = {}  # Dictionary to store users and their friend lists

    def add_user(self, username):
        if username in self.users:
            print("User already exists. Please choose another username.")
        else:
            self.users[username] = []

    def remove_user(self, username):
        if username in self.users:
            del self.users[username]
            # Remove user from friend lists
            for user in self.users:
                if username in self.users[user]:
                    self.users[user].remove(username)
        else:
            print("User not found. Please check the username.")

    def send_friend_request(self, sender, receiver):
        if sender in self.users and receiver in self.users:
            if receiver not in self.users[sender]:
                self.users[sender].append(receiver)
                self.users[receiver].append(sender)
                print(f"Friend request sent from {sender} to {receiver}.")
            else:
                print(f"You are already friends with {receiver}.")
        else:
            print("Invalid usernames. Make sure both users exist.")

    def remove_friend(self, user1, user2):
        if user1 in self.users and user2 in self.users:
            if user2 in self.users[user1] and user1 in self.users[user2]:
                self.users[user1].remove(user2)
                self.users[user2].remove(user1)
                print(f"{user2} has been removed from {user1}'s friend list.")
            else:
                print(f"{user2} is not in {user1}'s friend list.")
        else:
            print("Invalid usernames. Make sure both users exist.")

    def view_friends(self, username):
        if username in self.users:
            print(f"Friends of {username}: {', '.join(self.users[username])}")
        else:
            print("User not found. Please check the username.")

    def view_all_users(self):
        print("Registered users:")
        for user in self.users:
            print(user)

    def main(self):
        while True:
            print("\n1. Add a user")
            print("2. Remove a user")
            print("3. Send a friend request")
            print("4. Remove a friend")
            print("5. View your list of friends")
            print("6. View the list of users")
            print("7. Exit")
            
            choice = input("Enter a choice: ")
            
            if choice == '1':
                username = input("Enter a new username: ")
                self.add_user(username)
            elif choice == '2':
                username = input("Enter the username to remove: ")
                self.remove_user(username)
            elif choice == '3':
                sender = input("Enter your username: ")
                receiver = input("Enter the username of the recipient: ")
                self.send_friend_request(sender, receiver)
            elif choice == '4':
                user1 = input("Enter your username: ")
                user2 = input("Enter the username to remove from your friend list: ")
                self.remove_friend(user1, user2)
            elif choice == '5':
                username = input("Enter your username: ")
                self.view_friends(username)
            elif choice == '6':
                self.view_all_users()
            elif choice == '7':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    platform = SocialMediaPlatform()
    platform.main()
