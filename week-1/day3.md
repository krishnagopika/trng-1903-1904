
# Lecture Plan


1. Class & Objects
2. Object Oriented Programming
3. Python modules



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

