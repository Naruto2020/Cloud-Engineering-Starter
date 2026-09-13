
====================================================================

Topic 6 — Modules & Imports 🐍☁️

====================================================================


Now we move to a new topic, not another function exercise.

Until now, we've mostly put everything in one Python file. In real Cloud/DevOps projects, you'll split your code into multiple files and import what you need.

6.1 What is a module?

A module is simply a Python file (.py) containing code that you can use from another Python file.

For example:

cloud-project/
├── main.py
└── monitoring.py

monitoring.py could contain:

def check_cpu(cpu: int, limit: int = 80) -> str:
    if cpu > limit:
        return "WARNING"
    return "NORMAL"

Then main.py can import it:

from monitoring import check_cpu

result = check_cpu(90)

print(result)

So conceptually:

monitoring.py
     │
     │  import
     ▼
  main.py

This is extremely common in Python automation.


=======================================================================


Exercise 24 — Your first module

=======================================================================


Let's do it hands-on.

Step 1

Create a directory:

mkdir python-modules
cd python-modules

Step 2

Create two files:

touch main.py monitoring.py

You should have:

python-modules/
├── main.py
└── monitoring.py

Step 3

Inside monitoring.py, create this function:

CPU_LIMIT = 80

def check_cpu(cpu: int, limit: int = CPU_LIMIT) -> str:
    return (
        "WARNING"
        if cpu > limit
        else "NORMAL"
    )


Step 4

Inside main.py, import the function and use it:

from monitoring import check_cpu

result = check_cpu(90)

print(result)
Your task

Do the exercise yourself and send me:

Your monitoring.py
Your main.py
The output you get

Then we'll see exactly what import and from ... import ... are doing, 
before moving to the next exercise.


Perfect. ✅ Your module works correctly.

You ran:

python3 python/01-python-basics/python-modules/main.py

and got:

WARNING

That confirms that main.py successfully imported check_cpu() from monitoring.py and executed it.

What happened

Your structure is essentially:

python-modules/
├── main.py
└── monitoring.py

monitoring.py contains:

def check_cpu(...):
    ...

And main.py does:

from monitoring import check_cpu

Python then looks for monitoring.py, loads the function, and makes check_cpu() available inside main.py.

So this:

result = check_cpu(90)

is calling a function that isn't defined in main.py itself.

That's the main idea of modules.

=============================================================================================

Exercise 25 — Import the whole module

Now let's see the difference between:

from monitoring import check_cpu

and:

import monitoring

Change main.py to:

import monitoring

result = monitoring.check_cpu(90)

print(result)

Run it again.

Question

Before you run it, think about this:

Why do we now write:

monitoring.check_cpu(90)

instead of:

check_cpu(90)

Give me your explanation after trying it.

because we import the whole module and check_cpu function it is part of it 

Exactly. ✅

Your explanation is correct:

We import the whole monitoring module, and check_cpu is a function inside that module.

So Python uses:

monitoring.check_cpu(90)

Think of the . as “inside”:

monitoring
    └── check_cpu()

Whereas with:

from monitoring import check_cpu

we import the function directly, so we can write:

check_cpu(90)
The difference
import monitoring
monitoring.check_cpu(90)

vs.

from monitoring import check_cpu
check_cpu(90)

Both work. The first makes it more explicit where the function comes
from, which can be useful when modules contain many functions.


=======================================================================

Exercise 27 — Import with an alias (as)

=======================================================================

Sometimes a module has a long name, and we don't want to write the
full name every time.

For example:

import monitoring as mon

Now instead of:

monitoring.check_cpu(90)
monitoring.check_memory(75)

we can write:

mon.check_cpu(90)
mon.check_memory(75)
Your task

Modify main.py:

import monitoring as mon

cpu_status = mon.check_cpu(90)
memory_status = mon.check_memory(75)

print(f"CPU: {cpu_status}")
print(f"Memory: {memory_status}")

Run it and check that you get:

CPU: WARNING
Memory: NORMAL

The important thing to understand here is:

import monitoring as mon
        │            │
        │            └── local alias
        └── real module name

So mon is simply another name we give to the monitoring module.
