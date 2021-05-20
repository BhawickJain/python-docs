# Implements stackoverflow comment by nvd
# https://stackoverflow.com/questions/2682745/how-do-i-create-a-constant-in-python?noredirect=1&lq=1

class _const:
    
    """
    Defined constants with @property
    """
    
    @property
    def PI(self):
        return 3.14
    
import sys
sys.modules[__name__] = _const()