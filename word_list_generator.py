from itertools import product
import string

min_len = 4
max_len = 4
counter = 0
#char = string.ascii_uppercase + string.digits + string.ascii_lowercase
char = string.digits
#char = string.ascii_uppercase

file_open = open("WordList.txt", 'w')

for i in range(min_len, max_len + 1):
    for j in product(char, repeat=i):
        word = "".join(j)
        file_open.write(word)
        file_open.write("\n")
        counter += 1
print("Wordlist of {} passwords created".format(counter))
