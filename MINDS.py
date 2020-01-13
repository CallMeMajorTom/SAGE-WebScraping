import csv
import requests
import datetime
from lxml import html

url='https://en.wikipedia.org/wiki/2019_in_spaceflight#Orbital_launches'
page=requests.Session().get(url)
tree=html.fromstring(page.text)
tableXpath = '/html/body/div[3]/div[3]/div[4]/div/table[3]/tbody[1]/tr'
trList=tree.xpath(tableXpath)
header = trList[0].xpath('.//th')

# Loop Over All tr rows of table
row = 3
res = {}
while row < len(trList):
    if len(trList[row].xpath('.//td[@colspan="7"]')):# The Month Row
        row += 1
        continue
    elif not trList[row].xpath('attribute::style'):# First line of each launch
        launchTime = "_".join(trList[row].xpath('.//td')[0].xpath('.//text()'))
        numPayload = int(trList[row].xpath('.//td')[0].xpath('attribute::rowspan')[0])
        # Success if at least one payload is not fail
        succ = False
        for i in range(1,numPayload):
            newRow = row + i
            if len(trList[newRow].xpath('.//td[@colspan="6"]')): # Reach the comment line
                break
            if not trList[newRow].xpath(".//td")[-1].xpath('.//text()')[0].strip('\n') in ['Operational','Successful','En route']:
                continue
            else: ## Succ
                succ = True
                break
        if succ:
            res[launchTime] = res.get(launchTime,0) + 1
    row += numPayload # Next Launch

## Initialize data
date,counter = [],[]
startDate = datetime.datetime.strptime("01 January 2019",'%d %B %Y')
endDate = datetime.datetime.strptime("01 January 2020",'%d %B %Y')
day = datetime.timedelta(days=1)
for i in range((endDate-startDate).days):
    date.append((startDate + day*i).isoformat() + '+00:00')
    counter.append(0)

## count succ launches based on @res
for time, count in res.items():
    dateMD = time.split('_')[0]
    formatDate = datetime.datetime.strptime(dateMD+' 2019','%d %B %Y')
    counter[(formatDate - startDate).days] += count

# Output to file
with open("test.csv","w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["date","value"])
    for i in range(len(date)):
        writer.writerow([date[i],counter[i]])
