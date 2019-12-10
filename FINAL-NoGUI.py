from encode import encode
from decode import decode

def enc():
    text = input("What would you like to encrypt?\n\nIf it is a file than it needs to end in .txt encoded in unicode\nIf it is just text than go crazy: ")
    encode(text)
    input("\n\n\nPress any key to continue...")

def dec():
    decode()
    input("\n\n\nPress any key to continue...")

def decide():
    decision = input("Would you like to encrypt or decrypt? (e/d): ").lower()
    while decision != 'e' and decision != 'd':
        decision = input("Would you like to encrypt or decrypt? (e/d): ").lower()

    return decision

def main():

    decision = decide()
    if decision == 'e':
        enc()
    else:
        dec()


main()
