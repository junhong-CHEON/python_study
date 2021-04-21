class Member:
    username = None
    email = None
    
    def __init__(self, username, email):
        self.username = username
        self.email = email
        
    def view_info(self):
        tpl = "이름: {0} / 이메일: {1}"
        print(tpl.format(self.username, self.email))