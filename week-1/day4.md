Lecture Plan

1. File handiling
2. Python Modules


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

5. tell: current postition represented by no of bytes.

```
f.tell()
```

6. seek - to move the position to specified offset

```python
f.seek(offset, whence)
```

whence:

`0`: begining of the file
`1`: current file position
`2`: end of the file


#### deleting the files


```
import os

os.remove("path to file")
```

**References:**

[file handling](https://docs.python.org/3/tutorial/inputoutput.html)


---

### Python Modules


1. Math

2. JSON: JavaScript Object Notation

```json
{
    'name' : 'Krishna',
    'email': 'sample@email.com'
}

```

1. load : file to dict
2. dump : dict to file
3. loads :converts json str to dict
4. dumps :converts dict to json str


[json](https://docs.python.org/3/tutorial/inputoutput.html#saving-structured-data-with-json)


1. re - Regexp

**match:** checks for at the begining of the string
**search:** checkes anywhere in the string
**fullmatch** checkes for the entire string
**findall** matches all the occurances

- return a match if it exists or they return None


`.` - match a character

`^` - it matches the start of string 

`$` - the end of the string

`*` - 0 or more repetitions

`+` - matches one or more repetitions

`?` - 0 or 1 repetitions


[re-Regex](https://docs.python.org/3/library/re.html#)

**Unicode string patterns**


`\d` - digits `[0-9]`

`\D` - non-digits `[^0-9]`

`\s` - white spaces `[\n\t\r\f\v]`

`\S` - non white space `[^\n\t\r\f\v]`

`\w` - alphanumeric `[a-zA-Z0-9]`

`\W` - non alpha numeric `[^a-zA-Z0-9]`


[Regex](https://docs.python.org/3/howto/regex.html)


`pip` - python package index


**virtual env** - used to isolate the package instalations for a specific project

installing virtualenv package

```bash
pip install virtualenv
```

creating the venv

```
python -m venv /path/to/folder [.venv]
```
activate venv

```
.venv\Scripts\activate
```


deactivate venv


```
deactivate
```

`requirements.txt` - file to list all the packages  needed by your application in order to run correctly.


list the packages

```bash
pip list
```

```bash
pip freeze
```

to install the packages

```bash
pip install -r requirements.txt
```


1. Logging


when it's used

DEBUG - 10

- detailed info for diagnosing the problems

INFO - 20

- program is working as expected


WARNING - 30

- indication that something unexpected happened, or indicatin that some problem might occur if not corrected. application still works

ERROR - 40

- a serious problem, the application is not able to perform some functionality


CRITICAL - 50

- a serious error, indicats that the program failed.



[logging](https://docs.python.org/3/library/logging.html#)

1. unittest


- class should inherit the unnittest.TestCase

methods

- `assertEquals`
- `assertNotEquals`
- `assertTrue`
- `assertFalse`


[unittest](https://docs.python.org/3/library/unittest.html)


7. `pylint` : static code analyser - it analyses the code withoit runing it. It checks for code smells, coding standards and errors.

```
pip install pylint
```

[pylint](https://pypi.org/project/pylint/)


































