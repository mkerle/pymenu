import unittest
from unittest.mock import patch

import pymenu

import menuHandler


class testPositionalArgMenu(unittest.TestCase):

    def setUp(self):
        
        self.handler = menuHandler.menuHandler()

        self.val = 10

        self.menuOptions = [ 
            { 'id' : '1', 'text' : 'Positional Option 1', 'func' : self.handler.doPositionalArgOption1, 'args' : [self.val] }
        ]
        
    
    def testPositionalArg(self):
       
        menu = pymenu.PyMenu()
        menu.setMenuOptions(self.menuOptions)
        
        with patch.object(pymenu, 'input', create=True, return_value='1'):
            menu.doMenuOnce(exitOnError=True)
            self.assertTrue(self.handler.retVal == self.val*menuHandler.POSITIONAL_OPTION_1_MULTIPLIER, 'Return value for Option 1 is not expected [%d]' % (self.handler.retVal))


       
        
