from stats import * 

def get_book_text(file):
    with open(file) as f:
        return f.read()

def main():
    book = get_book_text("./books/frankenstein.txt")
    word_count = get_word_count(book) 
    chars = get_character_count(book)
    newList = get_sorted_list(chars)
    print_sorted_list(newList, word_count)


if __name__ == '__main__':
    main()


