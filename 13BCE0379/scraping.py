import csv
import requests
from BeautifulSoup import BeautifulSoup
import os
x=os.getcwd()
#print(os.path.abspath(__file__))
for file in os.listdir(data):
   # print(file)
    if file.endswith(".txt"):
        print(file)
    url = 'http://millercenter.org/president/speeches#washington'
    response = requests.get(url)
    html = response.content

    soup = BeautifulSoup(html)
    table = soup.find('tbody', attrs={'class': 'stripe'})

    list_of_rows = []
    for row in table.findAll('tr','George Washington')[1:]:
        list_of_cells = []
        for cell in row.findAll('td'):
            text = cell.text.replace('&nbsp;', '')
            list_of_cells.append(text)  
        list_of_rows.append(list_of_cells)

    outfile = open("./inmates.csv", "wb")
    writer = csv.writer(outfile)
    writer.writerow(["Transcription"])
    writer.writerows(list_of_rows)
