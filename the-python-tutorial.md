---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.0
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

## The Python Tutorial
[[doc](https://docs.python.org/3/tutorial/index.html)]

A tour of the noteworthy features of the Python Language and introduces the [Python Standard Library](https://docs.python.org/3/library/index.html#library-index). Python Docs also offer a glossary of terms [[py-docs-glossary](https://docs.python.org/3/glossary.html#glossary)]


`[?]` How do you define a dictionary?  

```python
dict = {"postcode":"BS1 5PL", "line1":"18 Parkstreet"}
```

```python
type(dict)
```

### Whetting your Appetite

`[?]` What problems does Python solve?  
`[>]` Slow development cycles like that of C/C++/Java, requiring write/compile/test/re-compiles. This is particularly true if you want to quickly write a test suite for a C/C++ library, writing it in Python is must faster.

`[?]` Why might you use python over Bash scripts?  
`[>]` Python is portable across many platforms and is a fully features programming language unlike Bash. Bash is also much harder to maintain if its codebase become very large.

`[?]` What are high-level data types?  
`>>>` High-level data structures don't expose pointers, are simpler and on usally faster to implement reliably in general situations.

`[?]` Why might an interpreted language be an advantage?  
`[>]` No compiling and linking is necessary. The code can be written interactively thanks to this. This is helpful to bottom-up development of a program.




### Invoking the Interpretor

`[?]` Where is the python interpreter usually stored?  
`[>]` `/usr/local/bin/python3.9`. Usually placed in the `PATH` variable to make it available in the shell directly.

```python
! python3 --version
```

Invoke a command or module directly through an interpreter.  
`python -c command [arg]`  
`python -m module [arg]`  

Invoke a script and then interact with it.  
`python script.py -1`


`[?]` What encoding do python script usually treated as?  
`[>]` UTF-8


`[?]` How do you declare an encoding that is different to UTF-8 in a script? 

```python
# -*- coding: encoding -*-

# or 

#!/usr/bin/env python3
# -*- coding: encoding -*-
```

### An Informal Introduction to Python


__Numbers__

`[?]` What data type does the `/` division return?  
`[>]` floating point number

```python
type(8/5)
```

```python
type(8/4)
```

`[?]` Does floor division `//` yield a `float` data type?  
`[>]` No, always an `int`.

```python
type(8//5)
```

```python
type(8%5)
```

`[?]` What notation is used for floor and remainder divisons?  


`[?]` What happens when you declare a variable that matches a function?  
`[>]` You mask the function with the local variable making it inaccessible. It almost as though have overwritten it in the local symbol table. Since the built-in symbol table is checked last, it won't check there.


`[?]` How common is it accidently declare variable that has a function of the same name?

```python
round(5.86,0)
```

```python
round = 5.596
```

```python
# round(5.86,0) # TypeError: 'float' object is not callable
```

`[ ]` Create an example that uses `Decimal`, `Fraction` and `ComplexNumbers` objects.


__Strings__

`"..."` `'...'` to write strings with `\` to escape characters.

```python
text = 'is\'t it great!'
text
```

or just do this

```python
text = "is't is great"
text
```

```python
print('first line.\nsecond line')
```

`[?]` When placing `\n` in a string, do you need a space after it?  


`>>>` No, since python knows its expecting a single character.


`[?]` What other characters need to be escaped?


`[?]` When `\n` is placed inside a string variable, what happens?

```python
a = "first line.\nsecond line"
a
```

```python
print(a)
```

You need the `print()` function to make use of the `\n` or equivalent.


`[?]` How can you escape characters in a string without `\`?
`[>]` Write the `r` character right before the quote to treat it as a raw text.

```python
print('C:\some\name')
```

```python
print(r'C:\some\name')
```

`[?]` How do you prevent a new line from printing when using triple-quote literals `"""..."""` and `'''...'''`?

```python
print("""
Usage: thing [OPTIONS]
    -h                           Display this usage message
    -H hostname                  Hostname to connect to
""")
```

Use `\` at the end of the line to remove the spare newline right at the start.

```python
print("""\
Usage: thing [OPTIONS]
    -h                           Display this usage message
    -H hostname                  Hostname to connect to
""")
```

```python
a = """\
Usage: thing [OPTIONS]
    -h                           Display this usage message
    -H hostname                  Hostname to connect to
"""
a
```

```python
print(a)
```

`[?]` What happens when you do the following?

```python
'py' 'thon'
```

`[?]`What happens when you do the following?

```python
3 * 'w' + '.google.com'
```

`[?]` What happens when you do the following?

```python
a = ('These are several string within parentheses '
     'what do you think happens?')
a
```

`[?]` When might it be useful?  
`[>]` Allows for a body of text to be placed without need to wrap text.


`[?]` When doesn't it work?

```python
b = 'what do you think happens?'
a = ('These are several string within parentheses '
     b)
```

```python
prefix = 'Py'
# prefix 'thon'
```

```python
prefix = 'Py'
prefix + 'thon'
```

__Slicing Strings__


`[?]` How do you select the second last character of a string?  

```python
word = 'python'
word[0]   # first character
word[-1]  # last character
word[-2]  # second last character
word[-6]  # first character
```

`[?]` How do you substring?

```python
word[:5]  # 0 to 4 char positions
```

The last number is always ignored. This enables the complementary substring slices to equal the complete word:

```python
word[:2] + word[2:]
```

```python
word[-2:] # last two char
```

```python
word[4:5] # fifth character, equivalent to word[4]
```

```python
word[2:80] # over extending the index leads to just returning 
```

yet when referring to the index directly will result in a type error.

```python
# word[80] # IndexError
```

```python
word[2:6] # word is 6 characters long
```

```python
word[2:5] # although last char is at position 5, the last position is ignored.
```

`[?]` What might be another way to remember the indices in a slice?  
`[>]` The indices can be treated as through they point between the numbers.


```
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```


`[?]` Can you change a single character of a string?

```python
# word[0] = 'j' # TypeError
```

You need to create a new string

```python
'j' + word[1:]
```

`[?]` How do you find the length of a string?

```python
len(word)
```

See also:  
[Text Sequence Type -- Str](https://docs.python.org/3/library/stdtypes.html#textseq)  
[String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)  
[Formatted string literals](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)  
[Format String Syntax](https://docs.python.org/3/library/string.html#formatstrings)  
[printf-style String Formatting](https://docs.python.org/3/library/stdtypes.html#old-string-formatting) -- Describes the `%` operator in more detail  


__Lists__



`[?]` What happens when you slice a list, what does it return?  
`[>]` Returns a new list


`[?]` What when you assign a variable with `alist[:]`?  
`[>]` A shallow copy is created of the list?


`[?]` What is a [shallow copy](https://docs.python.org/3/library/copy.html#shallow-vs-deep-copy)? <br>
`[>]` A shallow copy creates a new object and then creates references to the objects held within the original object to best possible extent. This is instead of deep copy which creates an object but then recursively copies all the objects within into this new object.

`[?]` When should the problem of deep copy and shallow copy be considered?  
`[>]` When you have an object that contains other objects like a `list` type.


`[?]` What problems can occur in deep copy?  
`[?]` Does Python offer a Copy-On-Write feature like Swift?  
`[?]` How might you use the `deepcopy()` function to mitigate this?


`[?]` How are lists different from strings when considering them to be a list of characters?
`[>]` String of Characters are immutible whilst lists are not. Python lists allows mixed data types whilst a string of characters is just that.

```python
squares = [1, 4, 9, 16, 25]
squares[0] # first items with index notation
squares[-1] # 25 
squares[-3:] # [9, 16, 25]
```

`[?]` What does slicing a list do?  
`[>]` It returns a new list.

```python
squares + [36, 49, 64, 81, 100] # Lists can be concatenated
```

```python
squares[-3] = 72  # Lists are mutable
squares
```

`[?]` What other data are `mutable` (like lists) and `immutable` (like strings)? 


`[?]` How do you replace a list of values in a list?

```python
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = ['C', 'D', 'E']
letters
```

`[?]` What is a nifty way to remove a list of items in a list?

```python
letters[2:5] = [] # resize list
letters
```

```python
letters[:] = [] # remove all items
letters
```

`[?]` Can you use the `len` function on `list` types?  
`[?]` Is it possible to implement your own `len` method for your own data structure?


`[?]` How do you select a list of lists?

```python
a = ['a', 'b', 'c']
n = ['1', '2', '3']
c = [a, n]
c
```

```python
c[0][-3]
```

`[?]` What is evaluated first in the two lines?  
`[>]` For Line 1, both variablesa are assigned simultaneously. For Line 2, the LHS terms are evaluated first then the RHS.

```python
a, b = 2, 1
a, b = b, a + b
a, b
```

`[?]` When evaluating an integer as a boolean what does Python and C have in common?  
`[>]` Zero values are considered `False` and non-zero values are considered `True`

`[?]` How is an iterable object evaluated as a boolean?  
`[>]` Its `len()` result is considered and treated: if zero condition is `False`, if non-zero condition is `True`.

```python
a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b
```

`[?]` What does the decorator property `@` in a class do?


### Control Flow Statements


__If Statements__

`[?]` What three statement can be used for an if statement in Python?  
`[>]` `if`, `elif`, `else`

`[?]` When would you use `elif` versus `else`?  <br>
`[>]` `elif` is great when you want to test for another condition. `else` is good _anything else_.

`[?]` What is the `elif` statement a substitute for?  
`[>]` It is a substitute for the `case` operator that is typically offered in a language like `C`. It prevents successive intentation or nesting of if statements.


__For Statements__

`[?]` How is Python's `for` statement different from `Pascals` or `C`?  <br>
`[>]` Pascals can only iterate over progressive number sequences, whilst in C you need to define the iteration and stopping condition. In Python it iterates until you reach the end of a collection, sort of generalising both problems.

`[?]` What is python documentation's recommendation on iterating and modifying a collection simultaneously?  
`[>]` It is tricky to get right and is it best if you create a new or work on a copy of the collection instead.

`[ ]` Create a minimal example to demo this.


__Range Statements__


Predict the following results:

```python
range(5)
```

```python
range(5, 10)
```

```python
range(0, 10, 3)
```

```python
range(-10, -100, -30)
```

`[?]` Why does range not give a list but you can iterate over it as if it is one?  
`[?]` It appears be an iterable object where the `range()` yields when iterated over until exhausted, this prevents a large range from having to be in memory.  

```python
sum(range(4)) # 0 + 1 + 2 + 3
```

`[?]` How do you convert a `range(a)` into a `list`?  <br>
`[>]` Use the `list()` function which takes an iterable object and puts its objects inside into a list

```python
list(range(4))
```

`[?]` Why do the terms in `range(b, a, c)` represent?  
`[>]` `a` is the end number and is never included by the range, `b` is the start point and is always yielded. `c` is the size of the step to add to the inital value. For `range(a)` is treated as `range(0, a, 1)` and `range(b, a)` is treated as `range(b, a, 1)`

```python
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
```

`[?]` How might you use the `range` function enumerate a collection whilst iterating it?  
`[>]` You can use `len(range(list))` to iterate over its yield. That yielded value can be used an index to both know it and access the list item at that index. 


`[?]` What alternatives does Python to iterating and enumerating a python list simulataneosly?  
`[>]` You can use the `enumerate()` statement instead. More info under [Looping Techniques](https://docs.python.org/3/tutorial/datastructures.html#tut-loopidioms)

```python
for i, v in enumerate(a):
    print(i, v)
```

__Break and Continue, and Else Clauses on Loops__


`[?]` What and when is the `break` statement used for?  
`[>]` `break` is used to break out of a while or for loop.  

`[?]` What and where is the `else` statement used for?  
`[>]` `else` can be in a `for` and a `while` statement is executed when loop is exhausted either because nothing was run or the iterable is exhausted.  

`[?]` What is the time when the `else` clause isn't executed?  
`[>]` When there is a break in the loop.  

`[?]` Conceptually, what is `for`, `else` statement similar to?  
`[>]` Python's `try`, `else` statements.


`[?]` What is a `continue` statement?  
`[>]` The `continue` statement like the `pass` clause enables the compiler to do nothing under a block. If you have a loop which under an `if` evaluation simply need to iterate without doing anything else, that's where you use the `continue` clause.  

example of using a `continue` clause

```python
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)

```

`[?]` How can you simplify the following statement?

```python
alpha = "y"
print(f"This is an alphabet: {alpha}")
```

```python
print("This is an alphabet:", alpha)
```

The concatenation in the `print` statement automatically adds a space in between.


`[?]` What is a good use case for the `continue` statement?

`[?]` Can you create good examples where the `break`, `continue` and `else` statements are useful?

```python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
```

__Pass Statements__

`[?]` What does a pass statement do?  
`[>]` Nothing, just tells the compiler to jog on to the next block.


`[?]` Where might the `pass` clause be used for?


Busy-wait statements

```python tags=[]
while True:
    pass # Busy-wait for keyboard interrupt (Ctrl+C)
```

minimal classes

```python
class MyEmptyClass:
    pass
```

`[?]` what are minimal classes?


placeholder for methods whilst they are under-development

```python
def initlog(*args):
    pass # Remember to implement this!
```

`[?]` Where can you use the pass statement in your work?


__Defining Functions__

`[?]` What does `def` stand for?  
`[?]` How does a function manage its local variables?  
`[>]` Through the creation of a new symbol table which stores all local variables.

`[?]` How does a function find the value or method behind a word?  
`[>]` It first checks its local symbol table, then another local symbol table for all the functions, then a global symbol table and then finally a table of built-in names. 

`[?]` Where do the function parameters sit?  
`[>]` In the local symbol table the moment you call it. This means when ever you call another function or itself (recursively) you end up creating a new symbol table for that call. The caller passes object references, instead of the values, which the callee function uses. Once returned back to the caller, that function check for any changes to the objects it referred to.

```python
def fib(n):    # write Fibonnacci series up to n
    """Print a Fibonacci series up to n"""
    a, b = 0, 1
    while a < n: 
        print(a," ")
        a, b = b, a+b
    print()
```

`[?]` How does a function call another function?  
`[>]` Each function has its own local symbol table, in which it has the name of the function and the reference to the function object. This also allows a variable to refer to the function variable.

```python
fib
```

```python
f = fib
f(100)
```

More documentation on [[docstrings](https://docs.python.org/3/tutorial/controlflow.html#tut-docstrings)] <br>
`[?]` What are some good docstring practices?


`[?]` What the difference between a procedure and a function?  
`[>]` A procedure doesn't return anything once it finishes, a function does.  

`[?]` Are Python function always functions?  
`[>]` Yes, as even without the `return` statement the function _still_ `None`

`[?]` What happens when the function stops before return?  
`[>]` Just returns `None`.

```python
print(fib(0))
```

`[?]` How does python enable user-defined type?  
`[>]` Through `Class` blocks.


__Functions and Arguments__

```python
def ask_ok(prompt, retries=4, reminder='Please Try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yee', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries -1 
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
```

`[?]` What are default arguments?  
`[>]` They are just variable names with an assigned value in the function definition, `retries=4`. It allows for sane defaults, and reduces the number of argument you need to send in. 

`[?]` Are there any example fo default arguments?  
`[>]` The `range()` function has sane default for example.

```python
ask_ok("You feeling great?!")
```

```python
ask_ok("You feeling great?", 2, reminder='you sure?')
```

`[?]` How do you check if a value exists in a sequence?  
`[>]` using the `in` keyword.

`[?]` Can the `in` keyword work with `list` and `tuple` types? What about other iterable types?  
`[>]` Yes, all iterable types can be evaluated with the `in` keyword, including the `range()` function.

```python
a
```

```python
'Mary' in a
```

```python
b = (1, 2, 4)
```

```python
4 in b
```

```python
c = range(1,4)
```

```python
3 in c
```

```python
type(c)
```

`[?]` Predict what happens in the following block of code?  

```python
i = 5

def f(arg=i):
    print(arg)
    
i = 6
f()
```

`[>]` `arg=5` as default argument are evaluated when defining the function. Including any expressions in the default arguments. This makes this behaviour a little bit like `const expression` in C++.

```python
i = 5

def f(arg=i**2):
    print(arg)
    
i = 6
f()
```

`[?]` Are default arguments in a function shared between calls?  
`[>]` Yes, default arguments which mutable like a list which are changed in function remain so in the next function all.

`[?]` How many times are default arguments evaluated and what is the consequences of that?  
`[>]` Default arguments are only evaluated once at function definition, this means if the function changes it, it remains to that new value for the next function call. That initial value is never created because the original default expression is never reevaluated.

```python
def f(a, L=[]):
    L.append(a)
    return L
```

```python
f(1)
```

```python
f(2)
```

```python
f(3)
```

`[?]` How might you prevent the sharing of default arguments between calls?  
`[>]` By setting the default argument to `None`, then changing it to the default value and type given it is None.

```python
def g(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
```

```python
g(1)
```

```python
g(2)
```

`[?]` Is `None` always evaluated even though the function default argument are always evaluated once?  
`[>]` My hunch is, that by setting the default arg as `None` you have not instatiated it in the symbol table. So when you declare the variable inside the function do a fresh evaluation for that specific call which resets the value to a default.


```python
def h(a, L=None):
    if L is None:
        pass
    return L
```

```python
h(2)
```

Notice how L is nothing, the `return` statement doesn't even give `None` as an answer.


__Keyword Arguments__

`[?]` What are keyword arguments? How are they different from normal arguments?  
`[>]` They are just arguments which are preceded by an identifier. [[py-docs-kwarg](https://docs.python.org/3/glossary.html#term-argument)]  

`[?]` Are default arguments keyword arguments?  
`[?]` Yes.



```python
def parrot(voltage, state='a stuff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "voltags through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
```

`[?]` Identify the result the type of arguments being sent in.

```python
parrot(1000)
```

```python
parrot(voltage=1000)
```

```python
parrot(voltage=1000, action='VOOM')
```

```python
parrot(action='VOOM', voltage=1000)
```

```python
parrot('a million', 'bereft of life' 'jump')
```

```python
parrot('a thousand', state='pushing up the daisies')
```

`[?]` Can you send a keyword argument a positional argument?  
`[>]` Yes, you just need to make sure you match the position and it precedes any keyword arguments being declared.

`[?]` Why might it be that you have you declare positional argument before keyword arguments?  
`[>]` Because keyword arguments can be declared in any order, once you have declared a keyword argument it wouldn't necessarily be in the next position. So you can't assume positional arguments.


`[?]` The following statements will throw errors, why might this be?

```python
parrot()
parrot(voltage=5.0, 'dead')
parrot(110, voltage=220)
parrot(actor='John Cleese')
```

`[?]` How do you make an argument optional?  
`[>]` By giving it a keyword argument with a default value.

```python
def function(a):
    pass

function(0, a=0)
```

__Tuple and Dictionary Arguments__



```python
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
```

`[?]` Of what `type` are `*arguments` and `**keywords`? <br>

```python
def afunc(word, *words, **keywords):
    print('*words',type(words))
    print('**keywords', type(keywords))

afunc('words', 'sun', 'lee', weather='sunny', beach='sand')
```

`[>]` Arguments marked by `*` are tuples and `**` keyword dictionaries. see [[py-doc-map-dict](https://docs.python.org/3/library/stdtypes.html#typesmapping)] and [[py-docs-tuples](https://docs.python.org/3/tutorial/datastructures.html#tut-tuples)].

```python
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
```

`[?]` Can you think of function that would require these features? <br>
`[?]` Why not use an `array` type instead of `tuple` for `*arguments`?  <br>
`[>]` Because `tuples` immutable, which is handy here.


__Special Parameters__

`[?]` What additional notation can you use when defining a function?  
`[>]` For the moment you can use `/` to say that to the left are positional arguments, and the right are position or keyword arguments, and `*` to the right are keyword only arguments. `def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2)`

`[?]` Why would you use the special parameters?  
`[>]` To force the user of the function to specify what parameters are positional or belong to a keyword. Without them, an argument can be both positional or a keyword.

```python
def standard_arg(arg):
    print(arg)
    
def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)
    
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)
```

```python
pos_only_arg(5)
```

```python
kwd_only_arg(arg=5)
```

```python
combined_example(5, standard=5, kwd_only=6)
```

```python
combined_example(5, 5, kwd_only=6)
```

`[ ]` explain the error messages 

```python
kwd_only_arg(5)
```

```python
combined_example(kwd_only=6, 5, 5)
```

```python
combined_example(pos_only=6, 5, kwd_only=5)
```

This notation can be used to prevent potential collision between function parameter names and keyword dictionaries

```python
def foo(name, **kwds):
    return 'name' in kwds
```

```python
foo(1, **{'name':2})
```

Here what you are essentially sending in is: `foo(name=1, name=2)`

```python
def foo(name, /, **kwds):
    return 'name' in kwds
```

```python
foo(1, **{'name':2})
```

`[?]` For function safety, why you want to use a `/` between positional and keyword dictionary inputs?  
`[>]` To prevent a potential clash in the names.


`[?]` Why does the following function definition fail?

```python
def foo(name, *, **kwds):
    return 'name' in kwds
```

`[>]` Because `*` is expecting a keyword argument straight after it, not a dictionary of keywords

```python
def foo(name, *, pos, **kwds):
    return 'name' in kwds
```

```python
foo('Ani', pos=5, **{'j':6, 'b':7})
```

`[?]` Which notation `*` or `/` can be removed without breaking the function?  

```python
def foo(name, /, *, pos, **kwds):
    return 'name' in kwds
```

```python
foo('Lemi', pos=8, **{'name':9, 'c':9})
```

`[>]` Both `*` and `/` can be used but `*` forces the user to refer to the `pos` arg by its keyword.

```python
foo('Lemi', 8, **{'name':9, 'c':9})
```

Using the `/` can give additional flexibiity but with a potential name clash if `**kwds` also has a `pos` keyword.

```python
def foo(name, /, pos=8, **kwds):
    return 'name' in kwds
```

```python
foo('Lemi', 8, **{'name':9, 'c':9})
```

```python
foo('Lemi', 8, **{'pos':9, 'c':9})
```

`[?]` Must `**kwds` Keyword dictionaries must always be the last terms in the function?  
`[>]` It must be a the last and only term as it enables an opportunity for the user of the function ot add additional keyword parameters they would other not be able to - without modifying the function itself.

```python
def foo(**kwds, word):
    return 'name' in kwds
```

You can still send in additional keywords after the `pos` keyword which is referred to in the positional form.

```python
foo('Lemi', 8, name=9, c=9)
```

`[?]` How do you specify a dictionary belongs to the keyword dictionary parameter of the function?  
`[>]` Use `**` to mark the dictionary to be the keyword dictionary parameter.


`[?]` Why are some of the basic run in parameter definitions when defining a function?  
`[>]` Positional argument then Keyword Arguments, Tuples, Keyword Dictinonaries, you can swap that order as then Python has no way of guaranteeing a match between the arguments sent in and the parameters.


`[?]` Can you have multiple Keywords Dictionary parameters in a function?  
`[>]` No, likely because of clashes. The only way to do it is to send two normal arguments as only one can be a keyword dictionary. [[so-two-kwd-arg](https://stackoverflow.com/questions/24355751/pass-multiple-dictionaries-to-a-function-as-an-argument)].

```python
def foo(word, **kwd1, **kwd2):
    print(word)
    print('name' in kwd1)
    print('person' in kwd2)
```

`[?]` Do the rules for `**kwds` apply for `*args` too?


`[?]` What makes positional arguments useful?  
`[>]` Positional arguments don't have any meaning which means they are easier to use and the user can just write the values in the order defined in the docs. It also helps enforce the order whilst not making the names of the parameters available. A positional argument could be seen as the essential part of the function, like the `string` input of the `print()` function.  


`[?]` What makes keyword arguments so useful?  
`[>]` Keyword argument ensure user is used specifying the terms and this means less errors are made. Making and forcing the usage of the names of the parameters gives the user more meaning over the functionality available. This is useful when there are options which no obvious order to them for example.


`[?]` What kind of argument should you use for APIs?  
`[>]` Best to use positional argument to prevent breaking changes if the name of the parameter is changed.  
`[>]` That said, if the name of the parameter is changed it might also change meaning of the parameter so the change would be breaking anyway.  
`[?]` Find an example where API change would support and no support positional-only arguments. Likely in CLI app development.  


__Arbitrary Argument Lists__


`[?]` What are `*arg` and `**kwds` referred to in functions?  
`[>]` variadic arguments.

`[?]` When are are they evaluated?  
`[>]` At function call but only once all the positional and keyword arguments are satisfied.  


`[?]` Can arguments be declared after `*arg`?  <br>
`[>]` Yes but only keyword arguments.  

```python
def concat(*arg, sep='/'):
    return sep.join(arg)
```

```python
concat("folders","file")
```

```python
concat("what", "three", "words", sep='.')
```

`[?]` Can arguments be delcared after `**kwds`?  <br>
`[>]` No, it must be the last one.

```python
def keys(**kwds, end='\n'):
    for k in kwds:
        print(k,kwds[k], end)
```

```python
def keys(end='\n', **kwds):
    for k in kwds:
        print(k, kwds[k], end)
```

```python
keys(word=1, print=2)
```

### Passing around a function

```python
def add(a, b):
    
    try:
        return a + b
    except TypeError as err:
        print(f"Type Error: ensure inputs are of integer / double type -- Message: {err}")
    except Exception as err:
        print(f"Unexected Error Occured: {err}")
```

```python
add(1, 4)
# 5
```

```python
add(4, "b")
```

Lets define a function called addition which one may call

```python
addition = add
```

```python
addition(1, 5)
```

```python
addition('b', 3)
```

```python
def annotate(add, a, b):
    
    try:
        return print(f"Annotate result {add(a, b)}")
    except Exception as err:
        print(f"Unexpected Error: {err}")
```

```python
annotate(add, 4, 5)
```

```python
addition(1, 3)
```

This feature nicely takes one to annotations using the `@` symbol


### Style Guide

[[pep-8](https://www.python.org/dev/peps/pep-0008/)] Style Guide for Python Code -- [trace](https://stackoverflow.com/questions/3298464/how-can-i-learn-more-about-python-s-internals)
