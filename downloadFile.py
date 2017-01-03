from urllib import request

goog_url = "http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=0&e=3&f=2017&g=d&a=7&b=19&c=2004&ignore=.csv"
destination = r'goog.csv'


def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = str(response.read())
    lines = csv.split("\\n")
    fw = open(destination, 'w')
    for line in lines:
        fw.write(line + "\n")
    fw.close()

download_stock_data(goog_url)

fr = open(destination, 'r')
x = fr.read()
print(x)
fr.close()
