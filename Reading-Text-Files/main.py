# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    opened_file = open(filename) 
    read_file_content = opened_file.read()
    stripped_content = read_file_content.strip(" ")
    split_content = stripped_content.split()
    return split_content


def count_words(text):
    temp_dictionary = {}
    # [assignment] Add your code here
    for x in text:
        index = text.count(x)
        temp_dictionary[x]=index
    return temp_dictionary
    
filename = "story.txt"
text = read_file_content(filename)
final_dictionary = count_words(text)
print(final_dictionary)
