import unittest
from unittest.mock import patch

import pymenu

import menuHandler


class testPositionalArgMenu(unittest.TestCase):

    def setUp(self):
        
        self.handler = menuHandler.menuHandler()

        self.menuOptions = [ 
            { 'id' : '1', 'text' : 'Positional Option 1', 'func' : self.handler.doPositionalArgOption1, 'args' : True }
        ]
        
    
    def testPositionalArg(self):

        val = 10
       
        menu = pymenu.PyMenu()
        menu.setMenuOptions(self.menuOptions)
        menu.setFunctionArgs(val)
        
        with patch.object(pymenu, 'input', create=True, return_value='1'):
            menu.doMenuOnce(exitOnError=True)
            self.assertTrue(self.handler.retVal == val*menuHandler.POSITIONAL_OPTION_1_MULTIPLIER, 'Return value for Option 1 is not expected [%d]' % (self.handler.retVal))


       
        
