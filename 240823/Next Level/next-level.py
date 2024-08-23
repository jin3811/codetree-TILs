class User:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return f"""user {self.name} lv {self.level}"""

print(User("codetree", 10), User(*input().split()), sep='\n')