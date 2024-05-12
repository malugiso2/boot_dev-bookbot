#!/bin/python
import sys

BOOK_PATH="books/frankenstein.txt"

def main():
    with open(BOOK_PATH) as f:
        file_contents = f.read()
        print(file_contents)

if __name__ == '__main__':
    sys.exit(main())
