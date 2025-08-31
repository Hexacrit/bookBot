def get_book_text(file):
    with open(file) as f:
        return f.read()

def get_word_count(book):
    book.split()
    word_count = 0
    for item in book:
        word_count += 1
    return f'{word_count} words found in the document'


def main():
    book = get_book_text("./books/frankenstein.txt")
    print(get_word_count(book))
if __name__ == '__main__':
    main()


