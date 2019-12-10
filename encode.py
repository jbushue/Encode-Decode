from random import randrange
import pickle

def generateKey():

    ##Declaring neccessary variables/opening neccessary files
    
    randomList = []
    dictEncode = {}
    randomAscii = 0
    outputDict = open ('key.jstn', 'wb')

    ##This checks to see if a specific character is already a key in the dictionary
    ##It gets each character using the ASCII table values for letters and important punctuation.
    ##It then gets a random integer from range 33-127. This corresponds to the ASCII
    ##integer value. The value is converted into the ASCII value and stored in a list.
    ##If the ASCII value is already in the list than it gets a new value.
    
    for numbPunctLet in range(33,126):
        if numbPunctLet not in dictEncode:
            randomAscii = randrange(33, 126)
            while chr(randomAscii) in randomList:
                randomAscii = randrange(33, 126)
            randomList.append(chr(randomAscii))
            dictEncode[chr(numbPunctLet)] = chr(randomAscii)

    ##This outputs the key dictionary into a txt file to be used for decoding

    pickle.dump(dictEncode, outputDict)
    outputDict.close()
    
    return dictEncode

def encode(inputFile):
    
    ##Declaring neccessary variables/opening neccessary files

    fileEncoded = open('encoded.txt', 'w')

    ##This section checks the argument passed to the function to see if it is
    ##a text file or if it is a simple string.
    
    if inputFile.endswith('.txt') == True:
        try:
            inputfile = open('SampleTextFiles/' + inputFile,'r')
        except FileNotFoundError:
            print("Looks like you tried to use a txt file. If the text file is not in the SampleTextFile folder than it will not be able to find it. Please try again")
            
            
    else:
        inputfile = inputFile
        
    exampleString = []
    outputEncoded = ''
    dictEncode = generateKey()

    ##This section encodes the original message into an encrypted message.
    try:        
        for lines in inputfile:
            for letter in lines:
                if letter not in dictEncode:    ##if the letter isn't in the key dictionary and it is white space it will be passed along to the encoded message without manipulation
                        if letter.isspace() == True:
                                outputEncoded = outputEncoded + letter
                else:                           ##Otherwise it will get the encrypted letter from the key dictionary and append it on to the encoded output
                    outputEncoded = outputEncoded + dictEncode[letter]
    except UnboundLocalError:
        pass

    ##Closing the files, outputting the encoded message to the console,
    ##and writes the encoded message to a file
    if inputFile.endswith('.txt') == True:
        try:
            inputfile.close()
        except UnboundLocalError:
            pass
    print(outputEncoded)
    fileEncoded.write(outputEncoded)
    fileEncoded.close()

    return outputEncoded

    
if __name__ == "__main__":
    encode("PrideandPred.txt")
    input("\n\nPress any key to continue...")
