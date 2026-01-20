class UserStore:
    def __init__(self, user_id: int, name: str, age: int):
        # We take the values passed in and "stick" them to the object
        self.user_id = user_id
        self.name = name
        self.age = age
        pass