import sys
from stats import count_words, count_character, sort

def get_book_text(file):
    with open(file) as b:
        whole_book = b.read()
    return whole_book

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(sys.argv[1])
    words = count_words(book)
    character = count_character(book)
    sorted_character = sort(character)
    read_time  = estimate_reading_time(words)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("-------- Reading Time -----------")
    print(f"Estimated reading time: {read_time}")
    print("--------- Character Count -------")
    for char in sorted_character:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")
    print("============= END ===============")
    
main()