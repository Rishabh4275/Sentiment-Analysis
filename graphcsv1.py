import csv
import plotly.plotly as py
 
#----------------------------------------------------------------------
def plot_counties(csv_path):
    """
    http://census.ire.org/data/bulkdata.html
    """
    counties = {}
    county = []
    pop = []
 
    counter = 0
    with open(csv_path) as csv_handler:
        reader = csv.reader(csv_handler)
        for row in reader:
            if counter  == 0:
                counter += 1
                continue
            county.append(row[1])
            pop.append(row[1])
 
    trace = dict(x=county, y=pop)
    data = [trace]
    py.plot(data, filename='ia_county_populations')
 
if __name__ == '__main__':
    csv_path = 'freq.csv'
    plot_counties(csv_path)
