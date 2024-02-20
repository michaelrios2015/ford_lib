# going to just keep a few title and
formatted = []

# Opening our text file in read only
# mode using the open() function
with open(r"LC.txt", "r") as file:

    # Reading the content of the file
    # using the read() function and storing
    # them in a new variable
    data = file.readlines()

    # this keeps track of where i am in the new list
    counter = 0

    for ind, line in enumerate(data):

        # print(ind)

        if "Title:" in line:
            # print(line)
            # print("--------------")
            line = line.strip()
            if line[-1] == ",":
                line = line[:-1]

            formatted.append(line)
            if ind > 0:
                # print(counter)
                # print((data[ind-2]))
                formatted[counter] += " |" + data[ind - 2].strip()
                counter += 1


formatted[counter] += " |" + data[-1].strip()

print(formatted[0])

with open(r"LCformatted.txt", "w") as fp:
    for item in formatted:
        # write each item on a new line
        fp.write("%s\n" % item)
    print("Done")

import pandas as pd

df = pd.read_csv("RHformatted.txt", sep="|")

print(df[0])
