# define the input data
data = [
    "1, first item",
    "2, second item",
    "3, third item",
    "1, fourth item",
    "2, fifth item",
    "3, sixth item",
    "4, seventh item",
    "1, eighth item",
    "2, ninth item"
]

f = open('test1.csv')
# create a dictionary to store the reordered data
reordered_data = {}

# iterate over each line of the input data
for line in f:
    # split the line into its two parts
    parts = line.split(",")
    key = int(parts[0])
    value = parts[1]
   
    # add the value to the dictionary, using the key as the index
    if key not in reordered_data:
        reordered_data[key] = []
    reordered_data[key].append(value)

# print the reordered data
for key in sorted(reordered_data.keys()):
    if key > 5:
        for value in reordered_data[key]:
            print(value)