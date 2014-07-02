#!/usr/bin/python

import sys
import re
#parser for santander text file

transactions=[]
# date description amount balance
with open(sys.argv[1],'r') as fp:
    while True:
        line = fp.readline()
        if not line:
            break
        m = re.search('Account:.XXXX XXXX XXXX ([0-9]+)', line)
        if m:
            print "account ending "+ m.group(1)
            print "date , description,  amount, balance"
        m = re.search('Date:.([0-9]{2}/[0-9]{2}/[0-9]{4})', line)
        if m:
            date = m.group(1)
            desc = fp.readline() # desc starts on 14th character
            amt = fp.readline()
            amount = re.search('Amount:.(-?[0-9]+\.[0-9]+).',amt).group(1)
            bal = fp.readline()
            balance = re.search('Balance:.(-?[0-9]+\.[0-9]+).',bal).group(1)    
            transactions.append( date+" ; '"+desc[13:-2]+"' ; "+amount+" ; "+balance)
            

# print transactions in reverse order
for i in range(len(transactions)-1,-1,-1):
    print transactions[i]
