import pickle

def decode():

    ##Opens the neccessary files (the encoded message and the key)
    try:
        inputfile = open("encoded.txt", 'r')
        keyFile = open('key.jstn', 'rb')
        output = open('decoded.txt','w')
    except FileNotFoundError:
        print("There is not any file to decrypt. Please encrypt something first.\n\n")

    ##Declaring the variables used
    
    outputDecoded = ''

    ##Gets the key dictionary from the file
    try:
        key = pickle.load(keyFile)
    except UnboundLocalError:
        pass

    ##This part goes through the encoded message line by line letter by letter.
    ##If the letter in the line is white space than the white space is passed
    ##Along to the decoded output, otherwise, it gets the key and the corresponding
    ##Value from the key and checks the encoded letter for the decoded value and
    ##Appends it to the decoded output string
    try:
        for lines in inputfile:
            for letter in lines:
                if letter.isspace() == True:
                    outputDecoded = outputDecoded + letter
                else:
                    for kv, vk in key.items():
                        if vk == letter:
                            outputDecoded = outputDecoded + kv
    except UnboundLocalError:
        pass

    ##Prints the decoded message, closes the file, and writes the decrypted message
    ##to a file.
    try:           
        print(outputDecoded)
        inputfile.close()
        keyFile.close()
        output.write(outputDecoded)
    except UnboundLocalError:
        pass
    
    return outputDecoded

if __name__ == "__main__":
    decode()
    input("\n\n\nPress enter to exit...")

