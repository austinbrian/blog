with open('../datasets/Austin_family_tree.txt','rU') as f:
    data = [row.split('\n') for row in f]

# First generation are the first two lines
gen_1 = data[:1]

# After the first generation, the gens are bracketed with 4 dashes
for i in data[2:]
