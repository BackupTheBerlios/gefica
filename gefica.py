#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""gefica.py (©2005-2011 Romain Ballais <rballais@users.berlios.de> - See LICENSE file for licence information.)"""

import sys
import gtk

import gfc.GFCCard
import gfc.GFCCardsManager
import gfc.GFCInterfaceManager

def main():
	"""Application start point. Initializes managers instances and lauch the event loop."""
	interface_manager = gfc.GFCInterfaceManager.GFCInterfaceManager(sys.prefix+'/share/gefica/glade/interface.glade')
	cards_manager = gfc.GFCCardsManager.GFCCardsManager()
	interface_manager.register_cards_manager(cards_manager)
	interface_manager.init_application()

	# Starts the GTK toolkit:
	gtk.main()
	return

if __name__ == '__main__':
	main()
