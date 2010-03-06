#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gtk

# A the 'src' directory to the path:
import sys
import os.path
sys.path.append(os.path.abspath('./src'))

# Import of the main classes:
from GFCCard import *
from GFCCardsManager import *
from GFCInterfaceManager import *

def main():
	im = GFCInterfaceManager('src/glade/interface.glade')
	cm = GFCCardsManager()
	im.register_cards_manager(cm)
	im.init_application()

	# Starts the GTK toolkit:
	gtk.main()
	return

if __name__ == '__main__':
	main()
