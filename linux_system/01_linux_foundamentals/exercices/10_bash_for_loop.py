
======================================================================

		1.9 Bash — for loops

======================================================================


Now we move from checking one thing to checking multiple things.

Imagine you want to check several services:


nginx
ssh
cron

Instead of writing:

systemctl is-active nginx
systemctl is-active ssh
systemctl is-active cron

we can use a loop.

Exercise

Create a variable containing these three service names:

nginx ssh cron

Then use a for loop to go through each service.

For each service, execute:

systemctl is-active <service>

and print something like:

nginx: inactive
ssh: active
cron: active


#!/bin/bash


services="nginx ssh cron"

for service in $services
do
    echo "$service: $(systemctl is-active $service)"
done


===================================================================

1.9 Bash — for loop + exit codes

Let's make the loop more useful.

Instead of only displaying:

nginx: inactive

we want the script to classify each service:

nginx: OK
ssh: OK
cron: FAILED
Exercise

Start from:

#!/bin/bash

services="nginx ssh cron"

for service in $services
do
    ...
done

For each service:

Run systemctl is-active "$service".

If its exit code is 0, print:

<service>: OK

Otherwise, print:

<service>: FAILED
Constraint

Use the concepts you've already learned:

for
$service
systemctl is-active
exit code
if / else

Try it yourself. I won't provide the completed solution first.



#!/bin/bash


services="nginx ssh cron"

for service in $services
do
    systemctl is-active "$service" && echo "$service: ok" || echo "$service: FAILED"
done


What happens on each iteration

For:

service=nginx

Bash effectively runs:

systemctl is-active nginx && echo "nginx: ok" || echo "nginx: FAILED"

Then the same logic is applied to ssh and cron.

You've now combined several concepts:

for loop
   ↓
variable expansion
   ↓
command execution
   ↓
exit code
   ↓
&& / ||

That's a genuine little service health-check script.


Next: a more robust loop

There's one limitation with our current && ... || ... pattern: the systemctl command itself prints:

active
inactive

before our OK/FAILED message.

So your output might look like:

inactive
nginx: FAILED
active
ssh: OK

For a real monitoring script, we'd probably want:

nginx: FAILED
ssh: OK
cron: OK
Exercise

Modify your loop so that only your OK / FAILED messages are displayed, 
without the active/inactive output from systemctl.

Hint: Think about what you learned earlier about redirecting command output.


systemctl is-active "$service" > /dev/null && echo "$service: OK" || echo "$service: FAILED"
