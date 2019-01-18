"""
Word Counter

author: Mitchell Thomas

"""
import operator
import sys

# Read in fileRead

file = open(sys.argv[1], "r")

text = file.read()

file.close()

# Count the words

words = {}

for x in text.split():
    if x.lower() in words:
        words[x.lower()] += 1
    else:
        words[x.lower()] = 1

sortedWords = sorted(words.items(), key=operator.itemgetter(1), reverse=True)

# Write the counted words into a new file

file = open(sys.argv[1][:-4] + "-count" + sys.argv[1][-4:], "w")

file.write("Total Words - {}\nUnique Words - {}\n".format(len(text.split()), len(sortedWords)))
for stats in sortedWords:
    file.write("{} - {}\n".format(stats[0], stats[1]))

file.close()

print("Your file is ready.")
