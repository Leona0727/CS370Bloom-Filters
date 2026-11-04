Bloom Filter
Description

This project implements a Bloom Filter to detect weak passwords. The Bloom Filter is loaded with passwords from rockyou.ISO-8859-1.txt and tests passwords from dictionary.txt. SHA256 is used with Double Hashing to generate multiple hash positions.

Requirements
Python 3, hashlib, math, time
All required libraries are included in Python's standard library.

Files
main.py: Bloom Filter implementation
rockyou.ISO-8859-1.txt: Password dataset
dictionary.txt: Dictionary dataset

How to Run
Place all files in the same directory.
Run the following command:
bash
python3 main.py

Bloom Filter Configuration
Target False Positive Rate: 1%
Bit Array Size: 137491720 bits
Number of Hash Functions: 7
Hashing Method: SHA256 with Double Hashing
Output

The program displays:

True Positive
True Negative
False Positive
False Negative
Actual False Positive Rate
Projected False Positive Rate
Runtime
Encoding

Both password files are loaded using latin-1 encoding to support the provided datasets.
