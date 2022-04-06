class User:
    def __init__(self, chat_id: str, username: str, full_name: str, phone_number: str, is_admin: bool, language_code: str, receive_notifications: bool):
        self.chat_id               = chat_id
        self.username              = username
        self.full_name             = full_name
        self.phone_number          = phone_number
        self.is_admin              = is_admin
        self.language_code         = language_code
        self.recieve_notifications = receive_notifications
    
    def as_dict(self):
        return ({
            'chat_id':               self.chat_id,
            'username':              self.username, 
            'full_name':             self.full_name,
            'phone_numer':           self.phone_number,
            'is_admin':              self.is_admin,
            'language_code':         self.language_code,
            'receive_notifications': self.recieve_notifications
            })