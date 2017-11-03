import csv
import requests
from lxml import html

page = requests.get('https://www.coinspot.com.au/tradecoins')
tree = html.fromstring(page.content)

dataCoins = tuple(tree.xpath("/html/body/div[1]/div/div[2]/div/div[3]/ul/li[contains(@class, "
							  "'hidden-xs')]/@data-coin"))
coinPrice = tuple(tree.xpath("/html/body/div[1]/div/div[2]/div/div[3]/ul/li[contains(@class, 'hidden-xs')]/div["
							 "contains("
					"@class, 'marketrow')]/div[2]/text()"))
coinChange = tuple(tree.xpath("/html/body/div[1]/div/div[2]/div/div[3]/ul/li[contains(@class, "
									  "'hidden-xs')]/div["
							 "contains("
					"@class, 'marketrow')]/div[4]/span/text()"))

coinDict = dict(zip(dataCoins, zip(coinPrice, coinChange)))

with open('cryppybois.csv', 'w', newline='') as f:
	writer = csv.writer(f)
	writer.writerow(['Coin', 'Buy Rate', 'Change %'])
	for key, value in coinDict.items():
		writer.writerow([key, value[0], value[1].strip('%')])
