import unittest
from palindrome import Palindrome


class TestPalindrome(unittest.TestCase):
    '''
    Test class to define test cases for plaindrome beahvciours
    '''
    def setUp(self):
        '''
        Set up method to run before each test case
        '''
        self.new_palindrome = Palindrome("Madam")
        #create palindrome object

    def test_init(self):
        '''
        correct initialization
        '''
        self.assertEqual(self.new_palindrome.palindrome,"Madam")

    def test_save_palindrome(self):
        '''
        if palindrome entered is saving
        '''
        self.new_palindrome.save_palindrome()
        self.assertEqual(len(Palindrome.palindrome_list),1)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Palindrome.palindrome_list = []

    def test_save_multiple_palindromes(self):
        self.new_palindrome.save_palindrome()
        test_palindrome = Palindrome("level")
        test_palindrome.save_palindrome()
        self.assertEqual(len(Palindrome.palindrome_list),2)

    def test_display_palindromes(self):
        '''
        method that returns a list of all palindromes
        '''
        self.new_palindrome.save_palindrome()
        test_palindrome = Palindrome("level")
        test_palindrome.save_palindrome()

        self.assertEqual(Palindrome.display_palindromes(), Palindrome.palindrome_list)

if __name__ == '__main__':
    unittest.main()
