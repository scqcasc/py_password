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
    
    def check_in_list(self, password, list_to_check) -> bool:
        '''Make sure that at least one character is in the list to check'''
        for letter in password:
            if letter in list_to_check:
                return True
        return False
    
    def get(self) -> str:
        '''Returns the password string'''
        ready = False
        while not ready:
            password = random.sample(self.all_chars, self.length)
            # make sure there is at least one UC letter
            ready = self.check_in_list(password=password, list_to_check=self.alphasuc)
            if not ready:
                continue
            ready = self.check_in_list(password=password, list_to_check=self.numbers)
            if not ready:
                continue
            ready = self.check_in_list(password=password, list_to_check=self.alphaslc)
            if not ready:
                continue
            ready = self.check_in_list(password=password, list_to_check=self.special_chars)
            if not ready:
                continue
        return ''.join(password)


if __name__ == '__main__':
    p = Password(length=15)
    print(p.get())