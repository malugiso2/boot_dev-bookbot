#!/bin/python

import sys


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    wc = get_word_count(text)
    char_dict = get_char_dict(text)
    char_list = get_list_from_dict(char_dict)
    char_list.sort(reverse=True, key=sort_on)

    print_report(wc, char_list)


def print_report(wc, char_list):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{wc} words found in the document")
    print()

    for d in char_list:
        print(f"The '{d["name"]}' character was found {d["num"]} times")

    print("--- End report ---")


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


def get_list_from_dict(dict):
    result = []
    for key in dict:
        if key.isalpha():
            result.append({"name": key, "num": dict[key]})
    return result


def sort_on(dict):
    return dict["num"]


if __name__ == "__main__":
    sys.exit(main())
