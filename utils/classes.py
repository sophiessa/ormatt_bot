class User:
    def __init__(self, username: str, full_name: str, phone_number: str, chat_id: str):
        self.username = username
        self.full_name = full_name
        self.phone_number = phone_number
        self.chat_id = chat_id
    
    def as_dict(self):
        return ({
            'username':    self.username, 
            'full_name':   self.full_name,
            'phone_numer': self.phone_number,
            'chat_id' :    self.chat_id
                 })