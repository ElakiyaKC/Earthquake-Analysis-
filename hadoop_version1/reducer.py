#!/usr/bin/env python
from operator import itemgetter
import sys

map_output = None
current_count = 0
# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t')
    try:
        count = float(count)
    except ValueError:
        print "error"
        continue
    if map_word and map_output!= word:
        print '%s'+','+'%s' % (map_output , current_count)
        map_output  = 0
    current_count += 1
    current_word = word
# do not forget to output the last word if needed!
if current_word == word:
    print '%s'+','+'%s' % (current_word, current_count)