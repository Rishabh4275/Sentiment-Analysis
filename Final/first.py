import fileinput
import re

on = open("Proj1.txt", "r")
wn = open("clean2.txt", "a+")
#line=1
for line in on:
    wn.write(line)
    
    #wn.write("\n")
    #line=chr(ord(line[0])+1)
    wn.flush()
wn.close()

for  line in fileinput.FileInput('clean2.txt',inplace=1):
    line=line.replace('(',' ')
    line=line.replace('aV',' ')
    line=line.replace('@',' ')
    line=line.replace('\\',' ')
    line=line.replace('u2026',' ')
    line=line.replace('/',' ')
    line=line.replace('"',' ')
    line=line.replace('RT',' ')
    line=line.replace('#',' ')
    line=line.replace(')',' ')
    line=line.replace('t.co',' ')
    line=line.replace('u000a',' ')
    line=line.replace('I0',' ')
    line=line.replace('dp0',' ')
    line=line.replace('!',' ')
    line=line.replace('$',' ')
    line=line.replace('%',' ')
    line=line.replace('&',' ')
    line=line.replace('*',' ')
    line=line.replace(',',' ')
    line=line.replace(':',' ')
    line=line.replace('@',' ')
    #line=line.replace('\n\n','\n')
    print (line)

f = open('clean2.txt')
text = f.read()
f.flush()
f.close()

clean = re.sub('http:[^\n]+\n', ' ', text)
#clean = clean.replace('\n\n','\n')
#clean = re.sub(' [^:]+:', ' ', text)

f = open('clean3.txt', 'w')
f.write(clean)
f.flush()
f.close()
#
#for  line in fileinput.FileInput('randomshit3.txt',inplace=1):
 #   line=line.replace('\n\n','\n')
  #  print line

    
#for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
    #text = string.replace(text, ch, ' ')
