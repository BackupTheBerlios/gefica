# -*- coding: utf-8 -*-

import ConfigParser, os
import string

from gefica.GFCCard import GFCCard

class GFCCardsManager:
	""" """
	def __init__(self):
		""" """
		self.nb_cards = 0
		self.cards = []
		self.template_path = ""

	def get_nb_cards(self):
		""" """
		return self.nb_cards

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
		card = GFCCard(self.nb_cards)
		self.cards.append(card)
		self.nb_cards += 1
		return card

	def add_card(self):
		""" """
		self.create_card()
		return self.nb_cards -1

	def reset(self):
		""" """
		self.__init__()

	def set_template_file(self, new_template_path):
		""" """
		self.template_path = new_template_path

	def read_cards_from_file(self, cards_file):
		""" """
		cards_reader = ConfigParser.SafeConfigParser()
		cards_reader.read([cards_file])
		nb_cards = cards_reader.getint("infos", "nb_cards")
		self.template_path = cards_reader.get("infos", "template")
		for index in range(0, nb_cards):
			card = self.create_card()
			card.set_character(cards_reader.get(str(index), "character"))
			card.set_pinyin(cards_reader.get(str(index), "pinyin"))
			card.set_translation(cards_reader.get(str(index), "translation"))
			card.set_example(cards_reader.get(str(index), "example"))
			card.set_example_translation(cards_reader.get(str(index), "example translation"))

	def write_cards_into_file(self, cards_file):
		""" """
		cards_writer = ConfigParser.SafeConfigParser()
		cards_writer.add_section("infos")
		cards_writer.set("infos", "nb_cards", str(self.nb_cards))
		cards_writer.set("infos", "template", self.template_path)
		for index in range(0, self.nb_cards):
			cards_writer.add_section(str(index))
			cards_writer.set(str(index), "character", self.get_card_character(index))
			cards_writer.set(str(index), "pinyin", self.get_card_pinyin(index))
			cards_writer.set(str(index), "translation", self.get_card_translation(index))
			cards_writer.set(str(index), "example", self.get_card_example(index))
			cards_writer.set(str(index), "example translation", self.get_card_example_translation(index))
		datafile = open(cards_file,'w')
		cards_writer.write(datafile)
		datafile.close()
		

	def generate_svg(self, path):
		""" """
		svgtemplate = open(self.template_path)
		svgtemplatestring = svgtemplate.read()
		svgtemplate.close()
		for index in range(0, self.nb_cards):
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
			
	def generate_pdf(self, path):
		""" """
		for index in range(0, self.nb_cards):
			os.popen('inkscape -z -A '+path+'/card_'+str(index)+'.pdf -f '+path+'/card_'+str(index)+'.svg').read()


