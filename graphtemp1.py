import string
import matplotlib.pyplot as plt
import plotly.plotly as py
from plotly.graph_objs import *
import os
import numpy as np
from collections import defaultdict

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
    #n = input("Output analysis of how many words? ")
    n=10
    fout=open('Freq.txt','w')
    for i in range(n):
        print "%-10s%5d" % items[i]
        fout.write("%-10s%5d" % items[i])
        fout.write('\n')
    #raw_input()

    dic = defaultdict(list)
    j=0
    for item in items:                                                                                           
        key = "/".join(item[:-1])
        dic[key].append(item[-1])
        j+=1
        if j>100:
            break;
        
    print dic
    print '\n'

    #plt.bar(range(len(dic)), dic.values(), align='center')
    #plt.xticks(range(len(dic)), dic.keys())

    #plt.show()
    named=[]
    votes=[]
    for radish in dic:
        named.append(radish)
        votes.append(dic[radish])
    print named
    print votes
    print '\n'
    print dic.values()
    print dic.keys()

# The X axis can just be numbered 0,1,2,3...
    #some = np.arange(len(dic))
    #print some
    #plt.bar(some , dic.values() , align='center' , width=0.5)
    #plt.xticks(some , dic.keys())
    #plt.savefig()
    #plt.show()
    #data = [dic.transpose()]
    #print data
    #py.plot(data, filename='Soemthing or trhe other')
    
    data = Data([
        Bar(
            
            
            x = dic.values(),
            y = dic.keys()
        )
    ])
    plot_url = py.plot(data, filename='basic-bar')
    
    
if __name__ == '__main__': main()
