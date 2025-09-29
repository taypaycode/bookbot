def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def word_count(text):
    words = text.split()

    return len(words)


def main():
    book_path = "./books/frankenstein.txt"
    book_text = get_book_text(book_path)

    total_words = word_count(book_text)

    print(f"Found {total_words} total words")

main()

