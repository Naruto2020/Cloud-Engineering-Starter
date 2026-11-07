
=========================================================================

		Bash error handling and debugging

=========================================================================


Consider this script:

#!/bin/bash

mkdir /tmp/deployment
echo "Deployment directory created"

We want to prevent that misleading message.


Question: Do you remember which operator we've already studied that 
executes the second command only if the first command succeeds?

What would you change in the deployment script?

mkdir /tmp/deployement && echo "Deployment directory created"
Let's understand the behavior

Situation	 mkdir exit status	What happens?

Directory doesn't exist	  0	Prints Deployment directory created

Directory already exists Non-zero	Doesn't print the success
                                                                  message
Permission denied 	 Non-zero	Doesn't print the success message

One small detail: I used /tmp/deployment in the exercise, whereas your 
answer says /tmp/deployement. The spelling doesn't affect the Bash logic,
but the path must match the directory you intend to create.


========================================================================

		         The set -e option

========================================================================


So far, we've handled failures with &&. Bash also has an option that 
tells a script to exit when a command fails in many situations:

#!/bin/bash
set -e

mkdir /tmp/deployment
echo "Deployment directory created"
echo "Continuing deployment..."

If mkdir fails, set -e will normally stop the script before the following
messages execute.

Why is this useful? In deployment automation, you don't want later steps 
to run when an essential earlier step has failed.


However, set -e has exceptions and can behave unexpectedly in certain 
conditions, such as commands used in if tests or parts of && and || 
lists. We'll learn those limitations rather than treating it as a 
perfect error-handling mechanism.


Your exercise
Suppose /tmp/deployment already exists and you run the script above.

Which messages will be printed, and why?


==> No message will be printed , Because set -e ll stop the program 
after command fail 


You're close! Your understanding of set -e is correct, but there's one important detail to remember. ✅

The actual behavior is:
1. set -e enables automatic termination when a command fails in a situation where the option applies.
2. mkdir /tmp/deployment fails because the directory already exists.
3. Bash stops executing the script.
4. Neither echo command runs.
Output: No messages are printed by the script.

One nuance: mkdir itself may print an error message to standard error, 
such as:

mkdir: cannot create directory '/tmp/deployment': File exists


So the script prints no success messages, but you may still see the 
error from mkdir.

========================================================================

	Next concept — Debugging Bash scripts with set -x

========================================================================


We've learned how to stop a script when a command fails. Now let's 
learn how to understand what a script is actually executing.

Bash provides: 


set -x


The lines beginning with + show the commands Bash executes. The final 
line is the normal output of echo.

Your exercise
Consider this script:

#!/bin/bash
set -x

name="Steve"
echo "Hello $name"


Question: What is the difference between the lines printed by set -x and 
the line printed by echo?

Explain it in your own words, and we'll continue from there.


==> set -x will print line biginning with + while echo no. 
Because set -x print variable and echo print result


Correct! ✅ You've understood the main difference.

Let's refine your explanation slightly.

- set -x prints a trace of the commands Bash executes, after expanding 
variables. The trace lines usually begin with +.

- echo prints the actual message requested by the script.


Why this matters in DevOps: When a deployment script behaves unexpectedly
tracing helps you see which commands run and what values variables 
contain. Be careful with secrets, though: tracing can expose passwords, 
tokens, or other sensitive values in logs.

=========================================================================

	Next exercise — Combining error handling and debugging




Let's put your knowledge into a practical scenario.


#!/bin/bash
set -e
set -x

environment="$1"

echo "Starting deployment to $environment"

mkdir /tmp/deployment
echo "Deployment directory ready"


Suppose you run:

./deploy.sh production



and /tmp/deployment already exists.

Question: What happens, and which messages or trace lines do you expect 
to see?

==> The program ll exit at mkdir /tmp/deployment. we expect mkdir error 
message, first echo message : "Starting deployment to $environment" and 
+environment="production", + echo 'Starting deployment to production' ,
+ mkdir /tmp/deployment


