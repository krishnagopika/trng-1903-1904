
# Lecture Plan


1. Class & Objects
2. Object Oriented Programming
3. Exception handiling
4. File handiling



**Class:** A class to combine the data and functionality together.

**Object:** instance of a class

**private variable** 

```
_variableName
```

**name mangling:** used to override the methods of parent class with 

```python
class Parent:
    name = "Parent"
    def return_name(self):
        return self.name 
    
    __return_name = return_name # private copy for parent class

    # _Parent_return_name (_class_method)


class Child(Parent):
    def return_name(self, name):
        return self.name 
    
    __return_name = return_name

    # _Child_return_name (_class_method)
```

**dataclass**:  a data class bundles up few named data items

```python

from dataclasses import dataclass

@dataclass

class Name:
   data_item: data_type

```

### Exception handiling

1. Syntax errors - also known as parsing errors.
2. Exceptions : erros detected during execution

ex: `ZeroDivisionError`, `NameError` and `TypeError`

**Built in exception:** 

- all exceptions are instances of the class BaseException

#### Handiling Exceptions

- try
- except (single, multiple exceptions, multiple except blocks, as)
- finally
- else


#### Raising Exceptions

```python
raise  ExceptionName [, args]
```

#### Custom Exceptions

- a class that inherits the Exception class

### File Handiling


1. Open

```
open(filename, [mode], [encoding=None])
```

- returns a file object
- default encoding is platform specific
- utf-8 prefered
- append b to mode for opening file in binary

**mode**

- `r` : reading (default)
- `w`: writing and truncating the file first
- `a`: appending
- `b`: binary mode
- `t`: text mode (default)
- `+`: open for updating (reading and writing)
- `x` :open for exclusive creation, throws error if the file already exists


1. `with` keyword

- closes the file immediaty and frees up the memory

3. read

```python
f.read()
f.readline()
```

4. write

```python
f.write()
```

5. position

```
f.tell()
```








