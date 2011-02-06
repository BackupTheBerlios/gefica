#!/usr/bin/env python

from distutils.core import setup

setup(	name='gefica',
	version='0.1.0',
	description='Chinese character cards generator',
	author='Romain Ballais',
	author_email='rballais@users.berlios.de',
	url='http://gefica.berlios.de',
	scripts=['gefica.py'],
	packages=['gfc'],
	data_files=[
		('share/gefica/glade', ['gfc/glade/interface.glade', 'gfc/glade/interface.gladep']),
		('share/gefica/templates', ['data/Template.svg']),
		('share/doc/gefica', ['doc/_build/latex/GeFiCa.pdf']),
		]
	)
