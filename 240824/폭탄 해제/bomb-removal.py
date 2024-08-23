class Bomb:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second
    
    def __repr__(self) -> str:
        return f"""code : {self.code}
color : {self.color}
second : {self.second}"""

print(Bomb(*input().split()))