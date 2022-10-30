def palindrome(phrase):
    phrase = phrase.replace(' ', '')
    phrase = phrase.lower()
    phrase_inverted = phrase[::-1]

    return '\npalindrome' if phrase == phrase_inverted else '\nnot palindrome'


def app():
    phrase = input("Enter a word of your choice: ")
    print(palindrome(phrase))


if __name__ == '__main__':
    app()
