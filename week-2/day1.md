# Lecture Plan

1. Linux:
     - file system
     - user management
     - file permissions
     - package management
     - piping
     - scripting

---


- is an open source OS
- Ubuntu, Red-Hat, Amazon Linux -2.


**Shell**

- Environment in which one works. Interface with OS to execute commands
- Bash Shell (Bourne again) `bash`, C-Shell `csh`, Korn Shell `ksh` and Z Shell `zsh`.


```bash
# list all distors available for installation
wsl -l -o

wsl --install -d [Distro-name] 
```

**Kernel & User Spaces**

1. **Kernel** : networking and scheduling, running,  managing processes.
2. **User Spaces:** interact with kernel with system calls.
3. Process: 
   - user process : terminal input and output
   - deamon process : networking
   - kernel threads : not associates with the terminal
 - PID, PPID

### File Management



1. `mkdir` : create dir
2. `rmdir` : del empty dir
3. `rm` : del file
4. `touch` : create file
5. `cp` : copy
6. `mv` : move id dir exists or renames the file


#### File hierarchy


- `bin` : binaries and executables. can be accessed by all users in the system. link to `usr/bin`
- `sbin` :can be accssed by the root user. link `usr/sbin`
- `usr` - unix system resources
- `boot` - all the files that start and initialse the kernel are located here.
- `dev` - device files
- `etc` (extended text config) - config files
- `home` - noraml  user's home directory
- `root` - root user dir
- `var` - variable dir, cache, logs
- `lib` & `lib64` - application dir
- `tmp` - temp space


#### User & Group Management


- `user + 2 x tab` : list out the commands
- `group + 2 x tab` : list out the commands
- ` usermod -aG group1, group2` : `a` - appending
- ` usermod -a group1` : `a` - modifing the group
- `su - username` : swicth user
- `su -` : root user


`chmod` : modify file permissions
`chown` : change owner for a file
`chgrp` : change owning group for a file

```bash
chgrp/own user/group  file
```


#### file permissions


10 : 1 is type of file

3 - user
3 - group
3 - other

`r` - read 
`w` - write 
`x` - exec


**Special permissions**


1. SUID (u+s)
2. SGID (g+s)
3. sticky (o+t)


#### Pipe & Filter

**pipe `|`** : output of one command is passed to the another command. 

```bash
cmd1 | cmd2 | cmd3
```

ex:

counting all the files in a dir

```
ls | wc -l
```

checking user permissions and returning the count

```
ls -lR | grep dwex | wc -l
```

Checking if an NICs have an ip starting with a pattern
```
ifconfig | grep 172
```

**filter**

- `grep  [options] pattern` : global regex print
- `sort`
- `head [-n] [number]`
- `tail [-n] [number]`

#### Package Management


**package manager**

- obatain, install, manage and remove the packages.

**ex:**

- `apt` (advanced packaging tool) : Debian distros
- `rpm` (redhat  package management) : Fedora, CentOS. ex: package-name.rpm
- yum (Yellow dog update modified) 
- dnf (Dandified yum)
- pacman (Package Manager) : Arch Linux


```bash

# to search for a package
yum search package-name


# to install packages
yum install package-name


# to delete the packages
yum remove package-name
yum erase package-name
```
#### Scripting


**Script:** a program that contains a series of commands
- anything that is typed in cmd can be executed in a script.
- script is executed by interpretor
- usefull to automate the tasks

**Variables**

```bash
VARIABLE_NAME="Value"

echo "$VARIABLE_NAME

echo "${VARIABLE_NAME}

VARIABLE_NAME=`command`
VARIABLE_NAME=$(command)
```

**Operators**

1. Arithmatic
2. logical
3. boolean
4. bitwise
5. test


1. Arithmetic

- +
- -
- *
- /
- %

2. comparision operttors

- `-eq`
- `ne`
- `-gt`
- `ge`
- `lt`
- `le`

3. logical operators

- `&&`
- `||`
- `!`

4. String

- `=` or `==`
- `!=`
- `-z`: checks if string is empty
- `-n`: checks if string is not empty
- `>`: greater than in ASCII order
- `<`: less than in ASCII order


5. Assignment

- `=`
- `+=`
- `-=`
- `*=`
- `/=`
