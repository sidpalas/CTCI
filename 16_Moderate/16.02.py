# Design a method to find the frequency of occurences of any given word in a book.
# What if we were running the algorithm multiple times

# you will have to touch each word at least once to determine thisself.
# should variants of the same word (singular vs plural, etc...) be considered a single word or not?
#
# If just looking for a single word you could just keep a count of that word as you go through the book...
#
# ...if you want to speed up for future runs you could create hash table using the word as the key and keep a running count as the value
# after finishing going through the book this hashtable can be used to look up the frequency



def countFrequencyOfWord(inputWord,book):
    count = 0
    for word in book.split(' '):
        # make lowercase, remove special characters, etc...
        if word == inputWord:
            count += 1
    return count

class Book:
    def __init__(self, bookText):
        self.processed = False
        self.bookText = bookText

    def preProcessBook(self):
        self.wordDict = dict()
        for word in self.bookText.split(' '):
            # make lowercase, remove special characters, etc...

            if word in self.wordDict:
                self.wordDict[word] += 1
            else:
                self.wordDict[word] = 1
        return

    def countFrequencyOfWord(self, inputWord):
        if self.processed == False:
            self.preProcessBook()
            self.processed = True
        if inputWord in self.wordDict:
            return self.wordDict[inputWord]
        else:
            return 0

testBook = "Hello this is a very short book"

print(countFrequencyOfWord('this', testBook))
print(countFrequencyOfWord('NOTINBOOK', testBook))

testBookInstance = Book( testBook )

print(testBookInstance.countFrequencyOfWord('this'))
print(testBookInstance.countFrequencyOfWord('NOTINBOOK'))
