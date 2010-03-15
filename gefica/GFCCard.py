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

	def print_self(self):
		""" """
		print self.index
		print self.character
		print self.pinyin
		print self.translation
		print self.example
		print self.example_translation

	def set_card_index(self, new_index):
		""" """
		self.index = new_index

	def set_character(self, new_character):
		""" """
		self.character = new_character

	def get_character(self):
		""" """
		return self.character

	def set_pinyin(self, new_pinyin):
		""" """
		self.pinyin = new_pinyin

	def get_pinyin(self):
		""" """
		return self.pinyin

	def set_translation(self, new_translation):
		""" """
		self.translation = new_translation

	def get_translation(self):
		""" """
		return self.translation

	def set_example(self, new_example):
		""" """
		self.example = new_example

	def get_example(self):
		""" """
		return self.example

	def set_example_translation(self, new_example_translation):
		""" """
		self.example_translation = new_example_translation

	def get_example_translation(self):
		""" """
		return self.example_translation

