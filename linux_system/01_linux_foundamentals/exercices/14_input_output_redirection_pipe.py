
======================================================================

		Input/output redirection and pipes

======================================================================

practice: validate inputs before performing operations on infrastructure.
It helps prevent accidental deployments to unintended environments.

Next concept — Input/output redirection and pipes
We are moving to the next planned Bash topic.

When you run a command, it can produce two kinds of output:
- Standard output (stdout, file descriptor 1) — normal results.
- Standard error (stderr, file descriptor 2) — error messages.


Bash lets you redirect these streams to files or discard them. This is 
useful when writing automation scripts because you may want to save logs,
suppress expected output, or capture errors separately.


For example:
echo "Deployment started" > deployment.log


The > operator sends standard output to deployment.log, creating the file
if necessary or replacing its existing contents.

Compare these operators:

| Operator | Purpose |
|---|---|
| > | Redirect output; overwrite the destination |
| >> | Redirect output; append to the destination |
| 2> | Redirect standard error |
| | | Send one command's standard output to another command |


Exercise 1

Consider this command:
echo "Deployment started" >> deployment.log


What is the difference between using >> here and using > instead?

Answer in your own words, and we'll build on that.

==> > ll create file if not exist or ll overwrite its existing contents.

    >> ll add after existing contents


Example
Suppose deployment.log already contains:
Deployment started


If you run:
echo "Deployment completed" >> deployment.log


The file will contain:
Deployment started
Deployment completed


But if you use > instead, the file will contain only:
Deployment completed


DevOps application: When writing deployment logs, >> is useful because 
you usually want to preserve previous log entries rather than erase them.


======================================================================


Next exercise — Standard output vs. standard error
Bash has two separate output streams:
- stdout (file descriptor 1): normal output.
- stderr (file descriptor 2): error messages.
Consider this command:


ls /home/steve /directory_that_does_not_exist


Assume /home/steve exists and /directory_that_does_not_exist does not.

Question: Which output will go to stdout, and which will go to stderr?

==> stdout ==> /home/steve  and stderr ==> /directory_that_does_not_exist


========================================================================

Next exercise — Redirect errors to a file

Now suppose you want to save the error message to errors.log, while still
displaying the normal directory listing in your terminal.

Your task: Complete this command by adding the correct redirection 
operator and filename:

ls /home/steve /directory_that_does_not_exist _____ errors.log


Which operator should replace the blank, and why?

==> I ll use 2> .Because it is the operator to redirect standard error 


The complete command is:
ls /home/steve /directory_that_does_not_exist 2> errors.log


What happens when you run it?
- The contents of /home/steve are displayed in your terminal because stdout is unchanged.
- The error about /directory_that_does_not_exist is written to errors.log.
- If errors.log already exists, its contents are overwritten.


======================================================================


Next concept — Redirect both stdout and stderr

In DevOps automation, you sometimes want to capture both normal output 
and error messages in one log file.

Bash provides this syntax:
command > output.log 2>&1

Here's how it works:
1. > output.log redirects standard output (file descriptor 1) to the file.
2. 2>&1 redirects standard error (file descriptor 2) to wherever standard
output is currently going.
The order matters. In this example, both streams end up in output.log.


Your exercise
You want to run a service check and save both normal output and error messages to service.log, overwriting the file if it already exists.

Complete this command:

systemctl status nginx _____ service.log _____

==> > and 2>&1

Why does this work?

1. > service.log redirects stdout (1) to service.log. If the file exists,
 its contents are overwritten.

2. 2>&1 redirects stderr (2) to the same destination as stdout.
The result: both normal output and error messages go into service.log.

Important: 2>&1 means “send stderr to wherever stdout is currently going.” 
That's why we put > service.log first.


========================================================================

			Next concept — Pipes (|)




A pipe sends the standard output of one command directly into another 
command as input.

For example:

ps aux | grep nginx


ps aux lists running processes.

| sends that output to grep.

grep nginx displays only lines containing nginx.


This is especially useful in DevOps when filtering logs, inspecting 
processes, or checking network connections.


Your exercise

You want to display only the lines containing ERROR in a file named app.log.

You know that grep ERROR app.log can find those lines.

Question: If you first use cat app.log to display the file contents, 
which operator would you use to send that output into grep ERROR?

Write the complete command.

cat app.log | grep "ERROR"


How it works:

1. cat app.log reads the file and sends its contents to stdout.
2. | sends that output to the next command.
3. grep "ERROR" displays only the lines containing ERROR.

A useful DevOps tip

You can simplify this command:

grep "ERROR" app.log

grep can read a file directly, so cat isn't necessary here. This is 
often preferred because it avoids launching an unnecessary process.


Next exercise — Combine pipes with log troubleshooting

Imagine app.log contains thousands of lines, and you want to display 
only the last 20 lines that contain ERROR.

tail -n 20 app.log | grep "ERROR" 


