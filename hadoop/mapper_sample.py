#!/usr/bin/env python

import sys
#from datetime import datetime
from datetime import datetime, timedelta
from time import strptime


def station(country,station_name):
    country_details= ""

    if(country == 'ALBANIA'):
        country_details = country+" "+station_name
    else:
        country_details="none"
    map_result =  country_details
    print '%s\t%s' % (map_result, 1)

def main():
    # input comes from STDIN (standard input)
    for line in sys.stdin.readlines():
        # remove leading and trailing whitespace
        line = line.strip()
        
        # split the line into words
        
        words = line.split(',')
        #print words
        try:
            count = (words[4])
        except ValueError:
            continue
        station(words[0],words[1])
	
	

if __name__ == "__main__":
    main()

