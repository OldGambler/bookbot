import sys
from stats import num_words
from stats import num_characters
from stats import sorted_dictionary

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    num = num_words(text)
    chars = num_characters(text)
    sort_dict = sorted_dictionary(chars)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found " + str(num) + " total words")
    print("--------- Character Count -------")
    for item in sort_dict:
        char = item["char"]
        count = item["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

main()
