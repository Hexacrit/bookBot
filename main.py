from stats import get_word_count, get_character_count

def get_book_text(file):
    with open(file) as f:
        return f.read()

def main():
    book = get_book_text("./books/frankenstein.txt")
    print(get_word_count(book))
    print(get_character_count(book))

if __name__ == '__main__':
    main()


