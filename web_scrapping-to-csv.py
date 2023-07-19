import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

# html = urlopen('https://en.wikipedia.org/wiki/Wikipedia:WikiProject_National_Basketball_Association/National_Basketball_Association_team_abbreviations')

html = urlopen('https://stats.espncricinfo.com/ci/content/records/83548.html')
bs = BeautifulSoup(html, 'html.parser')

table = bs.findAll('table', {'class': 'wikitable'})[0]
rows = table.findAll('tr')

csvFile = open('nba_team_short.csv', 'wt+')
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
            writer.writerow(csvRow)
finally:
    csvFile.close()