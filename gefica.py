#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""gefica.py (©2005-2010 Romain Ballais <rballais@users.berlios.de> - See LICENSE file for licence information.)"""

import gtk

# A the 'gefica' directory to the path:
import sys
import os.path
sys.path.append(os.path.abspath('./gefica'))

# Import of the main classes:
from gefica.GFCCardsManager import GFCCardsManager
from gefica.GFCInterfaceManager import GFCInterfaceManager

def main():
	"""Application start point. Initializes managers instances and lauch the event loop."""
	interface_manager = GFCInterfaceManager('gefica/glade/interface.glade')
	cards_manager = GFCCardsManager()
	interface_manager.register_cards_manager(cards_manager)
	interface_manager.init_application()

	# Starts the GTK toolkit:
	gtk.main()
	return

if __name__ == '__main__':
	main()
