# Lecture Plan


1. Python Basics

2. Python Data Types

3. Python Flow-Control Statements

4. Python Functions & Arrays
---





### Python Basics

- Python is high level, interpeted and object oriented programming language.


#### Data Types


1. Numeric

- int
- float
- complex
 
2. Sequential

- list : ordered collection, mutable.

```python
my_list = [1,"hello",3.4]
```
- tuple: ordered collection and immutable

```python
my_tuple = (1,"hello",3)
```
- range

```python
range(start,end)
```

3. boolean : True, False

4. Mapping

- dictionary: used to store asscoaited data (key:value pairs ).


```python
my_dict={"name":"Krishna","role":"trainer"}
my_dict.keys()
my_dict.values()
my_dict.items()
``` 

5. str
6. set : unordered and mutable

```python
my_set = {1,3,5}
```
7. binary

```python
b = bytes([1,4,9])
ba = bytearray([1,4,9])
```
8. None Type


#### Operators


- Arthematic : `+ - * / % // **`
- Logical:  `and` `or` `not`
- Comparison: `==`, `>`, `<`, `>=`, `<=` `!=`
- Assignmet: `=`, `+=`, `-=`, `*=`, `/=` `//=`, `%=`,
- Membership : `in` and `not in`
- Identity: `is` and `is not`
- Bitwise: `&`, `|`, `^`, `~`, `<<` and `>>`
- Terninary : x if `condition` else y


**Datetime**


```python
from datetime import date, time, datetime

date(2024, 4, 9)

time(9,13,54)

datetime(2024, 4, 9, 9, 13, 54)
```

#### namespaces

mapping names to objects.


1. Built in

```python
dir(__builtins__)

```
2. global
3. local
4. enclosing


### Flow control statements


1. if - else
2. match case
3. for
4. while

#### Functions, Lambda and Arrays


Functions: resusable blocks of code.

```python
def function_name( parameters: data_type) -> return type:
    # statements


# function call
function_name(arguments)

```

Lambda: anyonymous func


```python

result = lambda variable: expression
```


Arrays: wrapper around the C arrays. collection of homogeneous elements

```python

import array

array.array(typecode, [i,j...])
```

| Type Code | C Type                | Python Type        | Minimum Size (bytes) | 
|-----------|-----------------------|--------------------|----------------------|
| 'b'       | signed char           | int                | 1                    |
| 'B'       | unsigned char         | int                | 1                    |
| 'u'       | wchar_t               | Unicode character  | 2                    |
| 'h'       | signed short          | int                | 2                    |
| 'H'       | unsigned short        | int                | 2                    |
| 'i'       | signed int            | int                | 2                    |
| 'I'       | unsigned int          | int                | 2                    |
| 'l'       | signed long           | int                | 4                    |
| 'L'       | unsigned long         | int                | 4                    |
| 'q'       | signed long long      | int                | 8                    |
| 'Q'       | unsigned long long    | int                | 8                    |
| 'f'       | float                 | float              | 4                    |
| 'd'       | double                | float              | 8                    |




**iterators**

1. iter()
2. next()

```python
my_list = [1,4,5,6]

my_iterator = iter(my_list)

while True:
    try:
        i = next(my_iterator)
        print(i)
    except:
        print("end of list")
        break

for j in range(len(my_list)):
    i = next(my_iterator)
    print(i)
```