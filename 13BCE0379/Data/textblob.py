
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import fileinput
import re
import os
x=os.getcwd()
#print(os.path.abspath(__file__))
for file in os.listdir(x):
   # print(file)
    if file.endswith(".txt"):
        g[]=print(file)
for f in g[]:
{
        x=0
        y=0
        wn = open("analysis10.txt", "w")
        blob = TextBlob(open(f).read())
        for item in blob.sentences:
                if item.sentiment.polarity > 0:
                    print("Positive Sentences")
                    print(item.replace('\n', ' '))
                    print("Polarity: " + str(item.sentiment.polarity))
                    print("Subjectivity" + str(item.sentiment.subjectivity))
                    x+=item.sentiment.polarity
                    y+=1
                    print("\n")
                    item=item.replace('\n', ' ')
                    wn.write("Positive Sentences\n")
                    wn.write(str(item.replace('\n', ' ')))
                    wn.write("\n")
                    wn.write("Polarity: " + str(item.sentiment.polarity))
                    wn.write("\n")
                    wn.write("Subjectivity" + str(item.sentiment.subjectivity))
                    wn.write("\n")
                    wn.write("\n")


            

        blo = TextBlob(open(f).read())
        for item in blo.sentences:
                if item.sentiment.polarity < 0:
                    print("Negative Sentences")
                    print(item.replace('\n', ' '))
                    print("Polarity: " + str(item.sentiment.polarity))
                    print("Subjectivity" + str(item.sentiment.subjectivity))
                    y+=1
                    print("\n")
                    x-=item.sentiment.polarity
                    item=item.replace('\n', ' ')
                    wn.write("Negative Sentence\n")
                    wn.write(str(item.replace('\n', ' ')))
                    wn.write("\n")
                    wn.write("Polarity: " + str(item.sentiment.polarity))
                    wn.write("\n")
                    wn.write("Subjectivity" + str(item.sentiment.subjectivity))
                    
                    wn.write("\n")
                    wn.write("\n")


        print("\nOverall Positivity or Negativity is")
        print(x/y)
        wn.write("\n")
        wn.write("Overall Positivity or Negativity is\n")
        wn.write(str(x/y))
        wn.close()
