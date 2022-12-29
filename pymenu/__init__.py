import re

class PyMenu(object):

    DEFAULT_PROMPT = 'Enter choice: '
    DEFAULT_UNKNOWN_MENU_OPTION = 'Unknown menu option!'

    def __init__(self, prompt=DEFAULT_PROMPT, unknownMenuOption=DEFAULT_UNKNOWN_MENU_OPTION):
        
        self.prompt = prompt
        self.unknownMenuOption = unknownMenuOption

        self.args = None
        self.kwargs = None

    def setFunctionArgs(self, *args, **kwargs):

        self.args = args
        self.kwargs = kwargs

    def _parseOption(self, option):

        if (type(option) == dict):
            if ('id' in option and 'text' in option and 'func' in option):

                if ('args' not in option):
                    option['args'] = False

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

    def doPrompt(self):

        return input('\n%s' % (self.prompt))

    def displayUnknownMenuOption(self):

        print('\n%s' % (self.unknownMenuOption))

    def parseMenuChoice(self, choice):

        return choice

    def handleMenuChoice(self, choice):

        foundOption = False
        for option in self.options:
            if (choice == option['id']):
                foundOption = True
                if (option['args']):
                    option['func'](*self.args, **self.kwargs)
                else:
                    option['func']()
                break
        
        if (not foundOption):
            self.displayUnknownMenuOption()

    def displayMenu(self):

        print('\n')
        for option in self.options:

            print(' [%s]\t%s' % (option.get('id', 'ERR!'), option.get('text', 'ERR!')))

        choice = self.doPrompt()

        parsedChoice = self.parseMenuChoice(choice)

        self.handleMenuChoice(parsedChoice)