# ============================================================
# Exercise 5 — stderr: 2> and 2>&1
# ============================================================

# Now let's learn something very important for Cloud/DevOps
# troubleshooting.

# Linux has different output streams:

# 1 = stdout → normal output
# 2 = stderr → error output


# For example:

# some-command > output.log

# saves normal output, but an error may still appear
# on the terminal.

# To redirect errors:

# some-command 2> errors.log


# ============================================================
# Your Exercise
# ============================================================

# Consider:

# ls /home/steve

# This command succeeds and produces normal output.


# Now consider:

# ls /does-not-exist

# This produces an error.


# ============================================================
# Question 1
# ============================================================

# What does this command do?

# ls /does-not-exist > output.log

# Does the error go into output.log,
# or does it remain in the terminal?

The error remains in the terminal because > only redirects stdout.
The stderr is not redirected.

# ============================================================
# Question 2
# ============================================================

# What does this command do?

# ls /does-not-exist 2> errors.log

# Where does the error go?

This command redirect error into errors.log file
So the error does not remains in the terminal


# ============================================================
# Question 3
# ============================================================

# What do you think this does?

# ls /does-not-exist > output.log 2>&1

This command redirects both stdout and stderr into the same file,
output.log.

# ============================================================
# chmod: Changing Permissions
# ============================================================

# Now we need to learn how to modify these permissions.

# The command is:

# chmod


# For example:

# chmod +x script.sh

# means:

# Add execute permission.


# And:

# chmod -x script.sh

# means:

# Remove execute permission.


# We can also specify who gets the permission:

# u = user/owner
# g = group
# o = others
# a = all


# Examples:


# chmod u+x script.sh

# → give the owner execute permission.


# chmod g+w app.log

# → give the group write permission.


# chmod o-r secret.txt

# → remove read permission from others.

# ============================================================
# Exercise 2
# ============================================================

# Starting with:

# -rw-r--r-- 1 steve developers 100 Sep 9 config.txt


# For each command, tell me what the new permissions will be.


# A

# chmod u+x config.txt
Owner steve have now : read, write and execute permissions

# B

# chmod g+w config.txt
developers group  have now : read and  write permissions


# C

# chmod o-r config.txt
This command remove read permission to other


# For each one, give me the resulting permission string.

# Example:

# A → -rwxr--r--
Owner : read, write, execute
group : read
other : read