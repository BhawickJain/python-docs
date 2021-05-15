# Manages variables defined under the class constant
# prevents them from being mutated
# modified from Alex Martelli Implementation
# http://web.archive.org/web/20100523132518/http://code.activestate.com/recipes/65207-constants-in-python/?in=user-97991

class _const:
    #TODO DocString it
    class ConstError(TypeError): pass
    
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("Can't rebind const(%s)"%name)
        self.__dict__[name] = value
        
    def __delattr__(self, name):
        if name in self.__dict__:
            raise self.ConstError("Can't unbind const(%s)"%name)
            
        raise NameError(name)

# import sys
# sys.modules[__name__] = _const()  # add _const as const in sys module
