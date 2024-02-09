"""Caeser Encryption."""
from string import ascii_letters

ACTION = "d" # e or d

if ACTION == "e":
    file_in = "s05_text.txt"
    file_out = "s05_cipher.txt"
    shift = 3
elif ACTION == "d":
    file_in = "s05_cipher.txt"
    file_out = "s05_plain.txt"
    shift = -3
else:
    print("Not a valid option.")
    exit(1)

def shift_alphabet(alphabet):
    if alphabet not in ascii_letters:
        return alphabet
    index = ascii_letters.index(alphabet)
    new_index = (index + shift) % len(ascii_letters)
    return ascii_letters[new_index]

with open(file_in, "r") as reader, open(file_out, "w") as writer:
    for line in reader:
        line_out = "".join(shift_alphabet(a) for a in line)
        writer.write(line_out)
        line_out = ""
