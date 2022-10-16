"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    TODO:
    """
    print('Welcome to stanCode \"Anagram Generator\" (or -1 to quit)')
    while True:
        enter = input('Find anagrams for: ')
        start = time.time()
        ####################
        if enter == EXIT:
            break
        else:
            print('Searching...')
            anagrams = find_anagrams(enter)
            print(str(len(anagrams)) + ' anagrams: ', end='')
            print(anagrams)
            ####################
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    f = open(FILE, 'r')
    d = []
    for line in f:
        voc = line.split('\n')
        d += voc[:-1]
    f.close()
    return d


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    anagrams = []
    dic = read_dictionary()
    find_anagrams_helper(s, '', anagrams, len(s), dic)
    return anagrams


def find_anagrams_helper(s, anagram, anagrams, ans_len, dic):
    if len(anagram) == ans_len:
        if anagram in dic:
            if anagram not in anagrams:
                print('Found: ' + anagram)
                print('Searching...')
                anagrams += [anagram]
    else:
        for i in range(len(s)):
            # Choose
            anagram += s[i]
            s_new = s[: i] + s[i + 1:]
            # Explore
            if has_prefix(anagram):
                find_anagrams_helper(s_new, anagram, anagrams, ans_len, dic)
            # Un-choose
            anagram = anagram[:-1]


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    dic = read_dictionary()
    exist = -1
    for i in range(len(dic)):
        if dic[i].startswith(sub_s):
            exist *= -1
            break
    if exist > 0:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
