import hashlib
import math
import time


#Read passwords from a file
def load_file(filename):

    words = []

    with open(filename, "r", encoding="latin-1") as file:

        for line in file:
            word = line.strip()
        
            if word:
                words.append(word)

    return words


# Get hash positions for a password
def hash_password(password, size, hash_count):

    positions = []

    data = password.encode("latin-1")

    hash1 = int(hashlib.sha256(b"1" + data).hexdigest(), 16)
    hash2 = int(hashlib.sha256(b"2" + data).hexdigest(), 16)

    for i in range(hash_count):

        position = (hash1 + i * hash2) % size

        positions.append(position)

    return positions


#Add to the Bloom Filter
def add_password(password, bit_array, size, hash_count):

    positions = hash_password(password, size, hash_count)

    for position in positions:

        bit_array[position] = 1


# Check if a password exists
def check_password (password, bit_array, size, hash_count):

    positions = hash_password(password, size, hash_count)

    for position in positions:

        if bit_array[position] == 0:
            return False

    return True

def main():

    start_time = time.time()

    # Load files
    rockyou = load_file("rockyou.ISO-8859-1.txt")
    dictionary = load_file("dictionary.txt")

    print("Rockyou passwords:", len(rockyou))
    print("Dictionary passwords:", len(dictionary))

    #Bloom Filter settings
    expected_items = len(rockyou)
    target_fpr = 0.01

    size = math.ceil(
        -expected_items * math.log(target_fpr)
        / (math.log(2) ** 2)
    )

    hash_count = round(
        (size / expected_items) * math.log(2)
    )

    # Create bit array
    bit_array = [0] * size

    # Load rockyou passwords into Bloom Filter
    for password in rockyou:

        add_password(password, bit_array, size, hash_count)

    # Create exact set for comparison
    rockyou_set = set(rockyou)

    # Counters
    true_positive = 0
    true_negative = 0
    false_positive = 0
    false_negative = 0

    #Test dictionary passwords
    for password in dictionary:

        actual = password in rockyou_set

        result = check_password(
            password, bit_array, size, hash_count
        )

        if actual and result:
            true_positive += 1

        elif not actual and not result:
            true_negative += 1

        elif not actual and result:
            false_positive += 1

        elif actual and not result:
            false_negative += 1

    # Calculate false positive rate
    if false_positive + true_negative > 0:

        fpr = false_positive / (
            false_positive + true_negative
        )

    else:
        fpr = 0

    # Calculate projected false positive rate
    projected_fpr = (
        1 - math.exp(-hash_count * len(rockyou) / size)
    ) ** hash_count

    #Calculate runtime
    end_time = time.time()
    runtime = end_time - start_time

    # Display results
    print("\n========== RESULTS ==========")

    print("Bit array size:", size)
    print("Hash functions:", hash_count)

    print("\nTrue Positive:", true_positive)
    print("True Negative:", true_negative)
    print("False Positive:", false_positive)
    print("False Negative:", false_negative)

    print("\nActual False Positive Rate:", fpr * 100, "%")
    print("Projected False Positive Rate:",
          projected_fpr * 100, "%")

    print("Runtime:", runtime, "seconds")

    print("=============================")


if __name__ == "__main__":
    main()
