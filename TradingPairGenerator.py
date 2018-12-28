#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 14:27:09 2018

@author: nathanielastudillo
"""


import requests
import json
import time
import numpy as np

'''
Functions to get lists of pairs from each of the 3 arbitrage exchanges
'''

def BFNXpairs():
    
    '''
    This function returns a list of pairs from Bitfinex
    All lowercase, format of base currency then market currency
    '''
    
    index = 0
    BFNXsymbolsURL = "https://api.bitfinex.com/v1/symbols_details" #url to pass to response object
    BFNXpairResponse = requests.get(BFNXsymbolsURL) #pull JSON from Bitfinex and store it in Request object
    responsedict = json.loads(BFNXpairResponse.text) #turn the JSON stored in Request object into a dictionary
    pairlistBFNX = [] #list to store pairs on Bitfinex
    
    for thing in responsedict: #storing pairs from BFNX as a list
        pairlistBFNX.append(responsedict[index]['pair'])
        index += 1
        
    return pairlistBFNX

def HITBTCpairs():
    
    '''
    This function returns a list of pairs from HITBtc
    All uppercase, base currency second, market currency first
    '''
    index = 0
    symbolURL = 'https://api.hitbtc.com/api/2/public/symbol'
    pairResponse = requests.get(symbolURL)
    responsedict = json.loads(pairResponse.text)
    pairlistHITBTC = []
    
    for thing in responsedict:
        pairlistHITBTC.append(responsedict[index]['id'])
        index += 1
    return pairlistHITBTC

def BITTREXpairs(): 
    '''
    This function returns a list of pairs from BITTREX
    BITTREX RESTapi returns JSON with 'MarketCurrency' and 'BaseCurrency' keys
    '''
    index = 0
    symbolURL = 'https://bittrex.com/api/v1.1/public/getmarkets'
    pairResponse = requests.get(symbolURL)
    responsedict = json.loads(pairResponse.text)
    pairlist = []
    
    for thing in responsedict['result']:
        pairlist.append(responsedict['result'][index]['MarketName'])
        index += 1
    return pairlist

BFNXpairs = BFNXpairs()
HITBTCpairs = HITBTCpairs()
BITTREXpairs = BITTREXpairs()

print(BFNXpairs)
print(HITBTCpairs)
commonpairs = []

for pair in BFNXpairs:
    if pair.upper() in HITBTCpairs:
        commonpairs.append(pair)
        
commondif = {}
difpercent = []

def BFNXprice(pair):
    time.sleep(3)
    BFNXbaseurl = 'https://api.bitfinex.com/v1/pubticker/'
    response = requests.get(BFNXbaseurl + pair)
    responsedict = json.loads(response.text)
    x = responsedict['last_price']
    print(x)
#    y = float(x) if '.' in x else int(x)
    return x

def HITBTCprice(pair):
    HITBTCbaseurl = 'https://api.hitbtc.com/api/2/public/ticker/'
    pair = pair.upper()
    response = requests.get(HITBTCbaseurl + pair)
    responsedict = json.loads(response.text)
    x = responsedict['last']
#    print(type(x))
#    y = float(x) if '.' in x else int(x)
    return x

for pair in commonpairs:
    BFNXfloat = float(BFNXprice(pair))
    HITBTCfloat = float(HITBTCprice(pair))
    commondif[pair] = {'BFNX': BFNXfloat, 'HITBTC': HITBTCfloat, 'dif' : abs(BFNXfloat - HITBTCfloat)}

for key in commondif.keys():
    print(key, (commondif[key]['dif'] / max(commondif[key]['BFNX'],commondif[key]['HITBTC']))*100)



        
        
        
                
                
            
            

