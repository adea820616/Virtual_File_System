import os
import sys

class UserManagement:
    def __init__(self):
        self.registered_users = set()
        self.registered_users_path = os.path.join(os.getcwd(), 'users')
        self.load_registered_users()


    def check_registered_users_file(self):
        if not os.path.exists(self.registered_users_path):
            os.mkdir(self.registered_users_path)


    def load_registered_users(self):
        self.check_registered_users_file()
        self.registered_users = set(os.listdir(self.registered_users_path))


    def check_exists(self, username, to_register):
        if username in self.registered_users:
            if to_register:
                print(f"Error: The '{username}' has already existed.", file=sys.stderr)
            else:
                print(f"The '{username}' exists.")
            return True
        else:
            print(f"The '{username}' has not registered.")
            return False
        

    def register_user(self, username):
        self.registered_users.add(username)
        os.mkdir(os.path.join(self.registered_users_path, username))
        print(f"Add '{username}' successfully.", file=sys.stdout)