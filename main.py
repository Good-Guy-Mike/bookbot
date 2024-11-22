def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_freq(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    report_letter_counts(num_letters)
    print("--- End report ---")
    

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_freq(text):
    letter_count = {}
    lowered_string = text.lower()
    for letter in lowered_string:
        if letter in letter_count:
            letter_count[letter] += 1
        elif letter.isalpha():
            letter_count[letter] = 1
    return letter_count

def report_letter_counts(letter_count):
    sorted_letters = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)
    for letter, count in sorted_letters:
        print(f"The '{letter}' character was found {count} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()




"""
def letter_sorter(num_letters):
    list_of_letters = []
    for letter in num_letters:
        value = num_letters[letter]
        list_of_letters.append({letter: value})
    list_of_letters.sort(reverse=True, key=lambda x: list(x.values())[0])
    return list_of_letters

def letter_report(sorted_list):
    for item in sorted_list:  
        for letter in item:  
            number = item[letter]  
            print(f"The '{letter}' character was found {number} times")
"""
