#!/usr/bin/env python

import sys

def survival_survey(pclass,survival,sex):
    temp=""
    category = 'Class_' + pclass + '_Gender_' + sex
    if (survival == '1'):
        temp = category + '_' + 'Survived'
    else:
        temp = category + '_' + 'Dead'
    map_result = temp
    print '%s\t%s' % (map_result, 1)

def main():
    # input comes from STDIN (standard input)
    for line in sys.stdin.readlines():
        #remove leading and trailing whitespace
        line = line.strip()
        # split the line into words
        words = line.split(',')
        # print words
        try:
            count = (words[4])
        except ValueError:
            continue
        survival_survey(words[0], words[1],words[3])


if __name__ == "__main__":
    main()