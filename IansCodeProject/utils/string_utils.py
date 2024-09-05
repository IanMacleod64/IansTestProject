import re
def count_vowels():
    vowel= re.compile(r'[aeiouAEIOU]')
    print('Enter a word or sentence and I will give you to number of vowels the statement holds!')
    response = input()
    vowel_total = vowel.findall(response)
    if (len(vowel_total)) == 0:
        print('That is not a proper word or sentence. Please Try again.')
    else:
        print(len(vowel_total))

def is_palindrome():
    print('Please give a word and I will confirm if it is a palindrome or not.')
    pali = input()
    pali = pali.lower()
    if pali == pali[::-1]:
        print('True')
    else:
        print('False')
