#!/usr/bin/env python
# encoding: utf-8
"""
towers.py

Created by Andrew Lenox on 2010-09-21.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import unittest
import stack


class towers:
	def __init__(self):
		#attributes
		self.A = stack.stack()
		self.B = stack.stack()
		self.C = stack.stack()
		self.stacks = [self.A,self.B,self.C]
		
		#need to change to 0,1,2
		self.allMoves = ((0,1) , (0,2) , (1,0) , (1,2) ,
									(2,0) , (2,1))
		self.path = []
		self.validMoves = []
		self.lastMove = ()
		self.steps = 0
									
		#setup stacks				
		self.setup()
		
	
	def setup(self):
		for x in range (5,0,-1):
			self.B.push(x)
		self.generateMoves()
		
	def generateMoves(self):
		moves = list(self.allMoves)
		
		#for every possible move
		for move in self.allMoves:
			fromStack = self.stacks[move[0]]
			toStack = self.stacks[move[1]]
			#if there is anything on the stack
			if fromStack.top():
				#if this move is not valid
				if not toStack.pushable(fromStack.top()):
					#remove it from the list of valid moves
					moves.remove(move)
			#else, there is no disk there, and isn't a valid move
			else:
				moves.remove(move)
		
		#if the previous move made is still valid		
		if self.lastMove in moves:
			#remove it to prevent back and forth
			moves.remove(self.lastMove)
		self.validMoves = moves
		
	def printValidMoves(self):
		print self.validMoves
		
	def move(self,t):
		if t in self.validMoves:
			fromStack = self.stacks[t[0]]
			toStack = self.stacks[t[1]]
			if fromStack.top():
				toStack.push(fromStack.pop())
			self.lastMove = t
			self.generateMoves()
			self.steps += 1
			self.path.append(t)
			
			
	def moveSmallestLeft(self):
		fromstack = None
		tostack = None
		for stack in self.stacks:
			if stack.top() == 1:
				fromstack = self.stacks.index(stack)
				tostack = fromstack - 1
				if tostack == -1:
					tostack = 2
				print "One is on: %d and one left of that is %d" %(fromstack,tostack)
		
		self.move((fromstack, tostack))
				
	def moveOneValid(self):
		#after moveing the smallest left, there should
		#only be one valid move to make other than moving the 1. Make it!
		print "Move the smallest disk to the left"
		self.moveSmallestLeft()
		self.toString()
		print ""
		self.generateMoves()
		moves = self.validMoves
		
		#remove all moves that involve moving the 1 disk
		theonestack = None
		for stack in self.stacks:
			if stack.top() == 1:
				theonestack = self.stacks.index(stack)
				
			
		removeAll = [(theonestack,0),(theonestack,1),(theonestack,2)]
		r = removeAll
		
		for move in r:
			if move[0] == move[1]:
				removeAll.remove(move)
		
		for move in removeAll:
			if move in self.validMoves:
				moves.remove(move)
		
		if(len(moves) > 1):
			print "error"
		elif self.validMoves:
			self.move(self.validMoves[0])
	
	def strategySolve(self):
		while(not self.solved()):
			self.moveOneValid()
			
	def reset(self):
		for stack in self.stacks:
			for x in range(stack.size()):
				stack.remove()
	
	def solved(self):
		return self.stacks[0].size() == 5
		
	def toString(self):
		for stack in self.stacks:
			print "Stack: %d" % self.stacks.index(stack)
			stack.printStack()
			
	def equal(self, t):
		return self.A.equal(t.A) and self.B.equal(t.B) and self.C.equal(t.C)

class towersTests(unittest.TestCase):
	def setUp(self):
		self.t = towers()
		
	def test_setup(self):
		testStack = stack.stack()
		for x in range (5,0,-1):
			testStack.push(x)
		self.t.move((1,0))
	
	def test_remove(self):
		self.t.reset()
		
	#def test_move_smallest(self):
	#	self.t.moveSmallestLeft()
	def moves(self):
		self.t.toString()
		self.t.move((1,0))
		self.t.toString()
		self.t.move((1,2))
		self.t.toString()
		self.t.move((0,2))
		self.t.toString()
		self.t.move((1,0))
		self.t.toString()
		self.t.moveOneValid()
		
	def test_solve(self):
		while not self.t.solved():
			self.t.moveOneValid()
			self.t.toString()
			print ""
			
		print "solved in %d steps!" % self.t.steps
		
	def test_equal(self):
		s = towers()
		s.toString()
		self.t.toString()
		print self.t.equal(s)
		

if __name__ == '__main__':
	unittest.main()