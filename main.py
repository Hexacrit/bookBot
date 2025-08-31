from stats import * 
import sys

def get_book_text(file):
    with open(file) as f:
        return f.read()

def main():
    try:
        book = get_book_text(sys.argv[1])
        word_count = get_word_count(book) 
        chars = get_character_count(book)
        newList = get_sorted_list(chars)
        print_sorted_list(newList, word_count)
       # sys.exit(0)
    except:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


if __name__ == '__main__':
    main()


