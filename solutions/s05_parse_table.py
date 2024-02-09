"""Parse the table into a dictionary."""

PATH = "s05_table.txt"
dictionary = {}

with open(PATH, "r") as reader:
    # read one line at a time
    for i, line in enumerate(reader):
        # ignore even lines
        if i % 2 == 0 or i == 1:
            continue
        # remove | = replace with ''
        line = line.replace("|", "")
        # split on empty space
        alphabet, freq, percentage = line.split()

        # record the three entries
        dictionary[alphabet] = int(freq)

print(dictionary)
