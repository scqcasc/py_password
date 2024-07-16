import random

class Password:
    '''Generates a password of a specified length from all available ASCII characters'''
    def __init__(self, length: int) -> None:
        self.length = length
        self.special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '[', '}', ']', '|', ';', ':', '<', ',', '>', '.', '?', '/']
        self.numbers = []
        self.alphaslc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.alphasuc = []
        for letter in self.alphaslc:
            self.alphasuc.append(letter.upper())
        for n in range(0, 10):
            self.numbers.append(str(n))
        self.all_chars = self.special_chars + self.numbers + self.alphaslc + self.alphasuc

    def select_char(self) -> str:
        return self.all_chars[random.randint(0, len(self.all_chars) - 1)]
    
    def get(self) -> str:
        '''Returns the password string'''
        password = []
        for x in range(1, self.length + 1):
            password.append(self.select_char())
        return ''.join(password)

if __name__ == '__main__':
    p = Password(length=15)
    print(p.get())