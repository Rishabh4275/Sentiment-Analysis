import pylab as plt
import numpy as np

import csv

f = open('Freq.csv')
csv_f = csv.reader(f)

names = []
votes = []

#csv_f.transpose()
for row in csv_f:
  names.append(row[0])
  votes.append(int(row[1]))
    
print names
print type(names)
print type(votes)
print votes

# Split the dictionary of name:votes into two lists, one for names and one for vote count
#for radish in counts:
 #   names.append(radish)
  #  votes.append(counts[radish])

# The X axis can just be numbered 0,1,2,3...
x = list(np.arange(len(votes)))
print type(x)
print x
x=[1,2,3,4,5,6,7,8,9,10]
plt.bar(x ,votes)
plt.xticks(x , names, rotation=90)
plt.show()
