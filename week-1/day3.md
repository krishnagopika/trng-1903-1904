
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
2. Exceptions : errors detected during execution

ex: `ZeroDivisionError`, `NameError` and `TypeError`

**Built in exception:** 

- all exceptions are instances of the class BaseException

#### Handiling Exceptions

- try
- except (single, multiple exceptions, multiple except blocks, as)
- finally
- else

<i><b>Note</b>

1. if an error occurs in try block the rest of the code in try block is skipped.
2. a try block should have a corresponding except block or finally block.
3. if try block contains return, break and continue statements, the finally block is executed just prior to those statements
4. if finally block contains  return statement then it will not re-raise the exceptions
</i>



#### Raising Exceptions

```python
raise  ExceptionName [, args]
```

#### Custom Exceptions

- a class that inherits the Exception class

```python
class ClassName(Exception):
    # statements

```