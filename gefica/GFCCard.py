# -*- coding: utf-8 -*-

class GFCCard:
	""" """
	def __init__(self, cardindex):
		""" """
		self.index = cardindex
		self.character = "Ø"
		self.pinyin = "ø"
		self.translation = "ø"
		self.example = "ø"
		self.example_translation = "ø"

	def PrintSelf(self):
		""" """
		print self.index
		print self.character
		print self.pinyin
		print self.translation
		print self.example
		print self.example_translation

	def SetCardIndex(self, i):
		""" """
		self.index = i

	def set_character(self, c):
		""" """
		self.character = c

	def get_character(self):
		""" """
		return self.character

	def set_pinyin(self, p):
		""" """
		self.pinyin = p

	def get_pinyin(self):
		return self.pinyin

	def set_translation(self, t):
		""" """
		self.translation = t

	def get_translation(self):
		""" """
		return self.translation

	def set_example(self, e):
		""" """
		self.example = e

	def get_example(self):
		""" """
		return self.example

	def set_example_translation(self, et):
		""" """
		self.example_translation = et

	def get_example_translation(self):
		""" """
		return self.example_translation

