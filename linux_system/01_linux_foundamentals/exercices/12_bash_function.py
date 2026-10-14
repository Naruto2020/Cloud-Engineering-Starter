
========================================================================

			Bash functions

========================================================================

We're still in BLOC 1 — Linux → 1.10 Bash / Shell scripting.
1. What problem does a function solve?
Imagine your script needs to check a service several times. Each time, 
you might write:

systemctl is-active nginx


Now imagine you want to perform several operations every time you check 
a service:

- Check its status.
- Print a message.
- Handle errors.

Copying those commands everywhere makes your script longer and harder to 
maintain.

A function lets you group commands under a name and reuse them whenever 
you need them.

2. How do you define a function?
In Bash, you can write:
check_service() {
    echo "Checking service"
}


Let's break it down:
Syntax	Meaning
check_service	The function's name
()	Declares a function
{ ... }	Contains the commands the function executes
Defining the function does not execute its commands. It makes the 
function available for later use.


3. How do you call a function?
After defining it, write its name:
check_service


Complete example:
#!/bin/bash

check_service() {
    echo "Checking service"
}

check_service
check_service


Output:
Checking service
Checking service


We defined the commands once but called the function twice.

4. Why is this useful in DevOps?
You can create reusable functions for common tasks such as:
- Checking whether a service is running.
- Logging messages.
- Validating script arguments.
- Checking whether a required command is installed.
- Handling errors consistently.
As your automation scripts grow, functions help you keep the code 
organized.



Your exercise
Create a script with a function named check_server that prints:
Checking server health


Then call the function twice.
Start with this structure and fill in the missing parts:
#!/bin/bash

check_server() {
    # Your command here
}

# Call the function twice


Send me your script, and I'll review it before we move on to passing 
arguments to functions.


#!/bin/bash

check_server() {
   echo "Checking server health"
}

check_server
check_server


Next concept: Functions with arguments
You already learned how script arguments work with $1 and $2. Functions 
can also receive arguments, using the same positional-parameter syntax.
For example:
check_service() {
    echo "Checking service: $1"
}


Calling:
check_service nginx


prints:
Checking service: nginx


Here, $1 refers to the first argument passed to the function, not 
necessarily the first argument passed to the script.
That's an important distinction in Bash.


Bash functions with arguments
Let's build on what you just learned.
1. Why pass arguments to a function?
Your current function always prints the same message:
check_server() {
    echo "Checking server health"
}


What if you want to check different services, such as nginx, ssh, or cron?
You could create three functions, but that would repeat code unnecessarily.
Instead, you can pass a value to a function.
2. How it works
check_service() {
    echo "Checking service: $1"
}


When you call:
check_service nginx


Bash assigns nginx to $1 inside the function.
The output is:
Checking service: nginx


If you call:
check_service ssh


the output becomes:
Checking service: ssh


Same function, different argument.
3. Functions have their own positional arguments
Consider this script:
#!/bin/bash

check_service() {
    echo "Function argument: $1"
}

check_service nginx
check_service ssh


Output:
Function argument: nginx
Function argument: ssh


Each time you call the function, $1 refers to that function call's first 
argument.
This is different from script arguments: inside a function, $1 refers to 
the function's argument, temporarily replacing the script's positional 
parameters in that context.


Your exercise

Modify your check_server function so that it accepts a server name.
When you call:
check_server production
check_server staging


the output should be:
Checking server: production
Checking server: staging

check_server() {
   echo "Checking server: $1"
}

check_server production
check_server staging



What you've learned

- check_server() defines the function.
- $1 receives the first argument passed to that function.
- check_server production calls the function with production.
- You reuse the same function without duplicating its logic.
You can also accept multiple arguments:

check_server() {
    echo "Server: $1"
    echo "Environment: $2"
}

check_server nginx production


Here, $1 is nginx and $2 is production.
Next concept: function return values
In Bash, a function can return an exit status to indicate whether an 
operation succeeded or failed. This is particularly useful when 
automating deployments or checking services.
There is an important distinction between:
- Printing a value with echo.
- Returning an exit status with return.


Bash functions: return vs echo
We're still in BLOC 1 — Linux → 1.10 Bash / Shell scripting.
Let's understand a distinction that's important for DevOps automation.

1. echo displays information
Consider this function:
check_server() {
    echo "Server is running"
}

check_server


Output:
Server is running


echo prints text to standard output (stdout). It's useful for messages intended for a user or for information another command can capture.
For example:
result=$(check_server)


Here, result receives the text printed by echo.

2. return communicates success or failure
Now consider:
check_server() {
    return 0
}


In Bash, return sets the function's exit status.
- return 0 means success.
- return 1 means failure (or, more generally, a non-zero status means an unsuccessful result).
You can inspect that status using $? immediately after calling the function:
check_server
echo "$?"


Output:
0


This is useful when a script needs to decide whether to continue or stop.

3. Why does this matter in DevOps?
Imagine a deployment script that checks whether a service is healthy 
before deploying an application.
Conceptually:
Check service health
        |
        v
   Is it healthy?
     /       \
   Yes        No
    |          |
 Deploy     Stop deployment


The function can return 0 when the service is healthy and a non-zero 
status when it isn't. The calling script can then make a decision.

4. Important distinction
Feature	echo	return
Purpose	Prints text	Sets exit status
Example	echo "OK"	return 0
Typical use	Messages and output data	Success/failure checks
One detail: Bash functions return an exit status, not an arbitrary text 
value. If you want a function to provide text, you typically print it and
capture it with $(...).

Your turn: a small prediction
Consider this function:

check_server() {
    echo "Server checked"
    return 1
}

check_server
echo "$?"


What do you think the output will be, and why?

Server checked
1
