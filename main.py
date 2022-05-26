# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    list_1 = list(word.lower().replace(" ", ""))
    list_2 = list(anagram.lower().replace(" ", ""))

    if sorted(list_1) == sorted(list_2):
        return True
    else:
        return False

print(find_anagram('Eleven plus two', 'Twelve plus one'))

