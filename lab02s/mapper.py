#!/usr/bin/python3

import sys

def emit(key, value):
    sys.stdout.write('{}\t{}\n'.format(key, value))

def map(line):
    objects = line.split('\t')
    uid, timestamp, url = objects
	url = url.strip()
    if uid != '-' and len(url) > 0:
       emit(url, 1)

def main():
    for line in sys.stdin:
        map(line.strip())

if __name__ == '__main__':
   main()
