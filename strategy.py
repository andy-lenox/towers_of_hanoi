#!/usr/bin/env python
# encoding: utf-8
"""
strategy.py

Created by Andrew Lenox on 2010-09-26.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import towers


def main():
	t = towers.towers()
	while not t.solved():
		t.moveOneValid()
		t.toString()
		print ""
	
	print "solved!"


if __name__ == '__main__':
	main()

