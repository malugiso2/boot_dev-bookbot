#!/bin/python

import sys

def main():
    book_path="books/frankenstein.txt"
    text=get_book_text(book_path)
    wc=get_word_count(text)
    print(wc)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)




if __name__ == '__main__':
    sys.exit(main())
