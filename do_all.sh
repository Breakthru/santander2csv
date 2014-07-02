#!/bin/bash
for i in Statements*txt
do
./santander2csv.py $i > ${i:0:-4}.csv
done
for i in Report*txt
do
./ccreport.py $i > ${i:0:-4}.csv
done

