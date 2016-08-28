
# bmi function
def calculate_bmi(weight, height):
    return (weight/(height * height))

# list of stripped lines
lines = [line.rstrip('\n') for line in open('osebe.txt', 'r')]

# out file
out_file = open("ITM.txt", "a")

# write only the first line with variable names
out_file.write(lines[0]+"\n")


# create weights and heights
weights = []
heights = []
for line in range(1, len(lines)):
    weights.append(float(lines[line].split(",")[1]))
    heights.append(float(lines[line].split(",")[2]))


# write the rest of the stuff
for line in range(1, len(lines)):
    out_file.write(lines[line]+",{0:.2f}".format(calculate_bmi(weights[line-1], heights[line-1]))+"\n")

# close after done writing
out_file.close()
