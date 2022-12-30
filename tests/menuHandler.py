
SIMPLE_OPTION_1_MSG = 'Simple Option 1 selected...'
SIMPLE_OPTION_2_MSG = 'Simple Option 2 selected...'

POSITIONAL_OPTION_1_MULTIPLIER = 2

NAMED_OPTION_1_APPEND_STR = '_appended'

MIXED_OPTION_1_Y_MULTIPLIER = 2

class menuHandler(object):

    def __init__(self):
        self.retVal = None

    def doSimpleOption1(self):
        self.retVal = SIMPLE_OPTION_1_MSG

    def doSimpleOption2(self):
        self.retVal = SIMPLE_OPTION_2_MSG

    def doPositionalArgOption1(self, x):

        self.retVal = x*POSITIONAL_OPTION_1_MULTIPLIER

    def doNamedArgOption1(self, name=''):

        self.retVal = name + NAMED_OPTION_1_APPEND_STR

    def doMixedArgOption1(self, x, y=MIXED_OPTION_1_Y_MULTIPLIER):

        self.retVal = x*y