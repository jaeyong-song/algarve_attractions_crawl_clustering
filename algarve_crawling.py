import requests as re
from bs4 import BeautifulSoup as bs

url = "https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C4258168%2C4270442%2C4306835%2C4317915%2C4322823%2C4328159%2C4371335%2C4395848%2C4401769%2C4403882%2C4412669%2C4413451%2C4414389%2C4416581%2C4421968%2C4270859%2C4284970%2C4291517%2C4412693&hl=ko&gl=kr&un=1&dest_mid=%2Fm%2F01gg84&dest_state_type=sattd&dest_src=ts&sa=X&otf=1#ttdm=37.138621_-8.488033_10&ttdmf=%25252Fm%25252F05pc448"
res = re.get(url = url)

soup = bs(res.text, 'html.parser')
main = soup.select('body > c-wiz')
main = main[1]
main = main.select('div > div > div > c-wiz > div > div:nth-child(2) > c-wiz > div > div > div > div')

result = {}

# 개별 셀
for cell in main:
    cell = cell.select('div > div')
    cell = cell[1]
    cell = cell.select('div:nth-child(2) > div')
    position = cell[0]
    position = position.text
    print(position)
    weight = cell[1]
    weight = weight.select('span > span')
    if len(weight)-1 >= 0:
        weight = weight[len(weight)-1]
        weight = weight.text
        weight = weight.replace("(", "")
        weight = weight.replace(")", "")
        weight = weight.replace(" ", "")
        weight = weight.replace(",", "")
        weight = int(weight)
        print(weight)
        result[position] = weight
    if position == "Praia Verde":
        break;
    print()

print(result)