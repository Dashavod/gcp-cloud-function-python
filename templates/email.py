
class Email:
    def __init__(self, data=None):
        self.company_name = ""
        self.content = ""
        self.email_type = 0
        self.legal_notice = ""
        self.recipient = ""
        self.sender = ""
        self.region = []
        if data: [setattr(self, key, data[key]) for key in data]
        print(f'Email {self.__dict__} created')
