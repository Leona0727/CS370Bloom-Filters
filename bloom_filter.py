import hashlib
import math
import time

def load_file(filename):

    words = []

    with open(filename, "r", encoding="latin-1") as file:

        for line in file:
            words.append(line.strip())

    return words

def main():

    rockyou = load_file("rockyou.ISO-8859-1.txt")
    dictionary = load_file("dictionary.txt")

    print("Rockyou passwords:", len(rockyou))
    print("Dictionary passwords:", len(dictionary))

    print("\nFirst 5 rockyou passwords:")

    for password in rockyou[:5]:
        print(password)


main()
