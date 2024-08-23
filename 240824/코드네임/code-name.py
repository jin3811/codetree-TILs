class User:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = int(score)
    
    def __repr__(self) -> str:
        return f"{self.codename} {self.score}"

users = [User(*input().split()) for i in range(5)]
print(min(users, key=lambda user: user.score))