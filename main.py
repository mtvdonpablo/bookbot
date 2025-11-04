from stats import get_book_text
from stats import num_words
from stats import count_char
from stats import sorted_dict
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_contents = get_book_text(sys.argv[1])
    word_count = num_words(file_contents)
    
    char_dict = count_char(file_contents)
    sorted_list = sorted_dict(char_dict)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        else:
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
            
main()