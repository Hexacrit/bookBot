
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

def get_sorted_list(char_count):
    list_of_char_counts = []
    for key, val in char_count.items():
        tempDict ={key : val}
        list_of_char_counts.append(tempDict)
        list_of_char_counts.sort(reverse=True)
    print(list_of_char_counts)
