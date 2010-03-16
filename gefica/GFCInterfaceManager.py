# -*- coding: utf-8 -*-
"""GFCInterfaceManager.py (©2005-2010 Romain Ballais <rballais@users.berlios.de> - See LICENSE file for licence information.)"""

import gtk
import gtk.glade
import poppler

import ConfigParser, os

class GFCInterfaceManager:
	"""Interface manager: manage all interface elements, callbacks and user interactions."""

	def __init__(self, gladefile):
		"""Class initializer: initialize internal data, create interface from Glade file, associate callbacks with graphical elements."""
		self.recent_project_files_number = 0
		self.recent_project_files_path = []
		self.filename = ""
		self.project_path = ""

		# Gtk stuff:
		self.gladefile = gladefile
		self.glade_trees = {
			"openFileChooserDialog" : gtk.glade.XML(self.gladefile, "openFileChooserDialog"),
			"saveFileChooserDialog" : gtk.glade.XML(self.gladefile, "saveFileChooserDialog"),
			"theAboutDialog" : gtk.glade.XML(self.gladefile, "theAboutDialog"),
			"popupMessageDialog" : gtk.glade.XML(self.gladefile, "popupMessageDialog"),
			"mainWindow" : gtk.glade.XML(self.gladefile, "mainWindow")
		}
		
		#---
		self.__getitem__("newImageMenuItem").connect("activate", self.new_project_cb)
		self.__getitem__("openImageMenuItem").connect("activate", self.open_project_cb)
		self.__getitem__("saveImageMenuItem").connect("activate", self.save_project_cb)
		self.__getitem__("saveasImageMenuItem").connect("activate", self.save_project_as_cb)
		self.__getitem__("quitImageMenuItem").connect("activate", self.quit_cb)
		#---
		self.__getitem__("cutImageMenuItem").connect("activate", self.cut_activate_cb)
		self.__getitem__("copyImageMenuItem").connect("activate", self.copy_activate_cb)
		self.__getitem__("pasteImageMenuItem").connect("activate", self.paste_activate_cb)
		self.__getitem__("deleteImageMenuItem").connect("activate", self.delete_activate_cb)
		#---
		self.__getitem__("newcardImageMenuItem").connect("activate", self.new_card_cb)
		self.__getitem__("newButton").connect("released", self.new_card_cb)
		self.__getitem__("editcardImageMenuItem").connect("activate", self.edit_card_cb)
		self.__getitem__("editButton").connect("released", self.edit_card_cb)
		self.__getitem__("applycardImageMenuItem").connect("activate", self.apply_card_modification_cb)
		self.__getitem__("applyButton").connect("released", self.apply_card_modification_cb)
		self.__getitem__("pdfImageMenuItem").connect("activate", self.generate_pdf_cb)
		#---
		self.__getitem__("aboutImageMenuItem").connect("activate", self.show_about_dialog_cb)
		#---
		self.__getitem__("goComboBox").connect("changed", self.go_cb)
		self.__getitem__("previousButton").connect("released", self.go_to_previous_cb)
		self.__getitem__("nextButton").connect("released", self.go_to_next_cb)
		#---
		self.__getitem__("previewDrawingArea").connect("expose-event", self.preview_expose_event_cb)
		#---
		self.__getitem__("mainWindow").connect("destroy", self.quit_cb)
		#---
		self.__getitem__("mainWindow").show()

	def __getitem__(self, key):
		"""Return the widget matching the given name."""
		for glade_tree in self.glade_trees:
			widget = self.glade_trees[glade_tree].get_widget(key)
			if(widget != None):
				return widget

	def register_cards_manager(self, new_cards_manager):
		"""Register a GFCCardsManager instance."""
		self.cards_manager = new_cards_manager

	def init_application(self):
		"""Init the application by reading the user configuration file and setting the interface primary state."""
		self.read_config_file()
		self.init_interface()
		
	def read_config_file(self):
		"""Read the user configuration file if there is one, else create one."""
		config_reader = ConfigParser.SafeConfigParser()
		user_home = os.getenv("HOME")
		parsed_files = config_reader.read([user_home+'/.config/gefica/gefica.conf'])
		if(parsed_files != []):
			self.recent_project_files_number = config_reader.get("recent", "files")
			for index in range(int(self.recent_project_files_number)):
				self.recent_project_files_path.append(config_reader.get("recent", str(index)))
		else:
			os.system("touch "+user_home+"/.config/gefica/gefica.conf")
			os.system("echo [preferences] > "+user_home+"/.config/gefica/gefica.conf")
			os.system("echo >> "+user_home+"/.config/gefica/gefica.conf")
			os.system("echo [recent] >> "+user_home+"/.config/gefica/gefica.conf")
			os.system("echo files: 0 >> "+user_home+"/.config/gefica/gefica.conf")

	def init_interface(self):
		"""Initialize interface. Update the combobox data."""
		for index in range(self.cards_manager.get_nb_cards()):
			self.__getitem__("goComboBox").remove_text(self.cards_manager.get_nb_cards()-index-1)
		for index in range(self.cards_manager.get_nb_cards()):
			self.__getitem__("goComboBox").append_text(self.cards_manager.get_card_character(index))
		if self.cards_manager.get_nb_cards() > 0:
			self.update_interface(0)

	def update_interface(self, index):
		"""Update the text fields and the preview area."""
		self.__getitem__("goComboBox").set_active(index)
		self.__getitem__("mainStatusBar").push(	self.__getitem__("mainStatusBar").get_context_id("displayed character"),
							"Fiche affichée : "+self.cards_manager.get_card_character(index))
		self.__getitem__("characterEntry").set_text(self.cards_manager.get_card_character(index))
		self.__getitem__("pinyinEntry").set_text(self.cards_manager.get_card_pinyin(index))
		self.__getitem__("translationEntry").set_text(self.cards_manager.get_card_translation(index))
		self.__getitem__("exampleEntry").set_text(self.cards_manager.get_card_example(index))
		self.__getitem__("translated_exampleEntry").set_text(self.cards_manager.get_card_example_translation(index))
		self.__getitem__("previewDrawingArea").queue_draw()

	# Callbacks definitions:
	#---
	def new_project_cb(self, item):
		"""New project callback."""
		self.cards_manager.reset()

	def open_project_cb(self, item):
		"""Open project callback. Call the cards manager, set some internal data."""
		response = self.__getitem__("openFileChooserDialog").run()
		self.__getitem__("openFileChooserDialog").hide()
		if response == gtk.RESPONSE_OK:
			self.filename = self.__getitem__("openFileChooserDialog").get_filename()
			self.cards_manager.read_cards_from_file(self.filename)
			self.init_interface()
			# Compute the path where cards will be generated:
			self.project_path = self.filename.rsplit('/', 1)[0]

	def save_project_cb(self, item):
		"""Store the project file."""
		if self.filename == None:
			self.saveas_project_cb(item)
		self.cards_manager.write_cards_into_file(self.filename)

	def save_project_as_cb(self, item):
		"""Store the project file with an other name."""
		response = self.__getitem__("saveFileChooserDialog").run()
		self.__getitem__("saveFileChooserDialog").hide()
		if response == gtk.RESPONSE_OK:
			self.filename = self.__getitem__("saveFileChooserDialog").get_filename()
			self.save_project_cb(item)

	def quit_cb(self, item):
		"""Quit callback"""
		gtk.main_quit()
	
	#---
	def cut_activate_cb(self, item):
		"""Cut callback"""
		pass

	def copy_activate_cb(self, item):
		"""Copy callback"""
		pass

	def paste_activate_cb(self, item):
		"""Paste callback"""
		pass

	def delete_activate_cb(self, item):
		"""Delete callback"""
		pass

	#---
	def new_card_cb(self, item):
		"""New card callback: ask the cards manager to create a new card, update the interface."""
		index = self.cards_manager.add_card()
		self.__getitem__("goComboBox").append_text(self.cards_manager.get_card_character(index))
		self.update_interface(index)

	def edit_card_cb(self, item):
		"""Set text fields sensitive and editable."""
		self.__getitem__("characterEntry").set_sensitive(True)
		self.__getitem__("pinyinEntry").set_sensitive(True)
		self.__getitem__("translationEntry").set_sensitive(True)
		self.__getitem__("exampleEntry").set_sensitive(True)
		self.__getitem__("translated_exampleEntry").set_sensitive(True)
		self.__getitem__("applyButton").set_sensitive(True)
		self.__getitem__("editButton").set_sensitive(False)
		self.__getitem__("applycardImageMenuItem").set_sensitive(True)
		self.__getitem__("editcardImageMenuItem").set_sensitive(False)

		self.__getitem__("characterEntry").set_editable(True)
		self.__getitem__("pinyinEntry").set_editable(True)
		self.__getitem__("translationEntry").set_editable(True)
		self.__getitem__("exampleEntry").set_editable(True)
		self.__getitem__("translated_exampleEntry").set_editable(True)

	def apply_card_modification_cb(self, item):
		"""Set text fields insensitive and not editable. Transmit card data to the cards manager."""
		self.__getitem__("characterEntry").set_sensitive(False)
		self.__getitem__("pinyinEntry").set_sensitive(False)
		self.__getitem__("translationEntry").set_sensitive(False)
		self.__getitem__("exampleEntry").set_sensitive(False)
		self.__getitem__("translated_exampleEntry").set_sensitive(False)
		self.__getitem__("applyButton").set_sensitive(False)
		self.__getitem__("editButton").set_sensitive(True)
		self.__getitem__("applycardImageMenuItem").set_sensitive(False)
		self.__getitem__("editcardImageMenuItem").set_sensitive(True)

		self.__getitem__("characterEntry").set_editable(False)
		self.__getitem__("pinyinEntry").set_editable(False)
		self.__getitem__("translationEntry").set_editable(False)
		self.__getitem__("exampleEntry").set_editable(False)
		self.__getitem__("translated_exampleEntry").set_editable(False)

		index = self.__getitem__("goComboBox").get_active()
		self.cards_manager.set_card_character(index, self.__getitem__("characterEntry").get_text())
		self.cards_manager.set_card_pinyin(index, self.__getitem__("pinyinEntry").get_text())
		self.cards_manager.set_card_translation(index, self.__getitem__("translationEntry").get_text())
		self.cards_manager.set_card_example(index, self.__getitem__("exampleEntry").get_text())
		self.cards_manager.set_card_example_translation(index, self.__getitem__("translated_exampleEntry").get_text())
		self.init_interface()
		self.update_interface(index)


	def generate_pdf_cb(self, item):
		"""Generate PDF callback: ask the cards manager to generate SVG and PDF files."""
		self.cards_manager.generate_svg(self.project_path)
		self.cards_manager.generate_pdf(self.project_path)
		self.__getitem__("popupMessageDialog").format_secondary_text("Les fiches ont été générées à l'emplacement suivant :\n"+self.project_path)
		self.__getitem__("popupMessageDialog").run()
		self.__getitem__("popupMessageDialog").hide()

	#---
	def show_about_dialog_cb(self, item):
		"""Show the about dialog."""
		self.__getitem__("theAboutDialog").run()
		self.__getitem__("theAboutDialog").hide()

	#---
	def go_to_previous_cb(self, item):
		"""Previous button callback"""
		if self.__getitem__("goComboBox").get_active() > 0:
			self.update_interface(self.__getitem__("goComboBox").get_active()-1)

	def go_to_next_cb(self, item):
		"""Next button callback"""
		if self.__getitem__("goComboBox").get_active() < self.cards_manager.get_nb_cards() -1:
			self.update_interface(self.__getitem__("goComboBox").get_active()+1)

	def go_cb(self, item):
		"""Combo box callback"""
		if self.__getitem__("goComboBox").get_active() > -1:
			self.update_interface(self.__getitem__("goComboBox").get_active())

	#---
	def preview_expose_event_cb(self, widget, event):
		"""Expose event callback: update the preview area."""
		index = self.__getitem__("goComboBox").get_active()
		if index > -1 and os.path.exists(self.project_path+"/card_"+str(index)+".pdf"):
			pdf = poppler.document_new_from_file ("file://"+self.project_path+"/card_"+str(index)+".pdf", None)
			width, height = pdf.get_page(0).get_size()
			widget.set_size_request(int(width), int(height))
			cairo_renderer = widget.window.cairo_create()
			cairo_renderer.set_source_rgb(1, 1, 1)
			cairo_renderer.scale(1, 1)
			cairo_renderer.rectangle(0, 0, width, height)
			cairo_renderer.fill()
			pdf.get_page(0).render(cairo_renderer)

