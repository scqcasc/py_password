import random
import string

class Password:
    '''Generates a password of a specified length from all available ASCII characters'''
    def __init__(self, length: int) -> None:
        self.length = length
        self.special_chars = string.punctuation
        self.numbers = string.digits
        self.alphaslc = string.ascii_lowercase
        self.alphasuc = string.ascii_uppercase
        self.all_chars = self.special_chars + self.numbers + self.alphaslc + self.alphasuc
        print(self.all_chars)
        ac = list(self.all_chars)
        random.shuffle(ac)
        self.all_chars = ''.join(ac)
        print(self.all_chars)
    
    def check_in_list(self, password, list_to_check) -> bool:
        '''Make sure that at least one character is in the list to check'''
        for letter in password:
            if letter in list_to_check:
                return True
        return False
    
    def get(self) -> str:
        '''Returns the password string'''
        ready = False
        checks = [self.alphaslc, self.alphasuc, self.special_chars, self.numbers]
        while not ready:
            password = random.sample(self.all_chars, self.length)
            # make sure there is at least one of each of the checks
            for check in checks:
                ready = self.check_in_list(password=password, list_to_check=list(check))
                if not ready:
                    break
        return ''.join(password)


if __name__ == '__main__':
    p = Password(length=15)
    print(p.get())