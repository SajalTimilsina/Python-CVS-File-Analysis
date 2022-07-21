#P1: Count the number of characters.
#P2: Count the number of words (separated by whitespaces, tabs, and newlines characters)
#P3: Count and print the number of unique words (separated by whitespaces, tabs, and newlines characters)
#P4: Count and print the number of lines.
#P5: Find and print the longest word
#P6: Find and print the 10 most common words
#P7: Find and print the 10 least common words.
#P8: Count and print the number of words that begin with each English letter
#P9: List unique words by each English letter.
#P10: Count and print the number of digits.
#All done in step
from collections import Counter
from string import ascii_letters
import time
def countCharacter(file1):

    # read the content of file
    data = file1.read()

    # get length of data
    num_char = len(data)

    print('P1: Number of characters in text file :', num_char)
    return data
def countWords(data):
    words = data.split()

    print('P2: Number of words in text file :', len(words))
    return(words)

def countUnique(words):
    count = 0
    words_set = set(words)
    for word in words_set:
        count += 1

    print('P3: Total Unique Words:', count)
def countLines(filename):
    with open("The_Bible.txt", "r") as fp:
        count = 0
        for line in fp:
            if line != "\n":
                count += 1
    print('P4: Total Lines', count)
def longestWords(filename):
    with open(filename, 'r') as infile:
        words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]



def countfreq(Counter,data_set):
    split_it = data_set.split()
    n = 10
    # Pass the split_it list to instance of Counter class.
    Counter = Counter(split_it)

    # most_common() produces k frequently encountered
    # input values and their respective counts.
    most_occur = Counter.most_common(10)
    least_common = Counter.most_common()[:-n-1:-1]
    print("P6: Most Common 10 Words: ",most_occur)
    print("P7: Least Common 10 Words: ", least_common)

def count_letters(s) :
    filtered = [c for c in s.lower() if c in ascii_letters]
    return print("P8: Count Words start with English Alphabet:",Counter(filtered))

file = open("The_Bible.txt", "r")
data = countCharacter(file)
words = countWords(data)
countUnique(words)
countLines("The_Bible.txt")
print("P5: ",longestWords("The_Bible.txt"))
countfreq(Counter,data)
count_letters(data)

text_file = open('The_Bible.txt', 'r')
text = text_file.read()


text_file = open('The_Bible.txt', 'r')
text = text_file.read()
import re
#cleaning
text = text.lower()
words = text.split()
words = [word.strip('.,!:?;()*"%$#-!<@/+=_[]0123456789') for word in words]
words = [word.replace("'s", '') for word in words]

#finding unique
unique = []
for word in words:
    if word not in unique:
        unique.append(word)

#sort
unique.sort()

#print

print("P9 : unique Values Printing.....\n")
time.sleep(10)
print(unique)





