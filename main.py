
def main():
    path_to_book = "books/frankenstein.txt"
    file_contents = get_book_text(path_to_book)
    words = get_word_count(file_contents)
    file_contents_lower = file_contents.lower()
    character_dictionary  = get_char_dict(file_contents_lower)

    #filters dictionary for only alphabetical characters
    filtered_dict = {key: value for key, value in character_dictionary.items() if key.isalpha()}

    #sortes dictionary into ascending order
    sorted_filtered_dict = sorted(filtered_dict.items(), key=lambda item: item[1], reverse = True)
    

    print(f"--- Begin report of {path_to_book} ---")
    print(f"There are {words} words in this book.")

    for character, number in sorted_filtered_dict:
        print(f"The '{character}' character was found '{number}' times ")
    print(f"---- End Report ----")

# pulls text from text file
def get_book_text(path):
    with open(path) as f:
        return f.read()

# makes a dictionary of each character within the text
def get_char_dict(text):
    character_dict = {}
    for letter in text:
        if letter in character_dict:
            character_dict[letter] += 1
        else:
            character_dict[letter] = 1
    return character_dict

# returns the word count of the book
def get_word_count(text):
    words = text.split()
    return len(words)


main()



