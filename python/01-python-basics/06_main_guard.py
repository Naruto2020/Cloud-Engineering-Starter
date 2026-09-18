
====================================================================

	Exercise 33 — __name__ == "__main__"

====================================================================


This is an important Python concept you'll encounter frequently in real 
projects.

Imagine you have this in monitoring.py:

print("Monitoring module loaded")

If main.py does:

from monitoring import check_cpu

that print() would execute just because the module was imported.

Python gives us a way to distinguish:

"This file is being imported"

from:

"This file is being executed directly."

We use:

if __name__ == "__main__":
    ...
Your task

At the bottom of monitoring.py, add:

if __name__ == "__main__":
    print("Monitoring module executed directly")

Then run:

python3 python/01-python-basics/python-modules/main.py

You should not see:

Monitoring module executed directly

Then run monitoring.py directly:

python3 python/01-python-basics/python-modules/monitoring.py

This time you should see:

Monitoring module executed directly

"Don't worry if __name__ looks strange right now. The exercise is mainly"
"to observe the difference. Then I'll explain exactly what Python is doing."

=======================================================================

	Exercise 34 — Turn the module into a reusable tool

=======================================================================


Now we'll make this more Cloud-oriented.

Instead of having check_server() return only CPU and memory, let's add disk monitoring too.

Modify check_server() so it expects:

server = {
    "name": "web-01",
    "cpu": 90,
    "memory": 65,
    "disk": 85
}

And returns:

web-01 -> CPU: WARNING, Memory: NORMAL, Disk: WARNING
Hint

Inside check_server() you'll need:

disk_status = check_disk(server["disk"])

Then include disk_status in the returned string.

Try to modify the function yourself rather than copying the complete
solution. This is the first step toward building a small reusable
Cloud monitoring module.

*** Go see "./python-modules"


