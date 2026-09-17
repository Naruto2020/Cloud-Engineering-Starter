
========================================================================

🎯 First exercise

=======================================================================


Don't worry about making it complicated.

Create these variables:

server_name
environment

Set them to:

server_name = your machine hostname
environment = development

Then print:

Server: <hostname>
Environment: development

You can use:

hostname

to get your hostname.

Your task

Write the Bash commands you would use.

==> I ll use : 

#!/bin/bash -> shebang

server_name=$(hostname)
environment="development"

echo "Server: $server_name"
echo "Environment: $environment"


Then create a third variable:

status

Set it to the result of:

systemctl is-active nginx

Finally, print:

Server: <hostname>
Environment: development
Nginx: <status>

status=$(systemctl is-active nginx)

echo "Server: $server_name"
echo "Environment: $environment"
echo "Nginx: $status"


1.9 Bash — Conditions (if)

Now we'll make the script take a decision.

Suppose:

status=$(systemctl is-active nginx)

We want the script to say:

if Nginx is active → "Nginx is running"
otherwise → "Nginx is NOT running"
Your exercise

Complete this script:

#!/bin/bash

status=$(systemctl is-active nginx)

if [ ... ]; then
    echo "Nginx is running"
else
    echo "Nginx is NOT running"
fi
...
...

Your complete logic then becomes:

if [ "$status" = "active" ]; then
    echo "Nginx is running"
else
    echo "Nginx is Not running"
fi


" Important Bash pattern "

Remember this structure:

if [ condition ]; then
    ...
else
    ...
fi

And spaces matter around the [ expression.
