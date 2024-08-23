class User:
    def __init__(self, name, addr, city):
        self.name = name
        self.addr = addr
        self.city = city
    
    def __repr__(self) -> str:
        return f"""name {self.name}
addr {self.addr}
city {self.city}"""

n = int(input())
users = [User(*input().split()) for i in range(n)]
print(max(users, key=lambda user: user.name))