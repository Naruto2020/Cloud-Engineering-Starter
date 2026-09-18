
===================================================================

	Exercise 30 — Mini Cloud Monitoring Module

===================================================================

Now we're going to combine what you've learned: functions + dictionaries + modules + imports.

monitoring.py

Create a function that analyzes one server:

def check_server(server: dict) -> str:
    cpu_status = check_cpu(server["cpu"])
    memory_status = check_memory(server["memory"])

    return (
        f"{server['name']} -> "
        f"CPU: {cpu_status}, "
        f"Memory: {memory_status}"
    )

Keep your existing check_cpu() and check_memory() functions in the same file.

main.py

Create this server:

server = {
    "name": "web-01",
    "cpu": 90,
    "memory": 65
}

Then import check_server:

from monitoring import check_server

And call it:

result = check_server(server)

print(result)
Expected output
web-01 -> CPU: WARNING, Memory: NORMAL
What we're practicing

The important part is the dependency inside the module:

main.py
   │
   │ imports
   ▼
monitoring.py
   │
   ├── check_cpu()
   ├── check_memory()
   └── check_server()
          │
          ├── calls check_cpu()
          └── calls check_memory()

Try it yourself first. Send me your code/output, and we'll correct it 
together.

***
***
Go see " python/01-python-basics/python-modules "


One important observation

Your main.py is now the entry point:

main.py
   │
   └── imports functions
          │
          ▼
     monitoring.py
          │
          ├── check_cpu()
          ├── check_memory()
          ├── check_disk()
          └── check_server()

This is a very useful pattern in Cloud/DevOps:

main.py → orchestrates what the program does
monitoring.py → contains reusable monitoring logic


====================================================================

	Exercise 31 — A module with constants

====================================================================

Now let's make the module more realistic.

In monitoring.py, we currently have limits such as:

CPU_LIMIT = 80

and:

limit: int = 80

Instead, let's centralize our limits at the top of the module:

CPU_LIMIT = 80
MEMORY_LIMIT = 80
DISK_LIMIT = 80

Then modify the functions so they use these constants by default:

def check_cpu(cpu: int, limit: int = CPU_LIMIT) -> str:
    ...
def check_memory(percentage: float, limit: int = MEMORY_LIMIT) -> str:
    ...
def check_disk(percentage: float, limit: int = DISK_LIMIT) -> str:
    ...

Don't change check_server() yet.

The goal is to understand that a module can contain not only functions, but also constants and other reusable data.

Try modifying monitoring.py and run your existing main.py.

*** Go see " python/01-python-basics/python-modules "


Perfect. ✅ Exercise 31 is correct.

Your output is unchanged, which is exactly what we expected:

CPU: WARNING
Memory: NORMAL
Disk: WARNING
web-01 -> CPU: WARNING, Memory: NORMAL

The important change is inside monitoring.py, where the limits are now centralized:

CPU_LIMIT = 80
MEMORY_LIMIT = 80
DISK_LIMIT = 80

and used by the functions:

def check_cpu(cpu: int, limit: int = CPU_LIMIT) -> str:

This is better organization because if tomorrow you want to change the CPU threshold from 80 to 85, you change it once:

CPU_LIMIT = 85

instead of searching through your code for every occurrence of 80.


=======================================================================

	Exercise 32 — Import a constant

=======================================================================

Now let's prove that constants can also be imported from a module.

In main.py, add:

from monitoring import CPU_LIMIT

Then add:

print(f"CPU limit: {CPU_LIMIT}%")

You should get something like:

CPU: WARNING
Memory: NORMAL
Disk: WARNING
web-01 -> CPU: WARNING, Memory: NORMAL
CPU limit: 80%
Important concept

Until now:

from monitoring import check_cpu

imports a function.

Now:

from monitoring import CPU_LIMIT

imports a constant.

Both are objects defined inside monitoring.py that main.py can reuse.

Try it and send me the output.

*** Go see " python/01-python-basics/python-modules "


Exactly. ✅ Exercise 32 is correct.

You've now seen that a Python module can expose different kinds of reusable things:

monitoring.py
│
├── CPU_LIMIT       ← constant
├── MEMORY_LIMIT    ← constant
├── DISK_LIMIT      ← constant
│
├── check_cpu()     ← function
├── check_memory()  ← function
├── check_disk()    ← function
└── check_server()  ← function

And main.py can import whichever ones it needs:

from monitoring import check_cpu, CPU_LIMIT
One important Cloud/DevOps takeaway

This separation is useful because configuration and logic can be organized separately:

main.py
   ↓
"Run the monitoring"

monitoring.py
   ↓
"How do we check things?"

You're getting into the pattern of reusable automation code, which is
exactly why we're learning modules here.
