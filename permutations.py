from itertools import permutations

#max len is maximum length of passwords - default is 12, change to bigger if needed
MAX_LEN = 12

# READ WORD LIST FROM input FILE
word_list = []
print("Reading input file...")
with open("input.txt") as wordlist:
    for line in wordlist:
        word_list.append(line.rstrip())
print("Word list created...proceeding with permutations")

# building list of possible permutations that have len of maximum MAX_LEN
powerset_list = []
for n in range(1, len(word_list)+1):
    for perm in permutations(word_list, n):
        wrd = "".join(perm)
        if len(wrd) < MAX_LEN:
            powerset_list.append(wrd)

#write the list of permutations in the output file
with open("output_list.txt", "w") as output_file:
    for item in powerset_list:
        output_file.write("%s\n" % item)
