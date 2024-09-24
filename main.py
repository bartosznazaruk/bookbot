def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words = get_word_count(text)
    print(f"--- Begin report of books {book_path} ---")
    print(f"There are {num_words} words in {book_path}")
    word_count = get_book_characters_count(text)
    sorted_count = dict(sorted(word_count.items(), reverse = True, key=lambda item: item[1]))
    for key in sorted_count:
        print(f"The \"{key}\" character occurs {sorted_count[key]} times")
    print("--- End of report ---")

def get_word_count(text):
    count = len(text.split())
    return count

def get_text(path):
    with open(path) as f:
        return f.read()
        
def get_book_characters_count(text):
    text_lowered = text.lower()
    word_dict = {}
    words_lowercase = text_lowered.split()
    for word in words_lowercase:
        for char in word:
            if char in word_dict and char.isalpha():
                word_dict[char] = word_dict[char]+ 1
            elif char.isalpha():
                word_dict[char] = 1
            else:
                continue
            
      
    return word_dict


main()







