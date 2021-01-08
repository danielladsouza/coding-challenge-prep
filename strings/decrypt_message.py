"""
    decrypt_message.py
    Messages consist of lowercase latin letters only, and every word is
    encrypted separately as follows:

    Convert every letter to its ASCII value. Add 1 to the first letter, and
    then for every letter from the second one to the last one, add the value
    of the previous letter. Subtract 26 from every letter until it is in the
    range of lowercase letters a-z in ASCII. Convert the values back to
    letters.

    Hint - Generate more test cases
    Write an encrypt() function to do this
"""


def decrypt(word):
    sub_value = 1
    decrypted = ''
    # For improved space complexity we are manipulating one character at a time
    for c in word:  # TC O(N)
        # Keep track of the previous value
        prev_value = ascii_value = ord(c)
        # Manipulation of the data
        ascii_value -= sub_value
        # sub_value += prev_value
        # Normalization Step
        while ascii_value < ord('a'):  # TC O(1)
            ascii_value += 26

        # The previous value becomes the new value we need to subtract
        sub_value = prev_value
        decrypted += chr(ascii_value)  # SC O(N)

    return decrypted


def encrypt(word):
    add_value = 1
    prev_value = 0

    encrypted = ''
    for c in word:
        prev_value = ascii_value = ord(c)
        ascii_value += add_value

        while ascii_value > ord('z'):
            ascii_value -= 26

        add_value += prev_value
        encrypted += chr(ascii_value)
    return encrypted


assert(encrypt('crime') == 'dnotq')


assert (decrypt('dnotq') == 'crime')
assert (decrypt('flgxswdliefy') == 'encyclopedia')
print("TC O(N) SC O(a)")

print(encrypt('newyear'))
print(decrypt('olarohr'))
print(encrypt('encyclopedia'))




