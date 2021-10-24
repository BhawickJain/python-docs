# Manages variables defined under the class constant
# prevents them from being mutated
# modified from Alex Martelli Implementation
# http://web.archive.org/web/20100523132518/http://code.activestate.com/recipes/65207-constants-in-python/?in=user-97991

# _const private class of const module
class _const:
    #TODO DocString it
    
    # Raise custom exception with TypeError as its Abstract Base Class
    class _ConstError(TypeError): pass
    
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self._ConstError("Can't rebind const(%s)"%name)
        self.__dict__[name] = value
        
    def __delattr__(self, name):
        if name in self.__dict__:
            raise self._ConstError("Can't unbind const(%s)"%name)
            
        raise NameError(name)

# Upgrades
# Modified exception raises: https://docs.python.org/3/tutorial/errors.html#raising-exceptions
# Modified __dict__ access with in statement instead of depreciated 

# overwrite the const module reference with _const in sys
import sys
sys.modules[__name__] = _const()

# Allows _const() to be available as a module and only
# instances can be accessed. _const() is hidden by itself.
# Without it, when you add another constant as an attribute,
# you add it to the const.py module instead of _const class. 
# This means that attribute is not subject to the custom
# attribute handling defined.
