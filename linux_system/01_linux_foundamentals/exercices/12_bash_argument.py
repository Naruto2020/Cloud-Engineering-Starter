
=========================================================================

		One more concept before $@

=========================================================================


There is also:
$#

$# tells you how many arguments were passed.
For:
bash script.sh nginx production 3

you get:
$1 → nginx
$2 → production
$3 → 3
$# → 3

This is extremely useful for validating scripts.
For example, you can check:
"Did the user provide the required number of arguments?"

But we'll learn that properly next.
No exercise yet. First, make sure the distinction is clear:
- $1, $2, $3 → what arguments were passed
- $# → how many arguments were passed
- $@ → all arguments passed


Great. Let's now understand $#, before doing another exercise.

$# — Counting Arguments

We saw that:

$1 → first argument
$2 → second argument
$3 → third argument

But sometimes your script doesn't know whether the user provided enough 
arguments.
That's where:

$#

comes in.

It tells you how many positional arguments were passed to the script.
Example
If you run:
bash script.sh nginx production 3

then:
$1 → nginx
$2 → production
$3 → 3
$# → 3

If you run:
bash script.sh nginx

then:
$1 → nginx
$# → 1

If you run:
bash script.sh

then:
$# → 0


Why is this useful?
Imagine your deployment script requires three arguments:
./deploy.sh nginx production 3

You don't want someone accidentally doing:
./deploy.sh nginx

and having the script continue with missing information.
You can therefore check:
if [ "$#" -ne 3 ]; then
    echo "Expected 3 arguments"
    exit 1
fi

The important part here is:
"$#"

= number of arguments.
And:
-ne

means not equal.
So:
[ "$#" -ne 3 ]

means:
"Is the number of arguments different from 3?"


DevOps example
A script might require:
environment
service
version

So:
./deploy.sh production api v2.4

has exactly 3 arguments.
The script can verify that before doing anything dangerous.
This is an important habit in automation:
Validate inputs before executing an operation.


=======================================================================


Now your exercise
Create a small script that expects exactly 3 arguments.
If the user gives exactly 3:
Correct number of arguments

Otherwise:
Expected 3 arguments

Use:
- $#
- if
- -ne
Don't worry about $@ yet. We'll do that after you understand argument 
validation.

#!/bin/bash

if [ $# -ne 3 ]; then
   echo "expected 3 arguments"
else
   echo "Correct number of arguments"
fi

3. Test it

If your file is script.sh, try these commands:

Command	Expected output

bash script.sh nginx production 3	Correct number of arguments
bash script.sh nginx	Expected 3 arguments
bash script.sh a b c d	Expected 3 arguments
DevOps takeaway: Validate your inputs before running a deployment or 
changing a server. Missing or unexpected arguments can cause automation 
to behave incorrectly.


Bash: $@ — Working with all arguments
So far, you've learned:
- $1, $2, $3: access arguments by position.
- $#: count how many arguments were passed.
Now, let's understand $@.

1. Why do we need $@?
Imagine you want your script to check several services, but you don't 
know in advance how many services the user will provide.
You might run:
bash script.sh nginx ssh cron


Or:
bash script.sh nginx ssh


You don't want to write separate code for each number of services. You 
want your script to process every argument automatically.
That's what "$@" helps you do.

2. How it works
Suppose you run:
bash script.sh nginx ssh cron


Inside your script:
Variable	Value
$1	nginx
$2	ssh
$3	cron
$#	3

"$@"	All three arguments, preserved separately
The last detail matters: "$@" preserves each argument as a separate 
item, including arguments containing spaces.

3. Combine it with a for loop
You already know how to write a for loop. You previously used one to 
iterate over a fixed list:
services="nginx ssh cron"

for service in $services
do
    echo "$service"
done


With "$@", the user supplies the list when launching the script:
for service in "$@"
do
    echo "Checking $service"
done


If you execute:
bash script.sh nginx ssh cron


the output will be:
Checking nginx
Checking ssh
Checking cron


This is useful for DevOps scripts that need to operate on a variable 
number of services, files, or other resources.


Your turn: one small exercise
Create a script that uses "$@" and a for loop to print every argument in this format:
Argument: nginx
Argument: ssh
Argument: cron


Test it with:
bash script.sh nginx ssh cron

#!/bin/bash

for service in "$@"
do
   echo "Argument: $service"
done



