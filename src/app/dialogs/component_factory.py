'''
Created on Dec 8, 2013

@author: Chris
'''

import wx
from argparse import (
	_StoreAction, _StoreConstAction, 
	_StoreFalseAction, _StoreTrueAction, 
	_CountAction, _AppendAction)

class ComponentFactory(object):
	'''
	Generates Wx Components from the argparse action types
	
	         COMPONENT MAP
	     Action   		 WxWidget 
	  --------------------------
        store        TextCtrl 
  store_const        CheckBox 
   store_true        CheckBox 
  store_False        CheckBox
       append        TextCtrl  
        count 			 DropDown
       choice        DropDown
       
  _HelpAction(option_strings=['-h', '--help'], dest='help', nargs=0, const=None, default='==SUPPRESS==', type=None, choices=None, help='show this help message and exit', metavar=None)
	_StoreAction(option_strings=[], dest='filename', nargs=None, const=None, default=None, type=None, choices=None, help='filename', metavar=None)
	_StoreTrueAction(option_strings=['-r', '--recursive'], dest='recurse', nargs=0, const=True, default=False, type=None, choices=None, help='recurse into subfolders [default: %(default)s]', metavar=None)
	_CountAction(option_strings=['-v', '--verbose'], dest='verbose', nargs=0, const=None, default=None, type=None, choices=None, help='set verbosity level [default: %(default)s]', metavar=None)
	_AppendAction(option_strings=['-i', '--include'], dest='include', nargs=None, const=None, default=None, type=None, choices=None, help='only include paths matching this regex pattern. Note: exclude is given preference over include. [default: %(default)s]', metavar='RE')
	_StoreAction(option_strings=['-e', '--exclude'], dest='exclude', nargs=None, const=None, default=None, type=None, choices=None, help='exclude paths matching this regex pattern. [default: %(default)s]', metavar='RE')
	_VersionAction(option_strings=['-V', '--version'], dest='version', nargs=0, const=None, default='==SUPPRESS==', type=None, choices=None, help="show program's version number and exit", metavar=None)
	_StoreAction(option_strings=['-T', '--tester'], dest='tester', nargs=None, const=None, default=None, type=None, choices=['yes', 'no'], help=None, metavar=None)
	_StoreAction(option_strings=[], dest='paths', nargs='+', const=None, default=None, type=None, choices=None, help='paths to folder(s) with source file(s) [default: %(default)s]', metavar='path')
	usage: example_argparse_souce.py [-h] [-r] [-v] [-i RE] [-e RE] [-V]
	'''
	
	def __init__(self, parser):
		self._parser = parser
		self._actions = self._parser._actions[:] # Copy all of the actions
		
		self._positionals = self.get_positionals(self._actions)
		self._choices			= self.get_optionals_with_choices(self._actions)
		self._optionals 	= self.get_optionals_without_choices(self._actions) 
		self._booleans 		= self.get_flag_style_optionals(self._actions)
		self._counters 		= self.get_counter_actions(self._actions)
		


if __name__ == '__main__':
	pass
		
				
				
				
				
				