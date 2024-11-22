def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters_dict(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_letters_dict(text):
    letter_count = {}
    lowered_string = text.lower()
    for letter in lowered_string:
        if letter in letter_count:
            letter_count[letter] += 1
        elif letter.isalpha():
            letter_count[letter] = 1
    return letter_count


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()