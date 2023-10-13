# reading the file and printing out the entirety of the text
    path_to_book = "/home/jpforbes/workspace/github.com/jpforbes5151/bookbot/books/frankenstein.txt"
    with open(path_to_book) as f:
        file_contents = f.read()

# splitting the text into words

words = file_contents.split()
#print(words[0])

#count words in all of the text

character_dict = {}
file_contents_lower = file_contents.lower()
for letter in file_contents_lower:
    if letter in character_dict:
        character_dict[letter] += 1
    else:
        character_dict[letter] = 1

# sorting and removing non-needed characters

# Filtering the dictionary to remove non-alphabet characters
filtered_dict = {key: value for key, value in character_dict.items() if key.isalpha()}

# sorting the filtered dictionary in descending order
sorted_filtered_dict = sorted(filtered_dict.items(), key=lambda item: item[1], reverse = True)


# Printing report

print(f"--- Begin report of books/frankenstein.txt ---")
for character, number in sorted_filtered_dict:
    print(f"The '{character}' character was found '{number}' times ")
print(f"---- End Report ----")






