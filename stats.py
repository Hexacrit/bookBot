import sys

def get_word_count(book):
    word_count = 0
    for _ in book.split():
        word_count += 1
    return word_count

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
        if key.isalpha():
            tempDict = {'char' : key, 'num' : val}
            list_of_char_counts.append(tempDict)
    sorted_list = sorted(list_of_char_counts, key=lambda x: x['num'], reverse=True)
    return sorted_list

def print_sorted_list(sorted_list, word_count):
    print(f"""============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------""")
   #print(get_word_count(sorted_list))
    for item in sorted_list:
         print(f'{item['char']}: {item['num']}')
