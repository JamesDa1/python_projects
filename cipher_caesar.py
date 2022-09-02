from string import ascii_uppercase

PLAINTEXT = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
CIPHERTEXT = "QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD"


def cipher_caesar_encrypt(plain_text, shift=23):
    """Take str input, and shift, returns encrypted string"""
    alphabet = [x for x in ascii_uppercase]
    numbers = [x for x in range(len(alphabet))]
    letters = {key: val for key, val in zip(numbers, alphabet)}

    cipher_text = ""
    for char in plain_text.upper():
        if char.isalpha():
            shifted_letter = ((ord(char) - 65) + shift) % 26
            cipher_text += letters[shifted_letter]
        else:
            cipher_text += char
    return cipher_text


def cipher_caesar_decrypt(cipher_text, shift=23):
    alphabet = [x for x in ascii_uppercase]
    numbers = [x for x in range(len(alphabet))]
    letters = {key: val for key, val in zip(numbers, alphabet)}

    plain_text = ""

    for char in cipher_text.upper():
        if char.isalpha():
            shifted_letter = ((ord(char) - 65) - shift) % 26
            plain_text += letters[shifted_letter]
        else:
            plain_text += char
    return plain_text


encoded_text = cipher_caesar_encrypt(PLAINTEXT)
decoded_text = cipher_caesar_decrypt(CIPHERTEXT)
