# -*- coding: utf-8 -*-

import gtk
import ConfigParser, os
import string

from GFCCard import *

class GFCCardsManager:
	""" """
	def __init__(self):
		""" """
		self.nbCards = 0
		self.cards = []
		pass

	def get_nb_cards(self):
		""" """
		return self.nbCards

	def get_card_character(self, index):
		""" """
		return self.cards[index].get_character()

	def get_card_pinyin(self, index):
		""" """
		return self.cards[index].get_pinyin()

	def get_card_translation(self, index):
		""" """
		return self.cards[index].get_translation()

	def get_card_example(self, index):
		""" """
		return self.cards[index].get_example()

	def get_card_example_translation(self, index):
		""" """
		return self.cards[index].get_example_translation()

	def set_card_character(self, index, text):
		""" """
		self.cards[index].set_character(text)

	def set_card_pinyin(self, index, text):
		""" """
		self.cards[index].set_pinyin(text)

	def set_card_translation(self, index, text):
		""" """
		self.cards[index].set_translation(text)

	def set_card_example(self, index, text):
		""" """
		self.cards[index].set_example(text)

	def set_card_example_translation(self, index, text):
		""" """
		self.cards[index].set_example_translation(text)

	def create_card(self):
		""" """
		c = GFCCard(self.nbCards)
		self.cards.append(c)
		self.nbCards+=1
		return c

	def read_cards_from_file(self, cf):
		""" """
		cards_reader = ConfigParser.SafeConfigParser()
		cards_reader.read([cf])
		nbcards = cards_reader.getint("infos", "nbcards")
		for index in range(0,nbcards):
			card = self.create_card()
			card.set_character(cards_reader.get(str(index), "character"))
			card.set_pinyin(cards_reader.get(str(index), "pinyin"))
			card.set_translation(cards_reader.get(str(index), "translation"))
			card.set_example(cards_reader.get(str(index), "example"))
			card.set_example_translation(cards_reader.get(str(index), "example translation"))

	def write_cards_into_file(self, cf):
		""" """
		cards_writer = ConfigParser.SafeConfigParser()
		cards_writer.add_section("infos")
		cards_writer.set("infos", "nbcards", str(self.nbCards))
		for index in range(0, self.nbCards):
			cards_writer.add_section(str(index))
			cards_writer.set(str(index), "character", self.get_card_character(index))
			cards_writer.set(str(index), "pinyin", self.get_card_pinyin(index))
			cards_writer.set(str(index), "translation", self.get_card_translation(index))
			cards_writer.set(str(index), "example", self.get_card_example(index))
			cards_writer.set(str(index), "example translation", self.get_card_example_translation(index))
		datafile = open(cf,'w')		
		cards_writer.write(datafile)
		datafile.close()
		

	def generate_svg(self, path):
		""" """
		svgtemplate = open(path+'/template.svg')
		svgtemplatestring = svgtemplate.read()
		svgtemplate.close()
		for index in range(0, self.nbCards):
			svgcode = string.Template(svgtemplatestring)
			data = dict()
			data["character"] = self.get_card_character(index)
			data["pinyin"] = self.get_card_pinyin(index)
			data["translation"] = self.get_card_translation(index)
			data["example_translation"] = self.get_card_example_translation(index)
			data["example"] = self.get_card_example(index)
			os.popen('touch '+path+'/card_'+str(index)+'.svg').read()
			filehandle = open(path+'/card_'+str(index)+'.svg', 'w')
			filehandle.write(svgcode.substitute(data))
			filehandle.close()
			
		

	def generate_latex(self):
		""" """
		for index in range(0, self.nbCards):
			latexcode = "\documentclass[12pt,french,b5paper]{article}" + "\n"
			latexcode+= "\usepackage[encapsulated]{CJK}" + "\n"
			latexcode+= "\usepackage[utf8]{inputenc}" + "\n"
			latexcode+= "\\begin{document}" + "\n"
			latexcode+= "\pagestyle{empty}" + "\n"
			latexcode+= "\\begin{center}" + "\n"
			latexcode+= self.cards[index].character + "\\\\" +"\n"
			latexcode+= self.cards[index].pinyin + "\\\\" +"\n"
			latexcode+= "\end{center}" + "\n"
			latexcode+= self.cards[index].translation + "\\\\" +"\n"
			latexcode+= self.cards[index].example + "\\\\" +"\n"
			latexcode+= self.cards[index].example_translation + "\\\\" +"\n"
			latexcode+= "\end{document}" + "\n"
			fileHandle = open('cards/card_'+str(index)+'.tex', 'w')
			fileHandle.write (latexcode)
			fileHandle.close()
		
	def generate_pdf(self, path):
		""" """
		for index in range(0, self.nbCards):
			#os.popen('cd cards; pdflatex card_'+str(index)+'.tex').read()
			os.popen('inkscape -z -A '+path+'card_'+str(index)+'.pdf -f '+path+'card_'+str(index)+'.svg').read()


