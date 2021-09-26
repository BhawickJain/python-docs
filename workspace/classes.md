## Classes


Now Python does offer typing / custom type definitions, so
`[?]` How do class emulate type definitions in Python, the [python docs](https://docs.python.org/3/tutorial/classes.html) seems to imply classes can be used to define new types of objects.
`[?]` How does this constrasto typed languages where you can choose something to be a type using some kind of `struct` token or a class?

```python
spam = "global spam trolol"
def another_wrapper():
    def scope_test():
        def do_local():
            spam = "local spam"

        def do_nonlocal():
            nonlocal spam
            spam = "nonlocal spam"

        def do_global():
            pass
#             global spam
#             spam = "global spam"

        spam = "test spam"
        do_local()
        print("After local assignment:", spam) #test spam
        do_nonlocal()
        print("After nonlocal assignment:", spam) #nonlocal spam
        do_global()
        print("After global assignment:", spam) #global spam

    scope_test()

    
another_wrapper()
print("In global scope:", spam)
```

local spam creates a `spam` table in the own symbol table within `do_local()`, which means the `spam` symbol in the next table up is unaffected. So the spam at the `scope_test()` level is unaffected.

`nonlocal` keyword causes python to seek a `spam` that is not in the current symbol table but somewhere earlier in the calling symbol tables. There it finds `spam` at the `scope_test()` level. This excludes the `global` scope, [[py-docs-nonlocal](https://docs.python.org/3/reference/simple_stmts.html#nonlocal)].

`global` keyword causes python to seek a `spam` at the module level which is the very first symbol table, with the largest scope. In this instance no such word exists so the keyword goes ahead and creates readies to create a new `spam` word at the global symbol table. Note that the word is not created until the assignment has been executed.


### Creating an attribute and deleting an attribute

```python
class modname: pass
modname.the_answer = 42
modname.the_answer
```

remove the binding of the attribute with the `del` token

```python
del modname.the_answer
modname.the_answer
```

<!-- #region -->
```python
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
/tmp/ipykernel_45/2084199004.py in <module>
      1 del modname.the_answer
----> 2 modname.the_answer

AttributeError: type object 'modname' has no attribute 'the_answer'
```
<!-- #endregion -->

### Class Objects

When the intepreter moves through a `class` definition, a class object is created. From there instances of it can be instantiated.

```python
class MyClass:
    """A simple example class"""
    i = 12345
    
    def f(self):
        return 'hello world'
```

`i` is a class scope variable.


the docstring automatically is parsed into the `MyClass.__doc__`

```python
MyClass.__doc__
```

Instantiated `MyClass` to x

```python
x = MyClass()
```

```python
x.f()
```

```python
y = MyClass()
y.f()
```

You can change the MyClass class scope attributes like so

```python
MyClass.i = 67890
```

This changes the `i` attribute each instance of `MyClass` object shares.

```python
x.i
```

```python
y.i
```

But you can overshadow that attribute with anothe `i` attribute that is local the instance of a `MyClass` object.

```python
y.i = 123456
y.i
```

This means that changing the attribute of `MyClass` does not affect instances of the object that have their local attributes.

```python
MyClass.i = "hello"
```

```python
y.i #123456
```

```python
x.i #123456
```

the `self` is passed in so that the object instance's own methods and attributes are availabel in the functions scope, otherwise they would all be not accessible or deleted when the scope is exited.

```python
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
        
y = Complex(3.0, -4.5)
y.r, y.i
```


Using the `__init__` method build into all classes, and runs whenever a new instance of a class object is created. 

You can automatically additional run code just when a new instance of the object has been created. So when you run `Complex()`, it creates an instance of the `Complex` class object, then runs `__init__` which is tasked to define the `i` and `r`. This means any arguments sent into the `__init__` will need to be given at instantiation, `Complex(3.0, -4.5)`.

```python
x.counter = 1  # create a data attribute to x object
while x.counter < 10: # mutate the data attribute
    x.counter *= 2

print(x.counter) 
del x.counter # remove data attribute to x object
```

```python
x.f()
```

```python
xf = x.f # pass x.f attribute to function f() to xf.
for _ in range(3):
    print(xf())
```

```python
class Dog:
    
    kind = 'canine' # class variable shared by all instances
    
    def __init__(self, name):
        self.name = name # instance variable unique to each instance
```

```python
d = Dog('Fido')
e = Dog('Buddy')
d.kind
d.kind
d.name
e.name
```

```python
class Dog: 
    
    tricks = {} # This is seen as a dictionary
    tricks = set()
    
    def __init__(self, name):
        self.name = name
    
    def add_trick(self, trick):
        self.tricks.add(trick)
```

```python
d = Dog('Fido')
e = Dog('Buddy')

d.add_trick('roll over')
e.add_trick('play dead')

d.tricks # but I thought d could only do roll over, only e knows how to play dead!
```

Other problems also include that `tricks` should be a set not an array to ensure only items are unique.


corrected version

```python
class Dog:

    kind = "canine"
    
    def __init__(self, name):
        self.name = name
        self.tricks = set()
    
    def add_trick(self, trick):
        self.tricks.add(trick)
```

```python
d = Dog('Fido')
e = Dog('Buddy')

d.add_trick('roll over')
e.add_trick('play dead')

d.tricks
```

```python
e.tricks
```

```python
isinstance(d, Exception)
```

```python
class Fluffy_Dog(Dog):

    def fluffiness(self, fluffiness):
        self.fluffiness = fluffiness
```

```python
f = Fluffy_Dog('Lolu')
f. fluffiness(10)
f.add_trick("super-fluffy")
f.name, f.tricks, f.kind
```

```python
isinstance(f, Dog)
```

```python
isinstance(f, Fluffy_Dog)
```

```python
issubclass(Fluffy_Dog, Dog)
```

Interestingly

```python
issubclass(bool, int)
```

```python
issubclass(float, int)
```

```python
issubclass(int, float)
```

### Using `super`

[Docs](https://docs.python.org/3/library/functions.html#super)  
[[py-docs-guide-super](https://rhettinger.wordpress.com/2011/05/26/super-considered-super/)]


`[ ]` Create a multiple inheretance example

`[ ]` Create a privat variables example


You can define a type using an empty `class` and treat is as though it is a `struct` like in C or C++.

```python
class Employee:
    pass

personA = Employee()
personA.name = "Bill Bryson"
personA.dept = "Literature"
personA.famous = True
```

```python
personA.__self__()
```

```python
class Reverse:
    """Iterator for looping over a sequence backwards"""
    
    def __init__(self, data):
        self.data = data
        self.index = len(data)
        
    def __iter__(self):
        """
        __iter__ usually returns a __next__ method but
        this is handled by this class and can be
        overshadowed.
        
        return
        ------
        self
        """
        
        return self
    
    def __next__(self):
        """
        When the next item whenever called
        
        return
        ------
        next item in self
        """
        
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
```

Uses the [`StopIteration`](https://docs.python.org/3/library/exceptions.html#StopIteration) signal, specifically raised by the `__next__` method to tell the calling function to stop called `__next__`. This must be handled by the caller.


`[?]` How can a generator be used to make the `Reverse` implementation even more concise?

```python
IterableObject = "abc"

class ReverseEnumerate(Reverse):
    
    def __next__(self):
        """
        return
        ------
        index, next item
        """
    
        if self.index == 0:
            raise StopIteration
        self.index -= 1

        return self.index, self.data[self.index]       
```

```python
a = ReverseEnumerate("abc")
for i, v in a:
    print(i, v)
    
# 2 c
# 1 b
# 0 a
```

### Private Definitions
Private Definitions can be defined by beginning the name with `_`. 

Private definitions can be accessed, including dunders when beginning with `_`, such as `object._`...

```python
class PrivateClassMethod:
    
    def __init__(self, a):
        self.a = a
        
#     def stringify(self):
#         __str__(self)
    
    def __str__(self):
        _str_rep(self.a)

    @classmethod
    def _str_rep(cls, string):
        return str(string)
```

```python
c = PrivateClassMethod("private print method")
```

```python
PrivateClassMethod._str_rep("print")
```

Using the `dir` method you can see that the private method is visible. [[src](https://stackoverflow.com/questions/451963/making-a-method-private-in-a-python-subclass)]

```python
dir(PrivateClassMethod)
```

```python
class AddonPrivateClassMethod(PrivateClassMethod):
    def __str__(self):
        return self._str_rep((self.a + ' x ')*2)
```

```python
d = AddonPrivateClassMethod("additional class")
```

```python
str(d)
```

```python
class Dog(object):
    
    @classmethod
    def __bark(self):
        print("woof")
```

```python
Dog._Dog__bark()
```

```python
dexter = Dog()
dexter._Dog__bark()
```

```python
class Num:
    def __init__(self,num):
        self.n1 = num

class Num2(Num):
    def show(self):
        print(self.n1)

mynumber = Num2(8)
mynumber.show()
```

```python
class Num2(Num):
    def __init__(self,num):
        self.n2 = num*2
    
    def show(self):
        print(self.n1, self.n2)
```

```python
mynumber = Num2(8)
mynumber.show()
```

the correction for this is

```python
class Num2(Num):
    def __init__(self,num):
        """
        Run __init__ of base class to get attributes and setup
        that provides before adding additional ones
        """
        Num.__init__(self,num)
        self.n2 = num*2
        
    def show(self):
        print(self.n1, self.n2)
```

```python
mynumber = Num2(8)
mynumber.show()
```

Trying to mimick PyTorch `__init__` definition of `super()` in [[src](https://pytorch.org/docs/stable/_modules/torch/nn/modules/container.html#Sequential)]  
`[?]` See if you can implement the above with `super()`

```python
class Num2(Num):
    def __init__(self, num):
        """
        Run __init__ of base class to get attributes and setup
        that provides before adding additional ones
        """
        super(Num, self).__init__()
        self.n2 = num*2
    
    def show(self):
        print(self.n1, self.n2)
```

```python
mynumber = Num2(8)
mynumber.show()
```

## `@property`

```python
class C_sugar:
    
    def __init__(self):
        self._x = None
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def setx(self, value):
        self._x = value
    
    @x.deleter
    def delx(self, value):
        self._x = None
```

Every attribute has a set of function that allow python to _get_, _set_ and _delete_ value in that attribute. They are called `fget`, `fset` and `fdel`. There is a built-in function called `property(f)`, where `f` is a function that allows you to change an attributes means of access by setting custom functions.


In the example we created a private attribute `_x` and a function called `x`. The function has the `property` decorator which makes the function itself an `fget`. Since `x` is an attribute to that function, we can now access `x` to access `_x` without having to call it directly.

```python
c = C()
c.x
```

Without using syntactic sugar, this is what the `@property` is doing.

```python
class C:
    
    def __init__(self):
        self._x = None
        
    def getx(self):
        return self._x
    
    def setx(self, value):
        self._x = value
        
    def delx(self, value):
        self._x = None
        
    x = property(getx, setx, delx, 'x is a hidden property')
```

```python
c = C()
c.x = "value"
```

You could create a `classproperty` [[src](https://stackoverflow.com/questions/5189699/how-to-make-a-class-property)]


## `@classmethod` and `staticmethod`

```python
https://stackoverflow.com/questions/12179271/meaning-of-classmethod-and-staticmethod-for-beginner


```
