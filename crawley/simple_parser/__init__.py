"""
    A simple parser that interpretes the KISS_Crawley-BNF
"""

from parsers import DSLAnalizer
from compilers import Interpreter

def interprete(dsl):
    
    analzier = DSLAnalizer(dsl)
    sentenses = analzier.parse_sentences()
    
    scraper = Interpreter(sentenses).compile()
    return scraper