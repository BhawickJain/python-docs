# Implements stackoverflow comment by nvd
# https://stackoverflow.com/questions/2682745/how-do-i-create-a-constant-in-python?noredirect=1&lq=1

class _const:
    
    """
    Defined constants with @property
    """
    
    @property
    def PI(self):
        return 3.14
    
#     # Uncomment to disallow new attributes to be set    
#     def __setattr__(self, name, value):
#         raise TypeError("Setting new attributes not allowed")
    
import sys
sys.modules[__name__] = _const()