class User:
    def __init__(self, code, meeting, time):
        self.code = code
        self.meeting = meeting
        self.time = time

    def __repr__(self):
        return f"""secret code : {self.code}
meeting : {self.meeting}
time : {self.time}"""

print(User(*input().split()))