import random
import networkx as nx
import matplotlib.pyplot as plt
import EoN

# Set the number of generations
generations = 10

# Creates array for 10 generations
virus = [[] for i in range(generations)]

# Sets first virus generation and picks heads or tails.
virus[0] = [[1, random.choice([True,False])]] # True is heads(1), False is tails(2)

# Moves person count to 2
person_count = 2

# Prints current virus state
#print(virus)

# For loop over the 10 generations in the array.
for i in range(1,generations):
    # Pulls the last virus generation
    per_virus = virus[i-1]
    
    # Loops over the last virus generation
    for person in per_virus:
        
        # if the last virus generation had heads of tails to either generate and link one or two people to it.
        if (person[1]): # Heads for only one person, increments once and adds one person
            virus[i].append([person_count, random.choice([True,False]), person[0]])
            person_count += 1
        else: # Tails for two people, increments twice and adds two people
            virus[i].append([person_count, random.choice([True,False]), person[0]])
            person_count += 1
            virus[i].append([person_count, random.choice([True,False]), person[0]])
            person_count += 1


# Prints state of virus after the generations are created.
#print(virus)

# Create graph using networkx
tree = nx.Graph()

# Loop over virus array
for i in virus:
    # Loop over each person in each generation of the virus.
    for person in i:
        # Print that person data
        print(person)
        # Used to ignore the first people in the virus that has no parent as they are the original creator.
        if (person[0] != 1):
            tree.add_edge(person[0], person[2])

# Used to create the hierarchy layout.
pos = EoN.hierarchy_pos(tree,1)    
# Draws the graph using the hierarchy layout and with labels on the nods.
nx.draw(tree, pos=pos, with_labels=True)
# Saves the graph to hierarchy.png
plt.savefig('hierarchy.png', dpi=250)
# Shows the graph once the python script has completed.
plt.show()