from stats import get_book_text, word_count, char_count, sort_output


def main():
    book_path = "./books/frankenstein.txt"
    
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

main()

