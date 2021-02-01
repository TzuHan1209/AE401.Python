Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('hello,world')
hello,world
>>> Print("hello world!")
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    Print("hello world!")
NameError: name 'Print' is not defined
>>> print("hello world!")
hello world!
>>> print(hello world!)
SyntaxError: invalid syntax
>>> print"hello world!"
SyntaxError: invalid syntax
>>> print(int(3.1412956))
3
>>> print(int(3.65))
3
>>> print(float(3.654))
3.654
>>> print(str(3.56))
3.56
>>> print(float(5.5*2.1))
11.55
>>> print(str(5.5*2.1))
11.55
>>> print('i','am','esmond)
      
SyntaxError: EOL while scanning string literal
>>> print('i','am','esmond')
i am esmond
>>>  print('a'+'b'+'c')
 
SyntaxError: unexpected indent
>>> print('a'+'b'+'c')
abc
>>> print('he is','15','years old')
he is 15 years old
>>> print('I''m Eric','He is','"cool"')
Im Eric He is "cool"
>>> print('I''"m Eric','He is','"cool"')
I"m Eric He is "cool"
>>> print('I'''m Eric','He is','"cool"')
      
SyntaxError: invalid syntax
>>> print("I""'m Eric"+'He is'+'"cool"')
I'm EricHe is"cool"
>>> print("I""'m Eric",'He is'+'"cool"')
I'm Eric He is"cool"
>>> name=input('what is your name')
what is your name
>>> name=input('what is your name')                                                 print(name,'hello!')
SyntaxError: invalid syntax
>>> SyntaxError: invalid syntax
SyntaxError: invalid syntax
>>> name=input('what is your name')                                                 
print(name,'hello!')
SyntaxError: multiple statements found while compiling a single statement
>>> 
