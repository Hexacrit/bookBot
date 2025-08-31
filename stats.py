
def get_word_count(book):
    word_count = 0
    for _ in book.split():
        word_count += 1
    return f'{word_count} words found in the document'

def get_character_count(book):
    chars = {}
    for char in book:
        new_char = char.lower()
        if new_char not in chars:
            chars[new_char] = 1
        else:
            chars[new_char] += 1
    return chars

