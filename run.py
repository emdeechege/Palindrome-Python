#!/usr/bin/env python3.6
import re
from palindrome import Palindrome

def add_palindrome(palindrome):
    new_palindrome= Palindrome(palindrome)
    return new_palindrome

def save_palindrome(palindrome):
    palindrome.save_palindrome()

def display_palindromes():
    return Palindrome.display_palindromes()

def main():
    print("Hello, Please contribute to our palindrome list by adding your palindrome")

    while True:

        print("Use these short codes : ap - add new palindrome, dp - display palindromes,ex -exit the palindrome list checker ")

        short_code = input().lower()


        if short_code == 'ap':
            print('New Palindrome')
            print("-"*50)
            palindrome = input("Check if word or palindrome is a palindrome: ")

            clean = re.sub(r'[^\w]','',palindrome)
            read_back = clean[::-1].lower()
            no_space = clean.lower()

            if palindrome:
                if read_back == no_space:
                    with open("try.txt","a") as file:
                        file.write(palindrome.capitalize() + '\n')

                    save_palindrome(add_palindrome(palindrome))

                    print('Great! new palindrome created!')
                    print("-"*50)
                else:
                    print("Iko shida")

            else:
                print("*"*50)
                print("Please enter a palindrome or word")
                print("*"*50)

        elif short_code == 'dp':

            if display_palindromes():
                print("Here is a list of Palindromes")
                print('\n')
                for palindromes in display_palindromes():
                    print(palindrome)
                    print('\n')
                    file = open("try.txt","r")
                    for line in file:
                        print (line,)
                    print("-"*50)
            else:
                print('\n')
                print("You don't seem to have any palindromes yet")
                print("-"*50)

        elif short_code == "exit":
            print("Bye .......")
            break
        else:
            print("I really didn't get that. Please use the short codes")
            print("-"*50)

if __name__ == '__main__':

    main()
