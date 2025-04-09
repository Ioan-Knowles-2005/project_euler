# XOR Decryption
#Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). 
# For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
#A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value,
#taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text,
#restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
#For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of 
# random bytes. The user would keep the encrypted message and the encryption key in different locations, and without
#both "halves", it is impossible to decrypt the message.
#Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key.
#If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message.
#The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.
 
# decrypt the message and find the sum of the ASCII values in the original text.

import itertools

def read_encrypted_file(filename):
    """
    Reads a file containing comma-separated integers (ASCII codes)
    representing the encrypted message.
    """
    with open(filename, 'r') as f:
        data_str = f.read().strip()
    return list(map(int, data_str.split(',')))

def decrypt(cipher_bytes, key):
    """
    Decrypts the cipher_bytes using the key (a tuple of 3 ASCII values)
    repeated cyclically.
    Returns a list of decrypted ASCII values.
    """
    plaintext = []
    key_len = len(key)
    for i, val in enumerate(cipher_bytes):
        plaintext.append(val ^ key[i % key_len])
    return plaintext

def is_printable(decrypted_bytes):
    """Return True if at least 95% of the bytes are in the printable ASCII range."""
    printable_count = sum(32 <= b <= 126 for b in decrypted_bytes)
    return printable_count >= 0.95 * len(decrypted_bytes)

def english_score(decrypted_bytes):
    """
    Returns a score based on how 'English-like' the decrypted text is.
    We add points for:
      - Spaces,
      - Frequent English letters,
      - And the presence of common words.
    """
    text = ''.join(chr(b) for b in decrypted_bytes)
    score = 0
    # Award points for spaces and common letters
    for ch in text:
        if ch == ' ':
            score += 5
        elif ch.lower() in 'etaoinshrdlu':
            score += 1
    # Bonus points for common words (you can adjust these values)
    common_words = [" the ", " and ", " to ", " of ", " in "]
    for word in common_words:
        if word in text.lower():
            score += 50
    return score

def find_key(cipher_bytes, key_length=3):
    """
    Tries all combinations of 3 lowercase letters as the key.
    Returns the key (tuple of 3 ASCII values) that gives the highest English score.
    """
    letters = range(ord('a'), ord('z')+1)
    best_key = None
    best_score = -1
    for key in itertools.product(letters, repeat=key_length):
        decrypted = decrypt(cipher_bytes, key)
        if not is_printable(decrypted):
            continue
        score = english_score(decrypted)
        if score > best_score:
            best_score = score
            best_key = key
    return best_key, best_score

def xor_decryption_main(filename='problem_59_cipher.txt'):
    """
    Main driver function:
      - Reads the encrypted message.
      - Assumes the key length is 3.
      - Finds the key by scoring all 3-letter lowercase keys.
      - Decrypts the message.
      - Prints the key, a preview of the plaintext, and the sum of
        ASCII values in the plaintext.
    """
    cipher_bytes = read_encrypted_file(filename)
    
    key, score = find_key(cipher_bytes, key_length=3)
    if not key:
        raise ValueError("No suitable key found.")
    
    plaintext_bytes = decrypt(cipher_bytes, key)
    ascii_sum = sum(plaintext_bytes)
    plaintext_str = ''.join(chr(b) for b in plaintext_bytes)
    
    print("Key found:", ''.join(chr(k) for k in key), "with score", score)
    print("Plaintext:", plaintext_str)
    print("Sum of ASCII values:", ascii_sum)
    
    return ascii_sum

# Run the decryption:
result = xor_decryption_main('problem_59_cipher.txt')
