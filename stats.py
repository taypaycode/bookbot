def get_book_text(path_to_file):
    """reads the entire book from a file path"""    
    with open(path_to_file) as f:
        return f.read()
    
def word_count(text):
    """Returns the number of words in the given text"""
    words = text.split()
    return len(words)

def char_count(text):
    """returns a dict of all chars lowercased and their counts"""
    char_dict = {}
    for char in text.lower():
        if char in char_dict:
            char_dict[char] +=1
    
        else: 
            char_dict[char] = 1
    return char_dict

def sort_output(char_dict):
    """convert char_dict to sorted list of dicts with 'char' and 'num' keys"""
    report_list = []

    for char, count in char_dict.items():
        if char.isalpha():
            report_list.append({"char": char, "num": count})


    report_list.sort(key=lambda item:item["num"], reverse=True)

    return report_list
