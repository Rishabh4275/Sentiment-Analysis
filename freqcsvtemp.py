import string
import csv
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
    writer = csv.DictWriter(fout, fieldnames = ["Names", "Frequency"], delimiter = ',')
    writer.writeheader()
    a=csv.writer(fout,delimiter=',')
    for i in range(n):
        print "%-10s%5d" % items[i]
        a.writerow(items[i])    
        #a.writerow("%-10s%5d" % items[i])
        #fout.write('\n')
    
    raw_input()

if __name__ == '__main__': main()
