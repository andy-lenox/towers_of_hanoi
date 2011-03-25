#!/usr/bin/env python
# encoding: utf-8
"""
depth.py

Created by Andrew Lenox on 2010-09-25.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import towers
from collections import deque
from copy import deepcopy
from copy import copy

def prune_children(children, open_states, closed):
	for child in children[:]:
		if open_states:
			for state in open_states:
				if child.equal(state):
					children.remove(child)
		if closed:
			for state in closed:
				if child.equal(state):
					children.remove(child)
	return children
	

def depth_first_search():
	"""non recursive depth first search on a game state"""
	start = towers.towers()
	print "starting state:"
	start.toString()
	print ""
	open_states = [start]
	closed = list()
	while open_states:
		X = open_states.pop()
		if X.solved():
			return X
		else:
			X.generateMoves
			moves = X.validMoves
			#generate children of X
			children = []
			for move in moves:
				Y = deepcopy(X)
				Y.move(move)
				children.append(Y)
			#put X on closed
			closed.append(X)
			#discard children of X if already on open or closed
			children = prune_children(children, open_states, closed)
			#put remaining children on left end of open
			open_states.extend(children)
		
def main():
	solved = depth_first_search()
	print "End State:"
	solved.toString()
	print "Complete! solved in %d steps!" % solved.steps
	print "Steps used to complete are as follows:"
	print solved.path

if __name__ == '__main__':
	main()

