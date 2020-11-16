import string
import csv
import pylab as plt
import numpy as np

def compareItems((w1,c1), (w2,c2)):
    if c1 > c2:
        return - 1
    elif c1 == c2:
        return cmp(w1, w2)
    else:
        return 1

def main():
    print "This program analyzes word frequency in a file"
    print "and prints a report on the n most frequent words.\n"

    # get the sequence of words from the file
    # fname = raw_input("File to analyze: ")
    text = open('randomshit3.txt','r').read()
    text = string.lower(text)
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
        text = string.replace(text, ch, ' ')
    words = string.split(text)

    # construct a dictionary of word counts
    counts = {}
    x=0
    y=0
    for w in words:
        counts[w] = counts.get(w,0) + 1
        x=x+1

    print x
    # output analysis of n most frequent words.
    items = counts.items()
    
    items.sort(compareItems)
    print type(items)
    for k in items:
        y+=1
    print y
    #for k,v in items:
     #   y=y+k;
    n = input("Output analysis of how many words? ")
    fout=open('Freq.csv','w')
    a=csv.writer(fout,delimiter=',')
    for i in range(n):
        print "%-10s%5d" % items[i]
        a.writerow(items[i])    
        #a.writerow("%-10s%5d" % items[i])
        #fout.write('\n')
    fout.close()
    raw_input()
    

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
    #print type(x)
    #print x
    #x=[1,2,3,4,5,6,7,8,9,10]
    plt.bar(x ,votes)
    plt.xticks(x , names, rotation=90)
    plt.show()

if __name__ == '__main__': main()
