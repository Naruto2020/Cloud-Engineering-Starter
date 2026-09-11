# ============================================================

# Lesson 1 — Reading and Searching Linux Logs

# ============================================================

# As a Cloud Engineer, you'll constantly inspect files such as:

# /var/log/syslog

# /var/log/auth.log

# /var/log/nginx/access.log

# /var/log/nginx/error.log

# The first commands to master are:

# cat

# less

# head

# tail

# grep

# ============================================================

# 1. cat

# ============================================================

# Displays the entire file:

# cat app.log

# Good for small files.

# ============================================================

# 2. less

# ============================================================

# Opens a file page by page:

# less app.log

# Useful for large files.

# Inside less:

# Space → next page

# b     → previous page

# q     → quit

# ============================================================

# 3. head

# ============================================================

# Shows the beginning of a file:

# head app.log

# By default, it shows the first 10 lines.

# You can specify the number:

# head -n 20 app.log

# → first 20 lines.

# ============================================================

# 4. tail

# ============================================================

# Shows the end of a file:

# tail app.log

# And:

# tail -n 20 app.log

# → last 20 lines.

# But this one is extremely important for Cloud/DevOps:

# tail -f app.log

# -f means follow the file.

# If an application is running and continuously writing logs,

# you can watch new entries appear in real time.

# ============================================================

# 5. grep

# ============================================================

# Searches for text inside a file:

# grep "ERROR" app.log

# For example:

# 2026-09-06 INFO Server started

# 2026-09-06 INFO Database connected

# 2026-09-06 ERROR Database connection failed

# 2026-09-06 INFO Retrying connection

# Then:

# grep "ERROR" app.log

# Returns only:

# 2026-09-06 ERROR Database connection failed

# ============================================================

# Exercise

# ============================================================

# Imagine app.log contains:

# INFO Server starting

# INFO Loading configuration

# INFO Connecting to database

# ERROR Database connection failed

# INFO Retrying connection

# ERROR Database connection timeout

# INFO Server shutting down

# What does each command return?


# Give the output of each command.

1. head -n 3 app.log

=> first three lines : 

INFO Server starting
INFO Loading configuration
INFO Connecting to database

2. tail -n 2 app.log

=> last two lines of app.log file

ERROR Database connection timeout
INFO Server shutting down


3. grep "ERROR" app.log

=> only the lines containing ERROR

ERROR Database connection failed
ERROR Database connection timeout


# ============================================================
# Next: Combining Commands
# ============================================================

# This is where Linux becomes powerful.

# You can combine grep with tail:

# tail -n 50 app.log | grep "ERROR"

# Meaning:

# Take the last 50 lines → search for ERROR.

# And:

# grep "ERROR" app.log | tail -n 5

# Meaning:

# Find all errors → show only the last 5.

# This | is called a pipe.


# ============================================================
# Exercise 2 — Log Troubleshooting
# ============================================================

# Imagine app.log contains 1,000 lines.

# You want to answer:

# "Were there any errors in the last 100 lines of the
# application log?"

# Which command would you use?

# A

# grep "ERROR" app.log | tail -n 100


# B

# tail -n 100 app.log | grep "ERROR"


# C

# head -n 100 app.log | grep "ERROR"


# Choose A, B, or C, and explain why.


B because we are looking errors in the last 100 lines, so the best way 
to find is to :

1. take the last 100 lines of application log -> tail -n 100 app.log
2. then search for  ERROR -> grep "ERROR"

# ============================================================
# Very Useful Rule
# ============================================================

# When you see:

# "in the last N lines"

# think:

# tail -n N file | grep "something"


# When you see:

# "the last N matching lines"

# think:

# grep "something" file | tail -n N


# That's an important distinction for real-world
# log troubleshooting.




# ============================================================
# Lesson 2 — Pipes & Redirections
# ============================================================

# These are core Bash skills for Cloud Engineering.

# You already saw:

# tail -n 100 app.log | grep "ERROR"

# The | is a pipe: it sends the output of one command
# to another command.


# ============================================================
# 1. Pipe |
# ============================================================

# Example:

# ps aux | grep nginx

# Meaning:

# Run ps aux, then search its output for nginx.

# Another example:

