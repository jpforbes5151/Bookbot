# reading the file and printing out the entirety of the text

path_to_book = "/home/jpforbes/workspace/github.com/jpforbes5151/bookbot/books/frankenstein.txt"
with open(path_to_book) as f:
    file_contents = f.read()

# splitting the text into words

words = file_contents.split()
print(words[0])

#count lwords in all of the text

character_dict = {}
for letter in file_contents:
    if letter in character_dict:
        character_dict[letter] += 1
    else:
        character_dict[letter] = 1
        
print(character_dict["a"])



