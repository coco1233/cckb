#!/usr/bin/env python
# coding=utf-8
size = float(raw_input("size of tank:"))
percent = float(raw_input("percent full:"))
km = int(raw_input("km per liter:"))
print size * percent * km
if size * percent * km >= 200:
    print "the next station is 200 km away,you can wait for the next station"
else:
    print "you can't wait for the next stationation"