# cat app.log | grep "ERROR"


# ============================================================
# 2. Redirect >
# ============================================================

# > sends command output into a file.

# echo "Server started" > status.txt

# If status.txt doesn't exist → it is created.

# If it already exists → its previous content is replaced.


# ============================================================
# 3. Append >>
# ============================================================

# >> adds output to the end of a file.

# echo "Server started" >> status.txt

# So:

# >   replace
# >>  append

# This distinction is very important when working with logs.


# ============================================================
# 4. Combining Pipes and Redirection
# ============================================================

# You can combine pipes and redirection:

# grep "ERROR" app.log | tail -n 10 > errors.txt

# Read it from left to right:

# app.log
#    ↓
# grep ERROR
#    ↓
# last 10 errors
#    ↓
# errors.txt

# So instead of displaying the result on the terminal,
# we save it to a file.


# ============================================================
# Exercise
# ============================================================

# Assume:

# app.log

# contains 1,000 lines.

# You want to:

# Find all ERROR lines, keep only the last 20,
# and save them into errors.log.

# Which command is correct?

# A

# grep "ERROR" app.log | tail -n 20 > errors.log


# B

# tail -n 20 app.log | grep "ERROR" > errors.log


# C

# grep "ERROR" app.log > errors.log | tail -n 20


# Choose A, B, or C, and explain the order of operations.


Correct command is A assume we are looking for : 
1. all ERROR lines -> grep "ERROR"
2. keep only the last 20 lines -> tail -n 20 
3. save them into errors.log -> > errors.log


# ============================================================
# Exercise 2 — > vs >>
# ============================================================

# Suppose errors.log already contains:

# ERROR Database failed
# ERROR Connection timeout


# Then you run:

# echo "ERROR Server crashed" > errors.log


# Question 1
#
# What will errors.log contain afterward?

errors.log will contain "ERROR Server crashed" afterward.


# Then, starting from that result, you run:

# echo "ERROR Database unavailable" >> errors.log

# Question 2
#
# What will errors.log contain now?

errors.log will contain :
1. "ERROR Server crashed"
2. "ERROR Database unavailable"


# Give me the content of the file after each command.

after each command the file ll contain :

1. "ERROR Server crashed"
2. "ERROR Database unavailable"


# ============================================================
# Exercise 3 — Pipes + Redirection
# ============================================================

# Suppose app.log contains:

# INFO Server started
# ERROR Database failed
# INFO User connected
# ERROR Connection timeout
# ERROR Server crashed
# INFO Request completed


# You want to:
#
# 1. Find all ERROR lines
# 2. Keep only the last 2
# 3. Save them into critical-errors.log


# Question
#
# Which command is correct?


# A

# grep "ERROR" app.log > critical-errors.log | tail -n 2


# B

# grep "ERROR" app.log | tail -n 2 > critical-errors.log


# C

# tail -n 2 app.log | grep "ERROR" > critical-errors.log


# And tell me step by step what each command does.

Command B is the correct one because
Assume we want : 

1. Find all ERROR lines -> grep "ERROR" app.log
2. Keep only the last 2 lines -> tail -n 2
3. Save them into critical-errors.log -> > critical-errors.log

Therefore the correct command is  :

grep "ERROR" app.log | tail -n 2 > critical-errors.log


# ============================================================
# Exercise 4 — > vs >> + pipe
# ============================================================

# You have this log:

# INFO Server started
# ERROR Database failed
# ERROR Connection timeout
# INFO Request completed
# ERROR Server crashed


# You run these commands in order:

# grep "ERROR" app.log > errors.log

# then:

# grep "ERROR" app.log | tail -n 1 >> errors.log


# ============================================================
# Questions
# ============================================================

# 1. What does errors.log contain after the first command?

After the first command, error.log ll contain:

1. ERROR Database failed
2. ERROR Connection timeout
3. ERROR Server crashed

# 2. What does errors.log contain after the second command?

After the second command, error.log ll contain:

1. ERROR Database failed
2. ERROR Connection timeout
3. ERROR Server crashed
4. ERROR Server crashed

# 3. Why does the second command use >> instead of >?
Because >> add the output to the end of file (append)
while > replace file contain by current output (overwrite)
