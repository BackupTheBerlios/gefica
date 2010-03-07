#!/usr/bin/env python

from distutils.core import setup

setup(	name='gefica',
	version='0.1.0',
	description='Chinese character cards generator',
	author='Romain Ballais',
	author_email='rballais@users.berlios.de',
	url='http://gefica.berlios.de',
	scripts=['gefica.py'],
	packages=['gefica'],
	data_files=[
		('local/share/gefica/glade', ['gefica/glade/interface.glade', 'gefica/glade/interface.gladep']),
		('local/share/gefica', ['doc/Template.svg']),
		('local/share/doc/gefica', ['doc/Exemple-s.svg', 'doc/Exemple-s.pdf']),
		]
	)
