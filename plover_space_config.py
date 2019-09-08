'''
Functionality to switch spacing styles in Plover without having to open your config.
'''

BEFORE='Before Output'
AFTER='After Output'

from plover.engine import StenoEngine

def toggle(engine: StenoEngine) -> None:
	'''
	Toggle the spacing type.
	'''

	if engine.config['space_placement'] == BEFORE:
		engine.config['space_placement'] = AFTER
	else:
		engine.config['space_placement'] = BEFORE

def before(engine: StenoEngine) -> None:
	'''
	Set spacing to before.
	'''

	engine.config['space_placement'] = BEFORE

def after(engine: StenoEngine) -> None:
	'''
	Set spacing to after.
	'''

	engine.config['space_placement'] = AFTER