class UserStore:
    def __init__(self, file_path):
        self.file_path = file_path

        users_store = UserStore("users.txt")
        admins_store = UserStore("admins.txt")

