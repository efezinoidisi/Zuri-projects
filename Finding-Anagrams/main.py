# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


#function to check if two strings are anagrams
def find_anagram(word, anagram):
    # [assignment] Add your code here
    if len(word)!= len(anagram):      #check if they have the same length
        return False
    else:
        if sorted(word) != sorted(anagram):    #arrange both strings in an alphabetical order
            return False
        else:
            return True
            
            
print(find_anagram("hello","check"))
print(find_anagram("below","elbow"))