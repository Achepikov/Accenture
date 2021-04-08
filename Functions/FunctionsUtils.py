import random
import string


class FunctionsUtils:

    def __init__(self):
        self.random = format(random.randint(0000, 9999), '04d')
        self.prefix = 'alexey'
        self.domain = 'domain.com'

    # random
    def generate_random(self):
        return self.random

    # email random
    def generate_email(self, number):
        email = self.prefix + number + '@' + self.domain
        return email

    def generate_password(self):
        chars = string.ascii_uppercase
        chars1 = string.digits
        chars2 = '!'
        chars3 = string.ascii_lowercase
        return ''.join((random.choice(chars) + random.choice(chars1) + random.choice(chars2) + random.choice(chars3)) for x in range(4))
