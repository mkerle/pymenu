import sys

sys.path.append('../pymenu')

from pymenu import PyMenu


class menuHandler(object):

    def __init__(self):
        pass

    def doOption1(self):
        print('Option 1')

    def doOption2(self, x):

        print('x=%d' % (x))

    def headerCallback(self, x=2):

        return 'This is the header callback text (x=%d)' % (x)


testHandler = menuHandler()

menuOptions = [
    { 'id' : '1', 'text' : 'Simple func (no params)', 'func' : testHandler.doOption1 },
    { 'id' : '2', 'text' : 'Func with positional arg', 'func' : testHandler.doOption2, 'args' : True }
]


menu = PyMenu()
menu.setMenuOptions(menuOptions)
menu.setFunctionArgs(5)
menu.setHeaderCallback(testHandler.headerCallback, x=5)

menu.doMenuOnce(exitOnError=True)