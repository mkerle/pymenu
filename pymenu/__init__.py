import pytext

class PyMenu(object):

    DEFAULT_PROMPT = 'Enter choice: '
    DEFAULT_UNKNOWN_MENU_OPTION = 'Unknown menu option!'
    DEFAULT_DISPLAY_CANCEL_OPTION = False
    DEFAULT_CANCEL_OPTION_ID = 'C'
    DEFAULT_CANCEL_OPTION_MSG = 'Cancel'

    def __init__(self, title='Menu', prompt=DEFAULT_PROMPT, unknownMenuOption=DEFAULT_UNKNOWN_MENU_OPTION, includeCancelOption=DEFAULT_DISPLAY_CANCEL_OPTION):
        
        self.title = title
        self.prompt = prompt
        self.unknownMenuOption = unknownMenuOption

        self.args = None
        self.kwargs = None

        self.includeCancelOption = includeCancelOption
        self.cancelOptionID = self.DEFAULT_CANCEL_OPTION_ID
        self.cancelOptionMsg = self.DEFAULT_CANCEL_OPTION_MSG

        self.exitMenu = False

        self.headerCallback = None
        self.headerCallbackArgs = None
        self.headerCallbackKwargs = None

    def overrideCancelOption(self, id, text):
        self.cancelOptionID = id
        self.cancelOptionMsg = text

    def exitMenuHandler(self):

        self.exitMenu = True

    def setHeaderCallback(self, callback, *args, **kwargs):

        self.headerCallback = callback
        self.headerCallbackArgs = args
        self.headerCallbackKwargs = kwargs

    def _parseOption(self, option):

        if (type(option) == dict):
            if ('id' in option and 'text' in option and 'func' in option):

                if ('args' not in option):
                    option['args'] = [ ]

                if ('kwargs' not in option):
                    option['kwargs'] = { }

                return True

            else:
                raise ValueError('Option should contain at least "id", "text" and "func" fields.')

        else:
            raise ValueError('Option is not of type dictionary')

    def _parseOptions(self, options):

        for option in options:
            self._parseOption(option)


    def setMenuOptions(self, options):

        self._parseOptions(options)

        self.options = options

        if (self.includeCancelOption):
            self.options.append( {'id' : self.cancelOptionID, 'text' : self.cancelOptionMsg, 'func' : self.exitMenuHandler, 'args' : [ ], 'kwargs' : { } })

    def doPrompt(self):

        return input('\n%s' % (self.prompt))

    def displayUnknownMenuOption(self):

        print('\n%s' % (self.unknownMenuOption))

    def parseMenuChoice(self, choice):

        return choice

    def handleMenuChoice(self, choice):
        
        for option in self.options:
            if (choice == option['id']):                

                option['func'](*option['args'], **option['kwargs'])
                return True
        
        self.displayUnknownMenuOption()
        return False
            

    def displayMenu(self):

        title = '\n<HEADER><UNDERLINE>%s</UNDERLINE></HEADER>' % (self.title)
        print(pytext.getConsoleText(title))

        if (self.headerCallback is not None):
            headerText = ''
            if (type(self.headerCallbackArgs == tuple)):
                headerText = self.headerCallback(*self.headerCallbackArgs, **self.headerCallbackKwargs)                
            else:
                headerText = self.headerCallback()
            print(' %s\n' % (headerText))

        for option in self.options:

            print(' [%s]\t%s' % (option.get('id', 'ERR!'), option.get('text', 'ERR!')))

        choice = self.doPrompt()

        parsedChoice = self.parseMenuChoice(choice)

        return self.handleMenuChoice(parsedChoice)

    def doMenuOnce(self, exitOnError=False):

        self.exitMenu = False
        
        if (exitOnError):
            self.displayMenu()
        else:
            while (not (self.includeCancelOption and self.exitMenu) or not self.displayMenu()):
                pass

    def doMenuLoop(self):

        self.exitMenu = False
        while (not self.exitMenu):
            self.displayMenu()



