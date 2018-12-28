#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 10:25:19 2018

@author: nathanielastudillo

HITBTC format is common format. 
"""

import tickers
import re

#BFNXpairs = tickers.BFNXpairs()
#HITBTCpairs = tickers.HITBTCpairs()
#BITTREXpairs = tickers.BITTREXpairs()
#
#pairlist = [BFNXpairs, HITBTCpairs, BITTREXpairs]

#for pair in pairlist:
#    print(pair)
'''
I need to rewrite the below common translators so that they're aware of the
length of each pair and return formatted common parameters as necessary. Will 
still use the list format of [original, common]

'''

def BITTREXtoCommon(BITTREXpairs):
    '''
    This bad boy translates BITTREX's format to common. Basically, 
    it flips the first 3 and last 3/4/5 characters depending on the
    length of the string so that it accounts for longer pairs than
    6 characters and thus returns an accurate pair
    '''
    index = 0
    for pair in BITTREXpairs:
        if len(pair) == 7:
            original = pair
            pair = re.sub('-', '', pair)
            newpair = pair[-3:] + pair[:3]
            BITTREXpairs[index] = [original, newpair]
            index += 1
        if len(pair) == 8:
            original = pair
            pair = re.sub('-', '', pair)
            newpair = pair[-4:] + pair[:3]
            BITTREXpairs[index] = [original, newpair]
            index += 1
        if len(pair) == 9:
            original = pair
            pair = re.sub('-', '', pair)
            newpair = pair[-5:] + pair[:3]
            BITTREXpairs[index] = [original, newpair]
            index += 1
        else:
            continue
    return BITTREXpairs
    
def HITBTCtoCommon(HITBTCpairs):
    index = 0
    for pair in HITBTCpairs:
        HITBTCpairs[index] = [pair, pair]
        index += 1
    return HITBTCpairs

def BFNXtoCommon(BFNXpairs):
    index = 0
    for pair in BFNXpairs:
        newpair = pair.lower()
        BFNXpairs[index] = [pair, newpair]
        index += 1
    return BFNXpairs

#BITTREXpairs = BITTREXtoCommon(BITTREXpairs)
#HITBTCpairs = HITBTCtoCommon(HITBTCpairs)
#commonpairs = {}

#print(BITTREXpairs)
#print(HITBTCpairs)
#
#for HITBTCpair in HITBTCpairs:
##    print('hitbtc: ',HITBTCpair[1])
#    for BITTREXpair in BITTREXpairs:
##        print('bittrex: ', BITTREXpair[1])
#        if HITBTCpair[1] == BITTREXpair[1]:
#            commonpairs[HITBTCpair[0]] = {'HITBTC': HITBTCpair[1], 'BITTREX': BITTREXpair[0]}
#        else:
#            continue
        

        