
====================================================================

		1.9 — Bash / Shell Scripting

====================================================================

It is a shell: a program that lets you interact with the Linux operating 
system.

For example, when you type:

ls

the flow is roughly:

You
 ↓
Bash
 ↓
Linux command
 ↓
Kernel
 ↓
Filesystem

Bash can also execute scripts: files containing a sequence of commands.

For example:

#!/bin/bash

echo "Hello Steve"
echo "Checking server..."
uptime

Save it as:

check_server.sh

Then execute it:

bash check_server.sh

2. Why Bash matters for Cloud/DevOps

Imagine you need to check 20 servers.

Doing this manually:

systemctl status nginx
free -h
df -h
uptime

on every server would be tedious.

A Bash script can automate it:

Server
  ↓
Bash script
  ├── Check CPU
  ├── Check memory
  ├── Check disk
  ├── Check services
  └── Report problems

That's why Bash remains very useful even when you also know Python, Terraform, Docker, etc.


3. Your first concept: variables

A Bash variable stores a value.

name="Steve"

Then:

echo "$name"

produces:

Steve


Important Bash syntax

You do not put spaces around =:

name="Steve"     # ✅

Not:

name = "Steve"   # ❌

To use the variable:

$name

or preferably:

"$name"



4. A Cloud-style example

server="production"
status="running"

echo "Server: $server"
echo "Status: $status"

Output:

Server: production
Status: running

You can also store command output:

hostname=$(hostname)

Then:

echo "Server name: $hostname"

Here:

$(hostname)

means:

Execute the hostname command and put its output into the variable.


There are actually two different ways to run a Bash script.

Option 1 — Execute it through Bash

If the file is not executable:

bash check_server.sh

This works because you're explicitly telling Bash to interpret the file.

Option 2 — Execute the script directly

For this:

./check_server.sh

the file must be executable.

So we need:

chmod +x check_server.sh

Then:

./check_server.sh

The complete workflow is:

touch check_server.sh
chmod +x check_server.sh
./check_server.sh

And because our script contains:

#!/bin/bash

the shebang tells Linux which interpreter should execute the script when we use:

./check_server.sh

So:

check_server.sh
      ↓
chmod +x
      ↓
./check_server.sh
      ↓
#!/bin/bash
      ↓
Bash executes the script
One useful distinction
bash check_server.sh

→ executable permission not required

./check_server.sh

→ executable permission required
