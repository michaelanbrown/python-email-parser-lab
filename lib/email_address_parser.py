import re

class EmailAddressParser:

    email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    def __init__(self, emails):
        self.emails = emails

    def parse(self):
        strings = re.split(r',|\s', self.emails)