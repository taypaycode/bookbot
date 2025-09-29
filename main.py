def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    book_path = "./books/frankenstein.txt"
    book_text = get_book_text(book_path)
    print(book_text)

main()
