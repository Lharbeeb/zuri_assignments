# Check if a word is an anagrams
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True
from posixpath import split


def find_anagrams(subject, anagram):
    word1=":".join(subject)
    word2=":".join(anagram)
    list1=word1.split(":")
    list2=word2.split(":")
    list1.sort()
    list2.sort()
    if list1 == list2:
        return "True"
    else:
        return "False"

print(find_anagrams("cream", "carem"))
print(find_anagrams("red", "rad"))
