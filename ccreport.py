#!/usr/bin/python

import sys
import re
#parser for santander credit card report file

transactions=[]
# Date			Card no.			Description				Money in	Money out
with open(sys.argv[1],'r') as fp:
    while True:
        line = fp.readline().rstrip('\r\n')
        if not line:
            break
        d=line.split('\t')
        idx=len(d)-1
        amount=0
        try:
            if d[idx]:
                amount=float(d[idx])
            else:
                # if last element is null, next is money-in
                while not d[idx]:
                  idx=idx-1
                amount=-float(d[idx])
        except Exception as e:
            continue
        # next non-empty is description
        idx=idx-1
        while not d[idx]:
            idx=idx-1
        description=d[idx]
        # next non-empty is card number
        idx=idx-1
        while not d[idx]:
            idx=idx-1
        cardno=d[idx]
        # next non-empty is date
        idx=idx-1
        while not d[idx]:
            idx=idx-1
        date=d[idx]
        # sometimes there's no card number
        if idx<0:
            date=cardno
            cardno=''
        transactions.append("%s;%s;%s;%s" % (date, cardno, description, amount))


# print transactions in reverse order
for t in transactions:
    print t