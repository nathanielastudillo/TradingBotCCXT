#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 11:57:52 2018

@author: nathanielastudillo
"""

import ccxt
import time

#Auth
bittrex = ccxt.bittrex ()
bittrex.apiKey = ''
bittrex.secret = ''

profitcount = 0
losscount = 0
'''
!!!Let's also add a way to keep track of all of the trades!!!

For each pair in bottom pairs, indexes are as follows:
    [name, volume, priceWhenPurchased]
    [  0 ,   1   ,     2             ]
'''
amount = 1000
                    
counter = 0
bottom10 = []
rounds = 0
cycles = 6
while counter < cycles:
#    counter = 0
    tickers = bittrex.fetch_tickers()
    pairlist = []
    
    for pair in tickers.keys():
        
        if ((tickers[pair]['quoteVolume'] >= 0.95) and (tickers[pair]['quoteVolume'])) <= 7 or tickers[pair]['last'] > 0.000005:
            continue
        
        else:
            pairlist.append([pair, tickers[pair]['baseVolume']])
            
    sortedlist = sorted(pairlist, key = lambda x: x[1])
    bottom10 = sortedlist[:10] #this can be tweaked for volume size range
    print(bottom10,len(bottom10))
    counter+=1
    
    for pair in bottom10: #buy 10 lowest market cap pairs
        
        price = bittrex.fetchTicker(pair[0])
        pair.append(price['last']) #now index position 2 for each list in bottom10
        bittrex.createLimitBuyOrder(pair[0], amount, price['last'] )
        print('Bought: {}'.format(pair[0]))
        
    approxseconds = 0
    
    while approxseconds < 60:
        for pair in bottom10:
            pricenow = bittrex.fetchTicker(pair[0])
            if len(bottom10) <= 0:
                break
            if pricenow['last'] > pair[2]*1.03: #profit at 3% gain
                bittrex.createLimitSellOrder(pair[0],amount,pricenow['last'])
                profitcount += 1
                profit = pricenow['last'] - pair[2]
                approxseconds += 1
                bottom10.remove(pair)
                print('TRADE: Profit of: {}, Loss Trades: {}, Profit Trades: {}'.format(profit, losscount, profitcount))
            if pricenow['last'] < pair[2]*0.99: #pull out at 1% loss
                bittrex.createLimitSellOrder(pair[0],amount,pricenow['last'])
                losscount += 1
                loss = pricenow['last'] - pair[2]
                approxseconds += 1
                bottom10.remove(pair)
                print('TRADE: Loss of: {}, Loss Trades: {}, Profit Trades: {}'.format(loss, losscount, profitcount))
            else:
                continue
        approxseconds += 1
        time.sleep(50)
        rounds += 1
        print('Round {} complete. Loss Trades: {}, Profit Trades: {}'.format(rounds, losscount, profitcount))
    if len(bottom10) <= 0:
        for pair in bottom10:
            pricenow = bittrex.fetchTicker(pair[0])
            bittrex.createLimitSellOrder(pair[0],amount,pricenow['last'])
            print('Sold: {}'.format(pair))
                
            
            
            
            
        
        
