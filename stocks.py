#!/usr/bin/env python
import urllib
import re
import time
def get_quote(symbol):
    base_url = 'http://finance.google.com/finance?q='
    content = urllib.urlopen(base_url + symbol).read()
    m = re.search('id="ref_(.*?)">(.*?)<', content)
    if m:
        quote = m.group(2)
    else:
        quote = "error"
    return quote

def checkStocks(max_iterations):
	

	stock_names = ['yhoo', 'goog', 'aapl']
	prev_prices = {}

	#init prev values:
	for name in stock_names:
		prev_prices[name] = [-1]


	curr_iter = 0
	while (curr_iter < max_iterations):
		for name in stock_names:			
			time.sleep(10)
			
			curr_price = get_quote(name)
			curr_price_clean = float(curr_price.replace(",",""))

			change = 0.0
			prev_price = prev_prices[name]
			if prev_price[-1] != -1:
				change = round(100 * (curr_price_clean - prev_price[-1]) / prev_price[-1] , 4)
			else:
				# remove -1 from the list:
				prev_prices[name] = []

			prev_prices[name].append(curr_price_clean)

			if change != 0.0:
				print name, ':', curr_price_clean, ',',change, '%'		
			else:
				print name, ':', curr_price_clean, ', NO CHANGE'

		print '\n'
		curr_iter += 1
	
	print '\n'
	print 40*'*'			
	print 'Summery:	'
	for name in stock_names:
		print '    ', name, ', min = ', min(prev_prices[name]), ', max = ', max(prev_prices[name])
	



print 40*'*'
print '*         Blimp stocks checker         *'
print '* [data taken from finance.google.com] *'
print 40*'*'

checkStocks(10)


