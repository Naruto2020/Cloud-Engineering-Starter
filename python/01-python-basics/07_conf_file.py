
===========================================================

Configuration Files and Relative Paths

============================================================

## `open()` and the Current Working Directory

`open()` uses the **current working directory (CWD)** to 
resolve relative paths.

If you run:

```bash
~/cloud-engineering-starter$ python3 python/01-python-basics/
python-modules/main.py
```

the current working directory is:

```text
/home/steve/cloud-engineering-starter
```

Therefore:

```python
with open("server.conf", "r") as file:
```

looks for:

```text
/home/steve/cloud-engineering-starter/server.conf
```

It does **not** automatically look in the directory 
containing `main.py`.

## Using a Relative Path

If `server.conf` is located in:

```text
python/01-python-basics/python-modules/server.conf
```

you can provide its path relative to the current working 
directory:

```python
with open("python/01-python-basics/python-modules/server.conf", "r") as file:
    for line in file:
        print(line)
```

## Relative vs Absolute Paths

A **relative path**:

```text
python/01-python-basics/python-modules/server.conf
```

is interpreted from the current working directory.

An **absolute path**:

```text
/home/steve/cloud-engineering-starter/python/01-python-basics/python-modules/server.conf
```

starts from the filesystem root `/`.

## Important Distinction

The path used to execute a Python script and the path used by
`open()` are separate concepts.

```bash
python3 python/01-python-basics/python-modules/main.py
```

tells Python **which script to execute**.

```python
open("python/01-python-basics/python-modules/server.conf")
```

tells Python **where to find the file**, relative to the 
current working directory.

The location of `main.py` does not automatically become the 
base directory for `open()`.

## Key Takeaway

Relative paths depend on **where the program is launched 
from**, not automatically on where the Python file is located.

This is particularly important in automation scripts that 
work with configuration files, logs, JSON files, 
certificates, `.env` files, and other external files.

