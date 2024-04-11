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


