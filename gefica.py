#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gtk

# A the 'gefica' directory to the path:
import sys
import os.path
sys.path.append(os.path.abspath('./gefica'))

# Import of the main classes:
from gefica.GFCCardsManager import GFCCardsManager
from gefica.GFCInterfaceManager import GFCInterfaceManager

def main():
	im = GFCInterfaceManager('gefica/glade/interface.glade')
	cm = GFCCardsManager()
	im.register_cards_manager(cm)
	im.init_application()

	# Starts the GTK toolkit:
	gtk.main()
	return

if __name__ == '__main__':
	main()
