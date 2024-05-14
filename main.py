#!/bin/python

import sys


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    wc = get_word_count(text)
    print(f"Number of words {wc}")

    letter_occurance = get_char_dict(text)
    print(f"letter dict {letter_occurance}")
    # for key in letter_occurance:
    #     print(f"{key}: {letter_occurance[key]}")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    words = text.split()
    return len(words)


def get_char_dict(text):
    result = {}

    for c in text.lower():
        if c in result:
            result[c] += 1
        else:
            result[c] = 1

    return result


if __name__ == "__main__":
    sys.exit(main())
