def get book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def word_count(text):
    words = text.split()

    return len(words)


