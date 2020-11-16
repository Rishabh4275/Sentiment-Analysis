from senti_classifier import senti_classifier
import fileinput
sentences = open("poe.txt").read()
a=0
b=0
#sentences = ['The movie was the worst movie', 'It was the worst acting by the actors']
for x in sentences:
    pos_score, neg_score = senti_classifier.polarity_scores(x)
   # print pos_score, neg_score
    a+= pos_score
    b+=neg_score
wn = open("senti_classifier result.txt", "w")
wn.write("Positive Sentences\n")
wn.write(str(a))
wn.write("Negative Sentences\n")
wn.write(str(b))
print "positive score",a,"\n negative score",b
