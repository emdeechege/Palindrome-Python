class Palindrome:
    '''
    generates new_palindrome instances
    '''
    palindrome_list= []

    def __init__(self,phrase):
        self.palindrome = phrase

    def save_palindrome(self):
        Palindrome.palindrome_list.append(self)

    @classmethod
    def display_palindromes(cls):
        return cls.palindrome_list
