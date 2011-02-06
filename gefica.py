#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""gefica.py (©2005-2011 Romain Ballais <rballais@users.berlios.de> - See LICENSE file for licence information.)"""

import gtk

import gefica.GFCCard
import gefica.GFCCardsManager
import gefica.GFCInterfaceManager

def main():
	"""Application start point. Initializes managers instances and lauch the event loop."""
	interface_manager = gefica.GFCInterfaceManager.GFCInterfaceManager('gefica/glade/interface.glade')
	cards_manager = gefica.GFCCardsManager.GFCCardsManager()
	interface_manager.register_cards_manager(cards_manager)
	interface_manager.init_application()

	# Starts the GTK toolkit:
	gtk.main()
	return

if __name__ == '__main__':
	main()