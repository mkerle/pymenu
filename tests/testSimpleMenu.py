import unittest
from unittest.mock import patch

import pymenu

import menuHandler


class testSimpleMenu(unittest.TestCase):

    def setUp(self):
        
        self.handler = menuHandler.menuHandler()

        self.menuOptions = [ 
            { 'id' : '1', 'text' : 'Simple Option 1', 'func' : self.handler.doSimpleOption1 },
            { 'id' : '2', 'text' : 'Simple Option 2', 'func' : self.handler.doSimpleOption2 },
        ]
        
    
    def testSimpleMenuDoOnce(self):
       
        menu = pymenu.PyMenu()
        menu.setMenuOptions(self.menuOptions)
        
        with patch.object(pymenu, 'input', create=True, return_value='1'):
            menu.doMenuOnce(exitOnError=True)
            self.assertTrue(self.handler.retVal == menuHandler.SIMPLE_OPTION_1_MSG, 'Return value for Option 1 is not expected [%s]' % (self.handler.retVal))


        with patch.object(pymenu, 'input', create=True, return_value='2'):
            menu.doMenuOnce(exitOnError=True)
            self.assertTrue(self.handler.retVal == menuHandler.SIMPLE_OPTION_2_MSG, 'Return value for Option 2 is not expected [%s]' % (self.handler.retVal))
        

    def testSimpleMenuDoOnceInvalidOption(self):

        menu = pymenu.PyMenu()
        menu.setMenuOptions(self.menuOptions)
        
        with patch.object(pymenu, 'input', create=True, return_value='3'):
            menu.doMenuOnce(exitOnError=True)
            self.assertTrue(self.handler.retVal == None, 'Return value for invalid option is not expected [%s]' % (self.handler.retVal))


    def testSimpleMenuCancelOption(self):

        menu = pymenu.PyMenu(includeCancelOption=True)
        menu.setMenuOptions(self.menuOptions)
        
        with patch.object(pymenu, 'input', create=True, return_value='C'):
            menu.doMenuOnce(exitOnError=False)
            self.assertTrue(self.handler.retVal == None, 'Return value for invalid option is not expected [%s]' % (self.handler.retVal))               
        
