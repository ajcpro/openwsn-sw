
import logging
class NullHandler(logging.Handler):
    def emit(self, record):
        pass
log = logging.getLogger('ParserError')
log.setLevel(logging.ERROR)
log.addHandler(NullHandler())

from ParserException import ParserException
import Parser

class ParserError(Parser.Parser):
    
    def __init__(self):
        
        # log
        log.debug("create instance")
        
        # initialize parent class
        Parser.Parser.__init__(self,1)
    
    #======================== public ==========================================
    
    #======================== private =========================================