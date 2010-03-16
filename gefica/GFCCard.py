# -*- coding: utf-8 -*-

class GFCCard:
	"""Card class: store data matching a card element."""

	def __init__(self, cardindex):
		"""Class initializer"""
		self.index = cardindex
		self.character = "Ø"
		self.pinyin = "ø"
		self.translation = "ø"
		self.example = "ø"
		self.example_translation = "ø"

	def print_self(self):
		"""Print internal data on stdout."""
		print self.index
		print self.character
		print self.pinyin
		print self.translation
		print self.example
		print self.example_translation

	def set_card_index(self, new_index):
		"""Set the new index."""
		self.index = new_index

	def set_character(self, new_character):
		"""Set the new character."""
		self.character = new_character

	def get_character(self):
		"""Return the new character."""
		return self.character

	def set_pinyin(self, new_pinyin):
		"""Set the new pinyin."""
		self.pinyin = new_pinyin

	def get_pinyin(self):
		"""Return the pinyin."""
		return self.pinyin

	def set_translation(self, new_translation):
		"""Set the new character translation."""
		self.translation = new_translation

	def get_translation(self):
		"""Return the character translation."""
		return self.translation

	def set_example(self, new_example):
		"""Set the example."""
		self.example = new_example

	def get_example(self):
		"""Return the example."""
		return self.example

	def set_example_translation(self, new_example_translation):
		"""Set the example translation."""
		self.example_translation = new_example_translation

	def get_example_translation(self):
		"""Return the example translation."""
		return self.example_translation

