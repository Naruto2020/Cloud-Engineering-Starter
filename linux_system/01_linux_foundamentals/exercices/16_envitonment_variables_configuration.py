
=======================================================================

	Next step — Environment variables and configuration

=======================================================================

We've now covered the main ideas of Bash error handling and debugging. 
Next, we'll learn how scripts use environment variables to receive 
configuration from outside the script.

For example:

#!/bin/bash

echo "Deploying to $ENVIRONMENT"

You can provide the environment when launching the script:

ENVIRONMENT=production ./deploy.sh

This is useful in DevOps because the same script can run in development,
staging, or production without changing its source code.


Your exercise

Suppose you run:

ENVIRONMENT=staging ./deploy.sh

and the script contain

echo "Deploying to $ENVIRONMENT"

What will it print, and why is using an environment variable useful when 
deploying to multiple environments?

==> It will print  "Deploying to staging". using an environment variable 
is useful when deploying to multiple environments because you can use the
same script for all of them without changing the source code.


For example:

ENVIRONMENT=development ./deploy.sh
ENVIRONMENT=staging ./deploy.sh
ENVIRONMENT=production ./deploy.sh

The script stays the same, but its configuration changes.


This is common in Cloud/DevOps workflows, where a deployment pipeline may
target development, staging, or production.

One important detail: in this command,
ENVIRONMENT=staging ./deploy.sh


ENVIRONMENT is set for the execution of ./deploy.sh. It doesn't 
permanently change your current shell's environment.


======================================================================

	Next concept — What if an environment variable is missing?



Consider this script:
#!/bin/bash

echo "Deploying to $ENVIRONMENT"


Now run it without setting the variable:
./deploy.sh


By default, if ENVIRONMENT is unset, Bash expands it to an empty string. 
The script will print:

Deploying to


That isn't ideal for a deployment script. We should validate required 
configuration before proceeding.

Your exercise

How would you modify the script so that it:
1. Checks whether ENVIRONMENT is empty or unset.
2. Prints Error: ENVIRONMENT is required if it is missing.
3. Exits with status 1 instead of continuing.


==> 
#!/bin/bash
set -e

ENVIRONMENT="$1"

if [ "$ENVIRONMENT" != "" ]; then
   echo "Deploying to $ENVIRONMENT"
else
   echo "ENVIRONMENT is required"
   exit 1
fi


=========================================================================


Next exercise — A more concise validation
Bash offers a shorter way to check whether a variable is empty:

if [ -z "$ENVIRONMENT" ]; then


Here, -z means the string has zero length.

Your turn: If ENVIRONMENT="production", is [ -z "$ENVIRONMENT" ] true 
or false? Explain why.

==> False , Because ENVIRONMENT variable is fill with "production"

=========================================================================

Next step — Your practical DevOps automation script
We've now covered input validation, redirection, pipes, error handling, 
debugging, and environment variables.

Let's bring these concepts together in a small deployment script.

Before we start, one important point: we should validate both that the 
environment is provided and that its value is allowed. An environment 
variable can be present but still contain an invalid value.

Exercise 1

Suppose the script accepts only staging or production.

You already know how to check whether a variable is empty using -z, and 
how to compare strings using =.

How would you check whether ENVIRONMENT is either staging or production?

You can answer with just the Bash condition for now. We'll build the full
script one step at a time.

#!/bin/bash

set -e
set -x

ENVIRONMENT="$1"

if [[ "$ENVIRONMENT" == "staging" || "$ENVIRONMENT" == "production" ]]; then
   echo "Continue to deploy on $ENVIRONMENT ENVIRONMENT"
else
   echo "Error: Environment must be staging or production"
   exit 1
fi

=========================================================================

	Next lesson — Building a practical DevOps automation script

=========================================================================

We're approaching the final stage of BLOC 1 — Linux & Bash, Step 1.10.

We'll combine the skills you've learned into a small service-health-check 
script that:


1- Validates the environment argument.

2- Checks whether a required service is running.

3- Logs the result.

4- Returns an appropriate exit status.

#!/bin/bash

set -e

ENVIRONMENT="$1"
service="nginx"
log_file="deployment.log"

# To reset log before script execution
: > "$log_file"


if [ -z "$ENVIRONMENT" ]; then
   echo "Error: ENVIRONMENT is required" >> "$log_file"
   exit 1
fi

if [[ "$ENVIRONMENT" == "staging" || "$ENVIRONMENT" == "production" ]]; then
   echo "Continue to deploy on $ENVIRONMENT ENVIRONMENT" >> "$log_file"
else
   echo "Error Environment must be staging or production." >> "$log_file"
   exit 1
fi

if systemctl is-active --quiet "$service" ; then
   echo "ENVIRONMENT: $ENVIRONMENT | Service: $service is running" >> "$log_file"
else
   echo "ENVIRONMENT: $ENVIRONMENT | Service: $service is not running" >> "$log_file"
   exit 1
fi


==============================================================================================

BLOC 1 — Linux: 1.10 Bash / Shell scripting is nearly complete. We just need a final short assessment before marking the entire Linux block complete.

One question to finish this practical exercise:

Why did your script return 1 even though systemctl is-active --quiet nginx returned 4?


==> because i implement it to exit with status 1 if something wrong


Exactly! Correct.

You explicitly defined your script's error-handling behavior:
else
    echo "ENVIRONMENT: $ENVIRONMENT | Service: $service is not running." >> "$log_file"
    exit 1
fi


systemctl returned 4, but your script handled that failure and returned 1 through exit 1.

This demonstrates an important DevOps principle: a script should return a predictable exit status to the process or pipeline that invokes it.
Bash assessment — final question

Before we close Linux, one last question:

What's the difference between these two commands?

command > output.log 2>&1


command 2>&1 > output.log

==> command > output.log 2>&1 ll send stdout and stderr in same file output.log
    command 2>&1 > output.log ll just send stdout in output.log 