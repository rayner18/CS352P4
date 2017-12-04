################################################################
# Charles Rayner CS 352 Project 4: Python
################################################################

import sys
import re
################################################################
# createIndex function:
# - Should print an index of all words in the file. It is presently
# dummied up.
#
# If you do the enhancement where you process multiple files, the
# 'fileName' parameter should be a list of strings rather than
# a single string.
################################################################
def createIndex(fileName) :

    # creates list of lines of file
    lineList = open(fileName).readlines()

    # removes non-alpha from lines, splits, and converts to lowercase
    # allows all single-quotes for now
    for i in range(len(lineList)):
        lineList[i] = re.sub("[^a-zA-Z']+", " ", lineList[i]).lower().split()

    # handles single quotes according to rules listed for enhancement
    for i in range(len(lineList)):
        for j in range(len(lineList[i])):
            if lineList[i][j].startswith("'") and lineList[i][j].endswith("'"):
                lineList[i][j] = lineList[i][j][1:-1]
            elif lineList[i][j].startswith("'"):
                lineList[i][j] = lineList[i][j][1:]

    # creates list of all words
    wordList = []
    for line in lineList:
        for word in line:
            wordList.append(word)

    # removes empty elements from list
    wordList = list(filter(None, wordList))

    # removes duplicates from list
    wordList = list(set(wordList))

    # sorts list
    wordList.sort()

    # initializes list of indexes from list of words
    indexList = []
    for word in wordList:
        indexList.append([word])

    # populates list of indexes by checking if a word appears on a line
    for w in range(len(wordList)):
        for l in range(len(lineList)):
            if wordList[w] in lineList[l]:
                indexList[w].append(l+1)

    # creates list of formatted strings for output
    formattedIndex = []
    for p in indexList:
        item = p[0] + " " + str(p[1])
        for i in range(2, len(p)):
            item+=("," + str(p[i]))
        formattedIndex.append(item)

    # prints formatted list of strings
    for p in formattedIndex: print(p)




################################################################
# main program:
# - prompts user for a file name
# - reads input from user
# - calls createIndex
################################################################

# prompt user and read the input line
fileName = input("Please type the name of a file: ")

# call createIndex
createIndex(fileName)
