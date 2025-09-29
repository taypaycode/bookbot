from stats import get_book_text, word_count, char_count, sort_output
import sys

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)   # non-zero exit code signals an error to the shell

    book_path = sys.argv[1]
    
    book_text = get_book_text(book_path)
    
    total_words = word_count(book_text)

    characters = char_count(book_text)
    
    report_list = sort_output(characters)

    print("============ BOOKBOT ============")
    print("Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    
    for item in report_list:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
